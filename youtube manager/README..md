# YouTube Video Database Manager

This project is a simple command-line application to manage a database of YouTube videos using SQLite. It allows you to list, add, update, delete, and search for videos.

## Features

- List all videos
- Add a new video
- Update an existing video
- Delete a video
- Search for a video by title

## Requirements

- Python 3.x
- SQLite

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/kamatealif/python_projects.git
    ```
2. Navigate to the project directory:
    ```sh
    cd youtube-video-manager
    ```

## Usage

Run the main script to start the application:
```sh
python main.py
```

follow the on-screen menu to perform various operations on the video database.

### datebase Schema
The `vidoes` table has the following columns:

* `id` : INTEGER PRIMARY KEY AUTOINCREMENET
* `title` : TEXT NOT NULL
* `description` : TEXT NOT NULL
* `date` : DATE DEFAULT CURRENT_DATE

---
## Example
1. <b>List all videos<b/>
```sh 
1. List All Videos
2. Add New Video
3. Update Video
4. Delete Video
5. Search Video
6. Exit
Enter your choice: 1
```

2. <b>Add New Video <b/>
```sh 
Enter your choice: 2
Enter the title: My First Video
Enter the description: This is a description of my first video.
Enter the date (YYYY-MM-DD) or leave blank for current date: 2023-10-01
```
3. <b>Update Video <b/>
```sh
Enter your choice: 3
Enter video ID to update: 1
Enter new title: My Updated Video
Enter new description: This is an updated description.
Enter new date (YYYY-MM-DD): 2023-10-02
```

4. <b>Update Video <b/>
```sh 
Enter your choice: 4
Enter video ID to delete: 1
```

5. <b>Delete Video <b/
```sh 
Enter your choice: 4
Enter video ID to delete: 1
```

6. <b>Search Video<b/
```sh 
Enter your choice: 5
Enter title to search: My First Video
```
---

## Notes 
This is a basic implementation and may not cover all edge cases. it is intended as a starting point for further development and improvment.
