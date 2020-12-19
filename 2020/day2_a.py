
contents = open("day2.input","r").read()
content_array = contents.splitlines()

total_valid = 0
for line in content_array:
    inp = line.split(": ")
    rule = inp[0]
    pw = inp[1]
    amount = rule.split(" ")
    ranges = amount[0].split("-")
    min_instances = int(ranges[0])
    max_instances = int(ranges[1])
    char = amount[1]
    char_count = 0
    for pw_char in pw:
        if pw_char == char:
            char_count += 1

    if char_count >= min_instances and char_count <= max_instances:
        total_valid += 1 

print(total_valid)