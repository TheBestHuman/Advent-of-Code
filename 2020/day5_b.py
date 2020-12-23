import math

def incrementor(min, max, content_char, towards_zero_char):
    if(content[i] == towards_zero_char):
        max = math.floor((max-min)/2) + min
    else:
        min = math.ceil((max-min)/2) + min 
    return min, max

def create_possibility_dictionary():
    possibilities = {}
    for row in range(0,128):
        for seat in range(0,8):
            possibilities[(row * 8) + seat] = False
    return possibilities


contents = open("day5.input","r").read()

content_array = contents.split("\n")

max = 127
min = 0

max_seat_id = 0
possibilities = create_possibility_dictionary()
for content in content_array:
    max = 127
    min = 0

    for i in range(0,7):
        min, max = incrementor(min, max, content[i], 'F')

    row = max

    min = 0
    max = 7
    for i in range(7,10):
        min, max = incrementor(min, max, content[i], 'L')
    
    seat = max

    seat_id = (row * 8) + seat
    possibilities[seat_id] = True
    if seat_id > max_seat_id:
        max_seat_id = seat_id
start_checking = False
for ky in possibilities.keys():
    if possibilities[ky] == True:
        start_checking = True
    if start_checking and possibilities[ky] == False:
        print(ky)
        break


