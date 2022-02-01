# *******************************************************************************
# Copyright (C) 2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

import warnings

def plus1(x):
    return x + 1

def str2bool(val):
    true = ['True', 'true', '1', 'yes', 'y']
    false = ['False', 'false', '0', 'no', 'n', 'null']
    if val in true:
        return True
    elif val in false:
        return False
    else:
        raise ValueError('input is not valid.')

def assert_error(val):
    assert val == None, 'input "val" is not NoneType'

def raise_error(val):
    try:
        val += None
    except:
        raise TypeError('you cannot sum NoneType values to input')

def raise_conditional_error(val):
    if val != None:
        print('do stuff')
    else:
        raise ValueError('val should be not None')

def throw_warning():
    warnings.warn('this is a deprecation warning', category=DeprecationWarning, stacklevel=2)
