import tkinter as tk
from tkinter import ttk
import sqlite3

# Create and connect to the SQLite database
db_connection = sqlite3.connect('contact_book.db')
db_cursor = db_connection.cursor()

# Create a table if it doesn't exist
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT,
        address TEXT
    )
''')
db_connection.commit()

# Function to display status messages in the main window
def display_status(message, color="green"):
    status_message_label.config(text=message, fg=color)
    status_message_label.after(5000, lambda: status_message_label.config(text=""))  # Clear the message after 5 seconds

# Function to add a new contact
def add_new_contact():
    contact_name = name_input.get().strip()
    contact_phone = phone_input.get().strip()
    contact_email = email_input.get().strip()
    contact_address = address_input.get().strip()
    
    if contact_name and contact_phone:
        db_cursor.execute('INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)',
                          (contact_name, contact_phone, contact_email, contact_address))
        db_connection.commit()
        load_contact_list()
        clear_input_fields()
        display_status("Contact added successfully!", "green")
    else:
        display_status("Name and Phone are required fields!", "red")

# Function to display all contacts
def load_contact_list():
    for row in contact_list_table.get_children():
        contact_list_table.delete(row)
    
    db_cursor.execute('SELECT id, name, phone FROM contacts')
    all_contacts = db_cursor.fetchall()
    
    for contact in all_contacts:
        contact_list_table.insert("", tk.END, values=(contact[0], contact[1], contact[2]))

# Function to search for a contact by name or phone number
def search_for_contact(event=None):
    search_query = search_input.get().strip()
    
    if search_query:
        db_cursor.execute('SELECT id, name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?', 
                          ('%' + search_query + '%', '%' + search_query + '%'))
        search_results = db_cursor.fetchall()
        
        for row in contact_list_table.get_children():
            contact_list_table.delete(row)
        
        for contact in search_results:
            contact_list_table.insert("", tk.END, values=(contact[0], contact[1], contact[2]))
        
        if not search_results:
            display_status("No contacts found!", "red")
        else:
            display_status(f"Found {len(search_results)} contact(s).", "green")
    else:
        load_contact_list()
        display_status("Displaying all contacts.", "blue")

# Function to update a contact
def update_selected_contact():
    selected_contact = contact_list_table.selection()
    
    if selected_contact:
        contact_id = contact_list_table.item(selected_contact)['values'][0]
        updated_name = name_input.get().strip()
        updated_phone = phone_input.get().strip()
        updated_email = email_input.get().strip()
        updated_address = address_input.get().strip()
        
        if updated_name and updated_phone:
            db_cursor.execute('''
                UPDATE contacts SET name=?, phone=?, email=?, address=?
                WHERE id=?
            ''', (updated_name, updated_phone, updated_email, updated_address, contact_id))
            db_connection.commit()
            load_contact_list()
            clear_input_fields()
            display_status("Contact updated successfully!", "green")
        else:
            display_status("Name and Phone cannot be empty!", "red")
    else:
        display_status("No contact selected for update!", "red")

# Function to delete a contact
def delete_selected_contact():
    selected_contact = contact_list_table.selection()
    
    if selected_contact:
        contact_id = contact_list_table.item(selected_contact)['values'][0]
        
        db_cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
        db_connection.commit()
        load_contact_list()
        display_status("Contact deleted successfully!", "green")
    else:
        display_status("No contact selected for deletion!", "red")

# Function to clear the input fields
def clear_input_fields():
    name_input.delete(0, tk.END)
    phone_input.delete(0, tk.END)
    email_input.delete(0, tk.END)
    address_input.delete(0, tk.END)

# Set up the main Tkinter window
main_window = tk.Tk()
main_window.title("Contact Book")
main_window.geometry("900x670")
main_window.configure(bg="#e8f4f8")  # Softer light blue background for a more pleasant feel

# Create a style for the buttons and Treeview
style = ttk.Style()
style.configure("TButton", font=("Arial", 10, "bold"), padding=6, background="#007acc", foreground="black")
style.configure("Treeview", background="#ffffff", foreground="black", rowheight=25, fieldbackground="#e8f4f8")
style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
style.map("TButton", background=[("active", "#005c99")], foreground=[("active", "white")])

# Title Label
title_label = tk.Label(main_window, text="Contact Book", font=("Arial", 20, "bold"), bg="#e8f4f8", fg="#007acc")
title_label.pack(pady=10)

# Entry fields for adding a contact
entry_frame = tk.Frame(main_window, bg="#e8f4f8")
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Name:", bg="#e8f4f8", font=("Arial", 10)).grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
name_input = tk.Entry(entry_frame, width=30)
name_input.grid(row=0, column=1, padx=5)

tk.Label(entry_frame, text="Phone:", bg="#e8f4f8", font=("Arial", 10)).grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
phone_input = tk.Entry(entry_frame, width=30)
phone_input.grid(row=1, column=1, padx=5)

tk.Label(entry_frame, text="Email:", bg="#e8f4f8", font=("Arial", 10)).grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
email_input = tk.Entry(entry_frame, width=30)
email_input.grid(row=2, column=1, padx=5)

tk.Label(entry_frame, text="Address:", bg="#e8f4f8", font=("Arial", 10)).grid(row=3, column=0, sticky=tk.W, padx=5, pady=2)
address_input = tk.Entry(entry_frame, width=30)
address_input.grid(row=3, column=1, padx=5)

# Add Contact Button
add_contact_button = ttk.Button(entry_frame, text="Add Contact", command=add_new_contact)
add_contact_button.grid(row=4, column=0, columnspan=2, pady=10)

# Search bar
search_frame = tk.Frame(main_window, bg="#e8f4f8")
search_frame.pack(pady=5)

search_label = tk.Label(search_frame, text="Search:", font=("Arial", 10, "bold"), bg="#e8f4f8")
search_label.pack(side=tk.LEFT)

search_input = tk.Entry(search_frame, width=30)
search_input.pack(side=tk.LEFT, padx=10)
search_input.bind("<Return>", search_for_contact)  # Bind the Enter key to search

search_button = ttk.Button(search_frame, text="Search", command=search_for_contact)
search_button.pack(side=tk.LEFT)

# Frame for the contact list
list_frame = tk.Frame(main_window)
list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

# Display Contact List with Scrollbars
columns = ('id', 'name', 'phone')
contact_list_table = ttk.Treeview(list_frame, columns=columns, show='headings', selectmode="browse")
contact_list_table.heading('id', text='ID')
contact_list_table.heading('name', text='Name')
contact_list_table.heading('phone', text='Phone Number')
contact_list_table.column('id', width=50, anchor='center')
contact_list_table.column('name', width=200, anchor='center')
contact_list_table.column('phone', width=200, anchor='center')
contact_list_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Adding a vertical scrollbar
table_scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=contact_list_table.yview)
table_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
contact_list_table.configure(yscroll=table_scrollbar.set)

load_contact_list()

# Frame for action buttons
action_button_frame = tk.Frame(main_window, bg="#e8f4f8")
action_button_frame.pack(pady=10)

update_button = ttk.Button(action_button_frame, text="Update Contact", command=update_selected_contact)
update_button.grid(row=0, column=0, padx=5)

delete_button = ttk.Button(action_button_frame, text="Delete Contact", command=delete_selected_contact)
delete_button.grid(row=0, column=1, padx=5)

view_all_button = ttk.Button(action_button_frame, text="View All Contacts", command=load_contact_list)
view_all_button.grid(row=0, column=2, padx=5)

# Status Label for displaying messages
status_message_label = tk.Label(main_window, text="", font=("Arial", 10), bg="#e8f4f8", fg="green")
status_message_label.pack(pady=5)

# Start the Tkinter event loop
main_window.mainloop()

# Close the database connection when the app window is closed
db_connection.close()
