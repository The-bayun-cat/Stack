class Stack:
    def __init__(self):
        """Инициализация пустого стека"""
        self.items = []

    def is_empty(self):
        """Проверка стека на пустоту"""
        return len(self.items) == 0

    def push(self, item):
        """Добавление нового элемента на вершину стека"""
        self.items.append(item)

    def pop(self):
        """Удаление и возврат верхнего элемента стека"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Возврат верхнего элемента стека без удаления"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

    def size(self):
        """Возврат количества элементов в стеке"""
        return len(self.items)


def is_balanced(brackets_string):

    stack = Stack()

    # Словарь соответствия открывающих и закрывающих скобок
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # Множество открывающих скобок
    opening_brackets = set(bracket_pairs.values())

    # Проходим по каждому символу в строке
    for char in brackets_string:
        if char in opening_brackets:
            # Если символ - открывающая скобка, помещаем ее в стек
            stack.push(char)
        elif char in bracket_pairs:
            # Если символ - закрывающая скобка
            if stack.is_empty():
                # Если стек пуст, а у нас закрывающая скобка - несбалансировано
                return False

            # Извлекаем последнюю открывающую скобку из стека
            last_opening = stack.pop()

            # Проверяем, соответствует ли она текущей закрывающей
            if bracket_pairs[char] != last_opening:
                return False

    # Если после обработки всех символов стек пуст - последовательность сбалансирована
    return stack.is_empty()


def check_brackets_sequence():
    """
    Основная функция для проверки последовательности скобок
    """
    # Ввод строки со скобками
    input_string = input("Введите строку со скобками: ")

    # Проверяем сбалансированность
    if is_balanced(input_string):
        print("Сбалансированно")
    else:
        print("Несбалансированно")


# Тестирование функции
if __name__ == "__main__":
    # Примеры из задания
    test_cases = [
        "(((([{}]))))",  # Сбалансированно
        "[([])((([[[]]])))]{()}",  # Сбалансированно
        "{{[()]}}",  # Сбалансированно
        "}{}",  # Несбалансированно
        "{{[(])]}}",  # Несбалансированно
        "[[{())}]",  # Несбалансированно
        "",  # Пустая строка - сбалансированно
        "(){}[]",  # Сбалансированно
        "({[]})",  # Сбалансированно
        "([)]",  # Несбалансированно
    ]

    print("Тестирование примеров из задания:")
    print("-" * 50)

    for test in test_cases:
        result = "Сбалансированно" if is_balanced(test) else "Несбалансированно"
        print(f'{test:<30} -> {result}')

    print("\n" + "=" * 50)
    print("Проверка произвольной последовательности:")

    # Запуск интерактивной проверки
    while True:
        try:
            check_brackets_sequence()

            # Спросим, хочет ли пользователь продолжить
            continue_check = input("\nПроверить еще одну строку? (да/нет): ").lower()
            if continue_check not in ['да', 'д', 'yes', 'y']:
                print("Программа завершена.")
                break
            print()
        except KeyboardInterrupt:
            print("\n\nПрограмма завершена пользователем.")
            break
        except Exception as e:
            print(f"Произошла ошибка: {e}")