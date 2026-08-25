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
| ``DJERBA_CORE_HTML_DIR``  | Directory            | No       | Location of templates and stylesheets for core HTML rendering                    |
+---------------------------+----------------------+----------+----------------------------------------------------------------------------------+
| ``DJERBA_PACKAGES``       | Colon-separated list | Yes      | Names of top-level Djerba packages; see [external plugins](FIXME)                |
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

Core Configuration Files
========================

Some core functions of Djerba are controlled using configuration files. These are distinct from the INI configuration file used to run Djerba and generate a report.

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

**Table 2**: Djerba core configuration files

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

.. _Djerba code repository: https://github.com/oicr-gsi/djerba/tree/main/src/lib/djerba/cor

**************
Running Djerba
**************


How to Produce a Report
=======================

The main command-line interface for Djerba is the ``djerba.py`` script, which has a number of subcommands or *modes* for different stages of the reporting process. The :doc:`How Djerba Works <../../how_djerba_works/how_djerba_works>` section has a :ref:`full description <user-interface>` of each mode and its purpose. In this section, we focus on the steps most commonly used to produce a report.

Main Script Usage
-----------------

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

Configuring the INI File
========================

TODO Example goes here



Other Command-Line Scripts
==========================

Other command-line scripts installed with Djerba include:

- [generate_ini.py](https://github.com/oicr-gsi/djerba/blob/main/src/bin/generate_ini.py): Generate a "blank" INI file for a named list of Djerba components. For regular use, this has been superseded by the `setup` mode of `djerba.py`. Retained for use by plugin developers.
- [mini_djerba.py](https://github.com/oicr-gsi/djerba/blob/main/src/bin/mini_djerba.py): Simplified script to update patient info and summary text in a Djerba report. Currently not supported, may be revived at a future date.
- [update_oncokb_cache.py](https://github.com/oicr-gsi/djerba/blob/main/src/bin/update_oncokb_cache.py): Update an offline cache of variant annotation, used for testing.
- [validate_plugin_json.py](https://github.com/oicr-gsi/djerba/blob/main/src/bin/validate_plugin_json.py): Check if plugin output is valid according to the Djerba JSON schema. Intended for plugin developers.

Run any script with `-h/--help` for details.
