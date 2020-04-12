#!/Users/jacogericke/anaconda3/bin/python3

import itertools

INPUTS = [3,8,1001,8,10,8,105,1,0,0,21,34,55,68,85,106,187,268,349,430,99999,3,9,1001,9,5,9,1002,9,5,9,4,9,99,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,4,9,99,3,9,101,3,9,9,102,3,9,9,4,9,99,3,9,1002,9,5,9,101,3,9,9,102,5,9,9,4,9,99,3,9,1002,9,4,9,1001,9,2,9,102,3,9,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99]

FAKE3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
FAKE2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
FAKE1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]

class OpCode(object):

    def __init__(self, program, inputs=[]):
        self.index = 0
        self.program = program
        self.len = len(program)
        self.inputs = inputs
        self.input_index = 0
        self.__last_out__ = None

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

        save = self.inputs[self.input_index]
        self.input_index += 1

        self.program[address] = int(save)
        self.index += 2
    
    def opcode4(self, modes):
        address = self.get_index(self.index+1)

        #print(self.program[address])
        self.__last_out__ = self.program[address]
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
    max_ans = 0
    max_itr = []

    for itr in itertools.permutations([0,1,2,3,4]):
        ans = 0
        for seq in itr:
            tmp = OpCode(INPUTS, inputs=[seq, ans])
            tmp.start()
            ans  = tmp.__last_out__
        if ans > max_ans:
            max_ans = ans
            max_itr = itr
    print(max_itr, max_ans)

    
    

