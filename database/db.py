import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://user:NmpeiIjEszTFpxoN@cluster0-qx6fz.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

mydb = client['unencryptedsecrets']
myuser = mydb['user']


def addUser(firstname, lastname, reddit_name):
    mydict = {
        'name': firstname + ' ' + lastname,
        'reddit_name': reddit_name,
        'diary_entries': [],
        'character': {
            'name': '',
            'skills': {
                'fitness': {
                    'level': 0,
                    'exp': 0,
                    'next_level_exp': 0
                },
                'academics': {}
            }
        },
        'reddit_content': []
    }
    x = myuser.insert_one(mydict)


def getRedditContent(obj):
    myquery = {
        'reddit_name': obj['reddit_name']
    }
    myuser.update_one(myquery, obj['reddit_content'])


