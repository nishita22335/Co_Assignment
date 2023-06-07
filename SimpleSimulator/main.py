f1 = open("input","r")
input = f1.readlines()
lines = []
registers = {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101', 'R6': '110', 'FLAGS': '111'}
opcodes ={
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
types = {'A':['add','sub','mul','xor','or','and',],'B':['mov1','rs','ls'],'C':['mov2','div','not','cmp'],'D':['ld','st'],'E':['jmp','jlt','jgt','je'],'F':['hlt']}
reg_values={'R0': 0, 'R1': 0, 'R2': 0, 'R3': 0, 'R4': 0, 'R5': 0, 'R6': 0,'FLAGS':'0000000000000000'}
input_memory=[]
while len(input_memory)<128:
    input_memory.append('0'*16)


def binary_To_Decimal(binary):
    decimal, i = 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal
def decimal_to_binary(decimal):
    binary = bin(decimal & 0xFFFF)[2:].zfill(16)
    return binary

fir_ele=[]
for i in input:
    lines.append(i[:-1])
    search_value = i[:5]
    for key, value in opcodes.items():
        if (value == search_value):
            fir_ele.append(key)
#print(fir_ele)
keys=[]
for j in fir_ele:
    for key, value in types.items():
        if j in value:
            keys.append(key)
# print(keys)
# print(lines)
ins = []
for j in range(len(input)):
    if keys[j] == 'A':
        ins.append([fir_ele[j]])
        register_order = [input[j][7:10], input[j][10:13], input[j][13:16]]
        for reg in register_order:
            for key, value in registers.items():
                if reg == value:
                    ins[j].append(key)
                    break
    if keys[j] == 'B':
        ins.append([fir_ele[j]])
        register_order = [input[j][6:9]]
        for reg in register_order:
            for key, value in registers.items():
                if reg == value:
                    ins[j].append(key)
                    break
        ins[j].append(binary_To_Decimal(int(input[j][9:16])))
    if keys[j] == 'C':
        ins.append([fir_ele[j]])
        register_order = [input[j][10:13], input[j][13:16]]
        for reg in register_order:
            for key, value in registers.items():
                if reg == value:
                    ins[j].append(key)
                    break
    if keys[j]=='D':
        ins.append([fir_ele[j]])
        register_order = [input[j][6:9]]
        for reg in register_order:
            for key, value in registers.items():
                if reg == value:
                    ins[j].append(key)
                    break
        ins[j].append(binary_To_Decimal(int(input_memory[binary_To_Decimal(int(input[j][9:16]))])))
        # mem_add.append(input[j][9:16])
    if keys[j]=='E':
        ins.append([fir_ele[j]])
        ins[j].append(binary_To_Decimal(int(input[j][9:16])))
        # mem_add.append(input[j][9:16])
    if keys[j] == 'F':
        ins.append([fir_ele[j]])
# print(ins)
# ins list contain all the instructions as per the assembly language.
i = 0
while (i<len(ins)):
    if ins[i][0]=='jmp':
        k=ins[i][1]
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        if i<k:
            i = k
            # continue
    elif ins[i][0]=='jgt':
        if reg_values['FLAGS']=='0000000000000010':
            k = ins[i][1]
            reg_values['FLAGS'] = '0000000000000000'
            print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
            if i < k:
                i = k
        else:
            print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
            i = i+1

                # continue
    elif ins[i][0]=='jlt':
        if reg_values['FLAGS'] == '0000000000000100':
            k = ins[i][1]
            reg_values['FLAGS'] = '0000000000000000'
            print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
            if i < k:
                i = k
                # continue
        else:
            print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
            i = i+1

    elif ins[i][0]=='je':
        if reg_values['FLAGS']=='0000000000000001':
            k = ins[i][1]
            reg_values['FLAGS'] = '0000000000000000'
            print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
            if i < k:
                i = k
                # continue
        else:
            print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
            i = i+1


    elif ins[i][0]=='add':
        reg_values[ins[i][1]]=reg_values[ins[i][2]]+reg_values[ins[i][3]]
        if reg_values[ins[i][1]]>65535:
            reg_values[ins[i][1]]=0
            reg_values['FLAGS'] = '0000000000001000'
        else:
            reg_values['FLAGS'] = '0000000000000000'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i=i+1
    elif ins[i][0] == 'sub':
        if reg_values[ins[i][2]] >= reg_values[ins[i][3]]:
            reg_values[ins[i][1]] = reg_values[ins[i][2]] - reg_values[ins[i][3]]
            reg_values['FLAGS'] = '0000000000000000'
        else:
            reg_values[ins[i][1]] = 0
            reg_values['FLAGS'] = '0000000000000100'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
    elif ins[i][0]=='mul':
        reg_values[ins[i][1]]=reg_values[ins[i][2]]*reg_values[ins[i][3]]
        if reg_values[ins[i][1]]>=128:
            reg_values[ins[i][1]]=0
            reg_values['FLAGS'] = '0000000000001000'
        else:
            reg_values['FLAGS'] = '0000000000000000'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
    elif ins[i][0]=='mov1':
        reg_values[ins[i][1]]=ins[i][2]
        if reg_values[ins[i][1]]>65535:
            reg_values[ins[i][1]]=0
            reg_values['FLAGS'] = '0000000000001000'
        else:
            reg_values['FLAGS'] = '0000000000000000'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
    elif ins[i][0]=='mov2':
        if ins[i][2]=='FLAGS':
            reg_values[ins[i][1]] = int(reg_values[ins[i][2]])
            reg_values['FLAGS'] = '0000000000000000'
        else:
            reg_values[ins[i][1]]=reg_values[ins[i][2]]
            reg_values['FLAGS'] = '0000000000000000'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
    elif ins[i][0]=='ld':
        reg_values[ins[i][1]]=ins[i][2]
        if reg_values[ins[i][1]]>65535:
            reg_values[ins[i][1]]=0
            reg_values['FLAGS'] = '0000000000001000'
        else:
            reg_values['FLAGS'] = '0000000000000000'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
    elif ins[i][0]=='st':
        ins[i][2]=reg_values[ins[i][1]]
        reg_values['FLAGS'] = '0000000000000000'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
    elif ins[i][0]=='div':
        if reg_values[ins[i][2]]==0:
            reg_values['FLAGS'] = '0000000000001000'
            reg_values['R0'] = 0
            reg_values['R1'] = 0
        else:
            reg_values['R0']=reg_values[ins[i][1]]//reg_values[ins[i][2]]
            reg_values['R1'] = reg_values[ins[i][1]] % reg_values[ins[i][2]]
            reg_values['FLAGS'] = '0000000000000000'

        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i+1
    elif ins[i][0]=='rs':
        reg_values[ins[i][1]]+=ins[i][2]
        if reg_values[ins[i][1]]>65535:
            reg_values[ins[i][1]]=0
            reg_values['FLAGS'] = '0000000000001000'
        else:
            reg_values['FLAGS'] = '0000000000000000'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i+1
    elif ins[i][0]=='ls'  :
        reg_values[ins[i][1]]-=ins[i][2]
        if reg_values[ins[i][1]]<=0:
            reg_values[ins[i][1]]=0
            reg_values['FLAGS'] = '0000000000000100'
        else:
            reg_values['FLAGS'] = '0000000000000000'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
    elif ins[i][0]=='xor':
        reg_values[ins[i][1]] = reg_values[ins[i][2]] ^ reg_values[ins[i][3]]
        if reg_values[ins[i][1]] > 65535:
            reg_values[ins[i][1]] = 0
            reg_values['FLAGS'] = '0000000000001000'
        else:
            reg_values['FLAGS'] = '0000000000000000'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
    elif ins[i][0]=='or':
        reg_values[ins[i][1]] = reg_values[ins[i][2]] | reg_values[ins[i][3]]
        if reg_values[ins[i][1]] > 65535:
            reg_values[ins[i][1]] = 0
            reg_values['FLAGS'] = '0000000000001000'
        else:
            reg_values['FLAGS'] = '0000000000000000'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
    elif ins[i][0]=='and':
        reg_values[ins[i][1]] = reg_values[ins[i][2]] & reg_values[ins[i][3]]
        if reg_values[ins[i][1]] > 65535:
            reg_values[ins[i][1]] = 0
            reg_values['FLAGS'] = '0000000000001000'
        else:
            reg_values['FLAGS'] = '0000000000000000'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
    elif ins[i][0]=='not':
        r2_value=decimal_to_binary(reg_values[ins[i][2]])
        result_int = ''.join('1' if bit == '0' else '0' for bit in r2_value)
        # print(result_int)
        k= int(result_int)
        reg_values[ins[i][1]]=(binary_To_Decimal(k))
        # print(reg_values[ins[i][1]])
        if reg_values[ins[i][1]] > 65535:
            reg_values[ins[i][1]] = 0
            reg_values['FLAGS'] = '0000000000001000'
        if reg_values[ins[i][1]]<0:
            reg_values[ins[i][1]]=0
            reg_values['FLAGS'] = '0000000000000100'
        else:
            reg_values['FLAGS'] = '0000000000000000'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
    elif ins[i][0]=='cmp':
        if reg_values[ins[i][1]] == reg_values[ins[i][2]]:
            reg_values['FLAGS'] = '0000000000000001'
        elif reg_values[ins[i][1]] > reg_values[ins[i][2]]:
            reg_values['FLAGS'] = '0000000000000010'
        else:
            reg_values['FLAGS'] = '0000000000000100'
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
    elif ins[i][0]=='hlt':
        print(f"{decimal_to_binary(i)[-7:]}        {decimal_to_binary(reg_values['R0'])} {decimal_to_binary(reg_values['R1'])} {decimal_to_binary(reg_values['R2'])} {decimal_to_binary(reg_values['R3'])} {decimal_to_binary(reg_values['R4'])} {decimal_to_binary(reg_values['R5'])} {decimal_to_binary(reg_values['R6'])} {reg_values['FLAGS']}")
        i = i + 1
        continue
for i in input:
    print(i.rstrip())
x=len(input)
count_var=0
for i in ins:
    if (i[0] =='st'):
        print(decimal_to_binary(i[-1]))
        count_var+=1
y=128-(count_var+x)
for i in range(y):
    print('0'*16)
