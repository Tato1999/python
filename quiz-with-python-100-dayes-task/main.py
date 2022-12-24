
from data import question_data

from question_model import Question
from quiz_brain import QuizBrain
import random
question = question_data
quest_array = []
answer_array = []

for i in question:
        
        question_text = i['text']
        question_answer = i['answer']
        new_question_both = Question(question_answer, question_text)
        quest_array.append(new_question_both) 
        

quiz = QuizBrain(quest_array)



while quiz.still_has_question():
    quiz.next_question()

print(f"Yuor Score is {quiz.score}/{len(quiz.question_list)}")