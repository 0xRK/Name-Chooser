import random
with open('names.txt', 'r') as names:
    lines = names.readlines()
    while True:
        i = input("Press Enter to select a name.")
        if i == '':
            print('-----------------------')
            print(f'||\t{random.choice(lines).strip()}\t||')
            print('-----------------------')
        else:
            break

