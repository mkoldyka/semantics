import spacy

# Load english language model
nlp = spacy.load('en_core_web_sm')


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))



# Write a note about what you found interesting about the similarities between cat, monkey, and banana, and think of an example of your own.
# The similarity between cat and money is high as they are both animals.
# the similarity between cat and banana is low as they are not related.
# the similarity between monkey and banana is high as they are related as monakey eats bananas.
# the similarity between cat and apple is low as they are not related.
# the similarity between apple and banana is high as they are both fruits.


tokens = nlp('light night car boat')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# the similarity between light and night is high as they are both related to darkness.
# the similarity between light and car is low as they are not related.
# the similarity between light and boat is low as they are not related.
# the similarity between car and boat is high as they are both vehicles.


# sentence_to_compare = "Why is my cat on the car"
# sentences = ["where did my dog go", "Hello, there is my car", "I've lost my car in my car", "I'd like my boat back", "I will name my dog Diana"]
# model_sentence = nlp(sentence_to_compare)

# for sentence in sentences:
#     similarity = nlp(sentence).similarity(model_sentence)
#     print(sentence + " - ", similarity)



