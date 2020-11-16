from collections import defaultdict


memory = defaultdict(int)
basememoryvalue = 0
instructionPointer = 0

def importarray(param):
    global memory
    with open(param, "r") as f:
        counter = 0
        for data in f.read().split(","):
            data = data.replace("\n", "")
            memory[counter] = data
            counter += 1

def processOpcode(opcode):
    global instructionPointer
    global basememoryvalue
    global memory
    opcode = str(opcode)
    while len(str(opcode)) < 5:
        if len(str(opcode))>2 and str(opcode[-2]) != "0" and str(opcode[-2:]) != "99":
            opcode = str(opcode)[:-1] + "0" + str(opcode)[-1]
        else:
            opcode = "0"+str(opcode)
    instruction = [int(opcode[0]), int(opcode[1]), int(opcode[2]), opcode[3]+opcode[4]]
    test = basememoryvalue
    if instruction[3] in ["01", "02", "07", "08"]:
        if instruction[2] == 0:
            parameter1 = memory[int(memory[instructionPointer+1])]
        elif instruction[2] ==1:
            parameter1 = memory[instructionPointer+1]
        else:
            parameter1 = memory[basememoryvalue+int(memory[instructionPointer+1])]

        if instruction[1] == 0:
            parameter2 = memory[int(memory[instructionPointer+2])]
        elif instruction[1] ==1:
            parameter2 = memory[instructionPointer+2]
        else:
            parameter2 = memory[basememoryvalue+int(memory[instructionPointer+2])]

        if instruction[0] == 0:
            parameter3 = memory[instructionPointer+3]
        elif instruction[0] ==1:
            parameter3 = instructionPointer+3
        else:
            parameter3 = int(memory[instructionPointer+3])+basememoryvalue

    elif instruction[3] == "03":
        if instruction[2] == 0:
            parameter1 = memory[instructionPointer+1]
        elif instruction[2] == 1:
            parameter1 = instructionPointer+1
        else:
            parameter1 = basememoryvalue+int(memory[instructionPointer+1])
        parameter2 = 0
        parameter3 = 0

    elif instruction[3] == "04":
        if instruction[2] == 0:
            parameter1 = memory[instructionPointer+1]
        elif instruction[2] == 1:
            parameter1 = instructionPointer+1
        else:
            parameter1 = basememoryvalue+int(memory[instructionPointer+1])
        parameter2 = 0
        parameter3 = 0

    elif instruction[3] in ["05","06"]:
        if instruction[2] == 0:
            parameter1 = memory[int(memory[instructionPointer+1])]
        elif instruction[2] == 1:
            parameter1 = memory[instructionPointer+1]
        else:
            parameter1 = memory[basememoryvalue+int(memory[instructionPointer+1])]

        if instruction[1] == 0:
            parameter2 = memory[int(memory[instructionPointer+2])]
        elif instruction[1] == 1:
            parameter2 = memory[instructionPointer+2]
        else:
            parameter2 = memory[basememoryvalue+int(memory[instructionPointer+2])]
        parameter3 = 0

    elif instruction[3] == "09":
        if instruction[2] == 0:
            parameter1 = memory[int(memory[instructionPointer+1])]
        elif instruction[2] == 1:
            parameter1 = memory[instructionPointer+1]
        else:
            parameter1 = memory[basememoryvalue+int(memory[instructionPointer+1])]
        parameter2 = 0
        parameter3 = 0


    elif instruction[3] == "99":
        parameter1 = 0
        parameter2 = 0
        parameter3 = 0

    return [parameter3, parameter2, parameter1, instruction[3]]




def runprogram(input):
    global memory
    global instructionPointer
    global basememoryvalue
    instructionPointer = 0
    step = 1
    output = 0
    while True:
        instruction = processOpcode(memory[instructionPointer])
        opcode = int(instruction[3])
        instruction1 = int(instruction[2])
        instruction2 = int(instruction[1])
        outputaddress = int(instruction[0])
        if opcode == 1:
            memory[outputaddress] = str(instruction1+instruction2)
            instructionPointer += 4
        elif opcode == 2:
            memory[outputaddress] = str(instruction1*instruction2)
            instructionPointer += 4
        elif opcode == 3:
            memory[instruction1] = str(input)
            instructionPointer += 2
        elif opcode == 4:
            output = memory[instruction1]
            print(f"diagnostic: {output}")
            instructionPointer += 2
        elif opcode == 5:
            if instruction1 != 0:
                instructionPointer = instruction2
            else:
                instructionPointer += 3
        elif opcode == 6:
            if instruction1 == 0:
                instructionPointer = instruction2
            else:
                instructionPointer += 3
        elif opcode == 7:
            if instruction1 < instruction2:
                memory[outputaddress] = str(1)
            else:
                memory[outputaddress] = str(0)
            instructionPointer += 4
        elif opcode == 8:
            if instruction1 == instruction2:
                memory[outputaddress] = str(1)
            else:
                memory[outputaddress] = str(0)
            instructionPointer += 4
        elif opcode == 9:
            basememoryvalue = basememoryvalue + instruction1
            instructionPointer += 2
        elif opcode == 99:
            print(f"final output: {output}")
            break




def compute(input, program):
    importarray(program)
    runprogram(input)
importarray("input.txt")
runprogram(0)