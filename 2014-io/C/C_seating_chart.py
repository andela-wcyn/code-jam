import math
import itertools
import collections
import pprint

"""
from itertools import cycle
For cyclic lists
"""


def get_arrangements(people, tables, case_no):
    people, tables = integize(people), integize(tables)
    case_str = "Case #{}: ".format(case_no)
    all_arrangements = itertools.permutations(range(0, people))
    grouping = get_grouping(people, tables)
    # print("Grouping:{} ".format(grouping))
    diff_arrangements = []
    for arrangement in all_arrangements:
        group_sum = 0
        grouped = []
        for group in grouping:
            grouped.append(arrangement[group_sum: group_sum + group])
            group_sum += group
        if different_group(grouped, diff_arrangements):
            # print("Different: {}".format(grouped))
            diff_arrangements.append(grouped)
    pprint.pprint("Arr: {}".format(diff_arrangements))

    return case_str + "{}\n".format(len(diff_arrangements))

def get_grouping(people, tables):
    per_table = people // tables
    extras = people % tables
    grouping = [per_table] * tables
    grouping[:extras] = map(lambda x: x + 1, grouping[:extras])
    return grouping

def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''

    # Check if sizes of two strings are same
    if size1 != size2:
        return 0

    # Create a temp string with value str1.str1
    temp = string1 + string1

    # Now check if str2 is a substring of temp
    # string.count returns the number of occurences of
    # the second string in temp
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0

def different_group(grouped, grouped_list):
    # print("Grouped  List: {}".format(grouped_list))
    if not grouped_list:
        return True
    if grouped:
        # print("GD: ", grouped)
        for diff in grouped_list:
            # similar = []
            similarity = [False] * len(grouped)

            for i, group in enumerate(grouped):
                # print("Diff {}".format(diff))
                # print("G: ", group)
                # print("I: ", i)
                deques = map(lambda x: collections.deque(x), diff)
                # for j in deques:
                #     print('i before: ', i)
                #     i.rotate()
                #     print('i after:', i)
    #             try:
    # b=a.index(7)
    #             except ValueError:
    #                 "Do nothing"
                # try:
                #     rotations = map(lambda x: x if x.rotate(-list(x).index(group[0])) else None, deques)
                # except ValueError:
                #     rotations = []
                # try:
                rotations = []
                for d in deques:
                    # print("D: ", list(d))
                    if group[0] in list(d):
                        d.rotate(-list(d).index(group[0]))
                        rotations.append(d)
                        new = collections.deque(d)
                        new.reverse()
                        new.rotate(-list(new).index(group[0]))
                        # d.rotate(-list(d).index(group[0]))
                        rotations.append(new)
                        # print("G in D: ", group, d)

                if collections.deque(group) in rotations:
                    # print("Rotations: {}".format(list(rotations)))
                    # print("G: ", group)
                    similarity[i] = True
                # rotations = map(lambda x: x if x.rotate(-list(x).index(group[0])) or group[0] in list(x) else None, deques)

                # print("Rotations: {}".format(list(rotations)))
                # if collections.deque(group) in rotations:
                #     # print("Rotations: {}".format(list(rotations)))
                #     # print("G: ", group)
                #     similarity[i] = True
                # except ValueError:
                #     rotations = []
                # print("Group ({}) in diff ({})".format(group, diff))
            if similarity == [True] * len(grouped):
                # print()
                return False

        # grouped_list = similar
        # different_group(grouped, grouped_list)
        return True
    else:
        return True
def read_and_write_file(input_file, output_file):
    with open(output_file, 'w') as out_file:
        print("Opening write file...")
        with open(input_file, 'r') as input_data:
            print("Opening Read file...")
            first_test_cases = integize(input_data.readline())
            cases_total = first_test_cases
            for line_no, line in enumerate(input_data):
                line = line.rstrip('\n')
                people, tables = line.split(' ')
                print(people, tables)
                output_data = get_arrangements(people, tables, line_no + 1)
                out_file.write(output_data)
                if line_no and line_no == cases_total:
                    test_cases = integize(line)
                    cases_total += test_cases + 1
        print("Closing write file...")


def integize(num):
    try:
        return int(num)
    except ValueError:
        print("Not an integer: Skipping...")
        return 0

test_files = ('in.in', 'out.out')
s_files = ('C-small-practice.in', 'C-small-practice.out')
l_files = ('C-large-practice.in', 'C-large-practice.out')
read_and_write_file(*s_files)

