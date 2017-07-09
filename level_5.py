import urllib.request
import pickle

with urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p") as response:
	banner=pickle.load(response)
for line in banner:
	l=[character*times for character,times in line]
	print("".join(l))
