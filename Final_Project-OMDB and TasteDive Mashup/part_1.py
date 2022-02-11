import requests_with_caching
import json
#Be sure to include only q, type, and limit

def get_movies_from_tastedive(name_media=""):
    base_url="https://tastedive.com/api/similar"
    params={}
    dict_result={}
    params['q']=name_media
    params['type']="movies"
    #params['info']
    params['limit']=5
    #params['k']
    #params['callback']
    response_movie= requests_with_caching.get(base_url,params)
    print("\nSearching: '{}'".format(name_media))
    dict_result=response_movie.json()
    return dict_result
 
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
#get_movies_from_tastedive("Bridesmaids")
#get_movies_from_tastedive("Black Panther")
