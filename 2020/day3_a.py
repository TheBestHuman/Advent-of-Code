contents = open("day3.input","r").read()
content_array = contents.splitlines()

rightpos = 0
trees = 0

linelen = len(content_array[0])
for line in content_array:
    if line[rightpos] == "#":
        trees+=1
    
    rightpos = (rightpos + 3) % linelen

print(trees)

