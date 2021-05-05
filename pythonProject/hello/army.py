# dictionary to be dumped
# import json
# d ={'lang':'??? ????'}
#
# with open('myafile.json', 'w', encoding ='utf8') as json_file:
# 	json.dump(d, json_file, ensure_ascii = False)
# json_file.close()

import json


# dictionary to be dumped
d ={'lang':False}

with open('myfile.json', 'w', encoding ='utf8') as json_file:
	json.dump(d, json_file, ensure_ascii = True)
json_file.close()
r = open("myafile.json","r")
print(r.read())
# finally we are done with the things we need
print(json.loads("false"))
print(json.loads("false"))
minister = {"hello":"json",
			"mission":False,
			"hellos":("420","120","520")}
print(json.dumps(minister))
r = open('myafile.json','r')
rp = json.load(r)
print(rp)
# hello guys today we are going to write a code
rp = {"msiion":False}
rpr = open("rpsr.py",'w')
json.dump(rp,rpr)
rpr.close()


