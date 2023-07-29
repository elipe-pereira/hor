#!/bin/bash
base_dir=`pwd`
dist_path="."
work_path="/tmp"
spec_path="/tmp/hor"
name="hor"

pyinstaller --distpath $dist_path\
        --add-data "$base_dir/conf:conf"\
        --workpath $work_path\
        --specpath $spec_path\
        --name $name main.py

test -d $spec_path && rm -rf $spec_path
