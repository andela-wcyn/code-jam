def get_int_pos(num):
    h1 = []
    h2 = []
    half = num // 2
    for index, val in enumerate(range(half)):
        h1.append(val)
    for index, val in enumerate(range(num - half)):
        h2.insert(0, val)
    pos = h1 + h2
    print(pos)
    return pos

def get_sum_squared(burgers, num, case_no):
    case_str = "Case #{}: ".format(case_no)
    num = integize(num)
    burgers = burgers.rstrip()
    burgers = burgers.split(' ')

    optimized = optimize(burgers, num)
    sum_error = calculate_error(get_int_pos(num), optimized)
    # print("b: {} op:{}".format(burgers[::-1], optimized))
    # print(sum_error)
    return "{}{}\n".format(case_str, sum_error)

def calculate_error(current, optimized):
    print("Cal: ", current)
    values = zip(current, optimized)
    sum_error = 0
    for i in values:
        sum_error += (integize(i[0]) - integize(i[1])) **2
    # print(sum_error)
    return sum_error

def optimize(burgers, num):
    s = sorted(burgers)
    half = num // 2
    h1 = []
    h2 = []
    for index, val in enumerate(s):
        if index % 2 != 0:
            h1.append(val)
        else:
            h2.insert(0, val)
    optimized = h1 + h2
    # print(optimized)
    return optimized


def read_and_write_file(input_file, output_file, test_case_line_size):
    with open(output_file, 'w') as out_file:
        with open(input_file, 'r') as input_data:
            test_cases = integize(input_data.readline())
            cases_total = 1
            data = []
            sub_cases = 1
            for line_no, line in enumerate(input_data):
                # print("Data: ", line)
                data.append(line)
                # print("Line S: ", cases_total, test_case_line_size)
                if sub_cases % test_case_line_size == 0:
                    output_data = data
                    # output_data = get_arrangements(people, tables, line_no + 1)
                    # out_file.write(output_data)
                    # print("Output: ", output_data)
                    output_data = get_sum_squared(output_data[1], output_data[0], cases_total)
                    out_file.write(output_data)
                    data = []
                    cases_total += 1

                # print("Total: ", cases_total, test_cases)
                if cases_total > test_cases:
                    break

                sub_cases+=1

def integize(num):
    try:
        return int(num)
    except ValueError:
        print("Not an integer: Skipping...")
        return 0

test_files = ('in.in', 'out.out')
s_files = ('A-small-attempt0.in', 'A-small-attempt0.out')
l_files = ('A-large.in', 'A-large.out')
read_and_write_file(*l_files, test_case_line_size=2)
