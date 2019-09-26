# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:59:08 2019

@author: Ajay_Rana
"""
#
def get_lat_lon(apiKey, address):
    """
   
    """
    import requests
    
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'
           .format(address.replace(' ','+'), apiKey))
    
    response=requests.get(url) 

    resp_json = response.json()
    
    lat = resp_json['results'][0]['geometry']['location']['lat']
    lng = resp_json['results'][0]['geometry']['location']['lng']
    #print(resp_json_payload)
   

    return lat, lng

def get_state_name(lat, lon):
    import psycopg2

    conn = psycopg2.connect(database = "postgis_25_sample", user = "postgres", password = "xxxxxxxx", host = "127.0.0.1", port = "5432")
    print ("Opened database successfully")

    cur = conn.cursor()
    
    select_Query=("select name "
    "from public.tl_2019_us_state "
    "where intptlat='{0}' "
    "and intptlon='{1}'").format(str(lat), str(lon))
        
    cur.execute(select_Query)

    rows = cur.fetchall()
    for row in rows:
       print ("name = ", row[0], "\n")

    
    print ("Operation done successfully");
    conn.close()


if __name__ == '__main__':

    apiKey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

    # get coordinates 
    address = 'Stoney Creek Rd, Sutton, WV 26601'
    lat, lon = get_lat_lon(apiKey, address)
    print('{} Coordinates:\nLatitude:  {}°\nLongitude: {}°'.format(address,lat, lon))
    get_state_name(lat, lon)
    get_state_name('+38.6472854', '-080.6183274')

    