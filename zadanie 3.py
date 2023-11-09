#vim: set fileencoding=<"unicode-escape">
subjects_dict = {}

with open('subjects.txt', 'r') as file:
    for line in file:
        parts = line.strip().split(':')
        if len(parts) == 2:
            subject = parts[0].strip()
            info = parts[1].strip()

            numbers = [int(x.split('(')[0]) for x in info.split()]

            total_lessons = sum(numbers)
            subjects_dict[subject] = total_lessons

for subject, total_lessons in subjects_dict.items():
    print(f"{subject}: {total_lessons}")