import re
import csv
from time import sleep
import os
import sys
import pathlib
from timeit import default_timer as timer
import datetime



import urllib3
import instaloader



L = instaloader.Instaloader()
print("Dev by SaJaD_Fx")
print(" ")
print("Login to instagram")
print(" ")
instauser = input("UserName : ")
instapass = input("Password : ")

L.login(instauser, instapass)    

pathlib.Path('downloads/').mkdir(parents=True, exist_ok=True)

f = open('input.txt','r')
accounts = f.read()
p = accounts.split("\n")


PROFILE = p[:]

for ind in range(len(PROFILE)):
    pro = PROFILE[ind]
    try:
        print(f"Starting Getting Followers From {pro}")

        filename = 'downloads/'+pro+'.txt'
       
        profile = instaloader.Profile.from_username(L.context, pro)
        for person in profile.get_followers():
            try:
                
                username = person.username

                print('Username:',username)
                
                with open(f'{filename}','a+') as File:
                    File.write(f"{username}\n")
                
            except Exception as e:
                print(e)
                
            
    except:
        print('Skipping',pro)
