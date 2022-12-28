#!/bin/bash
# Install
pip install -e ./mypackage
# Obtaining file:///projects/scripts/python/005_package/01_distribute_pack/mypackage
#  Preparing metadata (setup.py) ... done
#Installing collected packages: mypackage
#  Running setup.py develop for mypackage
#Successfully installed mypackage-1.0.0

# Uninstall
pip uninstall mypackage

# Found existing installation: mypackage 1.0.0
#Uninstalling mypackage-1.0.0:
#  Would remove:
#    projects/.venv/bin/capitalize
#    projects/.venv/lib/python3.10/site-packages/mypackage.egg-link
#Proceed (Y/n)? y
#  Successfully uninstalled mypackage-1.0.0
