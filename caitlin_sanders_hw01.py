# Caitlin Sanders
# CIS 400: Assignment 1
# Due February 8, 2019

# Directions:

# Create a Python module with a __main__  (in other words, create a runnable Python script), and at least 60 lines of code.
# Define at least 1 class, and at least 1 function for each class you have defined.
# Your __main__ should instantiate objects of the classes you have designed, and use them to invoke the methods defined in those classes.
# Use list comprehensions to create lists
# Use dictionary comprehensions to create dictionaries
# Use at least 1 decision-making statement (if-elif)
# Use at least 1 looping statement (for or while)
# Use at least 1 try-except to catch some exceptions
# Use the input() function, or command-line arguments, to get some user input
# Produce some interesting output
# Add comments to make your script easy to understand
# Be creative and make sure it runs.

class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

prompts = ["Easy ","Easy ","Easy ","Easy ","Easy ","Easy ","Easy ","Easy ","Easy ","Easy "]
prompts_dict = {n: prompts[n] for n in range(len(prompts))}

questions = [
     Question(prompts_dict.get(1), "a"),
     Question(prompts_dict.get(2), "b"),
     Question(prompts_dict.get(3), "a"),
     Question(prompts_dict.get(4), "a"),
     Question(prompts_dict.get(5), "b"),
     Question(prompts_dict.get(6), "a"),
     Question(prompts_dict.get(7), "a"),
     Question(prompts_dict.get(8), "b"),
     Question(prompts_dict.get(9), "a"),
     Question(prompts_dict.get(10), "a"),
     Question(prompts_dict.get(11), "a"),
     Question(prompts_dict.get(12), "b"),
     Question(prompts_dict.get(13), "a"),
     Question(prompts_dict.get(14), "a"),
     Question(prompts_dict.get(15), "b"),
     Question(prompts_dict.get(16), "a"),
     Question(prompts_dict.get(17), "a"),
     Question(prompts_dict.get(18), "b"),
     Question(prompts_dict.get(19), "a"),
     Question(prompts_dict.get(20), "a"),
]

game_length = {
'short': [questions[i] for i in range(0, 5)], # [1,2,3,4,5]
'medium': [questions[i] for i in range(0, 10)],
'long': [questions[i] for i in range(0, 20)],
}

def final_score(score, length):
    if (score / length) >= 0.75:
        return "You are a lobster god!"
    elif (score / length) >= 0.5:
        return "Nice job!"
    else:
        return "Keep studying your lobster facts..."

def run_quiz(questions):
     score = 0
     print("Welcome to Lobster Quiz! Let's see how well you know the best animal in the sea!")
     while True:
        length = input("What length would you like the quiz to be? (Short/Medium/Long): ")
        if (length.lower()).strip() in ["short", "medium", "long"] :
           break
        else:
           print('Please choose between "Short", "Medium", or "Long". ')
     for counter, question in enumerate(game_length.get(length),1):
         answer = input("Question #" + str(counter) + ". " + question.prompt)
         if (answer.lower()).strip() == question.answer:
             print('Correct!')
             score+=1
         else:
             print('Wrong! The correct answer was: ' + question.answer)
     print("Thank you for playing! You got " + str(score)+ " out of " + str(len(game_length.get(length))) +". " + final_score(score, len(game_length.get(length))))

if __name__== "__main__":
    run_quiz(questions)
