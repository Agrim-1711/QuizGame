# random number generator
# quiz formatting
# score counter
# pick different questions each time
# check answer is correct
# display score after each question
# End game after 10 qs - display final score

import random

class QuizBrain:

  def __init__(self, q_list):
    self.score = 0
    self.q_num = 0
    self.q_num_used = []
    self.q_list = q_list

  def create_random_num(self):
    """Returns a random question number not used before"""
    r = random.randint(0,len(self.q_list)-1)
    if r not in self.q_num_used:
      self.q_num_used.append(r)
    else:
      self.create_random_num()
  
  def get_question(self):
    """Returns a new question"""
    self.create_random_num()
    return self.q_list[self.q_num_used[-1]].get_question()

  def still_has_questions(self):
    """Returns True if fewer than 10 questions already asked; otherwise False"""
    return len(self.q_num_used) < 10
  
  def is_correct(self, guess):
    """Returns True if guess correct; otherwise False"""
    if guess == self.q_list[self.q_num_used[-1]].get_answer():
      self.score += 1
      return True
    else:
      return False

  def format_q(self, question):
    """Formats question and asks user for a guess and then returns it"""
    print(f"Q{len(self.q_num_used)}: {question}")
    return input("T/F: ").upper()

  def format_a(self, answer):
    if answer:
      print("You got it right!")
    else:
      print("That was wrong...")
      if {self.q_list[self.q_num_used[-1]].get_answer()} == 'T':
        print("The correct answer was: True")
      else:
        print("The correct answer was: False")
    return f"Your current score is: {self.score}/{len(self.q_num_used)}\n"

  def end_of_quiz(self):
    print("End of Quiz")
    return f"Your final score was {self.score}/10!!!"