from sqlite3 import Time
import time
import paho.mqtt.client as mqtt
from geopy.geocoders import Nominatim
from flask import Flask, render_template
import folium
import smtplib,ssl
import string as str



def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg


client = mqtt.Client("C2")  # Create instance of client with client ID “C2”

client.connect('mqtt.eclipseprojects.io') # Connect to (broker)
client.loop_start()  # Start networking daemon
client.subscribe("T1")
client.on_message = on_message  # Define callback function for receipt of a message
time.sleep(5)
port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "m.bendaoud@esi-sba.dz"
receiver_email = "m.laroui@esi-sba.dz"
password = "Benmoham2020"
geolocator = Nominatim(user_agent="myapp")
location = geolocator.reverse("35.2101093,-0.6298645")
adr=location.address
print(adr)
context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    #server.login(sender_email, password)
    #server.sendmail(sender_email, receiver_email,str(adr))

m = folium.Map(location=[35,-0.5], tiles="OpenStreetMap", zoom_start=10)
marker = folium.Marker(
    location=['35.2096271','-0.6303473'],popup=adr)
marker.add_to(m)

m.save('templates/map.html')
app = Flask(__name__)
@app.route('/')
def onclick():
 return render_template("frontend.html")

@app.route('/maplocation')
def maplocation():
  return render_template("map.html")

if __name__ == '__main__':
 app.run()