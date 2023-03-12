#!/bin/bash

echo "Name of a file or a directory:"
read name
if [ -d $name ];
then
    echo "$name is directory"
else
    echo "$name is not a directory"
fi
ls -l $name