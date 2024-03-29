'''
usage: python findAIProjects.py <lang> <module>
<lang>: must as the line 12-55
'''

import subprocess
import sys

lang = sys.argv[1].lower()
module = sys.argv[2]

if lang == "cob":
	dir_lang = "Cob"
elif lang == "cs":
	dir_lang = "CS"
elif lang == "c" or lang == "cpp":
	dir_lang = "C"
elif lang == "erlang":
	dir_lang = "Erlang"
elif lang == "fml":
	dir_lang = "Fml"
elif lang == "fortran":
	dir_lang = "F"
elif lang == "go":
	dir_lang = "Go"
elif lang == "ipynb":
	dir_lang = "ipy"
elif lang == "java":
	dir_lang = "java"
elif lang == "julia":
	dir_lang == "jl"
elif lang == "js":
	dir_lang = "JS"
elif lang == "lua":
	dir_lang = "Lua"
elif lang == "lisp":
	dir_lang = "Lisp"
elif lang == "php":
	dir_lang = "php"
elif lang == "pl":
	dir_lang = "pl"
elif lang == "py":
	dir_lang = "PY"
elif lang == "rb":
	dir_lang = "rb"
elif lang == "r":
	dir_lang = "R"
elif lang == "rs":
	dir_lang = "Rust"
elif lang == "scala":
	dir_lang = "Scala"
elif lang == "sql":
	dir_lang = "Sql"
elif lang == "swift":
	dir_lang = "Swift"

for i in range(32):
	#print("Reading gz file number " + str(i))
	command = "zcat /da0_data/play/" + dir_lang + "thruMaps/c2bPtaPkgP" + dir_lang + "." + str(i) + ".gz"
	p1 = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	p2 = subprocess.Popen('egrep -w ' + module, shell=True, stdin=p1.stdout, stdout=subprocess.PIPE)
	output = p2.communicate()[0]
	
	if output != "":
		for entry in str(output).rstrip("\n").split("\n"):
			line = str(entry)
			entry = str(entry).split(";")
			repo = entry[1]
			for word in entry[5:]:
				if module in word:
					print(line)
					#PInfoFile.write(line+"\n")
					break
