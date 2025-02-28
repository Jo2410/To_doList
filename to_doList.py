
def add_task():
    pass
def mark_task_complete():
    pass

def view_tasks():
    pass


message=("1-add tasks to a list\n"
         "2-mark task as complete\n"
         "3-view tasks\n"
         "4-Quit\n")

tasks=[]

while True:
    print(message)
    choice=input("enter your choice: ")

    if choice=="1":
        add_task()
    elif choice=="2":
        mark_task_complete()
    elif choice=="3":
        view_tasks()
    elif choice=="4":
        break
    else:
        print("Invalid choice,please enter a number between 1 and 4")


