from flask import Flask, redirect, url_for, render_template, request



from bs4 import BeautifulSoup
import requests
import json
from datetime import date
f=Flask(_name_)
@f.route("/")

def covid():
    return render_template('covid.html')

@f.route('/', methods=['GET'])

def getvalue():
    pin=request.form['Enter Your Pincode:']
    #getting date
    today = date.today()
    date = today.strftime("%d/%m/%Y").replace("/","-")
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date='.format(pin)+date
    request = requests.get(url).text
    soup = BeautifulSoup(request, 'lxml')
    sessions = json.loads(soup.p.text)
    
    #preference=input("What would you prefer : ")
    #Checkbox for options between Covaxin,Covishield,Any
    
    print("Availabilites on", date, "\n\n")
    
    #checking for availabilites on specific day
    i=1
    
    if len(sessions["sessions"])==0:
        print("No Availabilites Today")
        
    else:
        for a in sessions["sessions"]:
            print("CENTER", i)
            print("\n")
            result=availability(a)
            print("\n\n")
            i+=1
    return render_template('covid.html', result)
    


#function to parse through details of available centers
def availability(data):
    print("Center Name       : ", data["name"])
    if data["block_name"]=="Not Applicable":
        print("Address           : ", data["address"])
    else:
        print("Address           : ", data["address"], ", ", data["block_name"])
    print("Timings           : ", data["from"], " to ", data["to"])
    if data["fee"]=="0":
        print("Fee               :  Free")
    else:
        print("Fee               : ", data["fee"])
    print("Minimum Age Limit : ", data["min_age_limit"])
    print("Vaccine           : ", data["vaccine"])
    print("\nSlots")
    result=[]

    for a in data["slots"]:

        result.append(a)
        
    return result