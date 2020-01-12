import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://user:NmpeiIjEszTFpxoN@cluster0-qx6fz.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client.test

mydb = client['unencryptedsecrets']
myuser = mydb['user']


def addUser(firstname, lastname, reddit_name):
    x = None
    mydict = {
        'name': firstname + ' ' + lastname,
        'reddit_name': reddit_name,
        'diary_entries': [],
        'character': {
            'skills': {
                'fitness': {
                    'level': 0,
                    'exp': 0,
                    'next_level_exp': 0
                },
                'academics': {
                    'level': 0,
                    'exp': 0,
                    'next_level_exp': 0
                },
                'career': {
                    'level': 0,
                    'exp': 0,
                    'next_level_exp': 0
                },
                'social': {
                    'level': 0,
                    'exp': 0,
                    'next_level_exp': 0
                }
            }
        },
        'reddit_content': []
    }
    x = myuser.insert_one(mydict)

    return x


def getRedditContent(obj):
    myquery = {
        'reddit_name': obj['reddit_name']
    }
    myuser.update_one(myquery, {'$set': {'reddit_content': obj['reddit_content']}})


def updateUser(name, character):
    myuser.update_one({'name': name}, {'$set': {'character': character}})


def addDiaryEntry(name, diary_entry):
    person = myuser.find_one({'name': name})
    person['diary_entries'].append(diary_entry)
    myuser.update_one({'name': name}, {'$set': {'diary_entries': person['diary_entries']}})

addUser('test', 'test', 'test')
addUser('test', 'test', 'test')
