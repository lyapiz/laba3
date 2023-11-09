translation_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре'
}

with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for line in input_file:
        for key, value in translation_dict.items():
            line = line.replace(key, value)
        output_file.write(line)

print("Замена числительных выполнена, результат сохранен в файл 'output.txt'.")
