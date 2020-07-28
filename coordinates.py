import subprocess
import json
add = raw_input()
command = "curl https://maps.googleapis.com/maps/api/geocode/json?address="+add.replace(" ","+")+"&key=<ENTER_YOUR_API_KEY>"
output = subprocess.check_output(command, shell=True)
array = json.loads(output)
print("Latitude:")
print(array['results'][0]['geometry']['location']['lat'])
print("Longitude:")
print(array['results'][0]['geometry']['location']['lng'])
