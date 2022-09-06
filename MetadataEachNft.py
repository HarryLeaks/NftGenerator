import json

#### Generate Metadata for each Image    
f = open('./metadata/all-traits.json',) 
data = json.load(f)

# Changes this IMAGES_BASE_URL to yours 
IMAGES_BASE_URL = "https://gateway.pinata.cloud/ipfs/QmVH9K9YsXdi1QHtDNkWnxRnNLx8uiVJwn6aMBvDtF4rrA/"
PROJECT_NAME = "CryptoSperms"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URL + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("cor", i["cor"]))
    token["attributes"].append(getAttribute("cauda", i["cauda"]))
    token["attributes"].append(getAttribute("boca", i["boca"]))
    token["attributes"].append(getAttribute("chapeu", i["chapeu"]))
    token["attributes"].append(getAttribute("nariz", i["nariz"]))
    token["attributes"].append(getAttribute("olhos", i["olhos"]))
    token["attributes"].append(getAttribute("orelhas", i["orelhas"]))


    with open('./metadata/' + str(token_id) + ".json", 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()