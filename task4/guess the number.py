import random

def get_valid_number(min_val, max_val):
    """Запрашивает у пользователя целое число в диапазоне [min_val, max_val].
    Повторяет запрос при неверном вводе. Возвращает корректное число."""
    while True:
        user_input = input(f"Введите целое число от {min_val} до {max_val}: ").strip()
        if not user_input:
            print("Ввод не может быть пустым. Попробуйте снова.")
            continue
        try:
            num = int(user_input)
            if min_val <= num <= max_val:
                return num
            else:
                print(f"Число должно быть в диапазоне от {min_val} до {max_val}. Попробуйте снова.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

def play_game(min_num=1, max_num=100, max_attempts=7):
    """Основная логика игры."""
    secret_number = random.randint(min_num, max_num)
    attempts_left = max_attempts
    
    print("\n--- Добро пожаловать в игру «Угадай число»! ---")
    print(f"Я загадал число от {min_num} до {max_num}.")
    print(f"У вас есть {max_attempts} попыток, чтобы угадать его.")
    print("После каждой попытки я скажу, больше или меньше ваше число загаданного.\n")

    while attempts_left > 0:
        guess = get_valid_number(min_num, max_num)
        
        if guess == secret_number:
            print(f"\n🎉 Поздравляем! Вы угадали число {secret_number}!")
            print(f"Вы справились за {max_attempts - attempts_left + 1} попытку(ок).")
            return True
        elif guess < secret_number:
            print("📉 Ваше число слишком маленькое.")
        else:
            print("📈 Ваше число слишком большое.")
        
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Осталось попыток: {attempts_left}\n")
        else:
            print(f"\n😞 К сожалению, попытки закончились. Загаданное число было: {secret_number}")
            return False

def main():
    """Точка входа: управление циклом игры и настройками."""
    while True:
        # Можно легко менять параметры здесь или вынести в конфиг/аргументы
        won = play_game(min_num=1, max_num=100, max_attempts=7)
        
        play_again = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower()
        if play_again not in ("да", "д", "yes", "y"):
            print("Спасибо за игру! До встречи!")
            break
        print()  # Пустая строка для читаемости

if __name__ == "__main__":
    main()
