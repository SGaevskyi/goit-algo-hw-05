import re
from typing import Callable


def generator_numbers(text: str):
    words = text.split()
    pattern = r'^\d+(\.\d+)?$'

    for word in words:
        if re.match(pattern, word):
            yield float(word)


def sum_profit(text: str, func: Callable):
    return sum(func(text))


def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == '__main__':
    main()
