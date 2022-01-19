# *******************************************************************************
# Copyright (C) 2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

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
        raise ValueError('Input is not valid.')