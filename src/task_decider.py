def get_preferred_option(task_1, task_2):
    
    # Wash dishes over cook dinner 
    if task_1.description == "Wash the dishes" and task_2.description == "Cook dinner":
        return task_1.description
    elif  task_1.description == "Cook dinner" and task_2.description == "Wash the dishes":
        return task_2.description
    
    # Cook dinner over clean windows
    elif  task_1.description == "Cook dinner" and task_2.description == "Clean windows":
        return task_1.description
    elif  task_1.description == "Clean windows" and task_2.description == "Cook dinner":
        return task_2.description

    # Clean windows over wash dishes
    elif  task_1.description == "Clean windows" and task_2.description == "Wash the dishes":
        return task_1.description
    else:
        return task_2.description