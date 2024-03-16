import sqlite3

con = sqlite3.connect("yt_videos.db")

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )               
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name,time))
    con.commit()

def update_video(video_id, newName, newTime):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (newName,newTime,video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    con.commit()

def main():
    videos = []
    
    while True:
        print("\n Youtube Manager App DB")
        print("\n 1. List all Youtube videos ")
        print("\n 2. Add a Youtube video ")
        print("\n 3. Update a Youtube video details")
        print("\n 4. Delete a Youtube video ")
        print("\n 5. Exit the app \n")
        
        choice = input("Enter Your Choice : ")
        
        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter the Video Name : ")
            time = input("Enter the Video Time : ")
            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter Video id to Update : ")
            name = input("Enter the Video Name : ")
            time = input("Enter the Video Time : ")
            update_video(video_id,name,time)
        elif choice == '4':
            video_id = input("Enter Video id to Delete : ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            
            print("Invalid Choice!")
        
    con.close()


if __name__ == "__main__":
    main()
    
