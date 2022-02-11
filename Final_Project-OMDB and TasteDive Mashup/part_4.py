# OMDB
# Api key: c2e1f1aa
# https://www.omdbapi.com/
import requests_with_caching
import json
# The function should return a 
# dictionary with information about that movie.
def get_movie_data(movie_title=""):
    #resp_dict={}
    info_dict={}
    params={}
    base_url="http://www.omdbapi.com/" #?apikey=[yourkey]&"
    params["t"]=movie_title #movie title
    params["r"]="json"
    
    resp=requests_with_caching.get(base_url,params)
    info_dict=resp.json()
    print(info_dict,"\ntype:", type(info_dict))
    
    
    return info_dict

    

