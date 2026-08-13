def print_menu():    
    print('''
    \nTo Do List:
    1. Veiw Task
    2. Add a Task
    3. Remove a Task
    4. Exit
        ''')
    
def get_choice():
    while True:
        choice = input('Enter your choice: ')
        valid_choices=('1','2','3','4')
        if choice not in valid_choices:
            print('invalid choice , please try again!!') 
            continue 
        else:
            return choice
        
def add_task(tasks):
    while True:
        task= input('Enter new task: ').strip()
        if task != '':
            tasks.append(task)
            break
        else:
            print('invalid task , please try again!!')
        return
    
def remove_task(tasks):
    display_tasks(tasks)
    while True:
        try:
            task_number=int(input('Enter the task number: '))
            if 1<=task_number>= len(tasks):
                tasks.pop(task_number-1)
                break
            else:
                raise ValueError
        except ValueError:
            print('invalid task number , please try again!!')

def display_tasks(tasks):
    if not  tasks:
        print('No task in the list')
        return
    for index,task in enumerate(tasks, start=1):
        print(f'{index}. {task}')
        

def main():
    tasks=[]
    while True: 
        print_menu()
        choice= get_choice()
        if choice == '1':
            display_tasks(tasks)
        elif choice== '2':
            add_task(tasks)
        elif choice =='3':
            remove_task(tasks)
        else:
            break
    
    
if __name__=='__main__':
    main()
