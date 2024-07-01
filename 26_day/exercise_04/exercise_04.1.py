sentence = ["What is the Airspeed Velocity of an Unladen Swallow?"]

#print(my_words(sentence))

result = {word:len(word) for word in sentence[0].split()}

print(result)
