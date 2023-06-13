#!/usr/bin/env python3

from autotest import filelist_test,res_code,announce_failure
from sys import argv

required = [#"README",
            "snake_main.py",
            "AUTHORS",
            ]

permitted = ["*.py"]
forbidden = ["game_display.py",
             "game_parameters.py"]
try:
    if filelist_test(argv[1], required, permitted, forbidden, format='zip'):
        announce_failure('',filelist=True)
except:
    res_code("zipfile",output="Testing zip file failed...")
    announce_failure('',filelist=True)
    exit(-1)
