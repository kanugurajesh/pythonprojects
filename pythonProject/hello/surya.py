import json

# python object(dictionary) to be dumped
dict1 ={
	('addresss', 'street'):'Brigade road',
}

# the json file where the output must be stored
out_file = open("myfile.json", "w")

json.dump(dict1, out_file, indent = 6,skipkeys=True)
# ship keys endure some things
out_file.close()
# import antigravity
# print(antigravity)
# the above thing has cool function
# it takes you to an website for coding

print("print","print","print",sep="-")
print("seperators are used for many scenerios")
# so with no delay let's begin our journey
import json
dict2 = {"hello":2,"man":3,"kello":4,"joy":2}
# using sort_keys we can generally sort the words in a miraculous way sor_keys is used to sort words
out = open("myne.json","w")
json.dump(dict2,out,sort_keys=True)
out.close()
p = open("myne.json")
print(p.readlines())
# python is used to type in various languages
# hello guys today we are going to learn about some weird functions which can be used in many scenario's so with
# no delay so with no delay let's begin the programming
# dump is one of the things you can use to provide a syntax many things so with no delay let's begin our work
# let's learn using ascii
print(ascii("$"))
# the function of ascii is to replace non-ascii-characters with escape characters
import json
# dictionary to be dumped
d = {'lang':'??? ????'}

with open('myfile.json', 'w', encoding ='utf8') as json_file:
	json.dump(d, json_file, ensure_ascii = False)
m = open('myfile.json','r')
print(m.readlines())
# see we have accomplished the language
# okay let's begin our program from beginning