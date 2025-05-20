class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            person.wife = Person.people[wife_name]
        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            person.husband = Person.people[husband_name]

    return person_list

