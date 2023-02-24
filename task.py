# Eric Cuevas, Andrew Molina
# Assigned February 21, due February 23, 2023
# Task class


class Task:

  def __init__(self, description, date, time):
    self.description = description
    self.date = date
    self.time = time

  def get_description(self):
    return self.description

  def __str__(self):
    return f"{self.description} due on {self.date} at {self.time}"

  def __repr__(self):
    return f"{self.description},{self.date},{self.time}"

  def __lt__(self, other):
    if self.date < other.date:
      return True
    elif self.date > other.date:
      return False
    else:
      if self.time < other.time:
        return True
      elif self.time > other.time:
        return False
      else:
        return self.description < other.description
