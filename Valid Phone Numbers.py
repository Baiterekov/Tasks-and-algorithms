f = open('file.txt', 'r')
valid_number = []
str_number = ""

for i in f:
	str_number = i.replace("\n", "")
	for j in str_number:
		if j=="-":
			valid_number.append(str_number)
			break
		if j=="(":
			valid_number.append(str_number)
			break

print(valid_number)