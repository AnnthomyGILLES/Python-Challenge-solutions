import urllib.request
import re
with urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html") as response:
	html=response.read().decode("utf-8")

# Method 1
regex=re.compile("[^a-zA-Z]")
extraction="[^a-zA-Z]".sub('',html)
print(extraction)

# Method 2
print("".join(re.findall("[A-Za-z]", html)))
