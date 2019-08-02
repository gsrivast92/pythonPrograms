import json
with open('resource/jsonFile.json') as handle:
	dictdump = json.loads(handle.read())
	for i in dictdump:
		print(dictdump[i])
