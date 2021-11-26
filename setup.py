# *******************************************************************************
# Copyright (C) 2020-2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

#!/usr/bin/python
# -*- coding: latin-1 -*-
from setuptools import setup, find_packages
setup( name='tutorials',
       version='0.0.1.dev1',
       author='Ambra Di Piano',
       author_email='ambra.dipiano@inaf.it',
       packages=find_packages(),
       package_dir={'tutorials': 'tutorials'},
       include_package_data=True,
       license='BSD-3-Clause'
     )
