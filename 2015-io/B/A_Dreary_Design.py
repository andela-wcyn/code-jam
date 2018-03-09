def chars_to_binary(chars):
    """
    :param chars: characters to be converted
    :type chars: string
    """
    chars = chars.replace("I", "1").replace("O", "0")
    # print(chars)
    return chars

def decode_binary(num_string, size, case_no):
    case_str = "Case #{}: ".format(case_no)
    num_string = chars_to_binary(num_string.rstrip())
    # print("Num: ", num_string)
    size = integize(size)
    word = []
    for i in range(1, size+1):
        # print("N2; ", num_string[(i-1)*8:i*8], i, size)
        word.append(chr(int(num_string[(i-1)*8:i*8], 2)))
    # print("Word: ", ''.join(word))
    return case_str + ''.join(word) + '\n'



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
                    output_data = decode_binary(output_data[1], output_data[0], cases_total)
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
s_files = ('A-small-practice.in', 'A-small-practice.out')
l_files = ('A-large-practice.in', 'A-large-practice.out')
read_and_write_file(*s_files, test_case_line_size=2)
