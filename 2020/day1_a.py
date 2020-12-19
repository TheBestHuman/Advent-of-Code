contents = open("day1.input","r").read()
content_array = contents.splitlines()


while len(content_array) > 0:
    first_num = int(content_array[0])
    content_array.remove(content_array[0])
    for second_num_str in content_array:
        second_num = int(second_num_str)
        if first_num + second_num == 2020:
            print(f"{first_num * second_num}")
            exit()

