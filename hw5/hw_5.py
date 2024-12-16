from decouple import Config, Csv
from logic import start_game

def load_config():
    config = Config(".env")
    min_number = config.get("MIN_NUMBER", cast=int)
    max_number = config.get("MAX_NUMBER", cast=int)
    attempts = config.get("ATTEMPTS", cast=int)
    initial_capital = config.get("INITIAL_CAPITAL", cast=int)
    return min_number, max_number, attempts, initial_capital

def main():
    min_number, max_number, attempts, initial_capital = load_config()

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Диапазон чисел: от {min_number} до {max_number}")
    print(f"Попытки: {attempts}")
    print(f"Начальный капитал: {initial_capital} рублей")

    start_game(min_number, max_number, attempts, initial_capital)

if __name__ == "__main__":
    main()
