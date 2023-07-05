<img src/kbmod="https://gist.githubusercontent.com/PWhiddy/d42e66a9dd8e4af205a706f388a90ed4/raw/ae5bb87ada12538289852b58ba8e54b564a81584/kbmod.svg?sanitize=true" alt="logo" width="400" height="160"/>

# LINCC Frameworks kbmod-utils

Sub-package of kbmod for sharing code among the kbmod package environment.

## Getting started

```
git clone https://github.com/dirac-institute/kbmod-utils.git
cd kbmod-utils
pip install .
```

To verify that the installation was successful run the tests:
```
pytest tests
```

Developers will want to install the package as editable with developer tools. This has additional requirements and capabilities.
```
pip install -e .[dev]
(cd docs && make html;) && open _readthedocs/html/index.html
```

## Acknowledgements

LINCC Frameworks is supported by Schmidt Futures, a philanthropic initiative
founded by Eric and Wendy Schmidt, as part of the Virtual Institute of 
Astrophysics (VIA).

This project was automatically generated using the LINCC-Frameworks [python-project-template](https://github.com/lincc-frameworks/python-project-template).

[![Template](https://img.shields.io/badge/Template-LINCC%20Frameworks%20Python%20Project%20Template-brightgreen)](https://lincc-ppt.readthedocs.io/en/latest/)

For more information about the project template see the [documentation](https://lincc-ppt.readthedocs.io/en/latest/).
