#!/Users/jacogericke/anaconda3/bin/python3

INPUT = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,23,6,27,1,5,27,31,1,10,31,35,2,6,35,39,1,39,13,43,1,43,9,47,2,47,10,51,1,5,51,55,1,55,10,59,2,59,6,63,2,6,63,67,1,5,67,71,2,9,71,75,1,75,6,79,1,6,79,83,2,83,9,87,2,87,13,91,1,10,91,95,1,95,13,99,2,13,99,103,1,103,10,107,2,107,10,111,1,111,9,115,1,115,2,119,1,9,119,0,99,2,0,14,0]

class OpCode(object):

    def __init__(self, program):
        self.index = 0
        self.program = program

    def get_index(self, get_index):
        if len(self.program) >= get_index+1:
            return self.program[get_index]
        else:
            raise Exception(f"No such index as {get_index}")

    def opcode1(self):
        first = self.get_index(self.get_index(self.index+1))
        second = self.get_index(self.get_index(self.index+2))
        third = self.get_index(self.index+3)

        self.program[third] = first + second


    def opcode2(self):
        first = self.get_index(self.get_index(self.index+1))
        second = self.get_index(self.get_index(self.index+2))
        third = self.get_index(self.index+3)

        self.program[third] = first * second

    def start(self):
        done = False

        while not done:
            if self.get_index(self.index) == 1:
                self.opcode1()
            elif self.get_index(self.index) == 2:
                self.opcode2()
            elif self.get_index(self.index) == 99:
                done = True
            self.index += 4

        print("OUTPUT", ",".join([str(x) for x in self.program]))


if __name__ == "__main__":
    INPUTS = [[1,0,0,0,99],
              [2,3,0,3,99],
              [2,4,4,5,99,0],
              [1,1,1,4,99,5,6,0,99]]
    for l in INPUTS:
        print("INPUT", l)
        oc = OpCode(l)
        oc.start()
        print('\n')

    print("FINAL\n")

    oc = OpCode(INPUT)
    oc.start()

    

