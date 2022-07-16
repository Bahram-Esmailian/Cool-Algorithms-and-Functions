#Quadratic Equation Builder created and written by Bahram Esmailian

#simply change the string to some simplified quadratic formula in the form (ai+b)(ci+d) where i is the independent variable
string = '(5i+1)(6i+2)'
new_string = ''

for s in string:
    print(new_string)
    if s == '(' or s == ')':
        new_string = new_string + ' '
    elif s.isalpha():
        variable = s
        new_string = new_string + ' '
    else:
        new_string = new_string + s
reduced = new_string.split()
if reduced
expanded = [int(reduced[0])*int(reduced[2]), int(reduced[0])*int(reduced[3])+int(reduced[1])*int(reduced[2]), int(reduced[1])*int(reduced[3])]
expanded_str = ''
if expanded[0] != 1:
    expanded_str = expanded_str + str(expanded[0])
expanded_str = expanded_str + str(variable) + '^2'
if expanded[1] > 0:
    expanded_str = expanded_str + '+'
elif expanded[1] < 0:
    expanded_str = expanded_str + '-'
if expanded[1] != 1:
    expanded_str = expanded_str + str(expanded[1])
expanded_str = expanded_str + str(variable)
if expanded[2] > 0:
    expanded_str = expanded_str + '+'
elif expanded[2] < 0:
    expanded_str = expanded_str + '-'
if expanded[2] != 1:
    expanded_str = expanded_str + str(expanded[2])

print(expanded)
print(variable)
print(expanded_str)
