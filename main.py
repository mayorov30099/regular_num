import re
file = open("tel.txt", "r")
for line in file:
    if re.findall(r'8[(]\d\d\d[)]\d\d\d-\d\d-\d\d\n', line) or (re.findall(r'8-\d\d\d-\d\d\d-\d\d-\d\d\n', line)):
        print(line)
file.close()
