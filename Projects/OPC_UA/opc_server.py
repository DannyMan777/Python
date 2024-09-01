from opcua import Server
import random
import datetime
import time

# Server Configuration Data
server = Server()
url = "opc.tcp://192.168.56.1:4840"
server.set_endpoint(url)
name = "OPCUA_SIM_SERVER"
add_space = server.register_namespace(name)
node =  server.get_objects_node()
Param = node.add_object(add_space, "Parameters")

# Parameters
Temp  = Param.add_variable(add_space, "Temperature", 0)
Press = Param.add_variable(add_space, "Pressure", 0)
Time  = Param.add_variable(add_space, "Time", 0)

Temp.set_writable()
Press.set_writable()
Time.set_writable()

# Server Start
server.start()
print(f"Server started at {url}")

while True:
    # generate random values for the Parameters
    Temperature = random.randint(10, 50)
    Pressure = random.randint(200, 999)
    TIME = datetime.datetime.now()

    print(f"Temperature: {Temperature} \nPressure: {Pressure} \nTime: {TIME}\n\n")

    Temp.set_value(Temperature)
    Press.set_value(Pressure)
    Time.set_value(TIME)

    time.sleep(2)

