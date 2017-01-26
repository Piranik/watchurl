#!/bin/bash
cat $1 | sort | uniq > $1.sorted
cat $2 | sort | uniq > $2.sorted
git diff --word-diff=porcelain $1.sorted $2.sorted | sed -e 's/([^()]*)//g' | sed -e 's/([^()]*)//g' | grep -e '^+\|^-' | awk -F' ' 'NF>=6 {print}' | sed 's/^.//'
