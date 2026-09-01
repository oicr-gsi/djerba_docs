==========
User Guide
==========

In this section, we describe how to install Djerba and run it to produce reports.

*****************
Installing Djerba
*****************

Requirements
============

Hardware
--------

- The core Djerba functions are very lightweight, 4 GB of RAM and a 1 GHz processor should be more than sufficient to run them.
- Certain plugins are more demanding, and may need up to 32GB of RAM and a 4 GHz or faster processor (preferably with multiple cores).
- A full installation of Djerba and its mainline plugins requires about 600 MB of disk space.

Operating System
----------------

- Djerba runs in production under `Ubuntu 20.04 LTS`_.
- OICR is preparing to move to `Ubuntu 22.04 LTS`_ and will update Djerba accordingly.
- Other versions of Linux are not supported but may be compatible.
- Limited testing of Djerba has successfully been carried out on MacOS.
- Djerba has *not* been tested on Microsoft Windows, and issues are likely to occur.

.. _Ubuntu 20.04 LTS : https://releases.ubuntu.com/focal/
.. _Ubuntu 22.04 LTS : https://releases.ubuntu.com/jammy/

Software
--------

- `Python`_ version 3.13 or greater (at time of writing, if in doubt consult the `setup script`_).
- The `wkhtmltopdf`_ utility is required for PDF conversion.
- *Optional*: :ref:`Apache CouchDB <couchdb-setup>` may be used for report archiving

.. _Python: https://www.python.org/downloads/
.. _setup script: https://github.com/oicr-gsi/djerba/blob/main/setup.py
.. _wkhtmltopdf: https://wkhtmltopdf.org/downloads.html

Installation Steps
==================

Overview
--------

Djerba is installed as follows:

1. Install core Djerba functionality using the standard Python tool ``pip3``
2. Install the `wkhtmltopdf`_ utility
3. Install additional plugins, if any
4. *Optional*: Set up a :ref:`CouchDB server <couchdb-setup>` for archiving

Installation with ``pip3``
--------------------------

The core functions of Djerba are written in Python, and installed using standard Python tools.

Python installation is covered in the `official Python documentation`_, in particular the `Python Packaging User Guide`_. You may wish to use a `Python virtual environment`_ to install Djerba without affecting your system Python directories.

From a download or clone of the `Djerba repository`_, simply run ``pip3 install .``. This will install Djerba and all its Python dependencies.

Djerba has a `setup.py script`_ which specifies exactly what is installed.

Note that Djerba plugins may contain R scripts and other non-Python code. Installing with ``pip3`` *will* copy these files to the installation directory, but *will not* install non-Python dependencies such as R libraries. Any such dependencies must be installed separately by the user. Consult documentation for individual plugins for details.

.. _Djerba repository: https://github.com/oicr-gsi/djerba/tree/main
.. _official Python documentation: https://docs.python.org/3/
.. _Python Packaging User Guide: https://packaging.python.org/en/latest/
.. _Python virtual environment: https://docs.python.org/3/library/venv.html
.. _setup.py script: https://github.com/oicr-gsi/djerba/blob/main/setup.py

The ``wkhtmltopdf`` Utility
----------------------------

- Djerba requires `wkhtmltopdf`_, an HTML to PDF conversion utility.
- The utility must be installed, with the ``wkhtmltopdf``  binary on the system ``PATH``.
- For best results, the Arial font family should be installed (in ``$HOME/.local/share/fonts`` on a Linux machine).

Additional Plugin Repositories
------------------------------

If using plugins (or helpers, or mergers) from a location other than the main Djerba repository, they must be installed and visible on the ``PYTHONPATH`` environment variable.

Typically, additional plugins will be installed using ``pip3``, similarly to core Djerba. Plugin dependencies may require additional steps to install and configure.

Djerba in Docker
================

As an alternative to installing Djerba on your own system, running in a `Docker container`_ is also supported. The Djerba repository includes a `Dockerfile`_ and `documentation`_.

.. _Docker container: https://docs.docker.com/get-started/
.. _Dockerfile: https://github.com/oicr-gsi/djerba/blob/main/Dockerfile
.. _documentation: https://github.com/oicr-gsi/djerba/blob/main/CONTAINERIZE.md

.. _couchdb-setup:

CouchDB Setup
=============

Djerba supports archiving the JSON report files to an instance of `Apache CouchDB`_, a type of `NoSQL database`_.

This feature allows reports to be stored in a central, searchable archive. We have found it to be extremely useful for consulting past reports and analyzing trends.

- For information on how to set up the database server, see the `CouchDB documentation`_.
- Djerba is configured to upload JSON to the server using a simple INI file. See: :ref:`archive-config`
- Archiving is optional, and can be omitted using the ``--no-archive`` option to the main Djerba script.


.. _Apache CouchDB: https://couchdb.apache.org/
.. _CouchDB documentation: https://docs.couchdb.org/en/stable/
.. _NoSQL database: https://www.mongodb.com/resources/basics/databases/nosql-explained

******************
Configuring Djerba
******************

Djerba has a number of global settings which control application behaviour. They are implemented using a combination of :ref:`environment variables <environment-variables>` and :ref:`configuration files <core-config-files>`.

.. _environment-variables:

Environment Variables
=====================

Djerba uses a number of `environment variables`_ for configuration. We recommend using a shell script, or a package such as `Environment Modules`_, to set up your preferred environment before each use of Djerba.

.. _environment variables: https://help.ubuntu.com/community/EnvironmentVariables
.. _Environment Modules: https://modules.readthedocs.io/en/latest/


+---------------------------+----------------------+----------+----------------------------------------------------------------------------------+
| Variable                  | Type                 | Required | Description                                                                      |
+===========================+======================+==========+==================================================================================+
| ``DJERBA_ARCHIVE_CONFIG`` | INI file             | No       | Upload of JSON report documents to a :ref:`CouchDB database <couchdb-setup>`     |
+---------------------------+----------------------+----------+----------------------------------------------------------------------------------+
| ``DJERBA_BASE_DIR``       | Directory            | Yes      | Base directory where Djerba was installed.                                       |
|                           |                      |          | Eg. ``/usr/lib/python3.13/site-packages/djerba``                                 |
+---------------------------+----------------------+----------+----------------------------------------------------------------------------------+
| ``DJERBA_CORE_HTML_DIR``  | Directory            | No       | Location of templates and stylesheets for core HTML rendering.                   |
|                           |                      |          | See :ref:`document-configuration`.                                               |
+---------------------------+----------------------+----------+----------------------------------------------------------------------------------+
| ``DJERBA_PACKAGES``       | Colon-separated list | No       | Names of top-level Djerba packages; see :ref:`finding_loading_components`.       |
|                           |                      |          | Defaults to ``djerba``.                                                          |
+---------------------------+----------------------+----------+----------------------------------------------------------------------------------+
| ``DJERBA_PRIVATE_DIR``    | Directory            | Yes      | Location of "private" files.                                                     |
+---------------------------+----------------------+----------+----------------------------------------------------------------------------------+
| ``DJERBA_RUN_DIR``        | Directory            | Yes      | Location of the ``util/data`` subdirectory of the Djerba installation.           |
|                           |                      |          | Typically ``${DJERBA_BASE_DIR}/util/data``                                       |
+---------------------------+----------------------+----------+----------------------------------------------------------------------------------+
| ``DJERBA_TEST_DIR``       | Directory            | No       | Location of data for unit tests                                                  |
+---------------------------+----------------------+----------+----------------------------------------------------------------------------------+
| ``DJERBA_TEST_DATA``      | Directory            | No       | Alternative to ``DJERBA_TEST_DIR``. Deprecated, but still used by some plugins.  |
+---------------------------+----------------------+----------+----------------------------------------------------------------------------------+

**Table 1**: Djerba environment variables

Required and Optional Variables
-------------------------------

- The ``DJERBA_BASE_DIR``, ``DJERBA_RUN_DIR``, and ``DJERBA_PRIVATE_DIR`` variables must be correctly set at runtime.
- ``DJERBA_ARCHIVE_CONFIG`` is required unless the ``--no-archive`` command-line option is in effect.
- If ``DJERBA_CORE_HTML_DIR`` is not set, it defaults to an appropriate directory in the Djerba installation.
- If ``DJERBA_PACKAGES`` is not set, it defaults to the Djerba installation directory.
- ``DJERBA_TEST_DIR`` and ``DJERBA_TEST_DATA`` are needed for testing only, not production.

The ``DJERBA_PRIVATE_DIR``
--------------------------

This is a location where Djerba can read and write files to control application-wide settings. In general the contents are not secret, but they are specific to configuring how Djerba runs.

.. It is also the output location for the [activity tracker](FIXME). If the tracker is in use, ``DJERBA_PRIVATE_DIR`` must have a subdirectory called ``tracking``.


.. _core-config-files:

Global Configuration Files
==========================

Some functions and behaviour of Djerba are controlled using configuration files. These are distinct from the INI configuration file used to run Djerba and generate a report.

All of these configuration files are optional. The archive config may be omitted if running with the ``--no-archive`` option. If the others are absent, Djerba will fall back to appropriate defaults. The files are summarized in **Table 2** and described in more detail below.

+------------------+------------------+----------------------------------------------------------------------------------+
| File             | Type             | Description                                                                      |
+==================+==================+==================================================================================+
| Archive config   | INI              | Configuration for upload to a :ref:`CouchDB database <couchdb-setup>`            |
+------------------+------------------+----------------------------------------------------------------------------------+
| User name config | JSON             | Mapping from UNIX usernames to display names for reports                         |
+------------------+------------------+----------------------------------------------------------------------------------+
| HTML config      | CSS, JSON, HTML  | Templates and stylesheets for core HTML rendering                                |
+------------------+------------------+----------------------------------------------------------------------------------+

**Table 2**: Djerba global configuration files

.. _archive-config:

Archive Config
--------------

Upload of Djerba documents to a :ref:`CouchDB server <couchdb-setup>` is configured using an INI file. The location of the file is specified by the ``DJERBA_ARCHIVE_CONFIG`` :ref:`environment variable <environment-variables>`.

The config format is as follows:

::

   [archive]
   database_name = djerba
   username = djerba_production_user
   password = VerySecretPassword
   address = my-djerba-server.example.com
   port = 1234

.. _user-name-config:

User Name Config
----------------

Djerba can use a JSON file to map from UNIX username to a display name for report documents. (Alternatively, the author name can be configured manually in the report INI file.) Djerba reads this configuration from the ``djerba_users.json`` file in the directory given by the ``DJERBA_PRIVATE_DIR`` :ref:`environment variable <environment-variables>`. File format is as follows:

::

   {
       "jlpicard": "Jean-Luc Picard",
       "bcrusher": "Beverly Crusher"
   }


Djerba looks up the username using standard UNIX environment variables: It first tries ``USER``; if there is no config entry, it next tries ``SUDO_USER``; and finally, it falls back to using the UNIX username as the display name.

.. note:: If running Djerba in a remote session, ensure the ``USER`` and/or ``SUDO_USER`` variables are correctly exported, for example by using the ``-V`` option to the `qrsh command`_.

.. _qrsh command: https://manpages.org/qrsh


HTML Configuration Files
^^^^^^^^^^^^^^^^^^^^^^^^

Djerba uses templates and stylesheets to control the overall look-and-feel of the HTML report output.

The default versions of these files have the OICR branding and colour scheme. They are part of the `Djerba code repository`_, and are automatically copied to the Djerba installation directory. The user may set an alternate location for these files using the ``DJERBA_CORE_HTML_DIR``  :ref:`environment variable <environment-variables>`.

For further details, see the :ref:`document-configuration` section.

.. _Djerba code repository: https://github.com/oicr-gsi/djerba/tree/main/src/lib/djerba/core

**************
Running Djerba
**************

Introduction
=======================

The main command-line interface for Djerba is the ``djerba.py`` script, which has a number of subcommands or *modes* for different stages of the reporting process. The :doc:`How Djerba Works <../../how_djerba_works/how_djerba_works>` section has a :ref:`full description <user-interface>` of each mode and its purpose. In this section, we focus on the steps most commonly used to produce a report.


The INI Configuration File
==========================

Introduction
------------

Parameters for a report are given to Djerba using a configuration file in INI format.

The INI format consists of one or more *sections*. Each section has a header in square brackets, followed by zero or more key/value pairs, written in the form ``key = value``.

The ``core`` component is always required. Users can include additional components as needed; each one has a section in the INI file. While the section header is always required, a component does not necessarily need to have any key/value pairs explicitly specified, as they may be filled in by default values.

.. _core-parameters:

Core Parameters
---------------

The ``core`` component has some parameters shared with other Djerba components, such as :ref:`priority values <runtime-priority-and-dependencies>`. Parameters specific to ``core`` are as follows.

==================== =======================================================================================================================
Name                 Description
==================== =======================================================================================================================
``author``           Name of the report author. May have a default based on the Linux username. See: :ref:`user-name-config`
``report_id``        Name for the report, used as a prefix for output files.
``report_version``   Version number of the report. From time to time, a report may need to be re-released with amendments, which can be tracked with this parameter.
``input_params``     Filename for input parameters. See: :ref:`input-params-file`
``document_config``  Filename for document configuration parameters. See: :ref:`document-configuration-file`
==================== =======================================================================================================================

.. TODO Attributes
.. TODO input params
.. TODO document config


Completing the INI File
-----------------------

To configure the INI file for Djerba, simply fill in appropriate values for the named parameters. Many parameters receive default values, so the INI file completed by the user can be quite compact.

Pre-Population
^^^^^^^^^^^^^^

A group of reports may share parameters, such as the project name and assay type. For convenience, the "configure" and "report" modes of the main Djerba script have a ``-p/--pre-populate`` option. This specifies a supplementary INI file with default configuration values. Any plugin parameters in the supplementary file, which are not otherwise specified, will be filled in as defaults.


Example
^^^^^^^

The following is a `test INI file`_ from the Djerba repository:

::

   [core]
   report_id = demo_report
   author = Test Author

   [demo1]
   question = Who wrote Romeo and Juliet?

   [demo2]
   question = question.txt
   demo2_param = The Pacific Ocean

The ``[core]`` section sets parameters for the Djerba ``core`` component, which is responsible for loading other components and executing them in the correct order. We also have parameters for two plugins, ``demo1`` and ``demo2``, which are installed as part of the main Djerba repository.

Having completed the INI, we can use it to generate a report as follows:

::

   djerba.py report -i config.ini -o . -p

The above command will write output to the current working directory, including a PDF file (enabled by the ``-p`` option).

.. _test INI file: https://github.com/oicr-gsi/djerba/blob/main/test-e2e/data/config.ini


.. _main-script-usage:

Main Script Usage
=================

A user may run ``djerba.py --help`` for general options, or ``djerba.py $MODE --help`` for specific instructions on a given mode.

The general syntax is as follows:

::

   djerba.py [logging options] [mode name] [mode options]

Logging options control status reports from the Djerba program. Djerba follows standard `software logging`_ conventions and formats. Default behaviour is to print warnings and error messages only. More detail is provided by the "verbose" option, and even more by "debug". The ``--log-path`` option may be used to write log output to a file instead of printing to the terminal.

The modes are listed in :ref:`How Djerba Works <user-interface>`. The most commonly used ones are:

* **setup**: Prepare an INI config file to be completed by the user
* **report**: Use the INI file to run Djerba's :ref:`production steps <production-steps>` in order and generate an HTML report, with optional PDF
* **update**: Modify the summary text in a draft report, previously generated in ``report`` mode

.. _software logging: https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
 

Example Session
---------------
==================================================================================== =============================================================================
Command                                                                              Description
==================================================================================== =============================================================================
``djerba.py setup -a wgts -c``                                                       Write an INI file to be completed by the user. The ``-a wgts`` option states it is for the WGTS assay, while ``-c`` requests a "compact" file with only a minimal set of parameters for the user to complete (others will receive standard default values).  The config file will be given the default name ``config.ini``.
``mkdir report``                                                                     Make a directory for report output.
``djerba.py -v report -i config.ini -o report -p``                                   Generate a draft report. The ``-v`` option writes log output to the terminal, so we can monitor progress. The options ``-i`` and ``-o`` denote the input config file and output directory respectively, while ``-p`` directs Djerba to produce PDF output.
``nano summary.txt``                                                                 Write a free-text summary describing important features of the case, using a text editor of your choice.
``djerba.py -v update -s summary.txt -j report/lorem_ipsum_v1.json -o report -p``    Update the report with our new summary text. The ``-s`` and ``-j`` options are the summary text file and draft report JSON, respectively. Again, ``-v`` enables verbose mode while ``-o`` denotes the output directory and ``-p`` enables PDF.
==================================================================================== =============================================================================

**Table 3**: Example Djerba session, with explanation of each step.

.. note:: A few other command-line scripts are installed with the Djerba Python package. They are not required for report production; all are currently deprecated and/or of use primarily to developers.

.. TODO  See the dev guide.

.. TODO "advanced usage" section
   covers variant annotation, troubleshooting, full_config.ini, component attributes, input params, document config, etc.

**************
Advanced Usage
**************

This section covers advanced topics and configuration options.

Variant Annotation
==================

A key function of Djerba is *annotation* of genomic variants, to determine which ones are clinically relevant. This is done by querying a database of variants; several such databases are available.

Annotation is handled by individual plugins, not the core Djerba code. This means Djerba is not committed to any particular method of annotation, and plugin authors may use any resources they see fit.

Clinical reporting at OICR uses `OncoKB`_, a comprehensive oncology annotation resource maintained by `Memorial Sloan Kettering Cancer Center`_. Djerba includes code to support `annotation with OncoKB`_.

OncoKB annotation with OICR Djerba plugins requires:

* Installation of the `oncokb-annotator`_ software package, version >=4.0.0
* A valid OncoKB access token:
  
  * Plugins read the token path from the environment variable ``ONCOKB_TOKEN``
  * To obtain a token, contact the OncoKB administrators.

.. _OncoKB: https://www.oncokb.org/
.. _Memorial Sloan Kettering Cancer Center: https://www.mskcc.org/
.. _annotation with OncoKB: https://github.com/oicr-gsi/djerba/tree/main/src/lib/djerba/util/oncokb
.. _oncokb-annotator: https://github.com/oncokb/oncokb-annotator

.. _document-configuration:

Document Configuration
======================

This section describes how to customize the appearance of Djerba's output. This is controlled by a combination of component attributes, and the document configuration file.

.. _component-attributes:

Component Attributes in the INI
-------------------------------

Every Djerba component has an ``attributes`` parameter in its INI section. By default, the permitted attributes are "clinical", "research", and "simple". These are labels applied to individual plugins, used at OICR to control different reporting types with distinct HTML stylesheets and formatting options.

Most OICR plugins default to the "clinical" attribute, and use the corresponding format for a clinical report.

.. note:: The ``attributes`` INI parameter should have the name of exactly one attribute -- either manually specified, or from a default for the plugin. Configuration of multiple attributes for a component in the same report is not supported. 


.. _document-configuration-file:

The Document Configuration File
---------------------------------

This is a file with a name specified by the :ref:`core component <core-parameters>`, defaulting to ``document_config.json``. It is located in the directory specified by the ``DJERBA_CORE_HTML_DIR`` :ref:`environment variable <environment-variables>`. 

Each permitted :ref:`component attribute <component-attributes>` corresponds to a *document type*. Each document type has a header and footer file, and a `CSS stylesheet`_.

.. _CSS stylesheet: https://www.w3schools.com/html/html_css.asp

These are specified in ``document_config.json`` as follows:

::

   {
    "document_types": ["clinical", "research", "simple"],
    "document_settings": {
	"clinical": {
	    "document_header": "clinical_header.html",
	    "document_footer": "clinical_footer.html",
	    "stylesheet": "stylesheet.css"
	    },
	"research": {
	    "document_header": "research_header.html",
	    "document_footer": "research_footer.html",
	    "stylesheet": "stylesheet.css"
	    },
	"simple": {
	    "document_header": "simple_header.html",
	    "document_footer": "footer.html",
	    "stylesheet": "stylesheet.css"
	    }	
        }
    }

At runtime, if plugins in the INI config have more than one attribute, the final PDF outputs will be merged into a single document. The merged elements will appear in the same order as the ``document_types`` list in the document configuration file. For example, this can be used to add a "research" appendix to a "clinical" report.



Additional Input and Output Files
=================================

.. _input-params-file:

The Input Params File
-----------------------

Djerba :ref:`components <modular-components>` are able to read and write files in a shared *workspace*. The files exist in a directory specified at runtime to the main Djerba script. This enables information to be shared between different components.

OICR plugins have the concept of an "input params helper", `for example in our WGTS assay`_. Recall that a helper component only writes files to the workspace, and does not generate JSON or HTML report output. The input params helper is given a priority order such that it runs before any other component. Its task is to collect information such as the donor and requisition identifiers, which may subsequently be used to query other resources and gather input data. It writes its output to a JSON file, called ``input_params.json`` by default.

The input params helpers are specific to OICR and their use is optional. However, the ``core`` component required for all reports does have a parameter named ``input_params_file``. This is a hook used to populate the report ID. The core will use a manually specified report ID if one is present in the INI; if not, it will look for an input params file; if the file is not found, it will fall back to a randomly generated default ID.

.. _for example in our WGTS assay: https://github.com/oicr-gsi/djerba/tree/main/src/lib/djerba/helpers/input_params_helper

.. _full-config-file:

The Full Config File
--------------------

The "configure" or "report" modes of the main Djerba script write a file called ``full_config.ini`` to the output directory. This is the fully-specified INI file generated by the configure step, including any default values which are in use. It may be useful for future reference or troubleshooting.


Troubleshooting
===============

Djerba has been used to generate more than 2000 clinical reports at OICR (as of August 2026), and for the most part it runs smoothly. As with any software, users may experience issues from time to time, so we offer the following tips for troubleshooting.

1. Ensure the core Djerba application is functional, for instance by running with a :ref:`minimal INI file <minimal-example>`.
2. Consult the log output, by :ref:`running the main script <main-script-usage>` with ``--verbose`` or ``--debug`` enabled.
3. Consult the :ref:`full config file <full-config-file>`, if any, to check all parameters are as expected.
4. Check existing `issues on Github`_, to see if your issue is already known or has a workaround.
5. You can :ref:`contact the Djerba developers <contact-us>`:
   
   a. Bug reports for general functions of Djerba are greatly appreciated, and we will do our best to fix them.
   b. We will also try to advise on user-specific issues, but we regret our capacity for external support is limited.

.. _issues on Github: https://github.com/oicr-gsi/djerba/issues
