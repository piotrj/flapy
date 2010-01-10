import urllib
import json
def getEntries(user):
  url = "http://api.flaker.pl/api/html:false/type:friends/login:"+user+"/tag:all/mode:raw/comments:false"
  connection = urllib.urlopen(url)
  response = connection.read()
  entries = json.loads(response)
  
  return entries