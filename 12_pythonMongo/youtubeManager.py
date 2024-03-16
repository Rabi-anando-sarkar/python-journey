from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubeManager:youtubeManager@side-project-database.o2kgdee.mongodb.net/")

db = client["ytManager"]
video_collection = db["videos"]

def list_videos():
    for video in video_collection.find():
        print(f"Id : {video['_id']} Name : {video['name']} Time : {video['time']}")

def add_video(name,time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(_vId,new_name,new_time):
    video_collection.update_one(
        {
            '_id': ObjectId(_vId)
        },
        {
            "$set": {
                "name" : new_name,
                "time" : new_time
            }   
        }
    )

def delete_video(_vId):
    video_collection.delete_one({
        '_id' : ObjectId(_vId)
    })

def main():
    while True:
        print("Youtube Manager App")
        print("1. List all videos")
        print("2. Add new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        
        choice = input("Enter Your Choice : ")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter Video Name : ")
            time = input("Enter Video Time : ")
            add_video(name,time)
        elif choice == '3':
            _vId = input("Enter Video Id : ")
            new_name = input("Enter Updated Video Name : ")
            new_time = input("Enter Updated Video Time : ")
            update_video(_vId,new_name,new_time)
        elif choice == '4':
            _vId = input("Enter Video Id : ")
            delete_video(_vId)
        elif choice == '5':
            break
        else:
            print("Invalid Choice!")
        

if __name__ == "__main__":
    main()
