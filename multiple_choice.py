from question import Question

question_prompts = [
    "What color are apples?\n(a) Red\n(b) Yellow\n(c) Blue\n\n",
    "What color are bananas?\n(a) Brown\n(b) Blue\n(c) Yellow\n\n",
    "What color are mangos?\n(a)Black\n(b) Yellow\n(c) White\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input (question.prompt)
        if answer == question.answer:
            score += 1
    print ("You got "+str(score)+"/"+str(len(questions))+" correct!")


run_test(questions)
