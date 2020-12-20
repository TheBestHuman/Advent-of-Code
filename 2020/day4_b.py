import re

def byr_validator(input):
    if re.match(r"^\d\d\d\d$", input) and \
        int(input) >= 1920 and \
        int(input) <= 2002:

        return True
    else:
        return False
def iyr_validator(input):
    if re.match(r"^\d\d\d\d$", input) and \
        int(input) >= 2010 and \
        int(input) <= 2020:

        return True
    else:
        return False
def eyr_validator(input):
    if re.match(r"^\d\d\d\d$", input) and \
        int(input) >= 2020 and \
        int(input) <= 2030:

        return True
    else:
        return False
def hgt_validator(input):
    cm_matcher = re.compile(r"^(\d\d\d)cm$")
    cm_height = cm_matcher.findall(input)
    if len(cm_height) > 0 and int(cm_height[0]) >= 150 and int(cm_height[0]) <= 193:
        return True
    else:
        in_matcher = re.compile(r"^(\d\d)in$")
        in_height = in_matcher.findall(input)
        if len(in_height) > 0 and int(in_height[0]) >= 59 and int(in_height[0]) <= 76:
            return True
        else:
            False
def hcl_validator(input):
    if re.match(r"^#[0-9a-f]{6}$", input):
        return True
    else:
        return False
def ecl_validator(input):
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if input in valid_colors:
        return True
    else:
        return False
def pid_validator(input):
    if re.match(r"^\d\d\d\d\d\d\d\d\d$", input):
        return True
    else:
        return False


contents = open("day4.input","r").read()

content_array = contents.split("\n\n")

required_fields = {"byr":byr_validator,
                    "iyr":iyr_validator,
                    "eyr":eyr_validator,
                    "hgt":hgt_validator,
                    "hcl":hcl_validator,
                    "ecl":ecl_validator,
                    "pid":pid_validator}

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

            current_required_field = list(rfi.keys())[0]
            if field[0] == current_required_field and rfi[current_required_field](field[1]):
                rfi.pop(current_required_field)
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



