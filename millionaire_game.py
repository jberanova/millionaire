"""
jklhkjh
"""
import language_module

language = "čeština"


 ## pytest
 ## py.exe -m pytest
 ## py.exe -m pip install pytest
def load_questions(file_path):
    """
    asdf
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    questions = [line.strip() for line in lines if line.strip()]
    return [questions[i:i + 6] for i in range(0, len(questions), 6)]

def question(question_set):
    global language
    question, *options, correct_answer = question_set
    print(question)
    for option in options:
        print(option)
        if language == 'čeština':
            user_answer = input("Tvoje odpověd: ").strip().upper()
        else:
           user_answer = input("Your answer: ").strip().upper()
    return user_answer == correct_answer

def ask_name():
    global language
    if language == 'čeština':
        return input("Zadej voje jméno: ").strip()
    else:
        return input("Enter your name: ").strip()

def millionaire(file_path):
    global language
    name = ask_name()
    money = 0
    questions = load_questions(file_path)
    if language == 'čeština':
        print(f"Vítej, {name}!")
    else:
        print(f"Welcome, {name}!")
    print()

    for question_set in questions:
        if question(question_set):
            print()
            if language == 'čeština':
                print("Šprávně! Získal jsi $1000.")
            else:
                print("Correct! You've earned $1000.")
            money += 1000
            if language == 'čeština':
                print(f"Celkem máš peněz: ${money}")
            else:
                print(f"Total money earned: ${money}")
            print()
        else:
            print()
            if language == 'čeština':
                print("Špatně! Prohrál jsi.")
                print(f"Celkem máš peněz: ${money}")
            else:
                print("Incorrect! Game over.")
                print(f"Total money earned: ${money}")


if __name__ == "__main__":
    language = language_module.choose_language()
    if language == 'čeština':
        print(f"Pojď hrát milionáře v čestině.")
        millionaire("questions_cs.txt")
    else:
        print(f"Let's play Millionaire in {language}.")
        millionaire("questions_en.txt")
