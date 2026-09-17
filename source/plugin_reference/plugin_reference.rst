.. _plugin-reference:

****************
Plugin Reference
****************

This section contains documentation for individual plugins.

Guide to Plugin Documentation
=============================

Documentation for plugins shares a common format.

At the top is a header with the top-level package name, the plugin name, and the plugin version.

We then have the following sections:

* **Summary**: Brief summary of what the plugin does
* **Specific parameters**: INI parameters specific to the plugin, with defaults
* **Generic parameters**: INI parameters common to all plugins, with defaults
* **Description**: Detailed description of the plugin


Plugin Parameters and Defaults
------------------------------

Plugin INI configuration parameters, and their default values, are presented in tables automatically generated from the plugin code.

In this context, a "default" is a simple, fixed value encoded in the plugin. A plugin may automatically pull in values from the Djerba workspace, database queries, or other resources; these are not considered to be defaults.
  
Two important default values are denoted as follows:

   * **N/A**: The parameter has no default, and must be filled in by an additional process or manually by the user.
   * **(empty)**: The parameter defaults to the empty string ``''``. This may be used to represent a null value; for example, if a plugin has no configuration dependencies, ``depends_configure`` is the empty string.

Other plugin defaults may be of any appropriate type, such as Booleans, integers, strings, etc.

The parameter tables also contain a **Notes** column, which may include further explanation and commentary by the Djerba developers.

Contents
========

.. toctree::
   :maxdepth: 1

   plugins/djerba/case_overview/djerba.case_overview.autodoc.rst
   plugins/djerba/wgts/snv_indel/djerba.wgts.snv_indel.autodoc.rst
   plugins/hmf_djerba/hmf/wgts/snv_indel/hmf_djerba.hmf.wgts.snv_indel.autodoc.rst



