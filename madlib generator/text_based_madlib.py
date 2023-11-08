# Step 1: get data from file
with open('Python-projects\\madlib generator\\madlib_templates.txt') as f:
    stories = f.read()
    # print(stories)

# Step 2: separate stories
list_stories = stories.split('\n')[1::3]
# print(len(list_stories))
# print(list_stories)

# Step 3: select a random story and identify key words and ask for another word inplace of them. Join the story and showcase it.
'''
import random
possible_blanks = ['<adjective>', '<noun>', '<verb>', '<emotion>', '<place>']
selected_story = random.choice(list_stories).split(' ')
# print(selected_story)
for word in selected_story:
    if word in possible_blanks:
        get_word = input(f"Enter a {word}: ")
        # print(get_word)
        selected_story[selected_story.index(word)] = get_word
print(' '.join(selected_story))
'''

# Step 4: Let's create a feature for people with poor vocabulary like myself
# 1. Create a different lists for such words.
nouns =  ['cat', 'mountain', 'bicycle', 'library', 'ocean', 'pizza']
adjectives =  ['Sparkling', 'Mysterious', 'Playful', 'Enchanting', 'Courageous', 'Lively']
verbs = ['jump', 'laugh', 'run', 'dance', 'explore', 'cook']
emotions = ['joyful', 'melancholic', 'excited', 'content', 'anxious', 'grateful']
places = ['paris', 'tokyo', 'sydney', 'venice', 'brazil', 'park']
# 2. create a dictionary to map them.
random_words = {
    '<noun>':nouns,
    '<adjective>':adjectives,
    '<verb>': verbs,
    '<emotion>':emotions,
    '<place>':places
    }
# 3. now provide an option to choose a random word.
import random
possible_blanks = ['<adjective>', '<noun>', '<verb>', '<emotion>', '<place>']
selected_story = random.choice(list_stories).split(' ')

for word in selected_story:
    if word in possible_blanks:
        get_word = input(f"Enter a {word} (or type random for random word): ").lower()

        if get_word == 'random':
            get_word = random.choice(random_words[word])

        selected_story[selected_story.index(word)] = get_word
print(' '.join(selected_story))
