def get_CEO_level(people, case_no):
    case_str = "Case #{}: ".format(case_no)
    # print("People: ", people)
    get_unmanaged(people)
    # h = create_hierarchy(people)
    # available, top_level = get_unmanaged(h)
    # ceo_level = 0
    # if available < 0:
    #     missing = available * -1
    #     if top_level >= missing:
    #         ceo_level = top_level + 1
    #     else:
    #         ceo_level = missing
    # else:
    #     ceo_level = top_level + 1

    # return "{}{}\n".format(case_str, ceo_level)

def create_hierarchy(people):
    people = map(str.rstrip, people)
    # print("People: ", people)
    h = {}
    if people:
        h = {p.split(' ')[1]:p.split(' ')[0] for p in list(people)}
        # print(h)
    return h

def get_unmanaged(people):
    people = map(str.rstrip, people)
    print("People: ", people)

    available = [0]
    numbers = []
    h = {}
    if people:
        h = {p.split(' ')[1]:p.split(' ')[0] for p in list(people)}
        print(h)
    for level in sorted(h.keys(), reverse=True):
        available.append(integize(level) * integize(h[level]))
        numbers.append(integize(h[level]))
    numbers.append(0)
    bal = 0
    for av, nums in zip(available, numbers):
        bal += av - nums

    print("Available: {}, Numbers:{}, Bal:{}".format(available, numbers, bal))
    return h

# def get_unmanaged(hierarchy):
#     unmanaged = 0
#     available = []
#     top_level = 0
#     count = 0
#     # left = 0
#     for level in sorted(hierarchy.keys(), reverse=True):
#         print("Level:{}  Hi: {}".format(level, hierarchy[level]))
#         print("Available:{}, Count:{}".format(available, count))
#         if count == 0:
#             top_level = integize(level)
#             unmanaged = integize(hierarchy[level])
#             available = integize(hierarchy[level]) * integize(level)
#             # print("Ex:{}, Count:{}, Level:{}".format(extra_slots, count, level))
#         else:
#             balance = available - integize(hierarchy[level])
#             if not balance:
#                 unmanaged += balance
#                 available = 0
#             available+=integize(hierarchy[level]) * integize(level)
#         # extra_slots+=integize(hierarchy[level])
#         count+=1
#     # print("Left: ", extra_slots)
#     # print("Top Level: ", top_level)
#     return (unmanaged, top_level)

# def get_unmanaged(hierarchy):
#     extra_slots = 0
#     top_level = 0
#     count = 0
#     for level in sorted(hierarchy, key=hierarchy.get, reverse=True):
#         if count == 0:
#             extra_slots+= -integize(hierarchy[level])
#             # print("Ex:{}, Count:{}, Level:{}".format(extra_slots, count, level))
#         else:
#             extra_slots+= -integize(hierarchy[level]) + (integize(level) * integize(hierarchy[level]))
#             # print("Ex2:{}, Count2:{}, Level:{}".format(extra_slots, count, level))

#         # extra_slots+=integize(hierarchy[level])
#         top_level = integize(level)
#         count+=1
#     # print("Left: ", extra_slots)
#     # print("Top Level: ", top_level)
#     return (extra_slots, top_level)

def read_and_write_file(input_file, output_file, test_case_line_size=1):
    with open(output_file, 'w') as out_file:
        with open(input_file, 'r') as input_data:

            file_data = input_data.readlines()
            # Strip newlines
            file_data = map(str.rstrip, file_data)
            test_cases = integize(file_data[0])
            data_set = []
            sub_cases = integize(file_data[1])
            total_cases = 0
            new_case = False
            for index, data in enumerate(file_data[2:]+['']):
                # print("Index:{}, sub_cases:{}, Data:{}\n".format(index, sub_cases, data))
                if sub_cases == index and index:
                    # print("data: ", data)
                    sub_cases += integize(data) + 1
                    # print("data_set: ", data)
                    new_case = True
                else:
                    data_set.append(data)
                    new_case = False

                if new_case:
                    total_cases += 1
                    output_data = get_CEO_level(data_set, total_cases)
                    # out_file.write(output_data)
                    # print("Data set: ", data_set)

                    data_set = []



            # test_cases = integize(input_data.readline())
            # test_case_line_size = integize(input_data.readline())
            # cases_total = 1
            # data = []
            # total_line_size = test_case_line_size
            # sub_cases = 1
            # new_case = False
            # for line_no, line in enumerate(input_data):
            #     # print("Data: ", line)
            #     if integize(line):
            #         new_case = True

            #     else:
            #         new_case = False
            #         data.append(line)

            #     if new_case:
            #         print("Output: ", data)
            #         output_data = get_CEO_level(data, cases_total)
            #         out_file.write(output_data)
            #         data = []
            #         cases_total+=1


def integize(num):
    try:
        return int(num)
    except ValueError:
        # print("Not an integer: Skipping...")
        return 0

test_files = ('in.in', 'out.out')
s_files = ('B-small-practice.in', 'B-small-practice.out')
l_files = ('A-large.in', 'A-large.out')
read_and_write_file(*test_files)
