# Write your x_length_words function here:
def x_length_words(sentence, x):
  list_of_words = sentence.split()
  count_of_trues = 0
  for word in list_of_words:
    if len(word) >= x:
      count_of_trues += 1
  if count_of_trues == len(list_of_words):
    return True
  else:
    return False
# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True