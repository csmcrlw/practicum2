from task_13.task_manager import tasks


def show_help():
    print(help(tasks.add_task))
    print(help(tasks.view_tasks))
    print(help(tasks.delete_task))
