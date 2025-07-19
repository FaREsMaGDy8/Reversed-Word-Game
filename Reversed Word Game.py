# list of words
words = [
    'have', 'that', 'they', 'with', 'this', 'from', 'which', 'would', 'will',
    'there',
    'make', 'when', 'more', 'other', 'what', 'time', 'about', 'than', 'into',
    'could',
    'state', 'only', 'year', 'some', 'take', 'come', 'these', 'know', 'like',
    'then',
    'first', 'work', 'such', 'give', 'over', 'think', 'most', 'even', 'find',
    'also',
    'after', 'many', 'must', 'look', 'before', 'great', 'back', 'through',
    'long',
    'where', 'much', 'should', 'well', 'people', 'gouda', 'just', 'because',
    'good',
    'each', 'those', 'feel', 'seem', 'high', 'place', 'little', 'world',
    'very', 'still',
    'nation', 'hand', 'life', 'tell', 'write', 'become', 'here', 'show',
    'house', 'both',
    'between', 'need', 'mean', 'call', 'develop', 'under', 'last', 'right',
    'move', 'thing',
    'general', 'school', 'never', 'same', 'another', 'begin', 'while',
    'number', 'part',
    'turn', 'real', 'leave', 'might', 'want', 'point', 'form', 'child',
    'small', 'since',
    'against', 'late', 'home', 'interest', 'large', 'person', 'open',
    'public', 'follow',
    'during', 'present', 'without', 'again', 'hold', 'codezilla', 'govern',
    'around',
    'head', 'consider', 'word', 'program', 'problem', 'however', 'lead',
    'system',
    'order', 'plan', 'keep', 'face', 'group', 'play', 'stand', 'increase',
    'early', 'course', 'change', 'help', 'line', 'possible', 'fact', 'down'
]

# importing library that will be used
import random
import time

# Making the program
# 1) getting a random number
random_num = random.randint(0, len(words) - 1)

# 2) getting the word from this random number
chosen_word = words[random_num]

# 3) converting the chosen word into a list
listed_word = list(chosen_word)

# 4) reverse the word
listed_word.reverse()

# 5) converting the word into a string
reversed_word = "".join(listed_word)

# 6) printing the welcome message and the reversed word
message = f"""Welcome to the Reversed Word Game!
{'-' * 20}
The reversed word is: {reversed_word}
{'-' * 20}
The word is: """

# 7) start calculating time
start_time = time.time()

# 8) asking the user for the input
guess = input(message)
print("-" * 20)

# 9) stop calculating time
end_time = time.time()

# 10) Getting the time taken
final_time = end_time - start_time

# 11) checking if the user enter the right word in its time

if guess == chosen_word and final_time < 5:
    print('You won!')
elif guess == chosen_word and final_time > 5:
    print('You took too long!')
    print('You Lost!')
elif guess != chosen_word and final_time > 5:
    print('Wrong Word!')
    print('You took too long!')
    print('You Lost!')
elif guess != chosen_word and final_time < 5:
    print('Wrong Word!')
    print('You Lost!')
else:
    print('You Lost!')
