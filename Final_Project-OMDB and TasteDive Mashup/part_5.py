# Get movie rating
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

# It takes an OMDB dictionary result for one movie 
# and extracts the Rotten Tomatoes rating as an integer.
def get_movie_rating(req_dict={}):
    print("-------------------------------")
    print("...getting rating...of...: '{}'".format(req_dict["Title"]))
    rating=0
    print(json.dumps(req_dict,indent=4))
    print("req_dict['Ratings']: \n",req_dict["Ratings"])
    
    for source in req_dict["Ratings"]:
        print(source["Source"])
        if (source["Source"] == "Rotten Tomatoes"):
            print(">Rotten Tomatoes rating: ",source["Value"]) 
            rating_str=source["Value"]
            #Process this string into a int
            rating=int(rating_str.replace("%",""))
            
            
    print("\n------------------------")    
    return rating
