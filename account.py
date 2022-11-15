from bson.objectid import ObjectId
import certifi
import pymongo

cluster = "mongodb+srv://spuddb:Recneps11db@accounts.wpmjif9.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(cluster, tlsCAFile=certifi.where())
db = client.accounts
print(client.list_database_names())
print(db.list_collection_names())
users = db.users



def create(username, password):
    user = {
    "username":username,
    "password":password
    }

    users.insert_one(user)
    
def find(username):
    query = users.find_one({ "username":username})
    return query

def login(username, password):
    query = users.find_one({ "username":username, "password":password})
    return query

def delete(username, password):
    users.delete_one({ "username":username, "password":password})
    
def update_username(username, new_username):
    users.update_one({"username":username}, {"$set": {"username":new_username} })

def update_password(username, password, new_pass):
    users.update_one({"username":username, "password":password}, {"$set": {"password":new_pass} })

#  count documents
# print(users.count_documents({}))