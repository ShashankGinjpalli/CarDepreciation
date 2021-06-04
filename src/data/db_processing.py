from pymongo import MongoClient
from pprint import pprint


class databaseConnector:
    # connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['CarData']
    listings_collections = db['listings_collections']
    serverStatusResult = db.command("serverStatus")
    # pprint(serverStatusResult)

    #db = client.business

    def upload_listing(self, listing_element):
        #print(listing_element)
        try:
            #obj_dict = self.slotted_to_dict(listing_element)
            result = self.listings_collections.insert_one(
                listing_element.to_dict())
            #print(result.inserted_id)
        except Exception as e:
            print("uhoh " + str(e))

    def slotted_to_dict(obj):
        return {s: getattr(obj, s) for s in obj.__slots__ if hasattr(obj, s)}
