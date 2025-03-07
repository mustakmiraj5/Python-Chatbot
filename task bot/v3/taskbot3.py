import json

def load_tasks():
    try:
        with open("tasks3.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open("tasks3.json", "w") as file:
        json.dump(tasks, file)


def task_bot():
    tasks = load_tasks()
    print("Hello! I'm a simple task bot. How can I assist you today?")
    print("Commands: 'add <task>', 'show', 'done <number>', 'undo <number>', 'remove <number>', 'view done', 'view undone', 'help', 'clear'")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["quit", "exit"]:
            print("TaskBot: Bye! Here’s your final task list:")
            if tasks:
                for i, task in enumerate(tasks, 1):
                    status = "[X]" if task["completed"] else "[ ]"
                    print(f"{i}. {status} {task['text']}")
            else:
                print("You have no tasks.")
            save_tasks(tasks)
            break

        parts = user_input.split(maxsplit=1)
        command = parts[0] if parts else ""
        argument = parts[1] if len(parts) > 1 else ""

        # Add a task
        if command == "add":
            if argument:
                tasks.append({"text": argument, "completed": False})
                print(f"TaskBot: Added '{argument}'!")
                save_tasks(tasks)
            else:
                print("TaskBot: Please provide a task to add.")

        # Show task list
        elif command in ["show", "list"] or user_input in ["show tasks", "list tasks"]:
            if tasks:
                print("TaskBot: Here are your tasks:")
                for i, task in enumerate(tasks, 1):
                    status = "[X]" if task["completed"] else "[ ]"
                    print(f"{i}. {status} {task['text']}")
            else:
                print("TaskBot: You have no tasks yet!.")

        # Mark a task as done
        elif command == "done":
            if argument:
                try:
                    task_num = int(argument)
                    if 1 <= task_num <= len(tasks):
                        tasks[task_num - 1]["completed"] = True
                        print(f"TaskBot: Task '{tasks[task_num - 1]['text']}' marked as done.")
                        save_tasks(tasks)
                    else:
                        print("TaskBot: Invalid task number.")
                except ValueError:
                    print("TaskBot: Please provide a valid task number to mark as done.")

        # Undo a task
        elif command == "undo":
            if argument:
                try:
                    task_num = int(argument)
                    if 1 <= task_num <= len(tasks):
                        tasks[task_num - 1]["completed"] = False
                        print(f"TaskBot: Task '{tasks[task_num - 1]['text']}' marked as undone.")
                        save_tasks(tasks)
                    else:
                        print("TaskBot: Invalid task number.")
                except ValueError:
                    print("TaskBot: Please provide a valid task number to undo.")

        # Remove a specific task
        elif command == "remove":
            if argument:
                try:
                    task_num = int(argument)
                    if 1 <= task_num <= len(tasks):
                        removed_task = tasks.pop(task_num - 1)
                        print(f"TaskBot: Task '{removed_task['text']}' removed.")
                        save_tasks(tasks)
                    else:
                        print("TaskBot: Invalid task number.")
                except ValueError:
                    print("TaskBot: Please provide a valid task number to remove.")
            else:
                print("TaskBot: Please provide a task number to remove.")

        # Show done tasks
        elif user_input in ["view done"]:
            done_tasks = [task for task in tasks if task["completed"]]
            if done_tasks:
                print("TaskBot: Here are your completed tasks:")
                for i, task in enumerate(done_tasks, 1):
                    print(f"{i}. [x] {task['text']}")
            else:
                print("TaskBot: You have no completed tasks.")

        # Show undone tasks
        elif user_input in ["view undone"]:
            undone_tasks = [task for task in tasks if not task["completed"]]
            if undone_tasks:
                print("TaskBot: Here are your undone tasks:")
                for i, task in enumerate(undone_tasks, 1):
                    print(f"{i}. [ ] {task['text']}")
            else:
                print("TaskBot: You have no undone tasks.")


        # Clear tasks
        elif command in ["clear", "delete"] or user_input in ["clear tasks", "delete all tasks", "delete tasks", "delete all"]:
            tasks.clear()
            print("TaskBot: All tasks cleared.")
            save_tasks(tasks)

        elif command == "help":
            print("TaskBot: Commands: 'add <task>', 'show', 'done <number>', 'undo <number>', 'remove <number>', 'view done', 'view undone', 'help', 'clear'")

        else:
            print("TaskBot: I'm sorry, I don't understand. Can you please rephrase?")

if __name__ == "__main__":
    task_bot()