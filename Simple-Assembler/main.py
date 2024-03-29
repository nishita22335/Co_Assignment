registers = {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101', 'R6': '110', 'FLAGS': '111'}

types={'A':['add','sub','mul','xor','or','and',],'B':['mov','rs','ls'],'C':['mov','div','not','cmp'],'D':['ld','st'],'E':['jmp','jlt','jgt','je'],'F':['hlt']}
def convert_binary(imm):
    sevbit = "0000000"
    a = bin(imm)[2:]
    lena = len(a)
    b = 7 - lena
    sevbit = sevbit[0:b] + a
    return sevbit
opcodes = {
    'add': '00000',
    'sub': '00001',
    'ld': '00100',
    'st': '00101',
    'mul': '00110',
    'div': '00111',
    'ls': '01001',
    'rs': '01000',
    'xor': '01010',
    'or': '01011',
    'and': '01100',
    'not': '01101',
    'cmp': '01110',
    'jmp': '01111',
    'jlt': '11100',
    'jgt': '11101',
    'je': '11111',
    'hlt': '11010',
    'mov1': '00010',
    'mov2': '00011',
}
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
fmz = open("input.txt","w")
while True:
    try:
        liness = input()
        fmz.writelines(liness+"\n")
    except EOFError:
        break
fmz.close()
f = open("input.txt", "r")
instructions = (f.readlines())
errors = open("error.txt","w")
lines = [i.strip() for i in instructions]
ins = []
insori = []
for i in lines:
    t = i.split()
    insori.append(t)
for j in lines:
    t2 = j.split()
    ins.append(t2)
labels = []
lab_index=[]
for i in ins:
    if i[0][-1] == ":":
        lab_index.append(ins.index(i))
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

mem_address= len(binaryins)-count1
variables = {}
for i in range(mem_address,mem_address+count1):
    b = index_empty[i-mem_address]
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
    p = lab_index[i]
    value = convert_binary(p - count1)
    lab_address[key] = value
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
    f2.write(i+"\n")
f2.close()
fk = open("output","r")
for lineyss in fk:
    print(lineyss,end="")
fk.close()