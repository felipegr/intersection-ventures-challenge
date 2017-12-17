# Intersection Ventures Challenge
The challenge was to implement a very simple web application for listing, creating and deleting Tutors.
The web app should also implement an API.

## Instalation instructions
- Install `SQLite` (for example in Ubuntu run `sudo apt-get update` and then `sudo apt-get install sqlite3 libsqlite3-dev`)
- Clone this repo
- (Optionally) Create a virtual environment
- Install the requirements running `pip install -r requirements.txt`
- Create the database running `python manager.py init_db`
- Run the application with `python app.py`

The application is set to run at `http://localhost:8080`

## API
The API base URL is `http://localhost:8080/api`

### Enpoints

- **GET `/api/tutors`**: retrieves all the Tutors
- **GET `/api/tutors/<id>`**: retrieves a specific Tutor identified by `<id>`
- **POST `/api/tutors`**: creates a Tutor, must receive a json in the body of the request in the format `{"name": "Tutor Name", "document_no": "Document number"}`
- **PUT `/api/tutors`**: updates a Tutor, must receive a json in the body of the request in the format `{"name": "Tutor Name", "document_no": "Document number"}` (at least one field must be present)
- **DELETE `/api/tutors/<id>`**: deletes a Tutor
