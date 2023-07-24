def create_list2(equation):
    equation_position = 0
    operator_signs = "-+*/÷^="
    integers = '0123456789'
    integers_position = 0
    equation_list = []
    addtolist = '' #remove me later, as I seem unnecessary unless debugging -update: perhaps untrue 

    while True:

        def locate_and_add(list, list_position, string, string_position):
            addtolist = ''
            while True:
                print("flag: ", "equation position:", string_position, "integer position:", list_position, "addtolist:", addtolist, "equation list:", equation_list)
                
                if list_position == len(list) or string_position == len(string):
                    print("final integers_position:", list_position)
                    list_position = 0
                    if addtolist == '':
                        return 0
                        break
                    return addtolist

                if string[string_position] == list[list_position]:
                    addtolist += str(string[string_position])
                    list_position += 1
                    list_position = 0
                else:
                    list_position += 1
                
                print("integer_position: ", integers_position)

            #addtolist = ''
    
        equation_list.append(int(locate_and_add(integers, integers_position, equation, equation_position)))
        #^ checking for an int may be unnecessary if we will also be checking operators and such, however, keep in mind that
        # adding empty strings to equation_list will not be preferable. Perhaps a function that locates and removes these
        # empty strings can be added after.

        #equation_position = len(str(equation_list[0])) - 1
        equation_position = len(str(equation_list[len(equation_list) - 1]))# - 1
        #equation_position = locate_and_add()


        if equation_position == len(equation) - 1 or equation_position == len(equation):
            return equation_list
        else:
            print("else has been reached")
            equation_position += 1
