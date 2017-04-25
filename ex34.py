animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

def list_animals_possition(animals):
    animal_position = 0
    for i in animals:
        print("The animal at %d is a %s" % (animal_position, i))
        animal_position += 1

print(list_animals_possition(animals))