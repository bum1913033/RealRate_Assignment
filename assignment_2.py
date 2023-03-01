import json

# define function to build a hierarchy based on given input and format the resulting output as required.
def build_hierarchy(paths):
    hierarchy = {}
    for path in paths:
        # reminder: path_parts is a list!
        path_parts = path.split(".")
        # current node represents selected node level
        current_node = hierarchy
        # iterate over path_parts list
        for element in path_parts:
            # if element is not in the selected node level, add new key as element and an empty dictionary as value.
            if element not in current_node:
                current_node[element] = {}
            # move currently selected node to next element node
            current_node = current_node[element]
    # at this point we should have a nested dictionary called hierarchy that stores key:value pairs
    # in order of the directory hierarchy

    # create new result dictionary to format values as seen in sample output
    result = dict()
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

    # return result dictionary
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
