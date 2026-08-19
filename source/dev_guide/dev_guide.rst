

.. currently in a rough draft state, not to be included in TOC


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

.. _Python name token: https://docs.python.org/3/reference/lexical_analysis.html#names-identifiers-and-keywords

