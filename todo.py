print "Welcome to the TODO task management program."
# all_tasks = []
#
# while True:
#     task = raw_input("Please enter a TODO task: ")
#     all_tasks.append(task)
#     print "Your task is: " + task
#
#     new = raw_input("Would you like to enter new task? (yes/no) ")
#
#     if new == "no":
#         break
# print "All tasks: %s" % all_tasks
# for ts in all_tasks:
#     print ts
#
# print "END"

# all_tasks = {
#     'Pridi na SmartNinjo': True
# }
#
# while True:
#     task = raw_input("Please enter a TODO task: ")
#     all_tasks[task] = False
#     print "Your task is: " + task
#
#     new = raw_input("Would you like to enter new task? (yes/no) ")
#
#     if new == "no":
#         break
# print "All tasks: %s" % all_tasks
# # for ts in all_tasks:
# #     print ts
# todo_file = open("todo.txt", "w+")
# todo_file.write("Completed tasks:\n")
# for item in all_tasks:
#     if all_tasks[item]:
#         print "- " + item
#         todo_file.write("- " + item + "\n")
#
# todo_file.write("\n")
#
# print "Incomplete tasks:"
# todo_file.write("Incomplete tasks:\n")  # write into the TXT file
# for item in all_tasks:
#     if not all_tasks[item]:
#         print "- " + item
#         todo_file.write("- " + item + "\n")
#
# todo_file.close()
#
# print "END"

# empty_list = []
# print empty_list
#
# list_with_items = ["first item", "second item", 34, 12.4]
# print list_with_items
#
#
# var1 = "first variable"
# var2 = "second variable"
# some_list = [var1, var2, 'neki']
# print some_list
