import re

contents = open("day4.input","r").read()

content_array = contents.split("\n\n")

required_fields = ["byr",
                    "iyr",
                    "eyr",
                    "hgt",
                    "hcl",
                    "ecl",
                    "pid"]

count = 1
validcount = 0
for content in content_array:
    content += '\n'
    kvp_matcher = re.compile(r"([^:]*):([^\n^ ]*)[\n ]", re.MULTILINE | re.DOTALL)
    kvps = kvp_matcher.findall(content)

    rfi = required_fields.copy()
    while len(rfi) > 0:
        found = False
        for field in kvps:
            if(len(rfi) == 0):
                break
            if field[0] == rfi[0]:
                rfi.remove(rfi[0])
                found = True
        if not found:
            break
    if len(rfi) == 0:
        print(f"{count} valid")
        validcount += 1
    else:
        print(f"{count} invalid")

    count += 1

print(f"valid: {validcount}")

