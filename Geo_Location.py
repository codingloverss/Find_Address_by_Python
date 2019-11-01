import requests
def get_location():
    data=requests.get("http://ip-api.com/json/").json()
    address={}
    address['country']=data['country']
    address['state']=data['regionName']
    address['city']=data['city']
    address['zip']=data['zip']
    address['latitude']=data['lat']
    address['longitude']=data['lon']
    address['isp']=data['isp']
    address['ip']=data['query']
    return address
if __name__=="__main__":
    print(get_location())