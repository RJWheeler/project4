import random

MIN_NUM = 1
MAX_NUM = 10
NUM_QUEST = 4

def ask_question():
    a = random.randint(MIN_NUM, MAX_NUM)
    b = random.randint(MIN_NUM, MAX_NUM)
    o = random.randint(0, 1)
    operator_str = "+"
    if o == 1:
        operator_str = "*"
    user_answer = input(f"What is {a} {operator_str} {b} = ")
    answer = a + b
    if o == 1:
        answer = a * b
    answer_int = int(user_answer)
    if answer == answer_int:
        return True

    return False


points = 0
for i in range(0,NUM_QUEST):
    print(f"Question #{i+1} of {NUM_QUEST}")
    if ask_question():
        print("That is Correct!!!")
        points += 1
    else:
        print("That is not correct")
    print(f"You score is {points} of {NUM_QUEST}")
    print()
if points == NUM_QUEST:
    print("Excellent")
elif points == 0:
    print("Work on your math skills.")
elif points > int(NUM_QUEST/2):
    print("Good job")
else:
    print("You can do better.")