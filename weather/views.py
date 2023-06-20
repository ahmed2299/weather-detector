from django.shortcuts import render
import json
import urllib.request

# Create your views here.

def index(request):
    city = ''
    data = {}
    if request.method=='POST':
        city=request.POST['city']
        if str(city)!='':
            try:
                res=urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?q={str(city)}&APPID=0cc67c653737634e577f30d9ea84a33f').read()
                json_data=json.loads(res)
                data={
                    'country_code':str(json_data['sys']['country']),
                    'coordinate':str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
                    'temp':str(json_data['main']['temp'])+' k',
                    'pressure':str(json_data['main']['pressure']),
                    'humidity':str(json_data['main']['humidity'])
                }
            except:
                return render(request, 'index.html', {'city': '', 'data': {}})

    return render(request, 'index.html', {'city': city, 'data': data})