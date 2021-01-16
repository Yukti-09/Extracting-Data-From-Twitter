import tweepy 
import string
from random import randint

#Assign values
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_token_secret) 
  
api = tweepy.API(auth) 
  
l = string.ascii_uppercase
l1 = (string.ascii_lowercase)
allowed_char=[]

for i in range(len(l)):
    allowed_char.append(l[i])
    allowed_char.append(l1[i])
allowed_char.append('_')

length = randint(4,15) #Length of user name

user_name = ''
for i in range(length):
	user_name+=allowed_char[randint(0,len(allowed_char))]

print(user_name)

try:
	user = api.get_user(user_name) 
	ID = user.id_str 
	print("The user name has been taken")
	print("The ID of the user is : " + ID) 
except:
	print("The user name has not been taken and is free for usage")