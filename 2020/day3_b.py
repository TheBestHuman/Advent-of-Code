


def check_slope_scenario(content_array, right, down):
    linelen = len(content_array[0])
    
    current_line_number = 0

    rightpos = 0
    trees = 0

    while(current_line_number < len(content_array)):
        line = content_array[current_line_number]
        if line[rightpos] == "#":
            trees+=1

        rightpos = (rightpos + right) % linelen
        current_line_number += down
    return trees

contents = open("day3.input","r").read()
content_array = contents.splitlines()


trees = check_slope_scenario(content_array, 1,1) * \
        check_slope_scenario(content_array, 3,1) * \
        check_slope_scenario(content_array, 5,1) * \
        check_slope_scenario(content_array, 7,1) * \
        check_slope_scenario(content_array, 1,2)

print(trees)

