

.. currently in a rough draft state, not to be included in TOC



Other Command-Line Scripts
==========================

Other command-line scripts installed with Djerba include:

- [generate_ini.py](https://github.com/oicr-gsi/djerba/blob/main/src/bin/generate_ini.py): Generate a "blank" INI file for a named list of Djerba components. For regular use, this has been superseded by the `setup` mode of `djerba.py`. Retained for use by plugin developers.
- [mini_djerba.py](https://github.com/oicr-gsi/djerba/blob/main/src/bin/mini_djerba.py): Simplified script to update patient info and summary text in a Djerba report. Currently not supported, may be revived at a future date.
- [update_oncokb_cache.py](https://github.com/oicr-gsi/djerba/blob/main/src/bin/update_oncokb_cache.py): Update an offline cache of variant annotation, used for testing.
- [validate_plugin_json.py](https://github.com/oicr-gsi/djerba/blob/main/src/bin/validate_plugin_json.py): Check if plugin output is valid according to the Djerba JSON schema. Intended for plugin developers.

Run any script with `-h/--help` for details.
   

Detailed Rules
^^^^^^^^^^^^^^

A plugin identifier:
- **Must** be a valid `Python name token`_
- **Must not** be the string ``core`` or ``base``
- **Must** correspond to the position of the plugin in the Python `package hierarchy`_, eg. a plugin with identifier ``my_plugin`` and Python package ``djerba.plugins.my_plugin``
- **May** contain additional package levels separated by dots, eg. a plugin with identifier ``foo.bar`` and Python package ``djerba.plugins.foo.bar``
- **Must not** end with the substring ``_helper`` or ``_merger``

A helper identifier is similar, but **must** end with the substring ``_helper``.

A merger identifier is similar, but **must** end with the substring ``_merger``.

.. _package hierarchy: https://docs.python.org/3/tutorial/modules.html#packages
.. _Python name token: https://docs.python.org/3/reference/lexical_analysis.html#names-identifiers-and-keywords

