import sqlite3
from datetime import datetime
connection = sqlite3.connect("youtube_video.db")

cursor = connection.cursor();

cursor.execute("""
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        date DATE DEFAULT CURRENT_DATE          
     )
""")

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    for video in videos:
        print(video)

def add_video(title, description,date=None):
    if date:
        # Ensure the date is in the Correct format
        date_part = datetime.strptime(date, "%Y-%m-%d").date()
        cursor.execute("INSERT INTO videos(title,description, date) values(?, ?, ?)", (title, description, date_part))
        connection.commit();
    else: 
        cursor.execute("INSERT INTO videos(title,description, date) values(?, ?, ?)", (title, description, date))
        connection.commit();

def update_video(video_id, new_title, new_description, new_date=None):
    
    # Ensure the date is in the Correct format
    new_formated_date = datetime.strptime(new_date, "%Y-%m-%d").date()
    cursor.execute("UPDATE videos SET title=?, description=?, date=? WHERE id=?", (new_title, new_description, new_formated_date,video_id))
    connection.commit();

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?", (video_id,))
    connection.commit();

def search_video(title):
    cursor.execute("SELECT * FROM videos WHERE title=?", (title,))
    videos = cursor.fetchall()
    if videos:
        for video in videos:
            print(video)
    else:
        print("No video found with title: ", title)



def menu():
    print("1. List All Videos")
    print("2. Add New Video")
    print("3. Update Video")
    print("4. Delete Video")
    print("5. Search Video")
    print("6. Exit")

def main():
    while 1:
        print("\n WELCOME TO YOUTUBE VIDEO DATABASE")
        menu();

        choice = input("Enter your choice: ")

        match choice:
            
            case '1':
                list_all_videos();
            case '2':
                title = input("Enter the title: ")
                description = input("Enter the description: ")
                date = input("Enter the time(YYYY-MM-DD) OR leave blank for current date: ")  
                add_video(title, description,date if date else None);
            case '3':
                video_id = input("Enter video ID to update: ")
                new_title = input("Enter new title: ")
                new_description = input("Enter new description: ")
                new_date = input("Enter new time (YYYY-MM-DD): ")
                update_video(video_id, new_title, new_description, new_date if new_date else None);
            case '4':
                video_id = input("Enter video ID to update: ")
                delete_video(video_id)
            case '5':
                title = input("Enter title to search: ")
                search_video(title)
            case '6':
                exit()
            case _:
                print("Invalid choice")
    connection.close();

if __name__ == '__main__':
    main();