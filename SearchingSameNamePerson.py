'''
Question
Write an algorithm that takes a list of n names and returns a set of names
that appear more than once in the list.
'''

from typing import Any, Sequence

def find_same_name(array: Sequence) -> Any:
    # Step 1. make dictionary to number of appearances each name.
    name_dict = {}
    for name in array:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1

    # Step 2. if number of appearances >= 2 then add the result.
    result = set()
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)

    return result

if __name__ == "__main__":
    name = ["Tom", "Jerry", "Mike", "Tom"]
    print(find_same_name(name))

    name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
    print(find_same_name(name2))