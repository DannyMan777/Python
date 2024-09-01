# 1. Find missing number in list

# 1st variant
def find_missing_int_naiveSolution(lst):
    missing_int_set = set(lst)
    int_set = {i for i in range(1, len(lst) + 2)}
    
    #solution. compare given list lst with own created list int_set
    missing_int = int_set.difference(missing_int_set)
    iterator = iter(missing_int)
    return next(iterator)

# 2nd variant
def find_missing_int(lst):
    missing_sum = sum(lst)
    non_missing_sum = 0

    for i in range(1, len(lst) +2):
        non_missing_sum +=i
    return non_missing_sum - missing_sum

# 3rd variant
def find_missing_int_formula(lst):
    # formula:   n * (n+1) / 2
    n = len(lst) + 1  # n is the total length of the given list
    sum_total = n * (n+1) // 2
    return sum_total - sum(lst)

# Function call:
    # missing_int = [1, 2, 6, 7, 9, 3, 4, 10, 8]
    # print(find_missing_int_formula(missing_int))




# 2. Codeland Username Validation
"""
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:
1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.
If the username is valid then your program should return the string true, otherwise return the string false.
"""

def CodelandUsernameValidation(strParam):

  if len(strParam) < 4 or len(strParam) > 25:
    return False
  elif strParam[0].isalpha() == False:
    return False
  elif not [i for i in strParam if i.isalnum() or i=='_'] :
    return False
  elif strParam.endswith('_'):
    return False
      
  else: 
    return True

  return strParam

# Function call:
# print(CodelandUsernameValidation(input()))




# 3. Count Letters, Digits, and Special Symbols
"""
Challenge: Count Letters, Digits, and Special Symbols Write a program that takes an input string and counts the number of letters (both uppercase and lowercase), digits, and special symbols (such as punctuation marks) in the string. For example:

If the input string is "Hello, World! 123", the output should be:
Letters: 10
Digits: 3
Special Symbols: 3
"""

s1 = "Hello, World! 123"

def count_letters_digits_specials(s1):
    Letters = 0
    Digits  = 0
    Symbols = 0
    for item in s1:
        if item.isalpha():
            Letters += 1
        elif item.isdigit():
            Digits += 1
        else:
            Symbols += 1

    print("Letters: ", Letters)
    print("Digits: " , Digits)
    print("Symbols: ", Symbols)

# Function call:
# count_letters_digits_specials(s1)



# 4. Find all longest words in string and display them as items in list
def find_longest_words(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Initialize variables to track the longest length and longest words
    max_length = 0
    longest_words = []

    # Iterate through each word
    for word in words:
        # Remove any punctuation marks from the word
        cleaned_word = word.strip(".,!?")

        # Check if the cleaned word is longer than the current max length
        if len(cleaned_word) > max_length:
            max_length = len(cleaned_word)
            longest_words = [cleaned_word]
        elif len(cleaned_word) == max_length:
            # If the word has the same length as the current max, add it to the list
            longest_words.append(cleaned_word)

    return longest_words

# Function call:
input_string = "The quick brown fox jumps over the lazy dog"
# result = find_longest_words(input_string)
# print(result)  # Output: ['quick', 'brown', 'jumps']



# 5. StringChallenge
"""
 Take a string grouped in 3 pairs of 3 numbers separated by points. 
The last digit must be larger than the previous two.
The sum of the first set must be even and the sum of the second set must be odd. 
If previous conditions are true return True, else return False.
"""
def StringChallenge(str):
    # Split the string by periods
    sets = str.split('.')

    # Check if there are exactly three sets
    if len(sets) != 3:
        return False

    for s in sets:
        # Check if each set contains exactly three digits
        if len(s) != 3 or not s.isdigit():
            return False

        # Convert the set to a list of integers
        digits = list(map(int, s))

        # Check if the last digit is larger than the previous two
        if not (digits[2] > digits[0] and digits[2] > digits[1]):
            return False

    # Check if the sum of the first set is even
    if sum(map(int, sets[0])) % 2 != 0:
        return False

    # Check if the sum of the second set is odd
    if sum(map(int, sets[1])) % 2 != 1:
        return False

    return True

# Function call:
# print(StringChallenge("123.456.789"))  # Output: False
# print(StringChallenge("246.135.789"))  # Output: True
