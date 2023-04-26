import string

count = 0
with open("custom_wordlist.txt", "w") as file:
	for l_upper in string.ascii_uppercase:
		for l_lower in string.ascii_lowercase:
			for l_number in string.digits:
				for l_special in string.punctuation:
					count += 1
					file.write(l_upper+l_lower+l_number+l_special+"\n")
print(f"Written {count} lines to wordlist.")
