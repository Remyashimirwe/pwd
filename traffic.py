import time

def traffic_light_simulation():
    while True:
        print("Light is RED 🔴 - Stop!")
        time.sleep(1)   # Red light stays on for 5 seconds

        print("Light is YELLOW 🟡 - Get Ready!")
        time.sleep(1)   # Yellow light stays on for 2 seconds

        print("Light is GREEN 🟢 - Go!")
        time.sleep(1)   # Green light stays on for 5 seconds

        print("Light is YELLOW 🟡 - Get Ready!")
        time.sleep(1)   # Yellow light stays on for 2 seconds

# Start the simulation
traffic_light_simulation()
