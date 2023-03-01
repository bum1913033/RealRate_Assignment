import json

# define function to build a hierarchy based on given input and format the resulting output as required.
def build_hierarchy(paths):
    # create an empty dict to be populated
    hierarchy = {}
    # for each path split path into strings using '.' as separator
    for path in paths:
        # reminder: path_parts is a list!
        path_parts = path.split(".")
        # set current node variable to the top level of the hierarchy dict
        current_node = hierarchy
        # iterate over path_parts list
        for element in path_parts:
            # check if element exists in the current_node dict
            if element not in current_node:
                # if element does not exist then add a new key with the element and set its value as an empty dict
                current_node[element] = {}
            # set current_node variable to the dict associated with the current element
            # this will allow it to iterate the next level of the hierarchy
            current_node = current_node[element]
    
    # at this point we should have a nested dictionary called hierarchy that represents
    # the hierarchical structure of the input paths.

    # create new dict result and populate it with keys and values 
    # that represent the hierarchical structure of the input paths
    
    # loop through each key in the "hierarchy" dictionary
    # For each key, the code adds a new key to the "result" dictionary with the same name as the current key 
    # in "hierarchy" and an empty list as its value. It then loops through each value associated with the 
    # current key in "hierarchy".

    # For each value, the code concatenates the current key and value with the "s" separator to create a new 
    # string called "path_accessed" and appends this string to the list associated with the current key in 
    # "result". It then creates a new key in the "result" dictionary with the name equal to the "path_accessed" 
    # string and an empty list as its value.

    # Continue this process for each subsequent level of the hierarchy, creating a new key in the "result" 
    # dictionary for each level and appending the corresponding paths to the list associated with the previous
    # level's key.

    result = dict()
    # separator
    s = "."

    for k1 in hierarchy:
        result[k1] = []
        for v1 in hierarchy[k1]:
            path_accessed = k1 + s + v1
            result[k1].append(path_accessed)
            # works so far!
            path1 = path_accessed
            result[path1] = []
            for k2 in hierarchy[k1][v1]:
                path_accessed = k1 + s + v1 + s + k2
                result[path1].append(path_accessed)
                # works so far!
                path2 = path_accessed
                result[path2] = []
                for k3 in hierarchy[k1][v1][k2]:
                    path_accessed = k1 + s + v1 + s + k2 + s + k3
                    result[path2].append(path_accessed)
                    # works so far!

    # return result dictionary which should be populated with all of the paths in the hierarchical structure
    return result


# create list of strings for input
paths = [
    "bs.ass",
    "bs.liability",
    "bs.ass.fixAss",
    "bs.ass.currAss",
    "bs.ass.fixAss.gain1",
    "bs.ass.fixAss.gain2",
    "bs.ass.currAss.currgain1",
    "bs.ass.currAss.currgain2",
    "bs.liability.lia1",
    "bs.liability.lia2",
]

# call build_heirarchy function and pass input list
hierarchy = build_hierarchy(paths)

# print in readable format using json dumps
print(json.dumps(hierarchy, indent=4))
