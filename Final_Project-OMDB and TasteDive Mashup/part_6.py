# It takes a list of movie titles as an input. 
# It returns a sorted list of related movie titles 
# as output, up to five related movies for each 
# input movie title. The movies should be sorted 
# in descending order by their Rotten Tomatoes rating, 
# as returned by the get_movie_rating function. 
# Break ties in reverse alphabetic order, so that
# ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.
import requests_with_caching
import json
#1
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
    print("\n    Searching: '{}'".format(name_media))
    response_movie= requests_with_caching.get(base_url,params)
    print("    URL: ", response_movie.url,"\n")
    dict_result=response_movie.json()
    #print("\ndict_result - type ", type(dict_result))
    x=json.dumps(dict_result,indent=2) #json.dumps() returns a string
    return dict_result
#2
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

#3
def get_related_titles(lst_movies=[]):
    print("\n...getting related titles for :")
    related_titles=[]
    print("    List of movies: ",lst_movies)
    req_dict={}
    a=[]
    
    for mov in lst_movies:
        req_dict=get_movies_from_tastedive(mov)
        #print("\nDictionary for {}\n{}".format(mov,req_dict),"\n")
        #related_titles.append(req_dict["Similar"]["Results"])
        for x in req_dict["Similar"]["Results"]:
            print(x["Name"])
            # Creating list of suggested movies
            if (x["Name"] not in related_titles):
                related_titles.append(x["Name"])
                
    print("\n ->List of related movie titles: \n",related_titles)
    return related_titles
#4
def get_movie_data(movie_title=""):
    #resp_dict={}
    info_dict={}
    params={}
    base_url="http://www.omdbapi.com/" #?apikey=[yourkey]&"
    params["t"]=movie_title #movie title
    params["r"]="json"
    resp=requests_with_caching.get(base_url,params)
    info_dict=resp.json()
    return info_dict

#5
def get_movie_rating(req_dict={}):
    print("    ...getting rating...of...: '{}'".format(req_dict["Title"]))
    rating=0
    print(json.dumps(req_dict,indent=4))
    print("req_dict['Ratings']: ",req_dict["Ratings"])
    
    for source in req_dict["Ratings"]:
        #print(source["Source"])
        if (source["Source"] == "Rotten Tomatoes"):
            print("> Rotten Tomatoes rating: ",source["Value"]) 
            rating_str=source["Value"]
            #Process this string into a int
            rating=int(rating_str.replace("%",""))
            break
        else:
            print("> No Rotten Tomators rating found. Default=0")
            continue # goes to the beginning of the loop        
    return rating

    
#6
def get_sorted_recommendations(lst_mov_titles=[]):
    print("...getting sorted recomendations...\n")
    unsorted_lst=[]
    sorted_lst=[]
    lst_rel_titles=[]
    rating=0
    movie_dict={}
    #----
    # Getting related tittles
    lst_rel_titles=get_related_titles(lst_mov_titles) # takes in list, returns list
    print("\n...Analysing...")
    # Sorting the list by their Rotten Tomatoes Rating
    for movie in lst_rel_titles:
        print("------------------------------")
        print("    Title: ", movie)
        # Getting data for each suggested movie
        movie_dict[movie]=get_movie_data(movie) # takes in string, returns dictionary
        # Getting movie rating
        rating=get_movie_rating(movie_dict[movie])  # takes in dict, returns integer
        print("    Rating: ",rating)
        # Appending movies that are in rotten tomatoes
        if (rating !=None):
            unsorted_lst.append([movie,rating])
            
    print("\n-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
    print("Unsorted list: {}\nType: {} \nLength: {}".format(unsorted_lst,type(unsorted_lst),len(unsorted_lst)))
    # Sorting list of rotten tomatoes movies &  Break ties in reverse alphabetical order 
    sorted_lst=sorted(unsorted_lst,key=lambda unsorted_lst:(unsorted_lst[1],unsorted_lst[0]), reverse= True)
    #usin list ocmprehension we make aun auxiliary variable
    a=[sublist[0] for sublist in sorted_lst]
    print("a: ",a)
    sorted_lst.clear()
    sorted_lst=a         
    print("\n>Sorted List: ",sorted_lst)
    return sorted_lst
