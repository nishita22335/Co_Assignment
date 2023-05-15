for i in range(len(ins)):
    if ins[i][1] in registers:
        # a = ins.index(i)
        binaryins[i].append(registers[ins[i][1]])
for i in range(len(ins)):
    if (ins[i][2] == ""):
        continue
    if ins[i][2] in registers:
        binaryins[i].append(registers[ins[i][2]])
    if (ins[i][2][0] == "$"):
        a = int(ins[i][2][1:])
        binaryins[i].append(convert_binary(a))
    if ins[i][2] in variables:
        binaryins[i].append(variables[ins[i][2]])
    if ins[i][2][0] in numbers:
        x = convert_binary(int(ins[i][2]))
        binaryins[i].append(x)
count2 = 0
for i in range(len(ins)):
    if (ins[i][3] == ""):
        continue
    if ins[i][3] in registers:
        binaryins[i].append(registers[ins[i][3]])
for j in range(len(binaryins)):
        if (binaryins[j]==[]):
                count2+=1

for k in range(count1+1,hlt_index+1):
        if (binaryins[k]==[]):
                errors.write(f"Error in Line {k+1}: Variables must be declared at the very beginning\n")
lst = []
for i in binaryins:
    if len(i) == 4:
        lst.append(i[0] + '00' + i[1] + i[2] + i[3])
    if len(i) == 2:
        lst.append(i[0] + '0000' + i[1])
    if len(i) == 1:
        lst.append(i[0] + '00000000000')
    if len(i) == 3 and len(i[2]) == 3:
        lst.append(i[0] + '00000' + i[1] + i[2])
    if len(i) == 3 and len(i[2]) == 7:
        lst.append(i[0] + '0' + i[1] + i[2])
f2 = open("output", "w")
for i in lst:
    f2.write(i)
    f2.write("\n")
