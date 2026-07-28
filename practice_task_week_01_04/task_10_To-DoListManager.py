
# Task 10 — To-Do List Manager (menu loop)

# Ek khaali list todos = [] banao. Ek while True menu chalao: 1) Add 2) Remove 3) Show 4) Quit.
#  User ke choice ke hisaab se task add/remove/show karo. 4 par loop break karo.

# Concepts: while True, match/case (ya if/elif), list .append()/.remove(), break
# Hint: remove karte waqt check karo item list mein hai ya nahi (warna crash), if item in todos:.

print("===============To-Do List Manager (menu loop)============")

todos = []

while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a task: ")
        todos.append(task)
        print("Task added successfully!")

    elif choice == "2":
        task = input("Enter the task to remove: ")

        if task in todos:
            todos.remove(task)
            print("Task removed successfully!")
        else:
            print("Task not found!")

    elif choice == "3":
        if len(todos) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(todos, start=1):
                print(f"{i}. {task}")

    elif choice == "4":
        print("Thank you! Exiting To-Do List Manager.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 4.")









        # copy peast vala haii
        