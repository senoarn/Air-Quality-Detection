import random
import json
from tkinter import Tk, Label, PhotoImage, Canvas, LEFT, RIGHT, CENTER
from paho.mqtt import client as mqtt_client

broker = '0.tcp.ap.ngrok.io'  # Replace with your ngrok MQTT broker address
port = 15204  # Replace with the ngrok port
topic = "air_quality"  # Replace with the topic used by your ESP32
client_id = f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            client.subscribe(topic)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def on_message(client, userdata, msg):
    _data = json.loads(msg.payload.decode())
    
    # Convert float values to integers
    temp = str(int(_data["Temperature"])) + " °C"
    humidity = str(int(_data["Humidity"])) + " %"
    gas_value = str(int(_data["GasValue"]))
    air_quality = _data["AirQuality"]

    # Display only the numeric values
    temp_label.config(text=temp, fg="black")
    hum_label.config(text=humidity, fg="black")
    gas_label.config(text=gas_value, fg="black")
    air_quality_label.config(text=air_quality, fg="black")


def on_closing(client, window):
    print("Closing the window and stopping MQTT loop")
    client.loop_stop()
    window.destroy()

# Create Tkinter window
window = Tk()
window.title("MQTT Sensor Monitor")
window.geometry('760x470')  # Width, Height
window.resizable(False, False)  # Width, Height
window.configure(bg="white")

# Set background image
img_header = PhotoImage(file="dashboard_v2.png")
background_label = Label(window, image=img_header)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Label temperature (Temperature)
temperature_label = Label(window,
                         text="TEMPERATURE",
                         bg="white",
                         fg="black",
                         font=("Helvetica", 12),
                         justify='center')  # Center the text
temperature_label.place(x=47, y=140)

# Temperature
temp_label = Label(window,
                   text="",
                   bg="white",
                   fg="black",
                   font=("Helvetica", 30),
                   justify=LEFT)
temp_label.place(x=62, y=200)

# Label Kelembapan (Humidity)
kelembapan_label = Label(window,
                         text="KELEMBAPAN",
                         bg="white",
                         fg="black",
                         font=("Helvetica", 12),
                         justify='center')  # Center the text
kelembapan_label.place(x=230, y=140)

# Humidity
hum_label = Label(window,
                  text="",
                  bg="white",
                  fg="black",
                  font=("Helvetica", 30),
                  justify='center')  # Center the text
hum_label.place(x=240, y=200)

# Label Gas (Gas)
gas_label = Label(window,
                         text="GAS",
                         bg="white",
                         fg="black",
                         font=("Helvetica", 12),
                         justify='center')  # Center the text
gas_label.place(x=445, y=140)

# Gas 
gas_label = Label(window,
                  text="",
                  bg="white",
                  fg="black",
                  font=("Helvetica", 30),
                  justify='center')
gas_label.place(x=452, y=200)

# Label Air Quality (Air Quality)
air_quality = Label(window,
                         text="AIR QUALITY",
                         bg="white",
                         fg="black",
                         font=("Helvetica", 12),
                         justify='center')  # Center the text
air_quality.place(x=600, y=140)

# Air Quality
air_quality_label = Label(window,
                          text="",
                          bg="white",
                          fg="black",
                          font=("Helvetica", 30),
                          justify='center')  # Center the text
air_quality_label.place(x=600, y=200)

# Subscribe to MQTT topic and set the on_message callback
client = connect_mqtt()
client.on_message = on_message

# Start the MQTT client loop
client.loop_start()

# Start the Tkinter main loop
window.protocol("WM_DELETE_WINDOW", lambda: on_closing(client, window))
window.mainloop()
