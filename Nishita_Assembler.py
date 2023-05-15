labels = []
for i in ins:
    if i[0][-1] == ":":
        labels.append(i[0][:-1])
        i = i.pop(0)
for i in insori:
    if i[0] in labels:
        i = i.pop(0)
for i in ins:
    if (len(i) == 1):
        i.append(" ")
        i.append(" ")
        i.append(" ")
    if (len(i) == 2):
        i.append(" ")
        i.append(" ")
    if (len(i) == 3):
        i.append(" ")

halt = []
for i in insori:
        halt.append(i[0])
if 'hlt' not in halt:
    errors.write(f"Error: No hlt instruction present\n")
hlt_index= 0
for i in insori:
        if i[0] == "hlt":
                hlt_index = q = insori.index(i)
                if (len(insori)>q+1):
                        errors.write(f"Error in Line {q+1}: Can't execute lines after hlt\n")

binaryins = []
for i in range(len(ins)):
    if (ins[i][0] == "var"):
        binaryins.append([])
    elif (ins[i][0] == 'mov'):
        if ins[i][2] in registers:
            binaryins.append([opcodes['mov2']])
        else:
            binaryins.append([opcodes['mov1']])
    elif ins[i][0] in opcodes:
        binaryins.append([opcodes[ins[i][0]]])
    else:
        errors.write(f"Error in Line {i + 1}: Invalid operand\n")
count1 = 0
index_empty = []
for i in range(len(binaryins)):
    if (binaryins[i] == []):
        count1 += 1
        index_empty.append(i)
    if (binaryins[i] != []):
        break
