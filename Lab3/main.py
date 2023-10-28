def ex1(a_list, b_list):
    intersection = list(set(a_list) & set(b_list))
    union = list(set(a_list) | set(b_list))
    dif_a_b = list(set(a_list) - set(b_list))
    dif_b_a = list(set(b_list) - set(a_list))
    return intersection, union, dif_a_b, dif_b_a

def ex2(string):
    result = {}

    for char in string:
        if char in result:
            count = result[char]
            result[char] = count + 1
        else:
            result[char] = 1

    return result

def ex3(dict1, dict2):
    if type(dict1) is not type(dict2):
        return False

    if not (isinstance(dict1, dict) and isinstance(dict2, dict)
            or isinstance(dict1, list) and isinstance(dict2, list)):
        if dict1 != dict2:
            return False
    else:
        if len(dict1) != len(dict2):
            return False

        for key in dict1:
            if key not in dict2:
                return False

            value1 = dict1[key]
            value2 = dict2[key]

            if type(value1) != type(value2):
                return False

            if isinstance(value1, dict) and isinstance(value2, dict):
                if not ex3(value1, value2):
                    return False

            elif isinstance(value1, list) and isinstance(value2, list):
                if len(value1) != len(value2):
                    return False
                for i in range(len(value1)):
                    #list elements can also be dictionaries
                    if not ex3(value1[i], value2[i]):
                        return False

            elif isinstance(value1, set) and isinstance(value2, set):
                if len(value1) != len(value2):
                    return False

                aux = value2.copy()
                for element in value1:
                    if element not in aux:
                        return False
                    else:
                        aux.remove(element)
                if len(aux) != 0:
                    return False

            elif value1 != value2:
                return False

    return True

def ex4(tag, content, **args):
    result = "<" + tag + " "

    for key in args:
        result += key + "=" + "\"" + args[key] + "\"" + "\\ "

    result += ">" + content

    return result

def ex5(tuple_set, dict_to_validate):
    for rule in tuple_set:
        if len(rule) != 4:
            return "Invalid tuple"

        key = rule[0]
        prefix = rule[1]
        middle = rule[2]
        suffix = rule[3]

        if key not in dict_to_validate:
            return False

        if prefix != "":
            if not dict_to_validate[key].startswith(prefix):
                return False

        #middle can overlap with the prefix and the suffix but the string can't start or end with it
        if middle != "":
            if (middle not in dict_to_validate[key] 
                or dict_to_validate[key].index(middle) == 0
                or dict_to_validate[key].index(middle) == len(dict_to_validate[key]) - len(middle)):
                return False

        if suffix != "":
            if not dict_to_validate[key].endswith(suffix):
                return False

    return True

def ex6(lst):
    #unique includes the elements that appear more that 1 time in the list
    unique = set(lst)

    count = 0
    for element in unique:
        if lst.count(element) > 1:
            count += 1

    return (len(unique), count)

def ex7(*args):
    result = {}

    #make a list of all the sets
    sets = []
    index = 0
    for s in args:
        sets.append("ceva")
        sets[index] = s
        index += 1

    for i, e1 in enumerate(sets):
        for e2 in range(i+1, len(sets)):
            if len(e1) == 0 and len(sets[e2]) == 0:
                result["{} | {}"] = {}
                result["{} & {}"] = {}
                result["{} - {}"] = {}

            elif len(e1) == 0:
                result["{}" + f" | {sets[e2]}"] = sets[e2]
                result["{}" + f" & {sets[e2]}"] = {}
                result["{}" + f" - {sets[e2]}"] = {}
                result[f"{sets[e2]} - " + "{}"] = sets[e2]

            elif len(sets[e2]) == 0:
                result[f"{e1} | " + "{}"] = e1
                result[f"{e1} & " + "{}"] = {}
                result[f"{e1} - " + "{}"] = e1
                result[f"{sets[e2]} - {e1}"] = {}

            else:
                result[f"{e1} | {sets[e2]}"] = e1 | sets[e2]
                result[f"{e1} & {sets[e2]}"] = e1 & sets[e2]
                result[f"{e1} - {sets[e2]}"] = e1 - sets[e2]
                result[f"{sets[e2]} - {e1}"] = e1 - sets[e2]

    return result

def ex8(mapping):
    result = []

    current = mapping["start"]
    while current != "start" and current not in result:
        result.append(current)

        if current in mapping:
            current = mapping[current]
        else:
            return result

    return result

def ex9(*args, **more_args):
    count = 0
    
    for key in more_args:
        if more_args[key] in args:
            count += 1

    return count

def main():

    # ex1_a_list = [1, 2, 3, 4, 5]
    # ex1_b_list = [3, 4, 5, 6, 7]
    # intersection, union, dif_a_b, dif_b_a = ex1(ex1_a_list, ex1_b_list)
    # print("A intersected with B: ", intersection)
    # print("A reunited with B: ", union)
    # print("A - B: ", dif_a_b)
    # print("B - A: ", dif_b_a)

    # ex2_string = "Ana has apples."
    # result = ex2(ex2_string)
    # print(result)

    # ex3_dict1 = {"a": 1, "b": {"c": 2, "d": [3, 4, 5], "e": {1, 2, 3, 4}}}
    # ex3_dict2 = {"a": 1, "b": {"c": 2, "d": [3, 4, 5], "e": {1, 2, 3, 4}}}
    # result = ex3(ex3_dict1, ex3_dict2)
    # print(result)

    # result = ex4("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
    # print(result)

    ex5_rules = {("key1", "", "inside", ""), ("key3", "this", "not", "valid")}
    ex5_dict = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    result = ex5(ex5_rules, ex5_dict)
    print(result)

    # ex6_list = [1, 5, 2, 3, 1, 4, 5]
    # result = ex6(ex6_list)
    # print(result)

    # ex7_set1 = {1, 2}
    # ex7_set2 = {2, 3}
    # result = ex7(ex7_set1, ex7_set2, {})
    # print(result)

    # ex8_map = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
    # result = ex8(ex8_map)
    # print(result)
    
    # result = ex9(1, 2, 3, 4, x=1, y=2, z=3, w=5)
    # print(result)

if __name__ == "__main__":
    main()