from os import listdir,system
import py7zr

def extract_7z(path, name):
	archive = py7zr.SevenZipFile(f'{path}/{name}', mode='r')
	file_list = archive.getnames()
	archive.close()
	print("Archive {} has {} files inside:\n{}".format(name, len(file_list), "\n".join(file_list)+"\n"))
	for filename in file_list:
		archive = py7zr.SevenZipFile(f"{path}/{name}", mode='r', password=filename)
		archive.extract(targets=filename, path=f"{path}")
	archive.close()

files = listdir("_3-breakme.extracted")
for name in files:
	extract_7z("./_3-breakme.extracted", name)
system("cat {} > finale.7z".format(" ".join(["./_3-breakme.extracted/piece.7z.0{:0>2}".format(i) for i in range(1,len(files)+1)])))
extract_7z(".", "finale.7z")
print("---FINISHED---")
