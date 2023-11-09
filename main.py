with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите строку (или введите пустую строку для выхода): ")
        if not line:
            break
        f1.write(line + '\n')
with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    for line in f1:
        if not any(char.isdigit() for char in line):
            f2.write(line)

with open('F2.txt', 'r') as f2:
    count_lines_starting_with_A = sum(1 for line in f2 if line.strip().startswith('А'))

print(f"Количество строк, начинающихся с русской 'А' в файле F2: {count_lines_starting_with_A}")
