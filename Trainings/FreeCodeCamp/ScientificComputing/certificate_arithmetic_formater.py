# Certification Project: Build an Arithmetic Formatter Project
"""Students in primary school often arrange arithmetic problems vertically to make them easier to solve.

Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, 
and returns the problems arranged vertically and side-by-side. 
The function should optionally take a second argument. 
When the second argument is set to True, the answers should be displayed."""

def arithmetic_arranger(problems, show_answers=False):
    
    operands_up   = []
    operators = []
    operands_down = []
    answers = []
    arranged_problems = ""

    # Situations that will return an error
    if len(problems) > 5:
            return 'Error: Too many problems.'
    
    else:
      for problem in problems:
            operation_items = problem.split(' ')
            if '*' in problem or '/' in problem:
                  return "Error: Operator must be '+' or '-'."
            if  not operation_items[0].isdigit() or  not operation_items[2].isdigit():
                  return 'Error: Numbers must only contain digits.'
            if len(operation_items[0]) > 4 or len(operation_items[2]) > 4:
                 return 'Error: Numbers cannot be more than four digits.'
            
            operands_up.append(operation_items[0])
            operators.append(operation_items[1])
            operands_down.append(operation_items[2])
            if operation_items[1] == '+':
                  answers.append(str(int(operation_items[0]) + int(operation_items[2])))
            else:
                  answers.append(str(int(operation_items[0]) - int(operation_items[2])))

      first_line  = ""
      second_line = ""
      dashes_line = ""
      result_line = ""

      for op in range(len(problems)):
            length = max(len(operands_up[op]), len(operands_down[op])) + 2 
            first_line += operands_up[op].rjust(length)
            second_line += operators[op] + operands_down[op].rjust(length -1)
            dashes_line += '-' * length

            if show_answers:
                 result_line += answers[op].rjust(length)
            if op < len(problems) - 1:
                  first_line += "    "
                  second_line += "    "
                  dashes_line += "    "
                  if show_answers:
                        result_line += "    "
            
      arranged_problems = first_line + '\n' + second_line + '\n' + dashes_line
      if show_answers:
            arranged_problems += '\n' + result_line

    return arranged_problems


# Run Tests below
if __name__ == '__main__':
      # print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "2 + 42", "1000 + 77"])}')  #'Error: Too many problems.'
      print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')  #'Error: Too many problems.'
      # print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')
      # print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
      # print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"], True)}')
      # print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
      # print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
      # print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
      # print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')     #"Error: Operator must be '+' or '-'."
      # print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')  #'Error: Numbers cannot be more than four digits.'
      # print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')    #'Error: Numbers must only contain digits.'
      print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')