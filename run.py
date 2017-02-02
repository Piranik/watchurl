import os
import json
import uuid

import requests

# tempFiles = []
# tempFiles.append(str(uuid.uuid4()))
# r = requests.get("https://news.ycombinator.com/item?id=13554065")
# with open(tempFiles[-1],"w") as f:
# 	f.write(r.text)

# tempFiles.append(str(uuid.uuid4()))
# r = requests.get("https://news.ycombinator.com/item?id=13554065")
# with open(tempFiles[-1],"w") as f:
# 	f.write(r.text)

# os.system('./fix.sh %s %s' % (tempFiles[0],tempFiles[1]))
# outputFile = "%s.%s" % (tempFiles[0],tempFiles[1])
# tempFiles.append(outputFile)

os.system("./fix.sh 1.html 2.html")
outputFile = "1.html.2.html"

output = open(outputFile,'r').read()
print("Changes:")
print("-"*30)
for i, section in enumerate(output.split("~")):
	if i == 0 or "@@" in section:
		continue
	sentence = ""
	for line in section.split("\n"):
		line = line.strip()
		if len(line) < 1:
			continue
		if line[0]=="+":
			sentence += " " + line[1:]
		elif line[0]=="-":
			continue
		else:
			sentence += " " + line
	sentence = sentence.strip()
	if len(sentence.split()) > 5:
		print(sentence)
		print("-"*30)

# for f in tempFiles:
# 	os.remove(f)