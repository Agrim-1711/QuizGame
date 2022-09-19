class Question: 

  def __init__(self, q_text, q_answer):
    self.q_text = q_text
    self.q_answer = q_answer

  def get_question(self):
    return self.q_text

  def get_answer(self):
    return self.q_answer