# Djerba Documentation

![Djerba](./source/images/djerba_logo_small.png)

[Djerba](https://github.com/oicr-gsi/djerba) is a modular system for generating clinical report documents from bioinformatics data. It was developed by the Clinical Genome Interpretation team at the [Ontario Institute for Cancer Research](https://oicr.on.ca/) in Toronto, Canada.

This repository is a resource for public documentation of Djerba, hosted on [ReadTheDocs](https://djerba.readthedocs.io/en/latest/).

## Installing the documentation

These docs are built with Python 3 and Sphinx. It's best to install and run within a Python virtual environment.

To install:
```
python3 -m pip install -r requirements.txt
```

To build:
```
make html
```

Open the local copy of the website at `build/html/index.html`

## Updating documentation

Documentation is written in reStructuredText. Here's a [primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).

## Deploy documentation to ReadTheDocs

Documentation pushed to the `main` branch is automatically built on RtD.

* Project page on RtD : https://app.readthedocs.org/projects/djerba/
* Latest documentation : https://djerba.readthedocs.io/en/latest/

## Copyright and License

Copyright &copy; 2020-2026 by Genome Sequence Informatics, Ontario Institute for Cancer Research.

Licensed under the [GPL 3.0 license](https://www.gnu.org/licenses/gpl-3.0.en.html).

