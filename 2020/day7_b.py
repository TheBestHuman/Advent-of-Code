import re


def traverse(bag_type, contains_dict, include_self = True):
    iter_count = 0
    if bag_type not in contains_dict or "no other" in contains_dict[bag_type]:       
        return 1

    for contains_entry in contains_dict[bag_type].keys():
        iter_count += int(contains_dict[bag_type][contains_entry]) * traverse(contains_entry, contains_dict)
   
    if(include_self):
        iter_count += 1

    return iter_count

contents = open("day7.input","r").read()

content_array = contents.split("\n")


container_matcher = re.compile(r"(.*)bags contain")
contained_matcher = re.compile(r"(contain |, )(\d*)(.*?)bag[s]?")

contains = {}
for content in content_array:
    container_matches = container_matcher.findall(content)
    contained_matches = contained_matcher.findall(content)

    container_key = container_matches[0].strip().replace(",", "").replace(".","")

    for contained_match in contained_matches:
        contained_key = contained_match[2].strip().replace(",", "").replace(".","")
        if(not container_key in contains):
            contains[container_key] = {}
        
        contains[container_key][contained_key] = contained_match[1]


count = traverse("shiny gold", contains, False)
print(count)