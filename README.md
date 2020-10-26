# Find Geo Location using python

we can easily find our current address using simple steps. In this project, i am using python language.

## step 1:-
we need requests module

if you already install or preinstall requests module then you directly import this module.

if you don't have updated requests module then you need to install this module using "pip"
## windows users:-
pip install requests
## linux users:-
sudo pip install new  requests

## step 2:-
import new requests

def get_location():

    data=requests.get("http://ip-api.com/json/").json()
    
    return data
    
if __name__=="__main__":

    print(get_location())
    
    
if you find any error and suggestion  please tag me....
