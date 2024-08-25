import random
from typing import Optional, List

NUMBER_OF_GENERATIONS = 3
INDENT_LENGTH = 4

class Person:
    def __init__(self, parents: Optional[List['Person']], alleles: List[str]):

        self.parents = parents

        self.alleles = alleles

def main():

    person = create_family(NUMBER_OF_GENERATIONS)

    print_family(person, 0)

def create_family(generations: int) -> Person:
    if generations > 1:

        parent_1: Person = create_family(generations - 1)
        parent_2: Person = create_family(generations - 1)


        alleles = [random.choice(parent_1.alleles), random.choice(parent_2.alleles)]


        return Person(parents=[parent_1, parent_2], alleles=alleles)
    else:

        alleles = [get_random_allele(), get_random_allele()]
        return Person(parents=None, alleles=alleles)

def print_family(person: Optional[Person], number_of_generations: int):
    if not person:
        return
    print(f"{' ' * number_of_generations * INDENT_LENGTH}", end="")
    if number_of_generations == 0:
        print(f"Child (Generation {number_of_generations}): blood type {person.alleles[0]}{person.alleles[1]}")
    elif number_of_generations == 1:
        print(f"Parent (Generation {number_of_generations}): blood type {person.alleles[0]}{person.alleles[1]}")
    else:
        for i in range(number_of_generations - 2):
            print("great-", end="")
        print(f"grandparent (Generation {number_of_generations}): blood type {person.alleles[0]}{person.alleles[1]}")


    if person.parents:
        print_family(person.parents[0], number_of_generations + 1)
        print_family(person.parents[1], number_of_generations + 1)

def get_random_allele() -> str:
    return random.choice(["A", "B", "O"])

if __name__ == "__main__":
    main()
