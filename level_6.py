import zipfile
import os
path = os.path.join(os.getcwd(), "channel")

with zipfile.ZipFile("channel.zip") as zipped_file:
    zipped_file.extractall("channel")

element_to_found = []
for file in os.listdir(path):
    current_file = os.path.join(path,file)
    if os.path.isfile(current_file):
        with open(current_file, "r") as f:
            data = f.read().split()
            if "Next" not in data:
                 element_to_found.append(data)

# We obtain sentence "Collect the comments". That's mean there are comments in zipfile.
commentaire = []
start_with = "90052"
with zipfile.ZipFile("channel.zip") as zipped_file:
    while True:
        current_file = start_with + ".txt"
        data = zipped_file.read(current_file).decode("utf-8").split()
        commentaire.append(zipped_file.getinfo(current_file).comment.decode("utf-8"))
        if "Next" in data:
            start_with = data[-1]
        else:
            break
    
print("".join(commentaire))



