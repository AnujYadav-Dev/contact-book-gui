
# Contact Book - GUI Application

This is a **Graphical User Interface (GUI) Contact Book Application** built using **Python**, **Tkinter**, and **SQLite3**. The Contact Book allows users to manage contact information such as names, phone numbers, emails, and addresses. It features a clean and responsive interface using Tkinter, and the contact data is stored locally in an SQLite database.

## Features

- **Add New Contact**: Add a new contact with fields for name, phone number, email (optional), and address (optional).
- **Search Contact**: Search contacts by name or phone number.
- **Update Contact**: Modify an existing contact’s details.
- **Delete Contact**: Remove contacts easily with a button click.
- **View All Contacts**: Display all contacts stored in the database in a tabular format.
- **Real-time Feedback**: Status messages displayed for user actions like adding, updating, or deleting contacts.

## Technologies Used

- **Python**: Core language for application logic.
- **Tkinter**: Library for creating the graphical interface.
- **SQLite3**: A lightweight SQL database for contact storage.

## Installation and Setup

Follow the steps below to run the Contact Book GUI on your local machine.

### Prerequisites

Ensure you have **Python** installed on your system. Download it from [Python's official website](https://www.python.org/downloads/). Tkinter comes pre-installed with Python.

### Clone the Repository

1. Clone this repository using Git:

    ```bash
    git clone https://github.com/AnujYadav-Dev/contact-book-gui.git
    ```

    Alternatively, download the project as a [zip file here](https://github.com/AnujYadav-Dev/contact-book-gui/archive/refs/heads/main.zip) and extract it.

### Navigate to the Project Directory

2. Open your terminal or command prompt and navigate to the directory where the project files are located:

    ```bash
    cd contact-book-gui
    ```

### Run the Application

3. Run the Python script to start the Contact Book GUI:

    ```bash
    python contact_book_gui.py
    ```

This will launch the GUI window for the contact book, allowing you to add, search, update, and delete contacts.

## User Guide

### Interface Overview

- **Entry Fields**: Use the input fields to enter contact information (name, phone number, email, address).
- **Add Contact**: Click this button to add a new contact to the database.
- **Search**: Use the search bar to find contacts by name or phone number. Press the "Enter" key or click the "Search" button.
- **Contact List**: The table displays the contact ID, name, and phone number. Click on a contact in the list to select it.
- **Update Contact**: After selecting a contact from the list and editing the fields, click "Update Contact" to save changes.
- **Delete Contact**: Select a contact from the list and click "Delete Contact" to remove it.
- **View All Contacts**: Click this button to reload and display all contacts from the database.
- **Status Messages**: Displays success or error messages for actions like adding, updating, or deleting a contact.

### Example GUI Layout

```
+--------------------- Contact Book -----------------------+
|                                                          |
| Name:  [           ]   Phone: [            ]             |
| Email: [           ]   Address: [            ]           |
| [ Add Contact ]                                            |
|----------------------------------------------------------|
| Search: [       ]   [ Search Button ]                    |
|----------------------------------------------------------|
|  ID   |    Name     |  Phone Number                      |
|----------------------------------------------------------|
|   1   |   John Doe  |   123456789                        |
|----------------------------------------------------------|
| [ Update Contact ] [ Delete Contact ] [ View All ]       |
|                                                          |
| Status Message: Contact added successfully!              |
+----------------------------------------------------------+
```

## Contributing

Feel free to contribute to this project by:

1. Forking the repository.
2. Creating a new branch.
3. Making your changes.
4. Submitting a pull request.

Ensure that your code follows best practices and is well-documented.

## License

This project is licensed under the MIT License. You can see the full license [here](LICENSE).

---

### Download Link:

[Download the Contact Book GUI Project](https://github.com/AnujYadav-Dev/contact-book-gui/archive/refs/heads/main.zip)

---

If you have any questions or feedback, feel free to reach out or create an issue in the repository.

Enjoy managing your contacts with ease! 😊
