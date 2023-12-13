
import random

def load_questions(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    questions = [line.strip() for line in lines if line.strip()]
    return [questions[i:i + 6] for i in range(0, len(questions), 6)]

def ask_question(question_set):
    question, *options, correct_answer = question_set
    print(question)
    for option in options:
        print(option)
    user_answer = input("Tvoje odpověd: ").strip().upper()
    return user_answer == correct_answer

def ask_name():
    return input("Zadej tvoje jméno: ").strip()

def millionaire_game(file_path):
    name = ask_name()
    money = 0
    questions = load_questions(file_path)
    print(f"Vítej, {name}!")
    print()

    for question_set in questions:
        if ask_question(question_set):
            print()
            print("Správně! Získal $1,000.")
            money += 1000
            print(f"Celkem máš peněz: ${money}")
            print()
        else:
            print()
            print("Špatně! Prohrál jsi.")
            print(f"Celkem máš peněz: ${money}")
            print()
            break
    

if __name__ == "__main__":
    file_path = "questions_cs.txt"  
    millionaire_game(file_path)
