#!/bin/env python

from optparse import OptionParser


def install(option, opt_str, value, parser):
    print("start install tool envs!")



if __name__ == "__main__":
    helpstr = '''
        %prog custom help string
    '''
    parser = OptionParser(helpstr, description='this program is a tool environments!', version='%prog 1.0')
    parser.add_option('-i', '--install', default='',dest='',action="callback",callback=install, help='start install tool environments')
    parser.add_option('-o', '--output',default='install.log', dest='FILENAME',  help='output install log to file')
    parser.add_option('-v',action="store_false", help='show program\'s version number and exit')
    
    (options, args) = parser.parse_args()