# How To Write Doctests in Python
# https://www.digitalocean.com/community/tutorials/how-to-write-doctests-in-python

def add(a, b):
   """
   Given two integers, return the sum.

   :param a: int
   :param b: int
   :return: int

   >>> add(2, 3)
   5
   """
   return a + b

def count_vowels(word):
  """
  Given a single word, return the total number of vowels in that single word.

  :param word:str
  :return int
  
  >>> count_vowels("Curso")
  2

  >> count_vowels("Manilia")
  3

  >> count_vowels("Istanbul")
  3
  """
  total_vowels = 0
  for letter in word.lower():
    if letter in 'aeiou':
      total_vowels +=1
  
  return total_vowels

if __name__ == "__main__":
  import doctest
  doctest.testmod()
