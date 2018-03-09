def decorate_message(message, case_no):
    message = message.rstrip('\n')
    msg_len = len(message)
    case_text = "Case #{}:\n".format(case_no)
    up_down_border = "+" + ("-" * (msg_len + 2)) + "+\n"
    return case_text + up_down_border + "| " + message + " |\n" + \
        up_down_border


def read_and_write_file(input_file, output_file):
    with open(output_file, 'w') as out_file:
        with open(input_file, 'r') as input_data:
            first_test_cases = integize(input_data.readline())
            cases_total = first_test_cases
            for line_no, line in enumerate(input_data):
                output_data = decorate_message(line, line_no + 1)
                out_file.write(output_data)
                if line_no and line_no == cases_total:
                    test_cases = integize(line)
                    cases_total += test_cases + 1

def integize(num):
    try:
        return int(num)
    except ValueError:
        print("Not an integer: Skipping...")
        return 0

read_and_write_file('A-small-practice.in', 'A-small-practice.out')
