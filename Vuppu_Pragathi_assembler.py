variables = {}
for i in range(1, count1 + 1):
    b = index_empty[i - 1]
    a = ins[b][1]
    key = a
    value = convert_binary(i)
    variables[key] = value

for i in insori[:-1]:
        if i[0] in types['D']:
                if i[2] not in variables:
                        if (i[0] == 'ld'):
                                q = insori.index(i)
                                errors.write(f"Error in Line {q + 1} : No such memory address exist\n")
                        if (i[0] == 'st'):
                                q = insori.index(i)
                                errors.write(f"Error in Line {q + 1} : No variable name '{i[2]}'\n")
lab_address = {}
for i in range(len(labels)):
    key = labels[i]
    value = convert_binary(i + count1)
    lab_address[key] = value
print(lab_address)
for i in insori[:-1]:
        if i[0] in types['A']:
                if (len(i) != 4):
                        q = insori.index(i)
                        errors.write(f"Error in Line {q + 1} : {i[0]} must contain 3 parameters\n")
        elif (i[0] in types['B'] and i[-1] not in registers):
                if  (i[2][0]!='$') :
                        q = insori.index(i)
                        errors.write(f'Error in Line {q+1}:"{i[2]}" is not defined\n')
        elif (i[0] in types['C'] and i[-1] in registers) :
                if (i[-1] == "FLAGS"):
                        p = insori.index(i)
                        errors.write(f"Error in Line {p+1}: No variable named 'Flags'\n")
                if (len(i) != 3):
                        q = insori.index(i)
                        if i[0] =='cmp':
                                errors.write(f"Error in Line {q + 1} :Can't compare more than two registers\n")
                        elif i[0] =='mov':
                                errors.write(f"Error in Line {q + 1} :Can't use mov for more than two registers\n")
                        elif i[0] =='div':
                                errors.write(f"Error in Line {q + 1} :Can't use divide for more than two registers\n")
                        elif i[0] =='not':
                                errors.write(f"Error in Line {q + 1} :Can't use not for more than two registers\n")
        elif (i[0] in types['E'] and i[-1] not in labels ):
                q = insori.index(i)
                errors.write(f"Error in Line {q + 1} :No label named {i[-1]}\n")
