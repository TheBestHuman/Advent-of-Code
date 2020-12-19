


contents = open("day1.input","r").read()
content_array = contents.splitlines()

for a in content_array:
    for b in content_array:
        for c in content_array:
            if(int(a) + int(b) + int(c) == 2020):
                print (f"{int(a) * int(b) * int(c)}")
                exit()
