
from azure.cosmos import CosmosClient, partition_key

#keys
URL = 'ADD URI HERE'
KEY = 'ADD KEY 1 FROM COSMOS DB HERE'


#creating the client to interact with CosmosDB
client = CosmosClient(URL, credential=KEY)
DATABASE_NAME = 'ResumeCounterBase' # name of the data base
database = client.get_database_client(DATABASE_NAME)  #gets the database via APi
CONTAINER_NAME = 'CounterContainer'
container = database.get_container_client(CONTAINER_NAME)
ITEM_ID = 'item2' #the item i want to change 

item = container.read_item(ITEM_ID,partition_key='newpart') # reading the item

item['count'] += 1 #  increasing the current count of the database item

container.replace_item(ITEM_ID, item) # replacing the old count with the new and updating the database










# can read and print the current item 
"""
for item in container.query_items(
        query='Select * FROM mycontainer r WHERE r.id="item1"',
        enable_cross_partition_query=True):
  print(json.dumps(item, indent=True))
"""


