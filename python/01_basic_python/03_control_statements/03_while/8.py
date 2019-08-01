list_of_animals = [
    'monkey',
    'tiger',
    'tiger',
    'wolf',
    'zebra',
    'horse',
    'pig',
    'pig',
    'pig',
    'dog',
    'cat',
    'dog'
]

iterator = 0
previous_animal = None

while iterator < len(list_of_animals):
    current_animal = list_of_animals[iterator]

    if current_animal == previous_animal:
        print(
            f"Encountered a {current_animal} in spots {iterator - 1} and {iterator} of the animal list.")

    iterator += 1
    previous_animal = current_animal

While loops or code in general is harder than expected as humans make mistakes while maintaining state i.e they either forget to delete something,
or increment a variable, update a value, undo the effects of some piece of code and so on. If state is handled well you most likely
will have no issues running your while loops.

Let's try solving the problem without a computer first.

Apart from the iterator we need to mentally keep of the animal last seen. The current animal that we see becomes the previous animal in the next iteration. We need to keep that updated as well.
