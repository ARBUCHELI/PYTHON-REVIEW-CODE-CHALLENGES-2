# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
  first_index = word.find(start)
  #print(first_index)
  second_index = word.find(end)
  #print(second_index)
  if first_index == -1 or second_index == -1:
    return word
  else:
    return word[first_index+1:second_index]
# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"