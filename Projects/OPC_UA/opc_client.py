from opcua import Client
import time

# server IP 
url = "opc.tcp://192.168.56.1:4840"
client = Client(url)
client.connect()
print("Client Connected")

while True:
    Temp = client.get_node("ns=2; i=2")
    Temperature = Temp.get_value()
    print(f"Temperature: {Temperature}")

    Press = client.get_node("ns=2; i=3")
    Pressure = Temp.get_value()
    print(f"Pressure: {Pressure}")

    TIME = client.get_node("ns=2; i=4")
    TIME_value = Temp.get_value()
    print(f"TIME_value: {TIME_value}")
    print("\n*************\n")

    time.sleep(1)