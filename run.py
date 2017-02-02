import os
import json
import uuid

import requests

tempFiles = []
tempFiles.append(str(uuid.uuid4()))
r = requests.get("https://cowyo.com/test1/v?version=0")
with open(tempFiles[-1],"w") as f:
	f.write(r.text)

tempFiles.append(str(uuid.uuid4()))
r = requests.get("https://cowyo.com/test1/v?version=1")
with open(tempFiles[-1],"w") as f:
	f.write(r.text)

os.system('./fix.sh %s %s' % (tempFiles[0],tempFiles[1]))
tempFiles.append("%s.%s" % (tempFiles[0],tempFiles[1]))

for f in tempFiles:
	os.remove(f)