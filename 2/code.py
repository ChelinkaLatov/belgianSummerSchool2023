from string import punctuation
with open("wordlist.txt", "r") as file:
	names = [line.strip() for line in file.readlines()]

special_chars = punctuation
years = [str(y) for y in range(1950,2023)]

count = 0
with open("custom_wordlist.txt", "w") as file:
	for name in names:
		for special_char in special_chars:
			for year in years:
				if " " in name:
					file.write("".join(name.split(" ")).capitalize()+year+special_char+"\n")
				file.write(name.capitalize()+year+special_char+"\n")
				count += 1
print(f"{count} lines have be written to file")
