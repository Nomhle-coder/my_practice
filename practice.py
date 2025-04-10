def get_even_numbers(lst):
    # Your code here
    new_lst = []
    for num in lst:
        if num % 2 == 0:
            new_lst.append(num)
    return new_lst

def get_odd_numbers(lst):
    # Your code here
    odd_num = []
    for i in lst:
        if i % 2 != 0:
            odd_num.append(i)
    return odd_num

def sum_of_list(lst):
    # Your code here
    numbers = 0
    for number in lst:
        numbers += number
    return numbers
print(sum_of_list([1, 2, 3, 4]))


def get_max_number(lst):
    # Your code here
    max_number = []
    for number in lst:
        if number > max_number:
            max_number = number
            return number
print(get_max_number([1, 2, 3, 4, 5]))

def remove_duplicates(lst):
    # Your code here
    pass

def reverse_list(lst):
    # Your code here
    pass


# String Operations
def reverse_string(s):
    # Your code here
    pass

def count_vowels(s):
    # Your code here
    pass

def remove_whitespace(s):
    # Your code here
    pass

def capitalize_first_letter(s):
    # Your code here
    pass

def is_palindrome(s):
    # Your code here
    pass

def find_substring(s, sub):
    # Your code here
    pass

def replace_substring(s, old, new):
    # Your code here
    pass
