import os
import json

path = os.path.dirname(os.path.abspath(__file__))
flag_path = os.path.join(path, "src", "flags")

table = {}
styles = [
	"apple",
	"facebook",
	"google",
	"joypixels",
	"lg",
	"openmoji",
	"samsung",
	"skype",
	"twitter",
	"whatsapp"
]

for style in styles:
	table[style] = []
	for f in os.listdir(os.path.join(flag_path, style)):
		if f != "unknown.png":
			table[style].append(".".join(f.split(".")[:-1]))

# this needs to be copy pasted manually for now
print(json.dumps(table))
