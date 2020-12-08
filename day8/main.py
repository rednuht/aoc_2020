def part1(instructions):
    accumulator, _ = run_instructions(instructions)
    print('part1', accumulator)


def part2(instructions):
    for i, (instruction, argument) in enumerate(instructions):
        if instruction in ('nop', 'jmp'):
            instructions_copy = instructions.copy()
            if instruction == 'nop':
                instructions_copy[i] = ['jmp', argument]
            elif instruction == 'jmp':
                instructions_copy[i] = ['nop', argument]

            accumulator, successful = run_instructions(instructions_copy, check_termination=True)
            if successful:
                print('part2', accumulator)
                break


def run_instructions(instructions, check_termination=False):
    accumulator = 0
    visited_instructions = set()
    instruction_pointer = 0
    nr_instructions = len(instructions)
    terminated_successfully = False

    while True:
        if check_termination:
            if instruction_pointer == nr_instructions:
                terminated_successfully = True
                break
        instruction, argument = instructions[instruction_pointer]

        if instruction_pointer in visited_instructions:
            break

        visited_instructions.add(instruction_pointer)
        argument = int(argument)
        if instruction == 'acc':
            accumulator += argument
            instruction_pointer += 1
        elif instruction == 'jmp':
            instruction_pointer += argument
        elif instruction == 'nop':
            instruction_pointer += 1

    return accumulator, terminated_successfully


def day8():
    with open('input.txt') as file:
        instructions = [line.strip().split() for line in file]

    part1(instructions)
    part2(instructions)


if __name__ == '__main__':
    day8()
