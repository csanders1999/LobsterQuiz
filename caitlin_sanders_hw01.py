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

# Question class with prompt and answer
class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

# List of question prompts
prompts = ["What color is lobster's blood? ","Where are lobster's teeth located? ","What do lobster's taste with? ","What state's university has a lobster institute?  ","What year did the beach-party anthem 'Rock Lobster' come out?  ","In what show did one of the main characters reasure their friend by saying, 'but she’s your lobster.'? ","Lobsters mate for life. True or False? ","Where is a lobster's brain located? ","Lobsters scream when you boil them. True or False? ","In what show is the show 'Bring in the dancing lobsters' from? ", "When it comes to mating, do males (M) or females (F) make the first move? ", "What are the red things in cooked lobster? ", "What ball were their shells once used to make? ", "They were once prison food. True or False?", "Lobsters are cannibals. True or False?", "How many grams of protein (per cup) is lobster meat? ", "Where do lobsters pee out of? ", "What are lobster's eggs called? ", "What is the maximum number of lobsters you can hunt at night? ", "What is the name of the lifeguard on SpongeBob SquarePants? "]

# Prompts in dictionary form with number:question key:value pairs
prompts_dict = {n: prompts[n] for n in range(len(prompts))}

# Dictionary with Question objects (prompts and possible correct answers)
questions = [
     Question(prompts_dict.get(0), ["clear", "colorless"]),
     Question(prompts_dict.get(1), ["stomach", "their stomach"]),
     Question(prompts_dict.get(2), ["legs", "their legs", "leg", "their legs"]),
     Question(prompts_dict.get(3), ["Maine", "maine"]),
     Question(prompts_dict.get(4), ["1979"]),
     Question(prompts_dict.get(5), ["Friends", "friends", "Friend's", "friend's"]),
     Question(prompts_dict.get(6), ["False. A male lobster actually mated with an entire harem of female lobsters one at a time in flings that last about two weeks each.", "false"]),
     Question(prompts_dict.get(7), ["Throat", "their throat", "throat"]),
     Question(prompts_dict.get(8), ["False. Lobsters have no vocal cords. The sound one may hear is actually steam escaping from the shell as the lobster cooks.", "false"]),
     Question(prompts_dict.get(9), ["The Amanda Show", "amanda show", "the amanda show" ]),
     Question(prompts_dict.get(10), ["Females", "f","females", "girls"]),
     Question(prompts_dict.get(11), ["eggs", "their eggs"]),
     Question(prompts_dict.get(12), ["golf balls", "golf"]),
     Question(prompts_dict.get(13), ["True", "true", "t"]),
     Question(prompts_dict.get(14), ["True", "true", "t"]),
     Question(prompts_dict.get(15), ["28", "twenty eight", "twenty-eight"]),
     Question(prompts_dict.get(16), ["their face", "face"]),
     Question(prompts_dict.get(17), ["roe"]),
     Question(prompts_dict.get(18), ["7", "seven"]),
     Question(prompts_dict.get(19), ["Larry the Lobster", "larry", "larry lobster", "larry the lobster"]),
]

# Length of game dictionary with length:[question objects depending on length]
game_length = {
'short': [questions[i] for i in range(0, 5)],
'medium': [questions[i] for i in range(0, 10)],
'long': [questions[i] for i in range(0, 20)],
}

# Function to calculate what to say to person based on score
def final_score(score, length):
    if (score / length) >= 0.75:
        return "You are a lobster god!"
    elif (score / length) >= 0.5:
        return "Nice job! But the lobsters believe you could do better..."
    else:
        return "Keep studying your lobster facts..."

# Function that runs quiz
def run_quiz(questions):
     score = 0
     print("Welcome to Lobster Quiz! Let's see how well you know the best animal in the sea!")
     while True: # Checking length input is Short, Medium, or Long
        try:
            length = input("What length would you like the quiz to be? (Short/Medium/Long): ")
        except EOFError:
            print ('Please choose between "Short", "Medium", or "Long". ')
            continue
        if (length.lower()).strip() in ["short", "medium", "long"] :
           break
        else:
           print('Please choose between "Short", "Medium", or "Long". ')
     for counter, question in enumerate(game_length.get(length),1): # enumerated for loop to go through all questions
         answer = input("Question #" + str(counter) + ". " + question.prompt) # Asking question
         if (answer.lower()).strip() in question.answer: # Seeing if correct
             print('Correct!')
             score+=1
         else:
             print('Wrong! The correct answer was: ' + question.answer[0])
     print("Thank you for playing! You got " + str(score)+ " out of " + str(len(game_length.get(length))) +". " + final_score(score, len(game_length.get(length))))

if __name__== "__main__":
    run_quiz(questions)
