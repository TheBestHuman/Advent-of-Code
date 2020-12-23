
contents = open("day6.input","r").read()

content_array = contents.split("\n\n")

final_sum = 0
for group in content_array:
    answers = [0] * 26
    rows = group.split("\n")
    
    for row in rows:
        for cr in row:
            ordinal = ord(cr) - 97 #ascii value of a
            answers[ordinal] += 1

    group_sum = 0
    for answer in answers:
        if(answer == len(rows)):
            group_sum += 1

    final_sum+=group_sum

print (final_sum)
