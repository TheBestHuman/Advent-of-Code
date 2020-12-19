def check(original_array, current_parents, count_target, sum_target):
    print(current_parents)
    if len(current_parents)+1 == count_target:
        for val in original_array :
            val = int(val)
            if(val not in current_parents):
                sm = 0
                product = 1
                for parent in current_parents:
                    sm += parent
                    product *= parent
                sm += val
                if(sm == sum_target):
                    return product * val
                else:
                    return 0
    else:
        for val in original_array:
            if(val not in current_parents):
                new_parents = current_parents.copy()
                new_parents = new_parents.append(val)
                print(new_parents)
                retval = check(original_array, new_parents, count_target, sum_target)
                if(retval) != 0:
                    return retval


contents = open("day1.input","r").read()
content_array = contents.splitlines()

prod = check(content_array, [1], 3, 2020)
print(prod)