
import json
res="Nested Data\Tweet_data.json"
print(json.dumps(res, indent=2)[:100])
print("-----------")
print(type(res))
print(res.keys())


# ----
print(type(res))
print(res.keys())
res2 = res['statuses']
# --- 
print(type(res))
print(res.keys())
res2 = res['statuses']
print("----Level 2-----")
print(type(res2)) # it's a list!
print(len(res2))

# ----
print(type(res))
print(res.keys())
res2 = res['statuses']
print("----Level 2: a list of tweets-----")
print(type(res2)) # it's a list!
print(len(res2))  # looks like one item representing each of the three tweets
for res3 in res2[:1]:
   print("----Level 3: a tweet----")
   print(json.dumps(res3, indent=2)[:30])

# ----
print(type(res))
print(res.keys())
res2 = res['statuses']
print("----Level 2: a list of tweets-----")
print(type(res2)) # it's a list!
print(len(res2))  # looks like one item representing each of the three tweets
for res3 in res2[:1]:
   print("----Level 3: a tweet----")
   print(json.dumps(res3, indent=2)[:30])
   print(type(res3)) # it's a dictionary
   print(res3.keys())


## ----

print(type(res))
print(res.keys())
res2 = res['statuses']
print("----Level 2: a list of tweets-----")
print(type(res2)) # it's a list!
print(len(res2))  # looks like one item representing each of the three tweets
for res3 in res2[:1]:
   print("----Level 3: a tweet----")
   print(json.dumps(res3, indent=2)[:30])
   res4 = res3['user']

##  ---
print(type(res))
print(res.keys())
res2 = res['statuses']
print("----Level 2: a list of tweets-----")
print(type(res2)) # it's a list!
print(len(res2))  # looks like one item representing each of the three tweets
for res3 in res2[:1]:
   print("----Level 3: a tweet----")
   print(json.dumps(res3, indent=2)[:30])
   res4 = res3['user']
   print("----Level 4: the user who wrote the tweet----")
   print(type(res4)) # it's a dictionary
   print(res4.keys())

# ---


# print(type(res))
# print(res.keys())
res2 = res['statuses']
# print("----Level 2: a list of tweets-----")
# print(type(res2)) # it's a list!
# print(len(res2))  # looks like one item representing each of the three tweets
for res3 in res2[:1]:
   print("----Level 3: a tweet----")
   # print(json.dumps(res3, indent=2)[:30])
   res4 = res3['user']
   print("----Level 4: the user who wrote the tweet----")
   # print(type(res4)) # it's a dictionary
   # print(res4.keys())
   print(res4['screen_name'], res4['created_at'])

# ---

# print(type(res))
# print(res.keys())
res2 = res['statuses']
#print("----Level 2: a list of tweets-----")
#print(type(res2)) # it's a list!
#print(len(res2))  # looks like one item representing each of the three tweets
for res3 in res2:
   #print("----Level 3: a tweet----")
   #print(json.dumps(res3, indent=2)[:30])
   res4 = res3['user']
   #print("----Level 4: the user who wrote the tweet----")
   #print(type(res4)) # it's a dictionary
   #print(res4.keys())
   print(res4['screen_name'], res4['created_at'])


# Pendiente: Apernder el formato JSON  


