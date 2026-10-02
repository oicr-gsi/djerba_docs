#! /usr/bin/env python3

"""
Script to load a plugin and extract information on its INI parameters
(will also work for helpers and mergers)
Works on similar principles to the PluginTester class
Outputs RST files for ReadTheDocs.
"""

import argparse
import csv
import logging
import os
import re
import sys
import tempfile
from djerba.core.loaders import plugin_loader, helper_loader, merger_loader
from djerba.core.workspace import workspace

# functions to generate output tables

class rst_table_maker:
    # format inputs as a ReStructuredText table

    def __init__(self):
        pass

    def default_output(self, d):
        if d == '__DJERBA_NULL__':
            return 'N/A'
        elif d == '':
            return '(empty)'
        else:
            return d

    def get_col_widths(self, headers, contents, notes):
        # column width is the maximum width of header or contents/notes
        [h1, h2, h3] = headers # h3 is header for the notes column
        widths = [len(h) for h in headers]
        for k, v in contents.items():
            if len(k) > widths[0]:
                widths[0] = len(k)
            if len(v) > widths[1]:
                widths[1] = len(v)
            if k in notes and len(notes[k]) > widths[2]:
                widths[2] = len(notes[k])
        return widths

    def make_row(self, entries, widths):
        # arguments are column entries and column widths
        # find right-padding width, then construct the line
        if len(entries) != len(widths):
            raise ValueError("Number of column entries must equal number of column widths")
        cells = []
        for i in range(len(entries)):
            padding = widths[i] - len(entries[i])
            cells.append(entries[i]+' '*padding)
        row = ' '.join(cells)
        return row

    def make_table(self, contents, notes):
        # contents = key/value dictionary
        # notes = dictionary with (optional) extra notes for each key
        h1 = 'Parameter'
        h2 = 'Default'
        h3 = 'Notes'
        headers = [h1, h2, h3]
        widths = self.get_col_widths(headers, contents, notes)
        sep = ' '.join(['='*w for w in widths])
        output = []
        output.append(sep)
        output.append(self.make_row(headers, widths))
        output.append(sep)
        for k in sorted(list(contents.keys())):
            entries = [k, contents[k], notes.get(k, '')]
            output.append(self.make_row(entries, widths))
        output.append(sep)
        return "\n".join(output)

class djerbadoc:

    """Automatically generate documentation for a Djerba plugin"""

    # RST line to go before/after chapter headings
    CHAPTER_MARKER = '***********************************'

    # input filenames
    GENERIC_MAIN = 'generic.txt' # main text, generic parameters
    GENERIC_NOTES = 'generic_notes.tsv' # notes as key/value pairs, generic parameters
    SPECIFIC_MAIN = 'specific.txt' # main text, specific parameters
    SPECIFIC_NOTES = 'specific_notes.tsv' # main text, specific parameters
    DESCRIPTION = 'description.txt' # detailed description
    SUMMARY = 'summary.txt' # summary, defaults to pydoc
    ALL_INPUTS = [
        GENERIC_MAIN, GENERIC_NOTES, SPECIFIC_MAIN, SPECIFIC_NOTES, DESCRIPTION, SUMMARY
    ]

    def __init__(self, component_name, root_dir, tmp_dir):
        self.tmp_dir = tmp_dir # assign this first, needed by load_component
        self.component_name = component_name
        self.component, self.component_type = self.load_component()
        self.component_id = self.construct_component_id()
        self.component_version = self.component.get_version()
        self.main_dir = self.construct_main_dir_path(root_dir)
        # get the top-level package name
        # eg. djerba.plugins.wgts.snv_indel.plugin -> djerba
        self.top_package = re.split('\\.', self.component_id).pop(0)
        # generate (hopefully) unique section labels
        self.summary_label = self.component_id+"_summary"
        self.description_label = self.component_id+"_description"
        self.specific_params_label = self.component_id+"_specific_params"
        self.generic_params_label = self.component_id+"_generic_params"

    def construct_main_dir_path(self, root_dir):
        """get path of a standard directory hierarchy under the given root"""
        dirs = re.split('\\.', self.component_id)
        subdir = os.sep.join(dirs)
        main_dir = os.path.join(root_dir, subdir)
        return main_dir

    def construct_component_id(self):
        terms = re.split('\\.', self.component.__module__)
        non_component_terms = [x for x in terms if not re.match(self.component_type, x)]
        return '.'.join(non_component_terms)

    def get_docstring(self):
        """get the docstring for the parent module, or if not found, the component"""
        # in past practice, informative docstring is usually at the module level
        parent_module = sys.modules[self.component.__module__]
        doc_string = parent_module.__doc__ if parent_module.__doc__!=None else self.component.__doc__
        return doc_string

    def get_main_dir(self):
        return self.main_dir

    def get_component_id(self):
        return self.component_id

    def initialize(self):
        """make directory and write blank input files if they are not already present"""
        if not os.path.exists(self.main_dir):
            os.makedirs(self.main_dir)
        for input_name in self.ALL_INPUTS:
            input_path = os.path.join(self.main_dir, input_name)
            if not os.path.exists(input_path):
                open(input_path, 'a').close()

    def load_component(self):
        """
        set up a temporary directory (required for component workspace) and load the component
        return the component and its type (plugin, helper or merger)
        """
        work_dir = self.tmp_dir.name
        log_level = logging.WARNING
        if re.search('_helper$', self.component_name):
            component = helper_loader(log_level).load(self.component_name, workspace(work_dir, log_level))
            component_type = 'helper'
        elif re.search('_merger$', self.component_name):
            component = merger_loader(log_level).load(self.component_name) # merger loader does not have a workspace
            component_type = 'merger'
        else:
            component = plugin_loader(log_level).load(self.component_name, workspace(work_dir, log_level))
            component_type = 'plugin'
        return component, component_type

    def make_description(self):
        # insert contents of the description.txt file (if any)
        default = 'No description provided.'
        output = []
        output.append(".. _"+self.description_label+":\n")
        output.append(self.CHAPTER_MARKER)
        output.append("Description")
        output.append(self.CHAPTER_MARKER)
        output.append('')
        desc_path = os.path.join(self.main_dir, self.DESCRIPTION)
        if os.path.exists(desc_path):
            with open(desc_path) as desc_file:
                description = desc_file.read()
            if description.strip()=='':
                description = default
            output.append(description)
        else:
            output.append(default)
        output.append('\n')
        return "\n".join(output)

    def make_params_section(self, params_type):
        config = self.component.get_expected_config()
        section = config.sections()[0] # should be only one section
        contents = dict(config.items(section))
        generic = ['attributes', 'depends_configure', 'depends_extract',
           'configure_priority', 'extract_priority', 'render_priority']
        table_maker = rst_table_maker()
        if params_type == 'generic':
            label = ".. _"+self.generic_params_label+":\n"
            title = "Generic Parameters"
            txt_filename = self.GENERIC_MAIN
            tsv_filename = self.GENERIC_NOTES
            params = {k: table_maker.default_output(v) for k, v in contents.items() if k in generic}
        elif params_type == 'specific':
            label = ".. _"+self.specific_params_label+":\n"
            title = "Specific Parameters"
            txt_filename = self.SPECIFIC_MAIN
            tsv_filename = self.SPECIFIC_NOTES
            params = {k: table_maker.default_output(v) for k, v in contents.items() if not k in generic}
        else:
            raise ValueError("Params type must be 'generic' or 'specific'")
        output = []
        output.append(label)
        output.append(self.CHAPTER_MARKER)
        output.append(title)
        output.append(self.CHAPTER_MARKER)
        output.append('')
        output.append(table_maker.make_table(params, self.read_notes(tsv_filename)))
        # optionally, insert contents of a file with extra params info
        # if file does not exist, do nothing
        extra_path = os.path.join(self.main_dir, txt_filename)
        output.append('')
        if os.path.exists(extra_path):
            with open(extra_path) as extra_file:
                output.append(extra_file.read())
        output.append('')
        return "\n".join(output)

    def make_preamble(self):
        """Make the document header and contents"""
        title = self.top_package+": "+self.component_name
        marker = "="*len(title)
        output = []
        output.append(marker)
        output.append(title)
        output.append(marker)
        output.append('')
        output.append('.. rubric:: Version: '+self.component_version)
        output.append('')
        output.append(self.CHAPTER_MARKER)
        output.append("Contents")
        output.append(self.CHAPTER_MARKER)
        contents = """
        * :ref:`{0}`
        * :ref:`{1}`
        * :ref:`{2}`
        * :ref:`{3}`
        """.format(self.summary_label, self.generic_params_label, self.specific_params_label, self.description_label)
        output.append(contents)
        output.append('\n')
        output.append('For explanation of each section, see the main :ref:`component-reference` page.')
        output.append('\n')
        return "\n".join(output)

    def make_summary(self):
        """Make the summary from file or docstring, if any"""
        default = "No summary provided."
        output = []
        output.append(".. _"+self.summary_label+":\n")
        output.append(self.CHAPTER_MARKER)
        output.append("Summary")
        output.append(self.CHAPTER_MARKER)
        summary_path = os.path.join(self.main_dir, self.SUMMARY)
        doc_string = self.get_docstring()
        # read from a summary.txt file; if not found, fall back to the docstring
        if os.path.exists(summary_path):
            with open(summary_path) as sum_file:
                summary = sum_file.read()
            if summary.strip() == '':
                summary = default
            output.append(summary)
        elif doc_string != None:
            output.append(doc_string)
        else:
            output.append(default)
        output.append('\n')
        return '\n'.join(output)

    def read_notes(self, filename):
        """Read notes from given TSV file. If file does not exist, silently return an empty dictionary."""
        input_path = os.path.join(self.main_dir, filename)
        notes = {}
        if os.path.exists(input_path):
            with open(input_path) as input_file:
                reader = csv.reader(input_file, delimiter="\t")
                for row in reader:
                    if len(row)!=2:
                        raise ValueError("TSV for param notes must have exactly two columns")
                    notes[row[0]] = row[1]
        return notes

def main():
    """main method to run script"""

    # parse arguments
    parser = argparse.ArgumentParser(
        prog='plugin_config_inspect.py',
        description='Automatically generate Djerba documentatation',
        epilog='The input/output directory will be of the form ${ROOT}/${TOP_PACKAGE}/directories/from/component/name/. For example, with root directory ./doc/, top-level package djerba, and plugin name wgts.snv_indel, output is written to ./doc/djerba/wgts/snv_indel. An error is raised if the directory does not exist; run with --init to create the directory.'
    )
    parser.add_argument('component', help='Component identifier, eg. wgts.snv_indel')
    parser.add_argument('root', help='Root directory for input and output files, see below')
    parser.add_argument('--init', help='Create output directory and empty input files (if not already present)', action='store_true')
    args = parser.parse_args()
    component_name = args.component
    root_dir = args.root
    init = args.init
    if not os.path.exists(root_dir):
        print("Error: root directory argument '"+root_dir+"' does not exist!", file=sys.stderr)
        sys.exit(1)
    tmp_dir = tempfile.TemporaryDirectory(prefix='djerbadoc_tmp_')
    # create and run the documenter object
    documenter = djerbadoc(component_name, root_dir, tmp_dir)
    if init:
        documenter.initialize()
    main_dir = documenter.get_main_dir()
    if not os.path.exists(main_dir):
        msg = "Error: Expected output directory '"+main_dir+"' does not exist. "+\
            "Run with --init to create."
        print(msg, file=sys.stderr)
        sys.exit(1)
    output = []
    output.append(documenter.make_preamble())
    output.append(documenter.make_summary())
    output.append(documenter.make_params_section('specific'))
    output.append(documenter.make_params_section('generic'))
    output.append(documenter.make_description())
    tmp_dir.cleanup()
    filename = documenter.get_component_id()+'.djerbadoc.rst'
    with open(os.path.join(main_dir, filename), 'w') as out_file:
        out_file.write(''.join(output))

if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    main()
