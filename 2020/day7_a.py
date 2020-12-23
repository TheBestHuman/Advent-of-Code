import re


def traverse(bag_type, contained_by_dict, possible_containers, include_self = True):
    if bag_type not in contained_by_dict:
        if(include_self):
            possible_containers[bag_type] = 1
        return possible_containers
    elif bag_type in possible_containers:
        return possible_containers

    if(include_self):
        possible_containers[bag_type] = 1

    for contained_by_entry in contained_by_dict[bag_type].keys():
        possible_containers = traverse(contained_by_entry, contained_by_dict, possible_containers)
    
    return possible_containers

contents = open("day7.input","r").read()

content_array = contents.split("\n")


container_matcher = re.compile(r"(.*)bags contain")
contained_matcher = re.compile(r"(contain |, )(\d*)(.*?)bag[s]?")

contained_by = {}
for content in content_array:
    container_matches = container_matcher.findall(content)
    contained_matches = contained_matcher.findall(content)

    container_key = container_matches[0].strip().replace(",", "").replace(".","")

    for contained_match in contained_matches:
        contained_key = contained_match[2].strip().replace(",", "").replace(".","")
        if(not contained_key in contained_by):
            contained_by[contained_key] = {}
        
        contained_by[contained_key][container_key] = 1


possible_containers = traverse("shiny gold", contained_by, {}, False)
print(len(possible_containers))