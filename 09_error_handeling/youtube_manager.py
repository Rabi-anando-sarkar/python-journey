import json

def load_data():
    try:
        with open('youtube.json','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def sav_data_helper(videos):
    with open('youtube.json', "w") as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print('\n')
    print('*' * 50)
    for index,video in enumerate(videos, start=1):
        print('\n')
        print(f"{index} : Title : {video['name']} , Duration : {video['time']}")
 
def add_video(videos):
    name = input("Enter Video Name: ")
    time = input("Enter Video Time: ")
    videos.append({'name' : name, 'time' : time})
    sav_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the Video Number to Update : "))
    
    if 1 <= index <= len(videos):
        name = input("Enter the New Video Title : ")
        time = input("Enter the New Video Duration : ")
        videos[index-1] = {'name' : name, 'time': time}
        sav_data_helper(videos)
    else:
        print("Invalid Index Selected.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the Video Number to Delete : "))
    
    if 1 <= index <= len(videos):
        del videos[index-1]
        sav_data_helper(videos)
    else:
        print("Invalid Index Selected.")

def main():
    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose an option ")
        print("\n 1. List all Youtube videos ")
        print("\n 2. Add a Youtube video ")
        print("\n 3. Update a Youtube video details")
        print("\n 4. Delete a Youtube video ")
        print("\n 5. Exit the app \n")
        
        choice = input("Enter your Choice : ")
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print(f"{choice} is an Invalid input")
                
if __name__ == "__main__":
    main() 
        