# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
  word_list = word.split(x)
  new_word = ''.join(word_list)
  first_result = len(word) - len(new_word)
  return int(first_result/len(x))
 
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1