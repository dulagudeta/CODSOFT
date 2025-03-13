import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
import re

# Database Setup
def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT,
            address TEXT
        )
    """)
    conn.commit()
    conn.close()

# Add Contact
def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()
    
    if name and phone:
        if not validate_phone(phone):
            messagebox.showerror("Error", "Invalid phone number!")
            return
        if email and not validate_email(email):
            messagebox.showerror("Error", "Invalid email address!")
            return
        
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contacts (name, phone, email, address) VALUES (?, ?, ?, ?)", (name, phone, email, address))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_fields()
        view_contacts()
    else:
        messagebox.showerror("Error", "Name and Phone are required!")

# View Contacts
def view_contacts():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone FROM contacts")
    rows = cursor.fetchall()
    conn.close()
    
    listbox_contacts.delete(0, tk.END)
    for row in rows:
        listbox_contacts.insert(tk.END, f"{row[0]} - {row[1]} ({row[2]})")

# Delete Contact
def delete_contact():
    selected = listbox_contacts.curselection()
    if selected:
        contact_id = listbox_contacts.get(selected[0]).split(' - ')[0]
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
        if confirm:
            conn = sqlite3.connect("contacts.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Deleted", "Contact deleted successfully!")
            view_contacts()
    else:
        messagebox.showerror("Error", "Select a contact to delete!")

# Edit Contact
def edit_contact():
    selected = listbox_contacts.curselection()
    if selected:
        contact_id = listbox_contacts.get(selected[0]).split(' - ')[0]
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
        contact = cursor.fetchone()
        conn.close()
        
        clear_fields()
        entry_name.insert(0, contact[1])
        entry_phone.insert(0, contact[2])
        entry_email.insert(0, contact[3])
        entry_address.insert(0, contact[4])
        
        add_button.config(text="Update Contact", command=lambda: update_contact(contact_id))

# Update Contact
def update_contact(contact_id):
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    address = entry_address.get().strip()
    
    if name and phone:
        if not validate_phone(phone):
            messagebox.showerror("Error", "Invalid phone number!")
            return
        if email and not validate_email(email):
            messagebox.showerror("Error", "Invalid email address!")
            return
        
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE contacts
            SET name = ?, phone = ?, email = ?, address = ?
            WHERE id = ?
        """, (name, phone, email, address, contact_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_fields()
        view_contacts()
        add_button.config(text="Add Contact", command=add_contact)
    else:
        messagebox.showerror("Error", "Name and Phone are required!")

# Search Contacts
def search_contacts():
    search_term = entry_search.get().strip()
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone FROM contacts WHERE name LIKE ? OR phone LIKE ?", (f"%{search_term}%", f"%{search_term}%"))
    rows = cursor.fetchall()
    conn.close()
    
    listbox_contacts.delete(0, tk.END)
    for row in rows:
        listbox_contacts.insert(tk.END, f"{row[0]} - {row[1]} ({row[2]})")

# View Contact Details
def view_details():
    selected = listbox_contacts.curselection()
    if selected:
        contact_id = listbox_contacts.get(selected[0]).split(' - ')[0]
        conn = sqlite3.connect("contacts.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
        contact = cursor.fetchone()
        conn.close()
        
        # Create a new window to display details
        details_window = tk.Toplevel(root)
        details_window.title("Contact Details")
        details_window.geometry("300x200")
        
        # Display contact details
        tk.Label(details_window, text=f"Name: {contact[1]}", font=("Arial", 12)).pack(pady=5)
        tk.Label(details_window, text=f"Phone: {contact[2]}", font=("Arial", 12)).pack(pady=5)
        tk.Label(details_window, text=f"Email: {contact[3]}", font=("Arial", 12)).pack(pady=5)
        tk.Label(details_window, text=f"Address: {contact[4]}", font=("Arial", 12)).pack(pady=5)
    else:
        messagebox.showerror("Error", "Select a contact to view details!")

# Clear Input Fields
def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Validate Phone Number
def validate_phone(phone):
    return re.match(r"^\+?[0-9]{10,15}$", phone) is not None

# Validate Email Address
def validate_email(email):
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email) is not None

# GUI Setup
root = tk.Tk()
root.title("Contact Manager")
root.geometry("500x600")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
frame.pack(pady=20, fill=tk.BOTH, expand=True)

# Labels and Entries
tk.Label(frame, text="Name", bg="#ffffff").grid(row=0, column=0, sticky="w", pady=(0, 5))
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=0, column=1, pady=(0, 5))

tk.Label(frame, text="Phone", bg="#ffffff").grid(row=1, column=0, sticky="w", pady=(0, 5))
entry_phone = tk.Entry(frame, width=30)
entry_phone.grid(row=1, column=1, pady=(0, 5))

tk.Label(frame, text="Email", bg="#ffffff").grid(row=2, column=0, sticky="w", pady=(0, 5))
entry_email = tk.Entry(frame, width=30)
entry_email.grid(row=2, column=1, pady=(0, 5))

tk.Label(frame, text="Address", bg="#ffffff").grid(row=3, column=0, sticky="w", pady=(0, 5))
entry_address = tk.Entry(frame, width=30)
entry_address.grid(row=3, column=1, pady=(0, 5))

# Buttons
button_frame = tk.Frame(frame, bg="#ffffff")
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

add_button = tk.Button(button_frame, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white", width=15)
add_button.pack(side=tk.LEFT, padx=5)

tk.Button(button_frame, text="Edit Contact", command=edit_contact, bg="#FFC107", width=15).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Delete Contact", command=delete_contact, bg="#F44336", fg="white", width=15).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="View Details", command=view_details, bg="#2196F3", fg="white", width=15).pack(side=tk.LEFT, padx=5)

# Search
tk.Label(frame, text="Search", bg="#ffffff").grid(row=5, column=0, sticky="w", pady=(10, 5))
entry_search = tk.Entry(frame, width=30)
entry_search.grid(row=5, column=1, pady=(10, 5))

tk.Button(frame, text="Search", command=search_contacts, bg="#2196F3", fg="white", width=15).grid(row=6, column=0, columnspan=2, pady=5)

# Listbox
listbox_contacts = tk.Listbox(frame, width=50, height=10)
listbox_contacts.grid(row=7, column=0, columnspan=2, pady=10)

# Initialize DB
init_db()
view_contacts()

# Run the Application
root.mainloop()