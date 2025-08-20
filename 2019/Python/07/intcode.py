class IntCode(object):
    def __init__(self, program, input_function = input, output_function = print):
        self.program = program
        self.ip = 0
        self.mem = self.program.copy()
        self.arity = [
            0, # placeholder
            3, # opcode 1 : add
            3, # opcode 2 : mul
            1, # opcode 3 : store from input
            1, # opcode 4 : print
            2, # opcode 5 : jmp if not zero (true)
            2, # opcode 6 : jmp of false
            3, # opcode 7 : less than
            3, # opcode 8 : equals
        ]
        self.args = [0,0,0]
        self.input_function = input_function
        self.output_function = output_function


    def reset_memory(self):
        self.ip = 0
        self.mem = self.program.copy()

    def set_inputs(self, inputs):
        self.mem[1] = inputs[0]
        self.mem[2] = inputs[1]

    def read_value(self, mode, param):
        match mode:
            case 0:
                return self.mem[param]
            case 1:
                return param
        return None

    def run(self):
        while True:
            # print("ip", self.ip, ", mem", self.mem[self.ip: self.ip + 4])
            modes, op_code = divmod(self.mem[self.ip],100)
            # print("modes:", modes, "op_code:", op_code)
            if op_code == 99:
                # print("FINAL STATE", self.mem)
                break
            nargs = self.arity[op_code]
            ip_inc = nargs + 1
            for i in range(nargs):
                ## gets final immediate mode wrong but this is ignored by present implementation
                modes, mode = divmod(modes, 10)
                if i == 2:
                    mode = 1
                self.args[i] = self.read_value(mode, self.mem[self.ip+i+1])

            # print("TO DO:", op_code, get_op(op_code), "Args", self.args)
            match op_code:
                case 1:
                    self.mem[self.mem[self.ip + 3]] = self.args[0] + self.args[1]
                    self.ip += 4
                case 2:
                    self.mem[self.mem[self.ip + 3]] = self.args[0] * self.args[1]
                    self.ip += 4
                case 3:
                    self.mem[self.mem[self.ip+1]] = int(self.input_function())
                    self.ip += 2
                case 4:
                    self.output_function(self.args[0])
                    self.ip += 2
                case 5:
                    if self.args[0] != 0:
                        self.ip = self.args[1]
                    else:
                        self.ip += 3
                case 6:
                    if self.args[0] == 0:
                        self.ip = self.args[1]
                    else:
                        self.ip += 3
                case 7:
                    self.mem[self.mem[self.ip+3]] = int(self.args[0] < self.args[1])
                    self.ip += 4
                case 8:
                    self.mem[self.mem[self.ip+3]] = int(self.args[0] == self.args[1])
                    self.ip += 4
            # print("new ip", self.ip)
            # print("New STATE", self.mem)
