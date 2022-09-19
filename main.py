from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

list_qs = [Question(question_data[n]['text'],question_data[n]['answer'].upper()) for n in range(0,len(question_data))]

qb = QuizBrain(list_qs)

while qb.still_has_questions():
  ques = qb.get_question()
  guess = qb.format_q(ques)
  ans = qb.is_correct(guess)
  print(qb.format_a(ans))

print(qb.end_of_quiz())