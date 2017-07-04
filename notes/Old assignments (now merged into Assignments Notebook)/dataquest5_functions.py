# Open and read vocabulary to file
vocabularyinit = open("practice\dictionary.txt", "r")
vocabulary = vocabularyinit.read()

print(vocabulary)

# Tokenize vocabulary
tokenized_vocabulary = vocabulary.split(" ")
print(tokenized_vocabulary[:5])

# Replace substring
story_stringinit = open("practice/story.txt", "r")
story_string = story_stringinit.read()
print(story_string)

story_string = story_string.replace(",", "")
story_string = story_string.replace(".", "")
story_string = story_string.replace(";", "")
story_string = story_string.replace("'", "")
story_string = story_string.replace("\n", "")

print(story_string)

# Create function: Basic text cleaning
story_stringinit = open("practice/story.txt", "r")
story_string = story_stringinit.read()
print(story_string)


def clean_text(text_string):
    cleaned_string = text_string.replace(".", "")
    cleaned_string = cleaned_string.replace(",", "")
    cleaned_string = cleaned_string.replace(";", "")
    cleaned_string = cleaned_string.replace("\n", "")
    cleaned_string = cleaned_string.replace("'", "")
    cleaned_string = cleaned_string.lower()
    return cleaned_string

cleaned_story = clean_text(story_string)
print(cleaned_story)

############################################

# Advanced version of text cleaning function
story_stringinit = open("practice/story.txt", "r")
story_string = story_stringinit.read()

clean_chars = [",", ".", "'", ";", "\n"]

def clean_text(text_string, special_characters): # special_characters must be a list of strings

    cleaned_string = text_string
    for i in special_characters:
        cleaned_string = cleaned_string.replace(i, "")

    cleaned_string = cleaned_string.lower()
    return cleaned_string

cleaned_story = clean_text(story_string,clean_chars)
print(cleaned_story)

####################################################
# Tokenizer function
####################################################

story_stringinit = open("practice/story.txt", "r")
story_string = story_stringinit.read()

clean_chars = [",", ".", "'", ";", "\n"]

def tokenize(text_string, special_characters):
    cleaned_story =  clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return story_tokens

tokenized_story = tokenize(story_string, clean_chars)
print(tokenized_story[:10])

####################################################
# Spell Checker
####################################################
vocabulary = 'a about after almost along alternating an and anguish around at back ball became best but buy came cold come crop crazy curled day days decided decided eat even ever everyone farmer farmer find finest for found freezing farmer gave go going great grow growing guidance had hard he heat him his if immediately in into it journey julius juliuss keep knew last long magic managed many much months named never night noble noon of on once one out people persevered potatoes probably praises raining reggie roadside sang searing secret seek seen set shouldnt sign sky sleep so soaked started stopped store storekeeper that the there this to told travelled trees tried try umbrella underneath undeterred village was were who whole wondered world'
clean_chars = [",", ".", "'", ";", "\n"]

tokenized_vocabulary = tokenize(vocabulary, clean_chars)
print(tokenized_vocabulary)

misspelled_words = []

for i in tokenized_story:
    if i not in tokenized_vocabulary:
        misspelled_words.append(i)

print(misspelled_words)


####################################################
# ...
####################################################