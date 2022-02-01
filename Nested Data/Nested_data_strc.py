# Nested List

info = {'personal_data':
         {'name': 'Lauren',
          'age': 20,
          'major': 'Information Science',
          'physical_features':
             {'color': {'eye': 'blue',
                        'hair': 'brown'},
              'height': "5'8"}
         },
       'other':
         {'favorite_colors': ['purple', 'green', 'blue'],
          'interested_in': ['social media', 'intellectual property', 'copyright', 'music', 'books']
         }
      }
color=info['personal_data']['physical_features']['color']

# Nested Iteration
# Deep copy:
# Shallow copy:

# Structuring Nested Data
# One should not iterate over obejcts with differnet data types:
# foe example a int is not iterable
# # The following code will yield an error due to the rason mentioned aboved
# nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
# for x in nested1:
#     print("level1: ")
#     for y in x:
#         print("     level2: {}".format(y))

# ----------------------------------------------------------

 # Shallow copies:
 # if we make a copy of an object and then we modiy the original, that change will magicaly be made in the copy.
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_version = original[:]
print(copied_version)
print(copied_version is original)
print(copied_version == original)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_version)


# Deep Copy:
# is an independent copy of the original. We can do it with nested iteration. WE can also use the 'copy' library
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = []
    for item in inner_list:
        copied_inner_list.append(item)
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)
# o bien usando slices
original = [['dogs', 'puppies'], ['cats', "kittens"]]
copied_outer_list = []
for inner_list in original:
    copied_inner_list = inner_list[:]
    copied_outer_list.append(copied_inner_list)
print(copied_outer_list)
original[0].append(["canines"])
print(original)
print("-------- Now look at the copied version -----------")
print(copied_outer_list)

# This process above works fine when there are only two layers or levels in a nested list. 
# However, if we want to make a copy of a nested list that has more than two levels, then we 
# recommend using the copy module. 
# In the copy module there is a method called deepcopy that will take care of the operation for you
import copy
original = [['canines', ['dogs', 'puppies']], ['felines', ['cats', 'kittens']]]
shallow_copy_version = original[:]
deeply_copied_version = copy.deepcopy(original)
original.append("Hi there")
original[0].append(["marsupials"])
print("-------- Original -----------")
print(original)
print("-------- deep copy -----------")
print(deeply_copied_version)
print("-------- shallow copy -----------")
print(shallow_copy_version)

# Por lagun motico la shallow_copy_version no esta copiando el "Hi there" de la lsita original, debe ser algo built in de python


# Menciona un cocncepto que no vamos a ver en este curso -"recurtion" -> Recursión / Recursividad:






