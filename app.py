def task():
    Tasks=[]  #Empty list
    print("------WELCOME TO THE TASK MANAGEMENT APP------")
    
    Total_task=int(input("Enter how many task you want to add= ")) 
    for i in range(1, Total_task+1):
        Task_name=input(f"Enter task {i} = ")  #Enter task 1=
        Tasks.append(Task_name)
    
    print(f"Today's tasks are\n{Tasks}")
    
    while True:
        Operation=int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop"))
        
        if Operation == 1:   #Add tasks
            add=input("Enter task you want to add= ")
            Tasks.append(add)
            print(f"Task {add} has been succesfully added...")
        
        elif Operation == 2:   #Update tasks
            update=input("Enter task name you want to update= ")
            if update in Tasks:
                new=input("Enter new task= ") 
                ind = Tasks.index(update)
                Tasks[ind]=new
                print(f"Updated task {new}")

        elif Operation == 3:  #Delete tasks
            delete=input("Enter task name you want to delete= ")
            if delete in Tasks: 
                ind = Tasks.index(delete)
                del Tasks[ind]
                print(f"Task {delete} has been deleted...")

        elif Operation == 4:  #View tasks
            print(f"Total Tasks = {Tasks}")

        elif Operation ==5:  #Exit
            print("Closing the program...")
            break

        else:
            print("Invalid value")

task()
                