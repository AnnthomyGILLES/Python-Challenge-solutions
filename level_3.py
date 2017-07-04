import re
import urllib.request

# Extract data
with urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html") as response:
	html=response.read().decode("utf-8")
# Compite regex
regex=re.compile("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+")
# Extract pattern
extraction=regex.findall(html)
print("".join(extraction))
