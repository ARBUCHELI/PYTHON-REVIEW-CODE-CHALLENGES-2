# Write your max_key function here:
def max_key(my_dictionary):
  values = []
  for value in my_dictionary.values():
    values.append(value)
    maximum = values[0]
    for number in values:
      if number > maximum:
        maximum = number
  for key in my_dictionary.keys():
    if my_dictionary[key] == maximum:
      return key


# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"