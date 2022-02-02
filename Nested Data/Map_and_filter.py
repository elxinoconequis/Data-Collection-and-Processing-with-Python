# 2 Feb 2022
# Let’s revisit the accumulator pattern. We have frequently taken a list and produced another list 
# from it that contains either a subset of the items or a transformed version of each item. 
# When each item is transformed we say that the operation is a mapping, or just a map of the original list. 
# When some items are omitted, we call it a filter.

def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)

# ----

# Technically, in a proper Python 3 interpreter, the map function produces an “iterator”, 
# which is like a list but produces the items as they are needed. Most places in Python where 
# you can use a list (e.g., in a for loop) you can use an “iterator” as if it was actually a list. 
# So you probably won’t ever notice the difference. If you ever really need a list, you can 
# explicitly turn the output of map into a list: list(map(...)). In the runestone environment, 
# map actually returns a real list, but to make this code compatible with a 
# full python environment, we always convert it to a list.

def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list)
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)

# Excercise

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
greeting_doubled=[]
greeting_doubled=list(map(lambda elem:elem*2,lst))
print(greeting_doubled)

# -----> Filter
# Filter does not transform, it just ealuates if omsething is true or false
# Es similar   al paramtro key de la fnción 'sorted'

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
filter_testing=[]
filter_testing=list(filter(lambda word: "w" in word, lst_check))
print(filter_testing)






