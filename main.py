# ----------------------------------------------------------------
questions = {
    "1. What is the most popular programming language in a world?" : "A",
    "2. Which country has the largest amount of developers?": "B",
    "3. Which programming languages are considered the most challenging to learn?" : "A",
    "4. What are the key skills and qualities employers seek in software developers?": "C",
    "5. What year was Python created?": "D",
}

answers = [
    ["A. Python", "B. C", "C. Java", "D. PHP"],
    ["A. India", "B. China", "C. Vietnam", "D. US"],
    ["A. C++", "B. JavaScript", "C. Python", "D. Java"],
    ["A. Programming Language", "B. Database", "C. Data Struture and Algorithm", "D. OOP"],
    ["A. 1975", "B. 1980", "C. 2000", "D. 1991"],
]
# ----------------------------------------------------------------

def new_game():
    users = []
    num_questions = 1
    user_correct = 0
    for key in questions:
        print("--------------------------------")
        print(key)
        for i in answers[num_questions - 1]:
            print(i)
        user = input("Enter your answer: (A, B, C or D)?").upper()
        users.append(user)
        user_correct += check_user(user, questions[key])
        num_questions += 1
    display_result(user_correct, users)
            
def check_user(user, answer):
    if user == answer:
        return 1
    return 0
    
def display_result(user_correct, user_whole):
    print("--------------------------------")    
    print("------------RESULT--------------")
    
    print("Correct answer are: ", end=" ")
    for i in questions:
        print(questions[i],end=" ")
    print()
        
    print("Your answer are   : ", end=" ")
    for i in user_whole:
        print(i,end=" ")
    print()
    
    point = int((user_correct / len(questions) * 100))
    if point == 100:
        print("Congratulations! You are absolutely amazing!")
        print(f"Your point is {point}%")
    else:
        print(f"Your point is {point}%")

def play_again():
    choice = input("Would you like to play again?(Yes/no)?").upper()
    if choice == "YES":
        return 1
    else:
        return 0
def main():
    new_game()
    while play_again():
        new_game()
    print("Goodbye ~~~")    
        
if __name__ == "__main__":
    main()