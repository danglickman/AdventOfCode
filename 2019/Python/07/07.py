import itertools
from intcode import IntCode

program = [int(x.strip()) for x in open('input', 'r').read().strip().split(',')]

phase_settings = itertools.permutations([0,1,2,3,4,])

max_output = 0
for ps in phase_settings:
    outputs = [0]
    for phase in ps:
        gen = (x for x in (phase, outputs[-1]))
        input_function = lambda: next(gen)
        output_function = outputs.append
        computer = IntCode(program, input_function=input_function, output_function=output_function)
        computer.run()
    max_output = max(max_output, outputs[-1])

print("Part 1:", max_output)