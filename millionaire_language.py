
def choose_language():
    while True:
        language = input("Choose your language/Vyber si svůj jazyk (English/Čestina): ").strip().lower()
        if language in ['english', 'čestina']:
            return language
def millionaire_game():
    language = choose_language()
    file_path = f"questions_{language}.txt"
    money = 0
    if language in ['čestina']:
         print(f"Pojď hrát milionáře v čestině.")
    else:
         print(f"Let's play Millionaire in {language}.")
if __name__ == "__main__":
    millionaire_game()




