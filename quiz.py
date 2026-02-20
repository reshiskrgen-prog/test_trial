
questions = ( 
    ("What is 1 + 1?", "2"), 
    ("What is 2 + 2?", "4") 
)

def start():
    score = 0
    for question_text, correct_answer in questions:
       
        print(f"Question: {question_text}") 
        
        useranswer = input("Your answer: ").strip().lower()
        
        if useranswer == str(correct_answer).lower():
            print("Good job! That's correct!")
            score += 1
        else:
          
            print(f"WRONG LOSER!! THE ANSWER WAS {correct_answer}!")
            
        print() 

    print(f"You finished! Your score was {score}")

start()
