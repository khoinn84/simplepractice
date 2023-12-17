import random

when = ["Last year","Last night","Today", "Two days ago"]
who = ["a rabbit", "a dog", "an elephant", "a human"]
home = ["a house", "an apartment", "a cave", "the jungle"]
venue = ["Sydney", "London", "New York", "Hanoi"]
action = ["went to the supermarket", "played a football match", "cooked dinner", "watched a movie"]

beginning = random.choice(when) + ' ' + random.choice(who) +' who lives in ' + random.choice(home) + ' went to ' + random.choice(venue) + ' and ' + random.choice(action)

print(beginning)

