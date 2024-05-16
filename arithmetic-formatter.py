def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    lines = []
    answers = []

    for problem in problems:
        parts = problem.split()
        
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        first_number, operator, second_number = parts

        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not first_number.isdigit() or not second_number.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        if len(first_number) > 4 or len(second_number) > 4:
            return 'Error: Numbers cannot be more than four digits.'

        if operator == "+":
            answer = str(int(first_number) + int(second_number))
        elif operator == "-":
            answer = str(int(first_number) - int(second_number))
        
        width = max(len(first_number), len(second_number)) + 2

        first_line.append(first_number.rjust(width))
        second_line.append(operator + second_number.rjust(width - 1))
        lines.append("-" * width)
        answers.append(answer.rjust(width))

    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(lines)
    if display_answers:
        arranged_problems += "\n" + "    ".join(answers)
    problems = arranged_problems
    return problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')