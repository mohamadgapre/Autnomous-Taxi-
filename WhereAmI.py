import json
from urllib import request

# Server details will change between lab, home, and competition, so saving them somewhere easy to edit
server_ip = "?.?.?.?"
server = f"http://{server_ip}:5000"
authKey = "30"  # For the lab, your auth key is your team number, at competition this will be a secret key
team = 30

# Get the last reported vehicle position
res = request.urlopen(server + f"/WhereAmI/{team}")
if res.status == 200:
    data = json.loads(res.read())
    position = data[0].get("position")
    if position:
        print("Vehicle Position:")
        print(f"  X: {position['x']}, Y: {position['y']}")
        print(f"  Last Update: {data[0]['last_update']}")
    else:
        print("No position data available.", data[0]["message"])