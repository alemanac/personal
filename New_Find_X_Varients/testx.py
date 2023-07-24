#import new_find_x2

#def randomfunction():
#    xzy = 0

#addtolist = []

#addtolist.append(randomfunction)

#addtolist.append("random append")

#print(addtolist, " -end print")

import new_find_x

print(new_find_x.create_list("1 + 3 + x = 5"))

print(new_find_x.create_list("1s5dk441"))
#current issues:
#- The equation_position define after equation_list using the locate_add function (144) assumes
# that there is no blank spaces or other values besides integers and what's given to the
# function. This leads to a repeated equation position given from (147), as equation_list 
# remains constant.
#- (144) expects an addtolist int, but when the function is met with a space, it retuns
# nothing. This leads to an error at 144, as it needs an int to proceed. UPDATE: Perhaps I was
# wrong about this. Now the error is: "list index out of range".