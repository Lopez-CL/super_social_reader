# Super Social Reader
**Description**

A social reader tracker for superhero comic book readers to connect, discuss, and keep track of the comics they read. View video (demo of app)[https://drive.google.com/file/d/1SumQ-Uel-pAWqaXZRLFvE2EYTPzcH7ep/view?usp=sharing]

- Designed front-end with custom CSS and libraries ( jQuery & Bootstrap) to create dynamic, responsive modern web experience.
- Employed werzeug library to handle secure image file uploads to personalize user profile and comic book cover art.
- Optimized SQL query logic on the back-end to ensure responsive, customized user experience when viewing, rating, and creating comics.
- Utilized many-to-many relationship in database to allow for commenting on specific comics.
Leveraged the (superheroapi.com)[https://superheroapi.com/index.html] REST API to offer user suggestions on where to start reading for a character.


## Controller Routes
### Users
| Type | Path | Notes
| ------- | ------- | ------- |
| GET | / | Renders index.html |
| GET | /registration | Renders register.html |
| POST | /register | creates user data |
| POST | /login | sends user data |
| POST | /upload/page | sends user image data |
### Comics
| Type | Path | Notes
| ------- | ------- | ------- |
| GET | /dashboard | renders dashboard.html |
| GET | /add/comic | renders add_comic.html |
| GET | /comic/<int:id> | renders current_read.html |
| GET | /update/comic/<int:id> | enders update_comic.html |
| GET | /characters | renders character.html |
| POST | /create/comic | sends comic data |
| PUT | /update/<int:id> | updates comic data |
| DELETE | /delete/comic/<int:id> | deletes comic data |
### Comments
| Type | Path | Notes
| ------- | ------- | ------- |
| POST | /comment/<int:id> | creates comment data |
