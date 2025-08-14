instructions = [int(x) for x in open('input', 'r').read().strip().split(',')]

class IntCode(object):
    def __init__(self, program):
        self.program = program
        self.ip = 0
        self.mem = self.program.copy()

    def reset_memory(self):
        self.ip = 0
        self.mem = self.program.copy()

    def set_inputs(self, inputs):
        self.mem[1] = inputs[0]
        self.mem[2] = inputs[1]

    def run(self):
        while True:
            op = self.mem[self.ip]
            if op == 99:
                break
            if op == 1:
                self.mem[self.mem[self.ip + 3]] = self.mem[self.mem[self.ip + 1]] + self.mem[self.mem[self.ip + 2]]
            if op == 2:
                self.mem[self.mem[self.ip + 3]] = self.mem[self.mem[self.ip + 1]] * self.mem[self.mem[self.ip + 2]]
            self.ip += 4
    
    def get_output(self):
        return self.mem[0]

computer = IntCode(instructions)

## Part 1
computer.set_inputs((12, 2))
computer.run()
print("Part 1:", computer.get_output())


## Part 2
target = int(open("target", 'r').read().strip())

input_sum = 0
while True:
    for i in range(input_sum + 1):
        ic_input = (i, input_sum - i)
        computer.set_inputs(ic_input)
        computer.run()
        if computer.get_output() == target:
            print("Part 2", 100 * ic_input[0] + ic_input[1])
            exit()
        computer.reset_memory()
    input_sum += 1
    if input_sum > 200:
        break