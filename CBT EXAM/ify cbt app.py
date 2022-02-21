username= input("please enter name: ")
print(username,", you are welcome\n")

from Ajuju import Question

questions_prompts = [
    "what is the colour of the sky?\n(a) Blue\n(b) Purple\n(c) Orange\n\n",
    "what is the colour of the pawpaw?\n(a) Blue\n(b) Purple\n(c) Yellow\n\n",
    "what is the colour of the strawberries?\n(a) Red\n(b) Purple\n(c) Orange\n\n",
    "what is the colour of the onion?\n(a) Blue\n(b) White\n(c) Orange\n\n",
    "what is the colour of the banana?\n(a) green\n(b) Purple\n(c) Orange\n\n",
    "what is the colour of the orange?\n(a) Blue\n(b) Purple\n(c) Yellow\n\n",
    "what is the colour of the apples?\n(a) Blue\n(b) Green\n(c) Orange\n\n",
    "what is the colour of the watermelon?\n(a) Blue\n(b) Red\n(c) Orange\n\n",
    "what is the colour of the mango?\n(a) Green\n(b) Purple\n(c) Orange\n\n",
    "what is the colour of the carrot?\n(a) Blue\n(b) Yellow\n(c) Orange\n\n"
    ]
    

questions = [
    Question(questions_prompts[0], "a"),
    Question(questions_prompts[1], "c"),
    Question(questions_prompts[2], "a"),
    Question(questions_prompts[3], "b"),
    Question(questions_prompts[4], "a"),
    Question(questions_prompts[5], "c"),
    Question(questions_prompts[6], "b"),
    Question(questions_prompts[7], "b"),
    Question(questions_prompts[8], "a"),
    Question(questions_prompts[9], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            
    print(username,"," " you have got " + str(score) + "/" + str(len(questions)) + " correct")
    
run_test(questions)


