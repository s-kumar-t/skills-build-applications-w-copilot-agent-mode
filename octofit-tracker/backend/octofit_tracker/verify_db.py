from pymongo import MongoClient

def verify_collections():
    client = MongoClient('localhost', 27017)
    db = client['octofit_db']

    collections = ['users', 'teams', 'activity', 'leaderboard', 'workouts']

    for collection in collections:
        print(f"\nContents of {collection} collection:")
        documents = list(db[collection].find())
        for doc in documents:
            print(doc)

if __name__ == "__main__":
    verify_collections()
