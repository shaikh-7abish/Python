import random

when = [
    "A few years ago",
    "Yesterday",
    "Last night",
    "A long time ago",
    "Once upon a time",
]
pets = ["a rabbit", "an elephant", "a mouse", "a turtle", "a cat"]
name = ["Ali", "Tabish", "Leonardo", "Jennifer", "Peacemaker"]
residence = ["Barcelona", "Paris", "Qatar", "Boston", "Mumbai"]
went = ["cinema", "museum", "zoo", "university", "school"]
happend = (
    "made a lot of friends",
    "have a drink",
    "found a secret key",
    "wrote a poetry",
)

print(
    random.choice(when)
    + ", "
    + random.choice(name)
    + " that lived in "
    + random.choice(residence)
    + ", went to the "
    + random.choice(went)
    + " and "
    + random.choice(happend)
)

print(
    f" \n By the way, My name is {random.choice(name)}, \n and I have {random.choice(pets)}. \n <3"
)
