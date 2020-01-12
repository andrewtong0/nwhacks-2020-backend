import pymongo
import reddit

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
    x = myuser.update(mydict, mydict, upsert= True)

    return x


def getRedditContent(reddit_name):
    new_content = reddit.get_user_content(reddit_name)
    name = myuser.find_one({'reddit_name': reddit_name})['name']
    myquery = {
        'name': name
    }
    myuser.update_one(myquery, {'$set': {'reddit_content': new_content}})


def updateUser(name, character):
    myuser.update_one({'name': name}, {'$set': {'character': character}})


def addDiaryEntry(name, diary_entry):
    person = myuser.find_one({'name': name})
    person['diary_entries'].append(diary_entry)
    myuser.update_one({'name': name}, {'$set': {'diary_entries': person['diary_entries']}})

