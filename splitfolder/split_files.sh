#!/bin/bash

dir_size = 25000
dir_name = "label"
n=$((`find . -maxdepth 1 -type f | wc -l`/$dir_size + 1))

for i in `seq ` $n`;
do
    mkdir -p "$dir_names$i";
    find . -maxdepth 1 -type f | head -n $dir_size |zargs -i mv "{}" "$dir_names$i"
done
