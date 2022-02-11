import requests_with_caching
import json

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

def extract_movie_titles(dict_request={}):
    print("\n...extracting movie tittles")
    print("Dictionary from request: \n",dict_request)
    movie_title=[] # is  a list of strings
    
    print("\n",dict_request["Similar"]["Results"],"\n")
    for x in dict_request["Similar"]["Results"]:
        print(x)
        movie_title.append(x["Name"])
            
    print("Result: \n", movie_title)
    return movie_title

# It gets five related movies for each from TasteDive, 
# extracts the titles for all of them, and combines them 
# all into a single list.
# Don’t include the same movie twice.
def get_related_titles(lst_movies=[]):
    print("\n...getting related titles")
    related_titles=[]
    print("List of movies: \n",lst_movies)
    req_dict={}
    a=[]
    
    for mov in lst_movies:
        req_dict=get_movies_from_tastedive(mov)
        print("\nDictionary for {}\n{}".format(mov,req_dict),"\n")
        #related_titles.append(req_dict["Similar"]["Results"])
        for x in req_dict["Similar"]["Results"]:
            print(x["Name"])
            # Creating list of suggested movies
            if (x["Name"] not in related_titles):
                related_titles.append(x["Name"])
                
    print("\n ->List of related movie titles: \n",related_titles)
    return related_titles
    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])