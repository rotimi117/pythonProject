class Dog:
    species = "Canis familiaris"
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def speak(self,sound):
        print(f"{self.name} says {sound}")

class GoldenRetriever(Dog):
    def speak(self,sound = "bark"):
        print(f"{self.name} says {sound}")

# philo = Dog("philo", 5, "brown")
# print(f"{philo.name}'s coat is {philo.coat_color}")

philo = GoldenRetriever("philo", 5, "brown")
philo.speak()
philo.speak("woof")


