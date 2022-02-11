import requests_with_caching
import json
#Be sure to include only q, type, and limit
# json.loads(): takes a string and convertis into a dictionary/list
# json.dumps(): is the opposite of .loads(), it makes a dictionary/list into json format
#               it creates astring

def get_movies_from_tastedive(name_media=""):
    base_url="https://tastedive.com/api/similar"
    params={}
    dict_result={}
    params['q']=name_media
    params['type']="movies"
    params['limit']=5
    #params['info']
    #params['k']
    #params['callback']
    print("\nSearching: '{}'".format(name_media))
    response_movie= requests_with_caching.get(base_url,params)
    print("\nURL: \n", response_movie.url)
    
    dict_result=response_movie.json()
    print("\ndict_result - type ", type(dict_result))
    
    x=json.dumps(dict_result,indent=2) #json.dumps() returns a string
    #print("\n",x,"\n    type: ",type(x))
    
    return dict_result

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# extract_movie_titles(get_movies_from_tastedive("Tony Bennett"))
# extract_movie_titles(get_movies_from_tastedive("Black Panther"))

def extract_movie_titles(dict_request={}):
    print("\n...extracting movie tittles")
    print("Dictionary from request: \n",dict_request)
    movie_title=[] # is  a list of strings
    
    print("\n",dict_request["Similar"]["Results"],"\n")
    for x in dict_request["Similar"]["Results"]:
        print(x)
        movie_title.append(x["Name"])
            
    #movie_title=dict_request['Similar']['Results']['Name']
    print("Result: \n", movie_title)
    return movie_title