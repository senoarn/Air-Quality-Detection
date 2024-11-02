import random
import json
from tkinter import Tk, Label, CENTER
from paho.mqtt import client as mqtt_client

broker = 'localhost'
port = 1883
topic = "air_quality"
client_id = f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n" % rc)

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)  # Uncomment and provide credentials if authentication is required
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def on_message(client, userdata, msg):
    _data = json.loads(msg.payload.decode())
    temp = str(_data["parameters"]["temp"])
    temp_label.config(text=temp + " %", fg="black")

client = connect_mqtt()

# Create Tkinter window
window = Tk()
window.title("MQTT Temperature Monitor")

# Create label for displaying temperature
temp_label = Label(window, text="", bg="white", fg="black", font=("Helvetica", 100))
temp_label.place(x=250, y=320, anchor=CENTER)

# Subscribe to MQTT topic and set the on_message callback
client.subscribe(topic)
client.on_message = on_message

# Start the MQTT client loop in a separate thread
client.loop_start()

# Start the Tkinter main loop
window.mainloop()

# Stop the MQTT client loop when the Tkinter window is closed
client.loop_stop()
