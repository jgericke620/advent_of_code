#!/Users/jacogericke/anaconda3/bin/python3

REAL = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,11,91,225,1002,121,77,224,101,-6314,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1102,74,62,225,1102,82,7,224,1001,224,-574,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1101,28,67,225,1102,42,15,225,2,196,96,224,101,-4446,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1101,86,57,225,1,148,69,224,1001,224,-77,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1101,82,83,225,101,87,14,224,1001,224,-178,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1101,38,35,225,102,31,65,224,1001,224,-868,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,1101,57,27,224,1001,224,-84,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1101,61,78,225,1001,40,27,224,101,-89,224,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,1002,223,2,223,1006,224,329,101,1,223,223,8,226,677,224,102,2,223,223,1005,224,344,101,1,223,223,1107,226,677,224,102,2,223,223,1006,224,359,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,374,101,1,223,223,7,677,677,224,102,2,223,223,1005,224,389,1001,223,1,223,108,677,677,224,1002,223,2,223,1005,224,404,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,419,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,434,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,449,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,464,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,479,101,1,223,223,1007,226,677,224,1002,223,2,223,1006,224,494,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,509,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,524,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,539,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,554,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,569,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,584,101,1,223,223,1107,677,677,224,102,2,223,223,1005,224,599,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,614,101,1,223,223,8,226,226,224,102,2,223,223,1006,224,629,101,1,223,223,108,226,677,224,102,2,223,223,1005,224,644,1001,223,1,223,108,226,226,224,102,2,223,223,1005,224,659,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]

IN = 0

class OpCode(object):

    def __init__(self, program):
        self.index = 0
        self.program = program
        self.len = len(program)
        self.input_count = 0

    def get_index(self, get_index):
        if len(self.program) >= get_index+1:
            return self.program[get_index]
        else:
            raise Exception(f"No such index as {get_index}")
    
    def get_args(self, count=0, modes=[]):
        return_args = []
        for i, mode in enumerate(modes[:count]):
            if mode == 1:
                tmp = self.get_index(self.index+1+i)
            elif mode == 0:
                tmp = self.get_index(self.get_index(self.index+1+i))
            else:
                raise Exception(f"Mode {mode}")
            return_args.append(tmp)
        return return_args
        


    def opcode1(self, modes):
        values = self.get_args(2, modes)
        address = self.get_index(self.index+3)

        self.program[address] = values[0] + values[1]
        self.index += 4


    def opcode2(self, modes):
        values = self.get_args(2, modes)
        address = self.get_index(self.index+3)

        self.program[address] = values[0] * values[1]
        self.index += 4

    def opcode3(self, modes):
        address = self.get_index(self.index+1)
        #save = input("Please supply input\n")
        save = IN

        self.program[address] = int(save)
        self.index += 2
    
    def opcode4(self, modes):
        address = self.get_index(self.index+1)

        print(self.program[address])
        self.index += 2

    # Opcode 5 is jump-if-true: 
    # if the first parameter is non-zero, it sets the instruction pointer 
    # to the value from the second parameter. Otherwise, it does nothing.
    def opcode5(self, modes):
        #first = self.get_index(self.index+1)
        #sec = self.get_index(self.index+2)
        values = self.get_args(2, modes)
        if values[0] != 0:
            self.index = values[1]
        else:
           self.index += 3

    # Opcode 6 is jump-if-false: 
    # if the first parameter is zero, it sets the instruction pointer to 
    # the value from the second parameter. Otherwise, it does nothing.
    def opcode6(self, modes):
        #first = self.get_index(self.index+1)
        #sec = self.get_index(self.index+2)
        values = self.get_args(2, modes)
        if values[0] == 0:
            self.index = values[1] 
        else:
            self.index += 3


    # Opcode 7 is less than: 
    # if the first parameter is less than the second parameter, it stores 
    # 1 in the position given by the third parameter. Otherwise, it stores 0.
    def opcode7(self, modes):
        values = self.get_args(2, modes)
        address = self.get_index(self.index+3)
       
        if values[0] < values[1]:
            self.program[address] = 1
        else:
            self.program[address] = 0 
        
        self.index += 4

    # Opcode 8 is equals: 
    # if the first parameter is equal to the second parameter, it stores 
    # 1 in the position given by the third parameter. Otherwise, it stores 0.
    def opcode8(self, modes):
        values = self.get_args(2, modes)
        address = self.get_index(self.index+3)
       
        if values[0] == values[1]:
            self.program[address] = 1
        else:
            self.program[address] = 0 
        
        self.index += 4

    def parse_inst(self):

        value = self.get_index(self.index)
        value += 900000
        chars = str(value)
        
        mode3 = int(chars[1])
        mode2 = int(chars[2])
        mode1 = int(chars[3])
        opcode = int(chars[4] + chars[5])

        return (opcode, [mode1, mode2, mode3])


    def start(self):
        done = False

        while not done:

            op, modes = self.parse_inst()

            if op == 1:
                self.opcode1(modes)
            elif op == 2:
                self.opcode2(modes)
            elif op == 3:
                self.opcode3(modes)
            elif op == 4:
                self.opcode4(modes)
            elif op == 5:
                self.opcode5(modes)
            elif op == 6:
                self.opcode6(modes)
            elif op == 7:
                self.opcode7(modes)
            elif op == 8:
                self.opcode8(modes)

            elif op == 99:
                done = True


if __name__ == "__main__":

    BIG = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
             1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
             999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]


    INPUTS = [[3,9,8,9,10,9,4,9,99,-1,8], #- Using position mode, 1 if 8
              [3,9,7,9,10,9,4,9,99,-1,8],# - Using position mode, 1 if < 8
              [3,3,1108,-1,8,3,4,3,99], #- Using immediate mode, 1 if 8
              [3,3,1107,-1,8,3,4,3,99]] #- Using immediate mode, 1 if < 8

    JUMPS = [[3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], #(using position mode)
             [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]] #(using immediate mode)

    IN = 8
    print("IN 8")
    for INPUT in INPUTS:
        oc = OpCode(INPUT)
        oc.start()

    IN = 7
    print("IN 7")
    for INPUT in INPUTS:
        oc = OpCode(INPUT)
        oc.start()


    IN = 0
    print("IN 0")
    for INPUT in JUMPS:
        oc = OpCode(INPUT)
        oc.start()

    IN = 99
    print("IN 99")
    for INPUT in JUMPS:
        oc = OpCode(INPUT)
        oc.start()

    
    
    IN = 5
    print("IN 99")
    oc = OpCode(REAL)
    oc.start()

    

