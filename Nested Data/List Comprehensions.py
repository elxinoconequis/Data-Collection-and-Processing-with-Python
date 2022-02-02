# List Comprehensions
# ya que aprendimos lo que es el map y el filter, será útil ese conocmiento para
# (map y filter en realidad casi no se usa), sino que los programadores de Python hacen uso
#  "List Comprehension"

# General format: [<transformer expresion> for <variable name> in <sequence> if <filter expression>]
things=[2,5,9]
yourlist=[value*2 for value in things]
print(yourlist)
print("----")
def keep_event(nums=[]): # takes in a list
    new_lst=[]
    new_lst=[num for num in nums if (num % 2)==0] #"[" was not closed; Expected "else"
    return new_lst

k = [1,2,3,4,5,6,7,8,9,10]
print(keep_event(k))


# You can also combine map and filter 
# operations by chaining them together, or with a single list comprehension.

things = [3, 4, 6, 7, 0, 1]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])

# Write code to assign to the variable compri all the values of the key name in 
# any of the sub-dictionaries in the dictionary tester. Do this using a list comprehension.

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
compri=[]
inner_lst= tester['info']
#print(inner_lst)

import json
print(json.dumps(inner_lst,indent=2))

compri=[d['name'] for d in inner_lst]

