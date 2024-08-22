def arithmetic_arranger(problems, show_answers=False):
    output = {"line1": '', "line2": '', "line3": '', "line4": ""}
    if len(problems) > 5:
        return ("Error: Too many problems.")
        
    index = 0
    for problem in problems:
        if index > 0:
            seperator_spaces = "    " # four spaces here
        else:
            seperator_spaces = "" # zero spaces here

        if '+'  in problem:
            operator = problem[problem.index('+')]      
        
        elif '-' in problem:
            operator = problem[problem.index('-')]
        
        else:
            return ('"Error: Operator must be \'+\' or \'-\'."')
        
        operand1 = problem[:problem.index(operator)].strip()        
        operand2 = problem[problem.index(operator) + 1:].strip()
        
        if not operand1.isnumeric() or not operand2.isnumeric():
            return ('Error: Numbers must only contain digits.')
        if len(operand1) > 4 or len(operand2) > 4:
            return ('Error: Numbers cannot be more than four digits.')
        length1 = len(operand1)
        length2 = len(operand2)
        if length1 > length2:
            longest = length1
        else:
            longest = length2
    
        if operator == '+':
            answer = int(operand1) + int(operand2)
        else:
            answer = int(operand1) - int(operand2)

        line1 = seperator_spaces + operand1.rjust(longest + 2)               #line 1
        line2 = seperator_spaces + operator + ' ' + operand2.rjust(longest)  #line 2
        line3 = seperator_spaces + '-' * (longest + 2)                        #line 3
        line4 = seperator_spaces + str(answer).rjust(longest + 2)            #line 4
        output['line1'] += line1 
        output['line2'] += line2 
        output['line3'] += line3 
        output['line4'] += line4 
        index += 1


    print(output['line1'])
    print(output['line2'])
    print(output['line3'])
    if show_answers: print(output['line4'])

    return problems

arithmetic_arranger(["3801 - 2", "123 + 49"]) 