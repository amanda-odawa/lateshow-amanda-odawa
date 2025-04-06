# Lateshow API
A Flask API that tracks episodes, guests, and their appearances on the "Lateshow". This project is built using Flask, SQLAlchemy, and RESTful API principles to manage data related to TV show appearances.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Models](#database-models)
- [Seeding the Database](#seeding-the-database)
- [Contributing](#contributing)
- [License](#license)

## Features
- Create, Read, Update, and Delete (CRUD) operations for episodes and guests
- Link guests to episodes with appearances
- Track guest ratings for each appearance
- Input validations for ratings (1-5)

## Technologies Used
- Python
- Flask
- Flask-RESTful
- SQLAlchemy
- SQLite (default database)

## Installation
1. Fork and clone the repository, then navigate to it:
   ```sh
   git clone https://github.com/amanda-odawa/lateshow-amanda-odawa.git
   cd lateshow-amanda-odawa
   ```
2. Install dependencies using Pipenv:
   ```sh
   pipenv install
   ```
3. Activate the virtual environment:
   ```sh
   pipenv shell
   ```
4. Set up the database:
   ```sh
   flask db upgrade
   ```

## Usage
Run the Flask application:
```sh
python app.py
```
The API will be accessible at `http://127.0.0.1:5555/`.

## API Endpoints
| Method | Endpoint                | Description                  |
|--------|-------------------------|------------------------------|
| GET    | `/episodes`             | Get all episodes             |
| GET    | `/episodes/:id`         | Get an episode by ID         |
| GET    | `/guests`               | Get all guests               |
| POST   | `/appearances`          | Create a new appearance      |

## Database Models
- **Episode**: Represents an episode of the show with attributes like date and episode number.
- **Guest**: Represents a guest on the show with attributes like name and occupation.
- **Appearance**: Represents the relationship between a guest and an episode, including a rating (1-5) for the guest's appearance.

## Seeding the Database
To seed the database with sample data, run:
```sh
python seed.py
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
1. Fork the repository
2. Create a new branch 
    ```sh
    git checkout -b Your-Feature-Name
    ```
3. Make your changes
4. Commit changes 
    ```sh
    git commit -m 'Added new feature'
    ```
5. Push to GitHub 
    ```sh
    git push origin Your-Feature-Name
    ```
6. Submit a pull request

## License
This project is licensed under the MIT License.