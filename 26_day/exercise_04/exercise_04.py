def my_words(sentence):
    return (sentence[0].split())

sentence = ["What is the Airspeed Velocity of an Unladen Swallow?"]

#print(my_words(sentence))

words = []

for x in my_words(sentence):
    words.append(x)

print(words)

dict_list = {word:len(word) for word in words}

print(dict_list)
