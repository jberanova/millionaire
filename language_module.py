def choose_language():
    while True:
        language = input("Choose your language(english/čeština): ").strip().lower()
        if language in ['english', 'čeština']:
            return language
        