# Определение класса Task
class Task:
    # Конструктор класса - инициализирует свойства (атрибуты) объекта
    def __init__(self, description, deadline):
        self.description = description  # Описание задачи (атрибут)
        self.deadline = deadline        # Срок выполнения (атрибут)
        self.is_completed = False       # Статус выполнения (атрибут)

    # Метод для отметки задачи как выполненной
    def mark_completed(self):
        self.is_completed = True

    # Метод для строкового представления задачи
    def __repr__(self):
        status = 'Выполнено' if self.is_completed else 'Не выполнено'
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

# Определение класса TaskManager
class TaskManager:
    # Конструктор класса - инициализирует список для хранения задач
    def __init__(self):
        self.tasks = []  # Список задач (атрибут)

    # Метод для добавления задачи в список
    def add_task(self, task):
        self.tasks.append(task)

    # Метод для отметки задачи как выполненной по её описанию
    def mark_task_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.mark_completed()
                break

    # Метод для вывода списка невыполненных задач
    def show_incomplete_tasks(self):
        incomplete_tasks = [task for task in self.tasks if not task.is_completed]
        if incomplete_tasks:
            for task in incomplete_tasks:
                print(task)
        else:
            print("Все задачи выполнены!")

    # Метод для вывода списка выполненных задач
    def show_completed_tasks(self):
        completed_tasks = [task for task in self.tasks if task.is_completed]
        if completed_tasks:
            for task in completed_tasks:
                print(task)
        else:
            print("Нет выполненных задач.")

# Основной код программы для работы с объектами
def main():
    # Создаем объект TaskManager (менеджера задач)
    task_manager = TaskManager()

    # Взаимодействие с пользователем
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Отметить задачу как выполненную")
        print("3. Показать невыполненные задачи")
        print("4. Показать выполненные задачи")
        print("5. Выйти")

        choice = input("\nВыберите действие (1-5): ")

        if choice == "1":
            # Пользователь вводит описание и срок выполнения новой задачи
            description = input("Введите описание задачи: ")
            deadline = input("Введите срок выполнения задачи (например, 2024-09-25): ")
            task = Task(description, deadline)  # Создаем объект класса Task
            task_manager.add_task(task)  # Добавляем задачу через менеджер
            print("Задача добавлена!")

        elif choice == "2":
            # Пользователь вводит описание задачи, чтобы отметить её выполненной
            task_description = input("Введите описание задачи, которую хотите отметить как выполненную: ")
            task_manager.mark_task_completed(task_description)
            print("Задача отмечена как выполненная!")

        elif choice == "3":
            # Показываем список невыполненных задач
            print("\nНевыполненные задачи:")
            task_manager.show_incomplete_tasks()

        elif choice == "4":
            # Показываем список выполненных задач
            print("\nВыполненные задачи:")
            task_manager.show_completed_tasks()

        elif choice == "5":
            # Выход из программы
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")

# Запуск основной программы
if __name__ == "__main__":
    main()
