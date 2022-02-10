#flickr2022_jfos
# Nombre aplicación: Denmo-01
# Clave: 4e424ddedbfd67e884fd1fb31ee2f6c6
# Secreto: 3cb75325f9139099
# ------
# The structure of a URL for a photo search on flickr is:

# - base URL is https://api.flickr.com/services/rest/

# - ?

# - key=value pairs, separated by &s:
#     One pair is method=flickr.photos.search. This says to do a photo search, rather than one of the many other operations that the API allows. Don’t be confused by the word “method” here– it is not a python method. That’s just the name flickr uses to distinguish among the different operations a client application can request.

#     format=json. This says to return results in JSON format.

#     per_page=5. This says to return 5 results at a time.

#     tags=mountains,river. This says to return things that are tagged with “mountains” and “river”.

#     tag_mode=all. This says to return things that are tagged with both mountains and river.

#     media=photos. This says to return photos

#     api_key=.... Flickr only lets authorized applications access the API. Each request must include a secret code as a value associated with api_key. Anyone can get a key. See the documentation for how to get one. We recommend that you get one so that you can test out the sample code in this chapter creatively. We have included some cached responses, and they are accessible even without an API key.

#     nojsoncallback=1. This says to return the raw JSON result without a function wrapper around the JSON response.

# Ejemplo:
# No va funcioanr porque no existe el modulo requests_with_caching

# import statements
import requests
#import requests_with_caching
import json
# import webbrowser

# apply for a flickr authentication key at http://www.flickr.com/services/apps/create/apply/?
# paste the key (not the secret) as the value of the variable flickr_key
flickr_key = 'yourkeyhere'

def get_flickr_data(tags_string):
    baseurl = "https://api.flickr.com/services/rest/"
    params_diction = {}
    params_diction["api_key"] = flickr_key # from the above global variable
    params_diction["tags"] = tags_string # must be a comma separated string to work correctly
    params_diction["tag_mode"] = "all"
    params_diction["method"] = "flickr.photos.search"
    params_diction["per_page"] = 5
    params_diction["media"] = "photos"
    params_diction["format"] = "json"
    params_diction["nojsoncallback"] = 1
    #flickr_resp = requests_with_caching.get(baseurl, params = params_diction, permanent_cache_file="flickr_cache.txt")
    # Useful for debugging: print the url! Uncomment the below line to do so.
    #print(flickr_resp.url) # Paste the result into the browser to check it out...
    #return flickr_resp.json()

result_river_mts = get_flickr_data("river,mountains")

# Some code to open up a few photos that are tagged with the mountains and river tags...

photos = result_river_mts['photos']['photo']
for photo in photos:
    owner = photo['owner']
    photo_id = photo['id']
    url = 'https://www.flickr.com/photos/{}/{}'.format(owner, photo_id)
    print(url)
    # webbrowser.open(url)

