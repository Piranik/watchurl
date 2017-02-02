#!/bin/bash
html2text -width 10000 -o $1.txt $1
html2text -width 10000 -o $2.txt $2
cat $1.txt | sort | uniq > $1.sorted
cat $2.txt | sort | uniq > $2.sorted
git diff --no-index --word-diff=porcelain $1.sorted $2.sorted > $1.$2
#| sed "s/|//g" | sed "s/_/ /g" | sed -e 's/\[[^][]*\]//g' | sed 's/([^)]*)//g' | sed 's/[0-9]*//g' | awk -F' ' 'NF>=7 {print}' | sed "s/[[:space:]]\+/ /g"
# | sed -e 's/([^()]*)//g' | sed -e 's/([^()]*)//g' | grep -e '^+\|^-' | awk -F' ' 'NF>=6 {print}' | sed 's/^.//'
rm $1.sorted $2.sorted
rm $1.txt $2.txt

