# *******************************************************************************
# Copyright (C) 2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

import numpy as np

class MyLib():
    def __init__(self) -> None:
        pass

    def set_pointing(self, ra, dec):
        self.pointing = dict(ra=ra, dec=dec)
        return self

    def get_pointing(self):
        assert isinstance(self.pointing) is True, 'self.pointing has not been set.'
        return self.pointing

    def set_target(self, ra, dec):
        self.target = dict(ra=ra, dec=dec)
        return self

    def get_target(self):
        assert isinstance(self.target) is True, 'self.target has not been set.'
        return  self.target

    def set_offaxis(self, offset):
        self.offaxis = offset
        return self

    def get_offset(pointing, target):
        if type(pointing) is dict:
            pointing = (pointing['ra'], pointing['dec'])
        if type(target) is dict:
            target = (target['ra'], target['dec'])
        assert (type(pointing) and type(target)) is tuple or list, 'coordinates should be set as tuple = (RA, DEC) for target and pointing.'
        radius = np.sqrt((pointing[0]-target[0])**2 + (pointing[1]-target[1])**2)
        return radius

    def get_on_region(self, radius):
        assert type(self.target) == dict, 'target has not been set.'
        self.target['rad'] = radius
        return

    def get_off_regions(self, method):
        assert method.lower() in ('cross', 'wobble', 'reflection'), 'invalid method.'
        if method.lower() in ('cross', 'wobble'):
            regions = self.cross_regions()
        else:
            regions = self.reflected_regions()
        return regions

    def cross_regions(self):
        return

    def reflected_regions(self):
        return

