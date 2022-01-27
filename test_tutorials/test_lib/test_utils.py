# *******************************************************************************
# Copyright (C) 2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

import pytest 
from tutorials.lib.utils import *

def test_plus1():
    assert plus1(3) == 4

def test_str2bool():
    true = ['True', 'true', '1', 'yes', 'y']
    false = ['False', 'false', '0', 'no', 'n', 'null']
    error = [None, 1, 0, True, False, 'none']
    for val in true:
        assert str2bool(val) == True
    for val in false:
        assert str2bool(val) == False
    with pytest.raises(ValueError):
        for val in error:
            str2bool(val)
    