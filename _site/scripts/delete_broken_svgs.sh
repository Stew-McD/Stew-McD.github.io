#!/bin/bash

dir=$1

for file in "$dir"/*.svg
do
    xmllint --noout "$file"
    if [ $? -ne 0 ]; then
        echo "Invalid SVG file detected: $file. Deleting..."
        rm "$file"
    fi
done