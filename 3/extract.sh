#pip3 install py7zr
if [ -d "./_3-breakme.extracted" ]; then rm -rf ./_3-breakme.extracted; fi
binwalk 3-breakme -e -D '7-zip archive data, version 0.4'
python3 code.py
rm -rf ./_3-breakme.extracted
rm finale.7z
cat kintsugi.txt
