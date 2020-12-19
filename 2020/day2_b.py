
contents = open("day2.input","r").read()
content_array = contents.splitlines()

total_valid = 0
for line in content_array:
    inp = line.split(": ")
    rule = inp[0]
    pw = inp[1]
    amount = rule.split(" ")
    ranges = amount[0].split("-")
    min_place = int(ranges[0])
    max_place = int(ranges[1])
    char = amount[1]
    char_count = 0
    if len(pw) > max_place-1:
        
        if ((pw[min_place-1] == char) and pw[max_place-1] != char) or \
            ((pw[min_place-1] != char) and pw[max_place-1] == char):
            
            total_valid+=1


print(total_valid)