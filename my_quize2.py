import pyttsx3
from termcolor import colored

questions = [
    {
        "question": "1. What is the correct file extension for Python files?",
        "options": ["A) .py", "B) .java", "C) .txt", "D) .p"],
        "answer": "A"
    },
    {
        "question": "2. Which function is used to display output in Python?",
        "options": ["A) print()", "B) echo()", "C) display()", "D) show()"],
        "answer": "A"
    },
     {
        "question": "3. Which of the following is a valid variable name in Python?",
        "options": ["A) 2var", "B) my-variable", "C) _myVar", "D) my var"],
        "answer": "C"
    },
    
     {
        "question": """4. What is the output of print(3 * "Hello")?""",
        "options": ["A) HelloHelloHello", "B)  Hello Hello Hello", "C)  Error", "D)  3Hello"],
        "answer": "A"
    },
    
     {
        "question": "5. Which keyword is used to define a function in Python?",
        "options": ["A) function", "B) def ", "C) define", "D) fun"],
        "answer": "B"
    },
    
     {
        "question": "6. What will type(10.5) return?",
        "options": ["A) int", "B) float", "C) double", "D) str"],
        "answer": "B"
    },
    
     {
        "question": "7. Which of the following is used for single-line comments in Python?",
        "options": ["A) //", "B) <!-- -->", "C) #", "D) /* */"],
        "answer": "C"
    },
    
     {
        "question": "8. What is the output of bool([])?",
        "options": ["A) True", "B) False", "C) Error", "D) None"],
        "answer": "B"
    },
    
     {
        "question": "9. Which of these data structures is immutable?",
        "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
        "answer": "C"
    },
    
     {
        "question": "10. What will range(5) generate?",
        "options": ["A) [0, 1, 2, 3, 4]", "B) [1, 2, 3, 4, 5]", "C) [0, 1, 2, 3, 4, 5]", "D) [1, 2, 3, 4]"],
        "answer": "A"
    }
]

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

while True:
    score = 0

    for i in questions:
        print("\n" + "-" * 50)
        print(colored(i["question"], "blue"))
        for option in i["options"]:
            print(colored(option, "light_yellow"))
        speak(i["question"])
        
        user_answer = input("\nEnter your answer (A, B, C or D) or 'Q' to quite:  ").upper().strip()
        if user_answer == i["answer"]:
            print(colored("Correct! ✅", "green"))
            speak("Correct!")
            score += 1
        elif user_answer == "Q".upper().strip():
            break
        else:
            speak("Wrong!")
            print(colored(f"Wrong! ❌", "light_red") + f"The right answer is {i['answer']}")

    print("-" * 50)
    print(colored(f"Your final score is {score}/{len(questions)}. Thanks for playing!", "green"))
    speak(f"\nYour final score is {score}/{len(questions)}. Thanks for playing!")
    print("-" * 50)


    speak("Do you want to play again?")
    play_again = input(colored("Do you want to play again? (yes/no) ", "blue"))
    if play_again != "yes".lower().strip():
        break
    
