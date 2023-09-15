import pytankerkoenig
import datetime
from datetime import *
from config import *
import json
data = pytankerkoenig.getNearbyStations(API_KEY,'52.4819479','13.3213254','4','all','dist')

# Serializing json
json_object = json.dumps(data, indent= 4)
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# Writing to sample.json
with open(f"data/tankstellen_price_Stand_{current_time}.json", "w") as outfile:
    outfile.write(json_object)
