
import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results

# The get function in the requests module takes an optional parameter called params. 
# If a value is specified for that parameter, it should be a dictionary. The keys and v
# alues in that dictionary are used to append something to the URL that is requested from the
#  remote site.

d = {'q': '"violins and guitars"', 'tbm': 'isch'}
results = requests.get("https://google.com/search", params=d)
print(results.url)

# Many providers of APIs require you to register in advance to make use of an API, and 
# then authenticate yourself with each request. That way they can charge money, or restrict 
# usage in some way. A popular form of authentication is to 
# have a personal “api_key” that you pass as one of the key=value pairs in the URL

# Another example:
# import requests

def get_rhymes(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["rel_rhy"] = word
    params_diction["max"] = "3" # get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    return [d['word'] for d in word_ds]
    return resp.json() # Return a python object (a list of dictionaries in this case)

print("rhymes\n",get_rhymes("funny"))