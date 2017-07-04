####################################################
# Spell Checker
####################################################
story_stringinit = open("practice/story.txt", "r")
story_string = story_stringinit.read()

vocabulary = 'a about after almost along alternating an and anguish around at back ball became best but buy came cold come crop crazy curled day days decided decided eat even ever everyone farmer farmer find finest for found freezing farmer gave go going great grow growing guidance had hard he heat him his if immediately in into it journey julius juliuss keep knew last long magic managed many much months named never night noble noon of on once one out people persevered potatoes probably praises raining reggie roadside sang searing secret seek seen set shouldnt sign sky sleep so soaked started stopped store storekeeper that the there this to told travelled trees tried try umbrella underneath undeterred village was were who whole wondered world'
clean_chars = [",", ".", "'", ";", "\n"]


# Clean text by removing clean_chars from it
def clean_text(text_string, special_characters):  # special_characters must be a list of strings

    cleaned_string = text_string
    for i in special_characters:
        cleaned_string = cleaned_string.replace(i, "")

    cleaned_string = cleaned_string.lower()
    return cleaned_string


def tokenize(text_string, special_characters, clean=False):
    cleaned_story = clean_text(text_string, special_characters)
    story_tokens = cleaned_story.split(" ")
    return (story_tokens)


# Tokenize by splitting text into multiple strings by using 'split' command
def tokenize(text_string, special_characters, clean=False):
    if clean == True:
        cleaned_story = clean_text(text_string, special_characters)
        story_tokens = cleaned_story.split(" ")
        return (story_tokens)
    if clean == False:
        cleaned_story = text_string.split(" ")
        return (cleaned_story)


# Initiate variables
tokenized_story = []
tokenized_vocabulary = []
misspelled_words = []

tokenized_story = tokenize(story_string, clean_chars, clean=True)
print(tokenized_story)

tokenized_vocabulary = tokenize(vocabulary, clean_chars)
print(tokenized_vocabulary)

for i in tokenized_story:
    if i not in tokenized_vocabulary:
        misspelled_words.append(i)

print(misspelled_words)

#####################################
# Compact Spell Checker
#####################################

final_misspelled_words = []

def spell_check(vocabulary_file, text_file, special_characters = [",",".","'",";","\n"]):
    misspelled_words = []
    vocabulary = open(vocabulary_file, "r").read()
    text = open(text_file, "r").read()
    tokenized_vocabulary = tokenize(vocabulary, special_characters=clean_chars, clean=False)
    tokenized_text = tokenize(text, special_characters=clean_chars, clean=True)
    for i in tokenized_text:
        if (i not in tokenized_vocabulary) & (i != ''):
            misspelled_words.append(i)
    return misspelled_words

final_misspelled_words = spell_check("practice/dictionary.txt", "practice/story.txt")
print(final_misspelled_words)



print(open("practice/dictionary.txt", "r").read())
print(open("practice/story.txt", "r").read())
print(spell_check("practice/dictionary.txt", "practice/story.txt"))


#####################################
# Debugging
#####################################
def spell_check(vocabulary_file, text_file, special_characters=[",", ".", "'", ";", "\n"):
    misspelled_words = []

    vocabulary = open(vocabulary_file).read()
    text = open(text_file).read()

    tokenized_vocabulary = tokenize(vocabulary, special_characters)
    tokenized_text = tokenize(text, special_characters, True)

    for ts in tokenized_text:
        if ts not in tokenized_vocabulary and ts != '':
            misspelled_words.append(ts)
    return (misspelled_words)

final_misspelled_words = spell_check(vocabulary_file="dictionary.txt", text_file="story.txt")
print(final_misspelled_words)

print final_misspelled_words
