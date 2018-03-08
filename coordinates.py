import subprocess
import json
add = raw_input()
command = "curl https://maps.googleapis.com/maps/api/geocode/json?address="+add.replace(" ","+")+"&key=AIzaSyCRVnX1xe1phL8ZSKd7-dv5nJK5pYBiAE8"
output = subprocess.check_output(command, shell=True)
array = json.loads(output)
print("Latitude:")
print(array['results'][0]['geometry']['location']['lat'])
print("Longitude:")
print(array['results'][0]['geometry']['location']['lng'])

