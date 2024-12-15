questions_continents = [
    "Which continent is the largest by land area?",
    "Which continent has the most countries?",
    "Which continent is known as the birthplace of civilization?",
    "Which continent has the Sahara Desert?",
    "Which continent is home to the Amazon Rainforest?"
]

choices_continents = [
    ["a. Asia", "b. Africa", "c. Europe", "d. Antarctica"],
    ["a. Europe", "b. Asia", "c. Africa", "d. South America"],
    ["a. Europe", "b. Africa", "c. Asia", "d. North America"],
    ["a. North America", "b. Africa", "c. Europe", "d. Asia"],
    ["a. Africa", "b. Asia", "c. South America", "d. Europe"]
]

answers_continents = ["a", "c", "c", "b", "c"]

questions_general = [
    "What is the capital of Japan?",
    "Who painted the Mona Lisa?",
    "What is the smallest prime number?",
    "What is the boiling point of water in Celsius?",
    "Which planet is closest to the Sun?"
]

choices_general = [
    ["a. Tokyo", "b. Seoul", "c. Beijing", "d. Bangkok"],
    ["a. Van Gogh", "b. Picasso", "c. Da Vinci", "d. Monet"],
    ["a. 0", "b. 1", "c. 2", "d. 3"],
    ["a. 90°C", "b. 80°C", "c. 100°C", "d. 120°C"],
    ["a. Venus", "b. Mars", "c. Mercury", "d. Earth"]
]

answers_general = ["a", "c", "c", "c", "c"]

questions_animals = [
    "What is the largest land animal?",
    "Which bird is known for its colorful feathers and ability to mimic sounds?",
    "What do pandas primarily eat?",
    "Which sea creature has eight legs?",
    "What is the fastest land animal?"
]

choices_animals = [
    ["a. Elephant", "b. Giraffe", "c. Rhinoceros", "d. Hippopotamus"],
    ["a. Crow", "b. Parrot", "c. Peacock", "d. Sparrow"],
    ["a. Bamboo", "b. Grass", "c. Fruits", "d. Leaves"],
    ["a. Crab", "b. Octopus", "c. Starfish", "d. Lobster"],
    ["a. Cheetah", "b. Lion", "c. Tiger", "d. Leopard"]
]

answers_animals = ["a", "b", "a", "b", "a"]

themes = {
    "1": {"name": "Continents", "questions": questions_continents, "choices": choices_continents, "answers": answers_continents},
    "2": {"name": "General Knowledge", "questions": questions_general, "choices": choices_general, "answers": answers_general},
    "3": {"name": "Animals", "questions": questions_animals, "choices": choices_animals, "answers": answers_animals}
}

print("\n--- WELCOME TO THE QUIZ GAME! ---")

while True:
    print("Choose a theme:")
    for key, theme in themes.items():
        print(f"{key}. {theme['name']}")

    theme_choice = input("Enter the number corresponding to your chosen theme: ")
    if theme_choice in themes:
        theme = themes[theme_choice]
        print(f"\n--- THEME: {theme['name']} ---\n")
        questions, choices, answers = theme["questions"], theme["choices"], theme["answers"]

        score = 0

        for i, question in enumerate(questions):
            print(f"QUESTION {i + 1}: {question}")
            for choice in choices[i]:
                print(choice)

            while True:
                answer = input("Your answer (a/b/c/d): ").lower()
                if answer in {"a", "b", "c", "d"}:
                    break
                else:
                    print("Invalid input. Please enter 'a', 'b', 'c', or 'd' only!")

            if answer == answers[i]:
                print("Correct!\n")
                score += 1
            else:
                print(f"WRONG! The correct answer was {answers[i]}.\n")

        print("\n--- QUIZ RESULT ---")
        print(f"Your score: {score}/{len(questions)}")

        if score == len(questions):
            print("\nPerfect score! Well done!")
        else:
            print("\nBetter luck next time!")

        continue_choice = input("Do you want to try another theme? (yes/no): ").lower()
        if continue_choice != "yes":
            break
    else:
        print("Invalid choice. Please enter a valid number.")
