import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://user:NmpeiIjEszTFpxoN@cluster0-qx6fz.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

mydb = client['unencryptedsecrets']
myuser = mydb['user']


def addUser(firstname, lastname, reddit_name):
    mydict = {
        'name': firstname + ' ' + lastname,
        'reddit_name': reddit_name
    }
    x = myuser.insert_one(mydict)


def getRedditContent(obj):
    myquery = {
        'reddit_name': obj['reddit_name']
    }
    myuser.update_one(myquery, obj['content'])
