class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

    def say_age(self):
        print(f"I am {self.age} years old.")

class SuperHero(Person):
    def __init__(self, name, age, secret_identity, nemesis):
        super().__init__(name, age)
        self.secret_identity = secret_identity
        self.nemesis = nemesis

    def reveal_secret_identity(self):
        print(f"My secret identity is {self.secret_identity}.")

    def say_hello(self):
        print(f"Hello, I am {self.name}, also known as {self.secret_identity}.")

    def old_say_age(self):
        super().say_age()

    def say_age(self):
        print(f"As a superhero, I prefer to keep my age a secret.")

if __name__ == "__main__":
    person = Person("Mariam Abdalmagied", 23)
    person.say_hello()  
    person.say_age()    

    superhero = SuperHero("Peter Parker", 25, "Spider-Man", "Doc ock")
    superhero.say_hello()  
    superhero.reveal_secret_identity()  
    superhero.old_say_age()  
    superhero.say_age()     
