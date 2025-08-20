import intcode

def read_program(filename):
    with open(filename) as f:
        return [int(x.strip()) for x in f.read().strip().split(',')]

class TestIntcode():
    def test_d05_t00(self):
        captured_lines = []
        program = read_program('./2019/Python/07/intcode_test_data/test_d05_t00')
        n = 10
        for i in range(n):
            computer = intcode.IntCode(program, input_function=lambda: i, output_function=captured_lines.append)
            computer.run()
        assert (len(captured_lines) == n)
        assert (int(x) == int(i) for i, x in enumerate(captured_lines))

    def test_d05_t01(self):
        captured_lines = []
        program = read_program('./2019/Python/07/intcode_test_data/test_d05_t01_pos_mod_eq_8')
        n = 10
        for i in range(n):
            computer = intcode.IntCode(program, input_function=lambda: i, output_function=captured_lines.append)
            computer.run()
        assert(len(captured_lines) == n)
        assert(int(x) == int(i==8) for i, x in enumerate(captured_lines))

    def test_d05_t02(self):
        captured_lines = []
        program = read_program('./2019/Python/07/intcode_test_data/test_d05_t02')
        n = 10
        for i in range(n):
            computer = intcode.IntCode(program, input_function=lambda: i, output_function=captured_lines.append)
            computer.run()
        assert (len(captured_lines) == n)
        assert (int(x) == int(i < 8) for i, x in enumerate(captured_lines))

    def test_d05_t03(self):
        captured_lines = []
        program = read_program('./2019/Python/07/intcode_test_data/test_d05_t03')
        n = 10
        for i in range(n):
            computer = intcode.IntCode(program, input_function=lambda: i, output_function=captured_lines.append)
            computer.run()
        assert(len(captured_lines) == n)
        assert(int(x) == int(i==8) for i, x in enumerate(captured_lines))

    def test_d05_t04(self):
        captured_lines = []
        program = read_program('./2019/Python/07/intcode_test_data/test_d05_t04')
        n = 10
        for i in range(n):
            computer = intcode.IntCode(program, input_function=lambda: i, output_function=captured_lines.append)
            computer.run()
        assert (len(captured_lines) == n)
        assert (int(x) == int(i < 8) for i, x in enumerate(captured_lines))

    def test_d05_t05(self):
        captured_lines = []
        program = read_program('./2019/Python/07/intcode_test_data/test_d05_t05')
        n = 10
        for i in range(n):
            computer = intcode.IntCode(program, input_function=lambda: i, output_function=captured_lines.append)
            computer.run()
        assert (len(captured_lines) == n)
        assert (int(x) == int(i == 0) for i, x in enumerate(captured_lines))

    def test_d05_t06(self):
        captured_lines = []
        program = read_program('./2019/Python/07/intcode_test_data/test_d05_t06')
        n = 10
        for i in range(n):
            computer = intcode.IntCode(program, input_function=lambda: i, output_function=captured_lines.append)
            computer.run()
        assert(len(captured_lines) == n)
        assert(int(x) == int(i==0) for i, x in enumerate(captured_lines))

    def test_d05_t07(self):
        captured_lines = []
        program = read_program('./2019/Python/07/intcode_test_data/test_d05_t07')
        n = 20
        for i in range(n):
            computer = intcode.IntCode(program, input_function=lambda: i, output_function=captured_lines.append)
            computer.run()
        assert(len(captured_lines) == n)
        for i, x in enumerate(captured_lines):
            if i<8:
                intended = 999
            elif i==8:
                intended = 1000
            else:
                intended = 1001
            assert(x == intended)

    def test_d05_t08(self):
        # main puzzle input for day 5
        program = read_program('./2019/Python/07/intcode_test_data/test_d05_t08_input')
        inputs = read_program('./2019/Python/07/intcode_test_data/test_d05_t08_id')
        expected_results = read_program('./2019/Python/07/intcode_test_data/test_d05_t08_sols')

        # part 1
        captured_lines = []
        computer = intcode.IntCode(program, input_function=lambda: inputs[0], output_function=captured_lines.append)
        computer.run()
        assert({expected_results[0], 0} == set(int(x) for x in captured_lines))

        # part 2
        captured_lines = []
        computer = intcode.IntCode(program, input_function=lambda: inputs[1], output_function=captured_lines.append)
        computer.run()
        assert (len(captured_lines) == 1)
        assert (expected_results[1] == int(captured_lines[0]))

if __name__ == '__main__':
    pass
