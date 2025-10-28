### Hexlet tests and linter status:
[![Actions Status](https://github.com/annetmyshkina/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/annetmyshkina/python-project-50/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=annetmyshkina_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=annetmyshkina_python-project-50)

[![Python CI](https://github.com/annetmyshkina/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/annetmyshkina/python-project-50/actions/workflows/pyci.yml)

# Difference generator
#### Compares two configuration files and shows a difference.

[![asciicast](https://asciinema.org/a/ZxJbpt0p7f7JP2Bsuj3lUMhau.svg)](https://asciinema.org/a/ZxJbpt0p7f7JP2Bsuj3lUMhau)
[![asciicast](https://asciinema.org/a/BWtGpyV31ltWDV7M2GA7CPtQF.svg)](https://asciinema.org/a/BWtGpyV31ltWDV7M2GA7CPtQF)


### Installation

install the project via [pip](https://pypi.org/project/pip/)

```bash
pip install --user git+https://github.com/annetmyshkina/python-project-50.git
```

or clone the repository:

```bash
git clone https://github.com/annetmyshkina/python-project-50.git
cd python-project-50
```

### Usage
    gendiff -f stylish data/file1.json data/file2.json
    gendiff -f plain data/file1.json data/file2.json
    gendiff -f json data/file1.json data/file2.json


    gendiff -f stylish data/YML_file1.yml data/YML_file2.yml
    gendiff -f plain data/YML_file1.yml data/YML_file2.yml
    gendiff -f json data/YML_file1.yml data/YML_file2.yml

### Running tests
    make test
