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

    e_position = 0
    ol_position = 0

    while True:
        break
        #if 

    #print('norm is equal to:', norm)

#can be structured by doing the opposite of pemdas to the most normal side (answer side)
#in standard solving for x format. It'll just be a sequence of doing the opposite of 
#pemdas on that normal side. For example: (4x + 3 = 15) 1. subtract 3 from 15 2. divide 4
#from the right side

#calculate steps:
#1. create the side without x, called "norm"
#2. simplify
#3. subtract or add things to help isolate the variable / x
#4. use multiplication or division to solve for the variable 

#notes:
#you can only peform distrubutive property after simplifying 


def create_list(equation):
    equation_position = 0
    operator_signs = "-+*/÷^="
    integers = '0123456789s'
    integers_position = 0
    equation_list = []
    addtolist = '' #remove me later, as I seem unnecessary unless debugging -update: perhaps untrue 

    while True:

        while True:
            print("flag: ", "equation position:", equation_position, "integer position:", integers_position, "addtolist:", addtolist, "equation list:", equation_list)
            
            if integers_position == len(integers) or equation_position == len(equation): #once it checks all available integers & it reaches end of equation
                print("final integers_position:", integers_position)
                integers_position = 0
                if addtolist == '':
                    break
                equation_list.append(int(addtolist))
                addtolist = ''
                break

            if equation[equation_position] == integers[integers_position]: #if the position in the equation aligns with the integer in check
                addtolist += str(equation[equation_position])
                equation_position += 1
                integers_position = 0
            else:
                integers_position += 1
            
            print("integer_position: ", integers_position)

        #addtolist = ''
        

        if equation_position == len(equation) - 1 or equation_position == len(equation):
            return equation_list
        else:
            print("else has been reached")
            equation_position += 1

# ^ make a function and use two arguments as the replacement for the thing that is trying to be found and the position of it