import json
import random
from datetime import datetime

# ---------- LOAD QUESTIONS ----------
with open("questions.json", "r", encoding="utf-8") as file:
    questions = json.load(file)

random.shuffle(questions)

# ---------- PLAYER INFO ----------
name = input("Enter your name: ").strip()
print(f"\nWelcome {name}! Let's play Who Wants to Be a Millionaire\n")

# ---------- GAME SETTINGS ----------
questions = questions[:10]
prizes = [1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000]

lifeline_5050_used = False
money_won = 0

# ---------- GAME LOOP ----------
for i, q in enumerate(questions):
    print(f"\nQuestion {i+1}: {q['question']}")

    for idx, option in enumerate(q["options"], start=1):
        print(f"{idx}. {option}")

    if not lifeline_5050_used:
        print("0. Use 50-50 Lifeline")

    try:
        choice = int(input("Your answer (1-4 or 0): "))
    except ValueError:
        print("Invalid input. Game Over!")
        break

    # ---------- 50-50 LIFELINE ----------
    if choice == 0 and not lifeline_5050_used:
        lifeline_5050_used = True
        correct_index = q["answer"] - 1
        wrong_indexes = [i for i in range(4) if i != correct_index]
        removed = random.sample(wrong_indexes, 2)

        print("\n50-50 Lifeline Activated ")
        for i in range(4):
            if i not in removed:
                print(f"{i+1}. {q['options'][i]}")

        choice = int(input("Your answer (1-4): "))

    # ---------- CHECK ANSWER ----------
    if choice == q["answer"]:
        money_won = prizes[i]
        print(f"✅ Correct! You won Rs. {money_won}")
    else:
        print(f"❌ Wrong! Correct answer was option {q['answer']}")
        break

    # ---------- QUIT OPTION ----------
    quit_choice = input("Do you want to continue? (yes/no): ").lower()
    if quit_choice == "no":
        print(f"\nYou quit the game. You take home Rs. {money_won}")
        break

# ---------- SAVE SCORE ----------
with open("scores.txt", "a") as file:
    file.write(f"{name} | Rs.{money_won} | {datetime.now()}\n")

print("\n Game Over!")
print(f"Final Amount Won: Rs. {money_won}")
print("Thanks for playing ")
