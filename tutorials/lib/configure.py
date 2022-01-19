# *******************************************************************************
# Copyright (C) 2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

import yaml

class Configation:
    def __init__(self, filename):
        configuration = open(filename)
        self.conf = yaml.load(configuration, Loader=yaml.FullLoader)

    def get_configuration(self):
        return self.conf

    def set_parameter(self, key, value):
        self.conf[key] = value
        return self

    def get_parameter(self, key):
        return self.conf[key]
