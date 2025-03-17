# Глобальный словарь для хранения друзей
friends_dict = {}


def add_friends(name_of_person, list_of_friends):
    if name_of_person not in friends_dict:
        friends_dict[name_of_person] = set()
    friends_dict[name_of_person].update(list_of_friends)


def are_friends(name_of_person1, name_of_person2):
    return name_of_person2 in friends_dict.get(name_of_person1, set())


def print_friends(name_of_person):
    if name_of_person in friends_dict:
        print(" ".join(sorted(friends_dict[name_of_person])))
    else:
        print("")


# Пример использования:
add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))  # False
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))  # True
print_friends("Алла")  # Иван Марина Мария
