import requests
import json
from pprint import pprint

q = """
{
  website(url: "https://lethain.com/migrations") {
    title
    image
    description
  }
}
"""

resp = requests.post("http://localhost:5000/", params={'query': q})
obj = json.loads(resp.text)
pprint(obj)
