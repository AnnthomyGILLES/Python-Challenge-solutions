import re
import urllib.request

regex=re.compile("and the next nothing is (\d+)")
code=str(25357)
while True:
	# Extract data
	with urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+code) as response:
		html=response.read().decode("utf-8")
	print(html)
	if re.search(regex,html) is not None:
		extraction=regex.findall(html)
		code="".join(extraction)
	else:
		break
