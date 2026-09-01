
**********************
Introduction and FAQ
**********************

What is Djerba?
===============

`Djerba`_ is a system for generating `report documents`_ from data, with a modular structure based on *plugins*. It is named after a `Mediterranean island`_ and pronounced "jerba" (the initial letter D is silent).

.. _Djerba : https://github.com/oicr-gsi/djerba/tree/main
.. _report documents : https://github.com/oicr-gsi/djerba/blob/main/examples/WGS/PLACEHOLDER-v1_report.clinical.pdf
.. _Mediterranean island : https://en.wikipedia.org/wiki/Djerba

Who is Djerba for?
==================

`Djerba`_ was developed by the Clinical Genome Interpretation (CGI) team at the `Ontario Institute for Cancer Research`_ (OICR) in Toronto, Canada. It has been in use since 2021 to produce `accredited clinical reports`_.

The CGI team is part of Genome Sequence Informatics (GSI), which in turn is part of the `Joint Genomics Program`_ at OICR. GSI has developed a large suite of open-source software, including a number of tools used alongside Djerba to deliver bioinformatic analysis and reporting. The software can be found under the Github organizations `oicr-gsi`_ and `miso-lims`_, and is documented on the `GSI ReadTheDocs`_ site.

Djerba is open-source and we encourage its use beyond OICR. For example, CGI is collaborating on Djerba with teams at `McGill University`_ in Montreal and the `University of Calgary`_.

.. TODO link to Contact section

.. _Genome Sequence Informatics: https://oicr-gsi.readthedocs.io/en/latest/index.html
.. _Ontario Institute for Cancer Research: https://oicr.on.ca/
.. _accredited clinical reports: https://genomics.oicr.on.ca/our-mission/

.. _Joint Genomics Program: https://genomics.oicr.on.ca/
.. _oicr-gsi: https://github.com/oicr-gsi
.. _miso-lims: https://github.com/miso-lims
.. _GSI ReadTheDocs: https://oicr-gsi.readthedocs.io/en/latest/index.html

.. _McGill University: https://www.goodmancancer.ca/en/about-us
.. _University of Calgary: https://cumming.ucalgary.ca/research/cat/health-genomics/contact-us


Why was Djerba developed?
=========================

Bioinformatics analysis typically consists of a pipeline made up of multiple workflows, with output in structured data files (for example: the `ICGC-ARGO`_ pipeline). The data may be in general-purpose formats such as `TSV`_ or `JSON`_, or more specialized ones such as `BED`_ or `VCF`_. Pipeline outputs are a comprehensive source of information; but they are not easily read by humans, and key facts are split across multiple output files.

The purpose of `Djerba`_ is to produce a *report*, accomplishing three main tasks:
  1. *Collate:* Gather information from multiple files into a self-contained document.
  2. *Annotate*: Query databases to determine which genomic variants are clinically significant.
  3. *Summarise:* Present the most relevant information to the user, in a clear and readable format.

The report document is output in both machine-readable and human-readable formats. The reporting process is largely automated, but also allows contributions from human interpreters.

A key feature of Djerba is *flexibility*, to keep up with the rapid pace of change in bioinformatics. Its modular structure enables reporting to be quickly updated as requirements evolve. For example, as of 2026 the CGI team is developing a `new set of Djerba plugins`_ compatible with the `Hartwig Medical Foundation`_ analysis pipeline.

.. _ICGC-ARGO: https://docs.icgc-argo.org/docs/analysis-workflows/analysis-overview
.. _TSV: https://www.loc.gov/preservation/digital/formats/fdd/fdd000533.shtml
.. _JSON: https://www.w3schools.com/js/js_json.asp
.. _BED: https://useast.ensembl.org/info/website/upload/bed.html
.. _VCF: https://samtools.github.io/hts-specs/VCFv4.2.pdf
.. _new set of Djerba plugins: https://github.com/oicr-gsi/hmf_djerba
.. _Hartwig Medical Foundation: https://www.hartwigmedicalfoundation.nl/en/

What does Djerba do?
====================

Djerba is a command-line application, written primarily in `Python`_ and run in a `Linux`_ environment. It operates as follows:

* Djerba inputs a *config file* and outputs a *report*.
* The *config file* is in the widely-used `INI format`_.
* The *report* contains equivalent information in three different formats:
  
  1. `JSON`_ is a machine-readable format for the report data.
  2. `HTML`_ is used for typesetting, to specify the report appearance.
  3. `PDF`_ is shared with end users, such as clinical practicioners.

.. _Python: https://www.python.org/
.. _Linux: https://www.linux.org/
.. _INI format : https://docs.python.org/3/library/configparser.html
.. _HTML : https://www.w3schools.com/html/html_intro.asp
.. _PDF : https://www.adobe.com/ca/acrobat/about-adobe-pdf.html
 
What are Djerba plugins?
========================

Djerba plugins allow flexible generation of reports according to project requirements.

A plugin is a component of Djerba which has its own section in the INI config file, and generates its own JSON and HTML output. The HTML generated by multiple plugins is combined into a single HTML document, and then converted to PDF. The set of plugins used to generate a report can be changed by simply editing the config file. The main Djerba repository contains `plugins`_ developed by the CGI team, but Djerba also supports importing plugins from external sources.

The core Djerba code is written in `Python`_. Plugins have a common structure, which serves as a wrapper around plugin-specific functions. Djerba plugins may use other languages such as `R`_, executing commands within the Python wrapper.

.. TODO Link to External Plugins documentation.

.. _plugins: https://github.com/oicr-gsi/djerba/tree/main/src/lib/djerba/plugins
.. _R: https://www.r-project.org/

Can I change the appearance of report output?
=============================================

Yes! See the :ref:`document-configuration` section for details of how to specify the HTML header, footer and stylesheet.

Can I write my own plugins?
===========================

Yes! Our collaborators have successfully written plugins and deployed them to generate their own reports. When Djerba was originally developed, a high priority was making its structure as clear and straightforward as possible, to allow new plugins to be written and existing ones to be modified.

In the future, we intend to add a "Developer's Guide" to this documentation. For now, the existing `Djerba plugins`_ provide a wealth of examples showing how it can be done.

Please note Djerba is free software `licensed under GPL 3.0`_. There is *no warranty* for Djerba, and any software which copies or modifies code from Djerba is also affected by the terms of the license.

.. _Djerba plugins: https://github.com/oicr-gsi/djerba/tree/main/src/lib/djerba/plugins
.. _licensed under GPL 3.0: https://github.com/oicr-gsi/djerba/blob/main/LICENSE

What should I read next?
========================

:doc:`../how_djerba_works/how_djerba_works` covers key concepts and terminology. We recommend it as a starting point for all Djerba users.

The :doc:`../user_guide/user_guide` describes how to install Djerba, and run existing plugins to produce reports.

.. TODO We encourage users to write their own plugins, as described in the Developer Guide.

.. TODO The Component Reference has detailed descriptions of plugins and other components of Djerba, used for clinical reporting at OICR.

:doc:`../contact/contact` includes how to reach the Djerba developers, and some brief notes on development policy.


Copyright and Licensing
=======================

Djerba is copyright © 2020-2026 by Genome Sequence Informatics, `Ontario Institute for Cancer Research`_. All rights reserved.

Licensed under the `GPL 3.0 license`_.

.. _Genome Sequence Informatics: https://oicr-gsi.readthedocs.io/en/latest/index.html
.. _Ontario Institute for Cancer Research: https://oicr.on.ca/
.. _GPL 3.0 license: https://www.gnu.org/licenses/gpl-3.0.en.html
