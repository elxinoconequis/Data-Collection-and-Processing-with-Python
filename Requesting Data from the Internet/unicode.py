# When there are 75,000 possible characters, they can’t all be encoded with a single byte, 
# because there are only 256 distinct bytes (eight-bit sequences). There are many possible encodings.
# The one you will be most likely to encounter, using REST APIs, is called UTF-8. 
# A single unicode character is mapped to a sequence of up to four bytes.

# If you read in a UTF-8 encoded text, and get the contents using .read() or .readlines(),
#  you will need to “decode” the contents in order to turn it into a proper unicode string that
#   you can read and use.

# Fortunately, the requests module will normally handle this for us automatically. 
# When we fetch a webpage that is in json format, the webpage will have a header called 
# ‘content-type’ that will say something like application/json; charset=utf8. 
# If it specifies the utf8 character set in that way, the requests module will 
# automatically decode the contents into unicode: requests.get('that web page').text will 
# ield a string, with each of those sequences of one to four bytes coverted into a single character.

# If, for some reason, you get json-formatted text that is utf-encoded but the requests 
# module hasn’t magically decoded it for you, the json.loads() function call can take care
#  of the decoding for you. loads() takes an optional parameter, encoding. Its default 
#  value is ‘utf-8’, so you don’t need to specify it unless you think the text you have 
#  received was in some other encoding than ‘utf-8’