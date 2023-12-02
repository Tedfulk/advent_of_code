import re


def find_first_last_number_part_one(line):
    first_number = next((i for i in line if i.isdigit()), "")
    last_number = next((i for i in line[::-1] if i.isdigit()), "")
    return first_number + last_number


def find_sum_of_numbers_part_one(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    concatenated_numbers = [find_first_last_number_part_one(line) for line in lines]
    sum_of_numbers = sum(int(number) for number in concatenated_numbers if number)

    return sum_of_numbers


def replace_first_spelled_out_number(s):
    digit_mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for word, digit in digit_mapping.items():
        if word in s:
            s = s.replace(word, digit, 1)
            break
    return s


def replace_last_spelled_out_number(s):
    digit_mapping = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for word, digit in digit_mapping.items():
        index = s.rfind(word)
        if index != -1:
            s = s[:index] + digit + s[index + len(word) :]
            break
    return s


def find_first_last_number_part_two(line):
    line = replace_first_spelled_out_number(line)
    line = replace_last_spelled_out_number(line)

    first_number = next((i for i in line if i.isdigit()), "")
    last_number = next((i for i in line[::-1] if i.isdigit()), "")
    return first_number + last_number


def find_sum_of_numbers_part_two(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    concatenated_numbers = [find_first_last_number_part_two(line) for line in lines]
    sum_of_numbers = sum(int(number) for number in concatenated_numbers if number)

    return sum_of_numbers


# print(find_sum_of_numbers_part_one("input.txt"))
print(find_sum_of_numbers_part_two("2023/1D/input.txt"))  # 55902
