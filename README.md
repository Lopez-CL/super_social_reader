# Super Social Reader
**Description**

A social reader tracker for superhero comic book readers to connect, discuss, and keep track of the comics they read.

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
