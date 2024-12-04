[![Testing](https://github.com/sbradnam/open_nsafe/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/sbradnam/open_nsafe/actions/workflows/python-package.yml)
[![codecov](https://codecov.io/gh/sbradnam/open_nsafe/graph/badge.svg?token=9RHSDIUE7O)](https://codecov.io/gh/sbradnam/open_nsafe)

# Open NSafe

An open data visualisation repository developed for nuclear applications.

## Requirements
- Linux or MacOSX operating system.
- Python >= 3.10 installation.

## Installation

We reccomend that Open NSafe is installed within a python virtual environment, to ensure any dependencies do not interfere with the global python environment.

```
python3 -m venv open_nsafe_venv
source open_nsafe_venv/bin/activate
pip3 install --upgrade pip
```

Once the virtual environment is set up, clone and install Open NSafe into the virtual environment.

```
git clone https://github.com/JADE-V-V/JADE.git
cd open_nsafe
pip3 install .
```

After the initial installation, to use Open NSafe in the future, the user will only have to activate the virtual environment, by navigating to the folder containing the virtual environment, and running `source open_nsafe_venv/bin/activate`.
