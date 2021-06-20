from flask import Flask, request
import wikipedia as wiki
import random
from math import floor
# from cockroach import Cockroach
from pony.flask import Pony
from pony.orm import *
from datetime import datetime
# import PIL
# app = Flask(__name__)
db_params = dict(provider='cockroach', user='rudransh', host='free-tier.gcp-us-central1.cockroachlabs.cloud', port=26257, database='shiny-wolf-1947.defaultdb', password = "**********your Passwor*****")


app = Flask(__name__)
app.config.update(dict(
    DEBUG = True,
    PONY = db_params
))
Pony(app)


db = Database()
class User(db.Entity):
    # def __init__(self, table,userid, password, )
    
    _table_ = 'Users'
    user_id = PrimaryKey(str)
    password = Required(str)
    searchQ = Set('Search')

class Search(db.Entity):
  _table_ = 'Searches'
  # id = PrimaryKey(int)
  user = Required('User')
  searchText = Required(str)
  searchIntent = Required(str)
  imageLink = Required(str)
  searchKeyWord = Required(str)



sql_debug(True)  # Print all generated SQL queries to stdout
db.bind(**db_params)  # Bind Database object to the real database
db.generate_mapping(create_tables=True)  


@db_session  # db_session decorator manages the transactions
def add_values(userid, searchtext, searchintent, imagelink, searchkeyword):
  Search(user = User.get(user_id = userid), searchText = searchtext, searchIntent =searchintent, imageLink=imagelink, searchKeyWord = searchkeyword)

@db_session
def create_user(userid, password):
  User(user_id = userid, password = password, searchQ = None)

@db_session
def test():
  from textblob import TextBlob
  return str(TextBlob("tesing thsi lib").detect_language())

  return "added lol"


@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    return "Hello world!"

active_user = None

@app.route('/login', methods =  ["POST"])
def login():
  global active_user
  req = request.get_json(force = True, silent = True)
  # print(req.get('username'))
  try:
    user = User.get(user_id = req.get('username'))
    if not user:
      return "UserNotFound"
    # request.args
    # active_user = req.get('username')
    elif user.password != req.get('password'):
      return "WrongPassword"
    else:
      active_user = req.get('username')
      return "success"
  except Exception as e:
    return str(e)


@app.route('/wordcloud', methods = ['GET'])
def return_words():
  if not active_user:
    return "Sorry you need to be logged in to use this endpoint"
  else:
    a = select(s.searchKeyWord for s in Search if s.user.user_id == active_user)[:]
    a = list(a)
    return " ".join(a)

  
@app.route('/register', methods = ['POST'])
def signup():
  global active_user
  req = request.get_json(force = True, silent = True)  
  username = req.get('username')
  password = req.get('password')
  # print(user, password)
  try:
    user = User.get(user_id = username)
    if not user:
      print('i was here')
        # create_user(userid = user, password = password)
      User(user_id = username, password = password)
      active_user = username;
      return "SUCESSS, Your ID is created"
    else:
      return "FALIURE, Your ID was already taken"
  except Exception as e:
    return str(e)



def ProperNounExtractor(text):
    # Importing the required libraries
    import nltk 
    from nltk.corpus import stopwords 
    # from nltk.tokenize import word_tokenize, sent_tokenize
    print('PROPER NOUNS EXTRACTED :')
    ans = []
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word not in set(stopwords.words('english'))]
        tagged = nltk.pos_tag(words)
        for (word, tag) in tagged:
            if "NN" in tag: # If the word is a proper noun
                ans.append(word)
                print(word)
    return ans

@app.route('/test')
def hola():
  # create_user('1', 2)
  # return wiki.summary('Daisy', sentences = 2, auto_suggest= False)
  # return test()
  return what_to_choose_intent("plants", "summer")
  
  test()
  test()
  # Search()
  print(active_user)
  return 'added'
months = [".Jan", ".Feb", ".Mar", ".Apr", ".May", ".Jun", ".Jul", ".Aug", ".Sep", ".Oct", ".Nov", ".Dec"]

def featured_snippets_handler(snippet):
  # from textblob import TextBlob
  unprocess_text = snippet.split('\n')
  # print(unprocess_text)
  # return unprocess_text[1]
  # idx = None
  ans = []
  for i in unprocess_text:
    if "function" in i or "window" in i or "document" in i or "www" in i or "Featured" in i or "View" in i or "https" in i:
      continue
    elif i in months:
      break
    elif "..." in i:
      ans.append(i.replace("...", ""))
    elif " SHOP NOW" in i:
      print("                              no")
      ans.append(i.replace(" SHOP NOW", ""))
    elif "of 45." in i:
      ans.append(i.replace("of 45.", ""))

    else:

      ans.append(i)
      
  print(unprocess_text[1], ans)
  return " ".join(ans).replace("SHOP NOW", "", len(unprocess_text)).replace("of 45", "", len(unprocess_text)) if len(ans)>0 else unprocess_text[1]
      
# print(ans)
    
  return " ".join(ans)
  print(ans)
      # break
    
  
def related_search_handler(search):
  arr =search.split('\n')
  print(arr)



def tell_me_more(searchKeyword, intent, searchtext, active_user ):
  try:
    print(wiki.search(searchKeyword))
    keyword = wiki.search(searchKeyword)[0]
    # searchKeyword = searchKeyword[0].upper()+searchKeyword[1:]
    returnText = str(wiki.summary(keyword, sentences = 2,auto_suggest= False))
    print(searchKeyword)
    print(returnText)
    
    # page = wiki.WikipediaPage(title = searchKeyword)
    imagelink = "asasasa"
    add_values(userid = active_user, searchtext = searchtext, searchintent = intent, imagelink = imagelink , searchkeyword =keyword )
    return returnText
  except Exception as e:
    if e == wiki.exceptions.DisambiguationError or True:
      if "may refer to" in str(e):
        text = str(e).split(' ')
        print("here2")
        # print(text)
        for i, v in enumerate(text):
          if v == "to:" or v == "to":
            print("here3")
            # return text[i+1]
            return tell_me_more(searchKeyword =text[i+1] , intent= intent, searchtext=searchtext, active_user=active_user)
      elif "Attribute" in str(e):
        return "I am sorry you need to log in first"
    else:
      return str(e)




def the_what_intent(searchText):
  # import requests
  # from bs4 import BeautifulSoup
  url = "https://www.google.com/search?q="
  for i, v in enumerate(searchText.split(" ")):
    if i == 0:
      url+=v
    else:
      url+="+"+v
  print(url)

  from requests_html import HTMLSession

  session = HTMLSession()
  response = session.get(url)
  try:
    specs = response.html.find('.di3YZe', first=True).text
    # print(not specs)
    if not specs:
      print("herr")
      specs.get('raising an error')

    # print(specs)
  except Exception as e:
    if "NoneType" in str(e):
      try:
        specs = response.html.find('.RqBzHd', first = True).text
        print("yaha nahi hai")
        if not specs:
          specs= None.get("raising an errror")
      except Exception as e:
        if 'NoneType' in str(e):
              try:
                # ans = []
                specs = response.html.find('.ifM9O', first = True).text
                featured_text_return = featured_snippets_handler(specs)
                if len(featured_text_return)>0:
                  print(featured_text_return)
                    
                  return featured_text_return
                else:
                  return "Something went wrong at featured side I am sorry :("
                # unprocessed_text = specs.split('\n')

                # for i in unprocessed_text:
                    # if TextBlob(i).detect_language() == 'en':
                    # ans.append(i)
                # print(ans)
                # return "not here"
                # print(specs)
              except Exception as e:
                if "NoneType" in str(e):
                  return "I am sorry :( can you recheck the spelling and try again?"
                return "Sorry I am having some trouble with your query if you are developer I am probably unable to find the webelement because google has dynamic classes here is the error"+str(e)
        else:
              return "oops something went wrong"+str(e)
    else:
      return "oops something went wrong" + str(e)
  # print(len(specs), specs)
  if "Related search" in specs:
    unproces_list_text = specs.split("\n")
    for i, v in enumerate(unproces_list_text):
      if "Related" in v:
        unproces_list_text[i] = ""
      if "View" in v or "view" in v:
        unproces_list_text[i] = ""
      if len(v.split(" ")) > 10:
        unproces_list_text[i] = ""
    processed_text=  " ".join(unproces_list_text)
    # print(processed_text)
    
    return processed_text
  else:
    featured_text_return = featured_snippets_handler(specs)
    if len(featured_text_return)>0:
      print("featured_text_return")
                    
      return featured_text_return
    # print(specs.split("\n"))
    
    # text = related_search_handler()
  # unproces_list = specs.split("\n")
  # print(unproces_list)
  # ans = []
  # for i in unproces_list:
  #   ans.append(ProperNounExtractor(i))
  # print(ans)
  
  # print(ans)
  

  # return " ".join(ans)
        

  print(specs)
  # print(type(specs), specs)

def what_to_choose_intent(flower_or_plant, weather):
  url = "https://www.google.com/search?q=" + weather + "+"+ flower_or_plant
  from requests_html import HTMLSession
  print(url)
  session = HTMLSession()
  response = session.get(url)
  raw_reponse = response.html.find('.kp-blk', first= True).text
  processed_response = featured_snippets_handler(raw_reponse)
  print(processed_response)
  
  
  
  # print(raw_reponse)
  return processed_response

  
  



@app.route('/webhook', methods=['POST'])
def webhook():
  # for i in range(5):
  #   cock = Cockroach().add_values(user_id = 1*i+3, search_keyWord = "yp", imagesLink= "hsh", search_intent = "u")
  # req = request.get_json(force = True, silent = True)
  returnText = "Ooops, Something Went Wrong"
  theWhatIntentReturnText = ""
  try:
    req = request.get_json(force = True, silent = True)
    # print(req)
    res = req.get('queryResult')
 
    # print(searchKeyword)
    intent = req.get('queryResult').get("intent").get('displayName')
    if intent == "WhatIntent":
      searchtext = res.get("queryText")
      print("Control here here")
      searchKeyword = res.get("parameters").get("any")
      
      theWhatIntentReturnText = the_what_intent(searchtext)    
      if theWhatIntentReturnText =="" or len(theWhatIntentReturnText) <= 0 or "oops" in theWhatIntentReturnText or "Sorry" in theWhatIntentReturnText:
        # returnText = "sorry I couldn't process your request :( I am still learning try asking me in simpler words"
        returnText = theWhatIntentReturnText
        print(returnText== None, len(returnText)==0)
        return {
          "fulfillmentText": returnText,
          "source": 'webhook'
      }
      else:
        returnText =theWhatIntentReturnText
        try:
          print(active_user)
          add_values(userid = active_user, searchtext = searchtext, searchintent = intent, imagelink = "imagelink" , searchkeyword =searchKeyword )
        except Exception as e:
          if "Attribute" in str(e):
            returnText = "I am sorry but you need to log in first"
            # returnText = str(e)
            return {
          "fulfillmentText": returnText,
          "source": 'webhook'
                    }
        
        return {
          "fulfillmentText": returnText,
          "source": 'webhook'
      }
    # print("Control def not here not here")
    
    if intent == "WhatToChoose":
      # print('here')
      weather = res.get('parameters').get('weather')
      flower_or_plant = res.get('parameters').get('plantorflower')+"s"
      returnText = what_to_choose_intent(flower_or_plant = flower_or_plant, weather = weather)
      try:
        add_values(userid = active_user, searchtext = weather+" "+flower_or_plant,searchintent= intent,  imagelink = "yoImage", searchkeyword = flower_or_plant+ " "+ weather)
      except Exception as e:
        if "Attribute" in str(e):
          return {
            "fulfillmentText": "Sorry but you need to log in first",
            "source":"webhook"
          }

      return {
          "fulfillmentText": returnText,
          "source": 'webhook'
      }

    if intent == "Tell me more intent" or "Tell Me Intent":
      res = req.get('queryResult')
    # print(res)
      searchtext = res.get("queryText")
    # print(searchtext)
      searchKeyword = res.get("parameters").get("Search")
      
      
      returnText = tell_me_more(searchKeyword = searchKeyword, intent = intent, active_user = active_user, searchtext = searchtext)
    
      return {
          "fulfillmentText": returnText,
          "source": 'webhook'
      }
    print("control here")

    

      
    print('Control here')
  
    
    
  except Exception as e:
    print("def not here")
    return {
        "fulfillmentText": str(e),
        "source": 'webhook'
    }
  print("hell not here")
  
  return {
        "fulfillmentText": 'Something is probably wrong',
        "source": 'webhook'
    }
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) # This line is required to run Flask on repl.it
