import re

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


def find_spelled_out_numbers(s: str, digit_mapping: dict):
    """Returns a list of tuples containing the start index, end index, and corresponding digit
    for each spelled-out number found in the string.
    """
    matches = []
    length = len(s)
    for index in range(length):
        for word, digit in digit_mapping.items():
            word_len = len(word)
            # slice the string from the current index to the current index + the length of the word and check if it matches the word in the dict
            if s[index : index + word_len] == word:
                # Store the start index, end index, and the digit
                matches.append((index, index + word_len, digit))
                break
    return matches


def replace_spelled_out_numbers(s: str, matches: list):
    new_string = ""
    last_index = 0
    for start, end, digit in matches:
        # Add the part of the string before the match and the digit
        new_string += s[last_index:start] + digit
        last_index = end

    # Add the remaining part of the string starting from the last index of the last match
    new_string += s[last_index:]

    return new_string


def find_first_last_number_part_two(s: str):
    first_number = next((i for i in s if i.isdigit()), "")
    last_number = next((i for i in reversed(s) if i.isdigit()), "")
    return first_number + last_number


def find_sum_of_numbers_part_two(filepath):
    with open(filepath) as f:
        lines = f.readlines()

    concatenated_numbers = []
    for line in lines:
        line = line.replace("\n", "")
        matches = find_spelled_out_numbers(line, digit_mapping)
        new_line = replace_spelled_out_numbers(line, matches)
        new_number = find_first_last_number_part_two(new_line)
        concatenated_numbers.append(new_number)
    # print(concatenated_numbers)
    sum_of_numbers = sum(int(number) for number in concatenated_numbers if number)

    return sum_of_numbers


# print(find_sum_of_numbers_part_one("input.txt"))
print(find_sum_of_numbers_part_two("input.txt"))  # 55902
