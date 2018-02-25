subscription_key = "492e92ef6681492191b5f5378abcae1d"
assert subscription_key

vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
_maxNumRetries = 10

vision_analyze_url = vision_base_url + "analyze"
import json
import requests

headers  = {'Ocp-Apim-Subscription-Key': subscription_key }
params   = {'visualFeatures': 'Categories, Description, Color'} #changeable




#image_url = 'https://cdn.images.express.co.uk/img/dynamic/109/590x/hog-694202.jpg' 

def cogv_get_info(image_url):
    data     = {'url': image_url}
    response = requests.post(vision_analyze_url, headers=headers, params=params, json=data)
    print ("RESPONSE: ")
    print (response.json())
    response.raise_for_status()
    analysis = response.json()
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    image_tags = analysis["description"]["tags"]
    return image_caption, image_tags
#print(analysis)
#print(image_caption)

