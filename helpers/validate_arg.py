#!/usr/bin/python3
# coding: utf-8

def validate_arg(argv, pos=1):
    value = ""
    try:
        value = argv[pos]
    except IndexError:
        pass

    return value
