import re

def deleteContent(f):
    f.seek(0)
    f.truncate()

r = open('test.md', 'r')
f = open('Code.py', 'w+')
deleteContent(f)
re.DOTALL=true
m = re.search('```python\n(.*?)```', a)
print m.group(0)

# python Code.py

# iscode=0
# iscomment=1
# rm /tmp/code

# docstring
# vars
# text speader
# executor in next version
# one ` in next version
# in this version use it like markdown python script.mdpy

# while read -r line ; do
# #while [ -z "$eof" ]; do
# #    read SCRIPT_SOURCE_LINE || eof=true   ## detect eof, but have a last round
#     if [[ SCRIPT_SOURCE_LINE -eq "```" && iscode == 0 ]]; then
# 	iscode=1
# 	iscomment=1
#     fi

#     if [[ SCRIPT_SOURCE_LINE -eq "```" && iscode == 1 ]]; then
#         iscode=0
# 	iscomment=1
#     fi

#     if ! [[ SCRIPT_SOURCE_LINE -eq "```" ]]; then
#         iscomment=0
#     fi


#     if [[ iscode == 1 && iscomment == 0 ]]; then 
#     	echo "$SCRIPT_SOURCE_LINE" >> /tmp/code
# done < "$1"


