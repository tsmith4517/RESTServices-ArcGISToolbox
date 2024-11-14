from arcgis.auth import ArcGISProAuth
from arcgis.gis import GIS
import urllib3
import json

def generateToken(url, username, password):
    if url.lower() == "pro":
        token = ArcGISProAuth().token

    elif username and password:
        http = urllib3.PoolManager()
        token_POSTdata = {'username':username,'password':password}
        response = http.request("POST", 
                                "https://www.arcgis.com/sharing/generateToken?f=json&referer=https://www.arcgis.com",
                                fields=token_POSTdata)
        
        token_response = json.loads(response.data.decode("utf-8"))
        token = token_response.get("token")

        # gis = GIS(url, username, password)
        # token = gis.session.auth.token

    else:
        token = ""

    return token


