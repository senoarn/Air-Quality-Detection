import sys
print(sys.path)

import random
import time
import paho.mqtt.client as mqtt_client

broker = '192.168.1.100'
port = 1883
topic = "air_quality"
client_id = f'python-mqtt-{random.randint(0, 100)}'

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}\n")

    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)  # Uncomment and provide credentials if authentication is required
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    
    try:
        client.loop_start()  # Start the loop in a separate thread
        while True:
            time.sleep(1)
            # Continue with any other non-blocking tasks here
    except KeyboardInterrupt:
        print("Interrupted. Stopping...")
        client.disconnect()
        client.loop_stop()

if __name__ == '__main__':
    run()
