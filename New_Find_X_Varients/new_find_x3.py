def create_list3(equation):
    equation_position = 0
    operator_signs = "-+*/÷^="
    integers = '0123456789'
    integers_position = 0
    equation_list = []
    addtolist = '' #remove me later, as I seem unnecessary unless debugging -update: perhaps untrue 

    while True:

        class locate__add_and_position:#(list, position, equation, equation_position):

            def position(list, position, equation, equation_position):
                            if equation[equation_position] == list[position]:
                                addtolist += str(equation[equation_position])
                                equation_position += 1
                                position = 0
                            else:
                                position += 1

            def locate_add(list, list_position, string, string_position):
                addtolist = ''
                while True:
                    print("flag: ", "equation position:", string_position, "integer position:", list_position, "addtolist:", addtolist, "equation list:", equation_list)
                    
                    if position == len(list) or equation_position == len(equation):
                        print("final integers_position:", position)
                        position = 0
                        if addtolist == '':
                            break
                        return addtolist
                    equation_position = position(list,position, equation, equation_position)

            
            
            print("integer_position: ", integers_position)

            #addtolist = ''
    
        equation_list.append(int(locate_and_add(integers, integers_position, equation, equation_position)))

        #equation_position = len(str(equation_list[0])) - 1
        equation_position = len(str(equation_list[len(equation_list) - 1]))# - 1
        #equation_position = locate_and_add()


        if equation_position == len(equation) - 1 or equation_position == len(equation):
            return equation_list
        else:
            print("else has been reached")
            equation_position += 1