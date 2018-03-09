import math


def get_population(A, B, a, b, Y, case_no):
    A, B, a, b, Y = integize(A), integize(B), integize(a), integize(b), \
                    integize(Y)
    case_str = "Case #{}: ".format(case_no)
    last_five_popstats = [None] * 5
    for year in range(Y):
        A, B = calculate_single_year(A, B, a, b)
        last_five_popstats[year % 5] = (A,B)
        if last_five_popstats[1:] == last_five_popstats[:-1]:
            print("Breaking at year {}".format(year))
            break
    return case_str + "{} {}\n".format(A, B)

def calculate_single_year(A, B, a, b):
    # Reproduction
    couples = min(A, B)
    babies = math.floor(0.02 * couples)
    a_babies = math.floor((a * babies) / 100.0)
    b_babies = math.floor((b * babies) / 100.0)
    rem_babies = babies - a_babies - b_babies
    a_babies = a_babies + math.floor(rem_babies / 2.0)
    b_babies = b_babies + math.ceil(rem_babies / 2.0)
    a_dec = math.floor(0.01 * A)
    b_dec = math.floor(0.01 * B)
    A += a_babies - a_dec
    B += b_babies - b_dec
    return(A, B)

def read_and_write_file(input_file, output_file):
    with open(output_file, 'w') as out_file:
        print("Opening write file...")
        with open(input_file, 'r') as input_data:
            print("Opening Read file...")
            first_test_cases = integize(input_data.readline())
            cases_total = first_test_cases
            for line_no, line in enumerate(input_data):
                line = line.rstrip('\n')
                A, B, a, b, Y = line.split(' ')
                output_data = get_population(A, B, a, b, Y, line_no + 1)
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

test_files = ('int.in', 'outt2.out')
s_files = ('B-small-practice.in', 'B-small-practice.out')
l_files = ('B-large-practice.in', 'B-large-practice.out')
read_and_write_file(*test_files)
