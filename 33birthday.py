
import sys
import random

def has_duplicate_birthdays(people, days):
    birthdays = []
    for _ in range(people):
        birthday = random.randint(0, days - 1)
        if birthday in birthdays:
            return True
        birthdays.add(birthday)
    return False

def simulate_birthday_problem(trials, days, people):
    duplicate_count = sum(has_duplicate_birthdays(people, days) for _ in range(trials))
    return duplicate_count / trials * 100

def is_integer(value):
    return value.isdigit() or (value.startswith('-') and value[1:].isdigit())

def main():
    if len(sys.argv) != 4:
        print('Usage: python3 birthday.py <trials> <days> <people>')
        return

    if not all(is_integer(arg) for arg in sys.argv[1:]):
        print('Provide three integer values for trials, days, and people.')
        return

    trials = int(sys.argv[1])
    days = int(sys.argv[2])
    people = int(sys.argv[3])
    probability = simulate_birthday_problem(trials, days, people)
    print(f"Estimated probability: {probability:.2f}%")


main()


