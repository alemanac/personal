#equation = newvar + 4 * 3 #divides the equation in both sides (answer + expression)
# 4x + 3 = 15 is actually x = (15 - 3)/4

def mark_operator(equation):
    operator_signs = "-+*/÷^="
    add_to_list = []
    e_position = 0
    os_position = 0

    while e_position != len(equation) - 1:
        while True:
            if equation[e_position] == operator_signs[os_position]:
                add_to_list.append(e_position)
                break
            elif os_position == len(operator_signs) - 1:
                break
            else:
                os_position = os_position + 1
    
        e_position = e_position + 1
        os_position = 0

    return add_to_list

#returning the = position is needed. Perhaps include the = in add_to_list? It can be the
#first sign to find in the pemdas sequence thing

def calculate(equation, operator_list):
    e_position = 0
    ol_position = 0

    while True:
        if equation[operator_list[ol_position]] == '=':
            e_position = operator_list[ol_position] + 1
            while True: 
                try: 
                    norm = int(equation[e_position])
                    break
                except:
                    e_position += 1
            break
        else:
            ol_position += 1

    print('norm is equal to:', norm)

#can be structured by doing the opposite of pemdas to the most normal side (answer side)
#in standard solving for x format. It'll just be a sequence of doing the opposite of 
#pemdas on that normal side. For example: (4x + 3 = 15) 1. subtract 3 from 15 2. divide 4
#from the right side
