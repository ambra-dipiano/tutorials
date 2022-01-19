# *******************************************************************************
# Copyright (C) 2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

import argparse

parser = argparse.ArgumentParser(description='Exemple on the use of ARGPARSE')
parser.add_argument('-t', '--topic', type=str, required=True, choices=['argparse', 'yaml', 'logging', 'error'])
parser.add_argument('-s', '--source', type=str, default='crab', choices=['crab', 'grb', 'vela'], help="source to simulate")
parser.add_argument('-ra', type=float, default=83.6331, help='right ascension of source')
parser.add_argument('-dec', type=float, default=22.0145, help='declination of source')
parser.add_argument('-f', '--configfile', type=str, help='configuration file')
args = parser.parse_args()

# you can access inputs like attributes
if args.topic.lower() == 'argparse':
    # print the input given at execution
    print(f'Source name: {args.source}')
    print(f'RA = {args.ra}')
    print(f'DEC = {args.dec}')

if args.topic.lower() == 'yaml':
    from tutorials.lib.configure import Configation
    config = Configation(filename=args.configfile).get_configuration()
    print(f'Source name: {config["source"]}')
    print(f'RA = {config["ra"]}')
    print(f'DEC = {config["dec"]}')