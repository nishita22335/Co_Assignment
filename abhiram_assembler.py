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
f = open("input", "r")
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
    
