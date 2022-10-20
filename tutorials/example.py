# *******************************************************************************
# Copyright (C) 2021 INAF
#
# This software is distributed under the terms of the BSD-3-Clause license
#
# Authors:
# Ambra Di Piano <ambra.dipiano@inaf.it>
# *******************************************************************************

import argparse
import warnings
from tutorials.lib.mylib import MyLib
from tutorials.lib.utils import raise_error, throw_warning

parser = argparse.ArgumentParser(description='Exemple on the use of ARGPARSE')
parser.add_argument('-t', '--topic', type=str, required=True, choices=['argparse', 'yaml', 'logging', 'error', 'classes'])
parser.add_argument('-s', '--source', type=str, default='crab', choices=['crab', 'grb', 'vela'], help="source to simulate")
parser.add_argument('-ra', type=float, default=83.6331, help='right ascension of source')
parser.add_argument('-dec', type=float, default=22.0145, help='declination of source')
parser.add_argument('-f', '--file', type=str, help='configuration file')
parser.add_argument('-l', '--loglevel', type=str, default='debug', choices=['debug', 'info', 'warning', 'error', 'critical'], help='logging level')
args = parser.parse_args()

# you can access inputs like attributes
if args.topic.lower() == 'argparse':
    # print the input given at execution
    print(f'Source name: {args.source}')
    print(f'RA = {args.ra}')
    print(f'DEC = {args.dec}')

# load the configuration from external file
if args.topic.lower() == 'yaml':
    from tutorials.lib.configure import Configation
    # load the configuration from file
    config = Configation(filename=args.file).get_configuration()
    # print the input given via configuration file
    print(f'Source name: {config["source"]}')
    print(f'RA = {config["ra"]}')
    print(f'DEC = {config["dec"]}')

# logging levels and print outputs on terminal or file
if args.topic.lower() == 'logging':
    import logging
    # define format
    logformat='%(asctime)s|%(name)s|%(levelname)s|%(message)s'
    if args.file != None:
        # log to file with given logging level
        logging.basicConfig(filename=args.file, format=logformat)
    else:
        # log to terminal with given logging level
        logging.basicConfig(format=logformat)
    log = logging.getLogger(__file__)
    level = logging.getLevelName(args.loglevel.upper())
    log.setLevel(level)
    log.debug('code diagnostic useful for debugging and development')
    log.info('useful information about the execution')
    log.warning('something unexpected might happen or has happened')
    log.error('an error was encountered')
    log.critical('a serious error was encountered hindering the execution')

# rising and handling errors, asserting, try and except
if args.topic.lower() == 'error':
    # assert : verify a condition, i.e. that a parameter is float
    assert type(args.source) == str, 'this variable must be a string'
    # throw warning from function
    throw_warning()
    # throw warning from __main__
    warnings.warn('this is a syntax warning', category=SyntaxWarning)
    # handle errors with try/except sintax
    try:
        # this function raises an error if you pass something else than None
        raise_error(1)
    except:
        # instead or raising the error (which stops execution) print
        print('this way you can handle errors')
    
# classes and method chaining
if args.topic.lower() == 'classes':
    # instantiate the class
    my_object = MyLib()
    # phrase a simple arithmetic operation
    operation = my_object.set_value(5).add(2).multiply_by(3).divide_by(5).add(-3).output_result()
    print(f'Result of [(5+2)*3/5]-3 = {operation}')

