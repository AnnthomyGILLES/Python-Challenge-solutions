import string

# Naive version
phrase="""g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb 
rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

my_dict=list(string.ascii_lowercase)
my_dict.extend(["a","b"])
convert=[my_dict[my_dict.index(elt)+2] if elt in my_dict else elt for elt in phrase]
print("".join(convert))


# Optimize solution
trans=str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
print(phrase.translate(trans))
