TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

SEPARATOR = "-" * 40
users_and_passwords = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("username:")
password = input("password:")

if username not in users_and_passwords or users_and_passwords[username] != password:
    print("unregistered user, terminating the program..")
    quit()

pocet_textu = len(TEXTS)

print(SEPARATOR)
print(f"Welcome to the app, {username}")
print(f"We have {pocet_textu} texts to be analyzed.")
print(SEPARATOR)

text_number = input(f"Enter a number btw. 1 and {pocet_textu} to select: ")

if not text_number.isdigit() or not (1 <= int(text_number) <= pocet_textu):
    print("Wrong input, terminating the program..")
    quit()

print(SEPARATOR)

text = TEXTS[int(text_number) - 1]
words = text.split()

title_count = 0
upper_count = 0
lower_count = 0
numeric_count = 0
numeric_sum = 0
frequency = {}

for word in words:
    # Kontrola typů slov
    if word.istitle():
        title_count += 1
    elif word.isupper():
        upper_count += 1
    elif word.islower():
        lower_count += 1
    elif word.isnumeric():
        numeric_count += 1
        numeric_sum += int(word)
    clean_word = word.strip(".,;:?!")
    length = len(clean_word)
    if length > 0:
        frequency[length] = frequency.get(length, 0) + 1

print(f"There are {len(words)} words in the selected text.")
print(f"There are {title_count} titlecase words.")
print(f"There are {upper_count} uppercase words.")
print(f"There are {lower_count} lowercase words.")
print(f"There are {numeric_count} numeric strings.")
print(f"The sum of all the numbers {numeric_sum}")
print(SEPARATOR)

print("LEN|  OCCURRENCES  |NR.")
print(SEPARATOR)

for length in sorted(frequency.keys()):
    stars = "*" * frequency[length]
    print(f"{length:>3}|{stars:<17}|{frequency[length]}")