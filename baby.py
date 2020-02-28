from random import choice

questions = ["What is the sky blue? ", "Why are you old? ", "What time is it? ", "Where are dinosaurs from? ", "Why do you have a big nose? "]

question = choice(questions)
answer = input(question).strip().lower()


while answer != "just because":
    answer = input("but why?: ").strip().lower()

print("Oh, okay.")
