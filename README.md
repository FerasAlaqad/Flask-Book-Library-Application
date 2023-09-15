
# Flask Book Library Application

**Description:** This is a Flask web application designed for managing a library book collection. It offers user authentication and comprehensive CRUD functionality for book management.

## Features

- **User Authentication:** Secure user login with password hashing and session management.
- **Book Database:** Store book data including title, author, year, and ISBN fields.
- **CRUD Operations:** Full CRUD functionality (Create, Read, Update, Delete) for books.
- **Responsive UI:** Stylish and responsive user interface with Bootstrap styling.
- **Database Backend:** Utilizes MySQL with SQLAlchemy ORM.
- **Modular Structure:** Organized with blueprints for a clean application structure.
- **Customization:** Easily customizable templates and static assets.
- **RESTful API:** Provides RESTful API endpoints for book-related operations.

## Getting Started Prerequisites

Before you begin, ensure you have the following prerequisites:

- Python 3.6+
- Pip
- MySQL

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/FerasAlaqad/Flask-Book-Library-Application.git
   cd flask-library
   
1. Install dependencies:

   ```shell
   pip install -r requirements.txt

## Usage

### Homepage

The homepage displays a list of all books. Users can either register for new accounts or log in to existing accounts.

### Logged In Users

Once logged in, users can perform the following actions:

- **View Book Details:** Users can view detailed information about each book by clicking on its title.

- **Add New Books:** Users can add new books to the library by providing title, author, year, and ISBN information.

- **Edit Book Information:** For books already in the library, users can edit their information, including title, author, year, and ISBN.

- **Delete Books:** Users can remove books from the library if they are no longer needed.

- **Logout:** Users can log out of their accounts securely.


## Built With

- Flask: Web framework
- Flask-SQLAlchemy: ORM
- MySQL: Database

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Additional References

For more examples and inspiration, you can also check out the following GitHub repositories:

1. [FerasAlaqad/MySQL_flask_library](https://github.com/FerasAlaqad/MySQL_flask_library)

2. [techwithtim/Flask-Web-App-Tutorial](https://github.com/techwithtim/Flask-Web-App-Tutorial)

For any inquiries or support, please contact [ferasdc18@gmail.com](mailto:ferasdc18@gmail.com).
