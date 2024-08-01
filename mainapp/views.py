from django.shortcuts import render
from settings import API_KEY
import requests #for sending request



def index(request):

    BASE_URL ='http://api.weatherapi.com/v1'


    if request.method=='POST':
        city=request.POST.get('city').lower()
        print(city)

        if API_KEY == 'paste-your-api-key':
            print('Please add your generated API key into the "API_KEY" variable within the views.py')
            return render(request,'index.html',{'checker':'Please add your generated API key into the "API_KEY" variable within the views.py'})

        elif (city== ''):
            print('No value')
            return render(request,'index.html',{'checker':'Please enter valid info...!'})

        else:
            request_url = f"{BASE_URL}/current.json?key={API_KEY}&q={city}&aqi=no"  

            response = requests.get(request_url)

            if response.status_code == 200:
                data = response.json()
                # print(data)

                location=data['location']
                weather = data['current']
                # print(weather)
                print(location['tz_id'])
                print(weather['temp_c'])


                context = {
                    'weather':weather['temp_c'],
                    'city_name':location['name'],
                    'region':location['region'],
                    'country':location['country'],
                    'lat':location['lat'],
                    'lon':location['lon'],
                    'localtime':location['localtime'],
                    'continent':location['tz_id'],
                    'static_city':city
                }

                return render(request,'index.html', context)

            else:
                print("An error occurred")
                return render(request,'index.html',{'static_city':city,'checker':'Please enter valid city'})


    return render(request,'index.html',{})