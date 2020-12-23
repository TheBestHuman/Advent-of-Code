
contents = open("day6.input","r").read()

content_array = contents.split("\n\n")

final_sum = 0
for group in content_array:
    start_dict = [0] * 26
    rows = group.split("\n")
    for row in rows:
        for cr in row:
            ordinal = ord(cr) - 97 #ascii value of a
            start_dict[ordinal] = 1
    group_sum = sum(start_dict)
    final_sum+=group_sum

print (final_sum)
