import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)


def task_bot():
    tasks = load_tasks()
    print("Hello! I'm a simple task bot. How can I assist you today?")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["quit", "exit"]:
            print("TaskBot: Bye! Here’s your final task list:")
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("You have no tasks.")
            save_tasks(tasks)
            break

        # Add a task
        elif user_input.startswith("add"):
            task = user_input[4:].strip()
            if task:
                tasks.append(task)
                print("TaskBot: Task added!")
            else:
                print("TaskBot: Please provide a task to add.")
        
        # Show task list
        elif user_input == "show" or user_input == "show tasks" or user_input == "list tasks":
            if tasks:
                print("TaskBot: Here are your tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("TaskBot: You have no tasks yet!.")

        # Remove a specific task
        elif user_input.startswith("remove"):
            try:
                task_num = int(user_input[7:].strip())
                if 1 <= task_num <= len(tasks):
                    removed_task = tasks.pop(task_num - 1)
                    print(f"TaskBot: Task '{removed_task}' removed.")
                else:
                    print("TaskBot: Invalid task number.")
            except ValueError:
                print("TaskBot: Please provide a valid task number to remove.")
        
        # Clear tasks
        elif user_input == "clear" or user_input == "clear tasks" or user_input == "delete all tasks":
            tasks.clear()
            print("TaskBot: All tasks cleared.")

        else:
            print("TaskBot: I'm sorry, I don't understand. Can you please rephrase?")

if __name__ == "__main__":
    task_bot()