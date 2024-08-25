from datetime import datetime

class Person:
    def __init__(self, name: str, birth_year: int):

        self._name = name
        self._birth_year = birth_year


    def say_hello(self):
        print(f"Hello, my name is {self._name}.")


    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value


    @property
    def age(self) -> int:
        current_year = datetime.now().year
        return current_year - self._birth_year




if __name__ == "__main__":

    current_year = datetime.now().year
    birth_year = current_year - 23


    mariam = Person("Mariam", birth_year)
    

    mariam.say_hello() 
    
    print(f"Name: {mariam.name}")  
    print(f"Age: {mariam.age}")    


    mariam.name = "Maria"
    mariam.say_hello() 
