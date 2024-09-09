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
    dashes = []
    answers = []
    spaces_between_problems = []
    aranged_problems = ""

    # Situations that will return an error
    if len(problems) > 5:
            print('Error: Too many problems.')
    
    else:
      for item in problems:
            if '*' in item or '/' in item:
                  print("Error: Operator must be '+' or '-'.")
                  break
            
            operation_items = item.split(' ')
            if  not operation_items[0].isdigit() or  not operation_items[2].isdigit():
                  print('Error: Numbers must only contain digits.')
                  break
            elif len(operation_items[0]) > 4 or len(operation_items[2]) > 4:
                 print('Error: Numbers cannot be more than four digits.')
                 break
            
            operands_up.append(operation_items[0])
            operators.append(operation_items[1])
            operands_down.append(operation_items[2])
            answers.append(int(operation_items[0]) + int(operation_items[2]))

      for op in range(len(operands_up)):
            if len(operands_up[op]) > len(operands_down[op]):
                  longest_operand = operands_up[op]
            else:
                  longest_operand = operands_down[op]
            

      print(operands_up)
      print(operators)
      print(operands_down)
      print(answers)



      # print(f'\n{aranged_problems}')
     

    return problems


# Run Tests below

# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "2 + 42", "1000 + 77"])}')  #'Error: Too many problems.'
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
# print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
# print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
# print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
# print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
# print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')     #"Error: Operator must be '+' or '-'."
# print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')  #'Error: Numbers cannot be more than four digits.'
# print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')    #'Error: Numbers must only contain digits.'

