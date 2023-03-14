def roll_call_dwarves(list):
    number = 1
    for name in list:
        print(f"{number}. {name}")
        number += 1

def summon_captain_planet(calls):
    new_list = list()
    for name in calls:
        new_list.append(name.title() + "!")
    return new_list

def long_planeteer_calls(calls):
    longwords = list()
    for call in calls:
        if len(call) > 4:
            longwords.append(call)
    if len(longwords) > 0:
        return True
    else:
        return False
        

def find_the_cheese(foods):
    type_of_cheese=["cheddar", "gouda", "camembert"]
    for food in foods:
        if food in type_of_cheese:
            return food


    pass
