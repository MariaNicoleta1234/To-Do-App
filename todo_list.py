to_do_list = []

def add_task():
    task = input("Introdu task-ul: ")
    to_do_list.append({"task": task, "completed": False})
    print(f"Task-ul '{task}' a fost adăugat cu succes.")

def delete_task():
    view_tasks()
    if to_do_list:
        try:
            task_number = int(input("Introdu numărul task-ului de șters: ")) - 1
            if 0 <= task_number < len(to_do_list):
                removed_task = to_do_list.pop(task_number)
                print(f"Task-ul '{removed_task}' a fost șters.")
            else:
                print("Număr invalid. Te rog să alegi un număr din listă.")
        except ValueError:
            print("Te rog să introduci un număr valid.")

def mark_task_complete():
    view_tasks()
    if to_do_list:
        task_number = int(input("Introdu numărul task-ului de marcat ca fiind complet: ")) - 1
        if 0 <= task_number < len(to_do_list):
            to_do_list[task_number]["completed"] = True
            print(f"Task-ul '{to_do_list[task_number]['task']}' a fost marcat ca complet.")
        else:
            print("Număr invalid.")

def view_tasks():
    if not to_do_list:
        print("Lista de task-uri este goală.")
    else:
        print("Task-urile tale:")
        for idx, task in enumerate(to_do_list, start=1):
            status = "Completat" if task["completed"] else "Incomplet"
            print(f"{idx}. {task['task']} - {status}")

# Adaugă opțiunea de a marca un task ca fiind complet
def show_menu():
    while True:
        print("\n--- Meniu To-Do List ---")
        print("1. Adaugă task")
        print("2. Vizualizează task-urile")
        print("3. Șterge task")
        print("4. Marchează task-ul ca fiind complet")
        print("5. Ieși")
        choice = input("Alege o opțiune (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_complete()
        elif choice == "5":
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă. Încearcă din nou.")

if __name__ == "__main__":
    show_menu()
