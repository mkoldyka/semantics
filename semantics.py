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


# Run the example file with the simpler language model 'en_core_web_sm', and write a note on what you notice is different from the model 'en_core_web_md'.
# Looks like the sm model is less accurate than the md model.
# The sm model is less accurate as it is a smaller model and does not have as much data as the md model.
