from configparser import ConfigParser
from turtle import width
import requests
import tkinter as tk

root = tk.Tk()

root.title("AQI Tracker")
root.geometry("700x700")
root.configure(bg='light blue') 
#AQI 
def get_aqi(world):
    city = textbox1.get()
    print(city)
    key='37f96394ffe8b6cca1110af3d8270604c711c688'
    url='http://api.waqi.info/feed/' + city + '/?token='
    main_url = url + key  # Main URL
    r = requests.get(main_url)  # Accessing the URL
    data = r.json()['data']  # Fetching data in variable
    aqi = data['aqi']  # Air quality Index

    air_label['text'] = aqi
   
#weather 
def get_weather(city):
    city = textbox1.get()
        
    url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    config_file="config.ini" 
    config=ConfigParser()
    config.read(config_file)
    api=config['api_key']['key']
    result=requests.get(url.format(city,api))
    if result:
        json=result.json()
        
        city=json['name']
        country=json['sys']['country']
        condition = json['weather'][0]['description']
        temp_kelvin=json['main']['temp']
        temp_cel = temp_kelvin - 273.15
        temp_far = (temp_kelvin - 273.15) * 9/5 + 32
        air_label['text'] = city
        air_label1['text'] = country
        air_label2['text'] = condition
        air_label4['text'] = temp_far
 
textbox1 = tk.Entry(root,font=('times new roman',20),width=40)
textbox1.place(x = 200 , y=90 , width=300 , height=60)

button1 = tk.Button(root,text='AQI',fg='blue',font=('times new roman',18),width=8,command=lambda: get_aqi(textbox1.get()))
button1.place(x = 150 , y= 200 , width=200 , height=60)

button2 = tk.Button(root,text='weather',fg='blue',font=('times new roman',18),width=10,command=lambda: get_weather(textbox1.get()))
button2.place(x = 350 , y= 200 , width=200 , height=60)

air_label=tk.Label(root,text="",font=('times new roman',18),width=40)
air_label.place(x = 200 , y= 300 , width=150 , height=50)

air_label1=tk.Label(root,text="",font=('times new roman',18),width=40)
air_label1.place(x = 200 , y= 400 , width=150 , height=50)

air_label2=tk.Label(root,text="",font=('times new roman',18),width=40)
air_label2.place(x = 200 , y= 500 , width=150 , height=50)

air_label4=tk.Label(root,text="",font=('times new roman',18),width=40)
air_label4.place(x = 200 , y= 600 , width=200 , height=50)
root.mainloop()