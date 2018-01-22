all_tasks = {}
rf = open('todo.txt', 'r+')
lines = rf.readlines()
completed = True

for line in lines:
    if line != 'Completed tasks:\n' and line != 'Incomplete tasks:\n':
        if line == '\n':
            completed = False
        else:
            key = line.replace('- ', '').replace('\n', '')
            all_tasks[key] = completed

        # nek KODA

print all_tasks

while True:
    task = raw_input("Please enter a name of TODO task to update: ")
    all_tasks[task] = not all_tasks[task]

    new = raw_input("Would you like to upadte any other task? (yes/no) ")

    if new == "no":
        break

print all_tasks

todo_file = open("todo.txt", "w+")
todo_file.write("Completed tasks:\n")
for item in all_tasks:
    if all_tasks[item]:
        print "- " + item
        todo_file.write("- " + item + "\n")

todo_file.write("\n")

print "Incomplete tasks:"
todo_file.write("Incomplete tasks:\n")  # write into the TXT file
for item in all_tasks:
    if not all_tasks[item]:
        print "- " + item
        todo_file.write("- " + item + "\n")

todo_file.close()

print "END"
