import mysql.connector
from tkinter import *
from tkinter import Toplevel, messagebox, END
from tkinter import ttk ,Frame, Label, Entry, StringVar, Button
from conn import *  
from tkcalendar import DateEntry
import tkinter as tk

# Function to insert data into the Applicants table
def insert_data():
    
    adhar = entry_adhar.get()
    name = entry_name.get()
    father = entry_father.get()
    contact = entry_contact.get()
    age = entry_age.get()
    cast = entry_cast.get()
    education = entry_education.get()
    address = entry_address.get()
    noofbf = entry_noofbf.get()
    appmonth = entry_appmonth.get()
    appdate = entry_appdate.get()
    bankname = entry_bankname.get()
    hname = entry_hname.get()
    acn = entry_acn.get()
    ifsc = entry_ifsc.get()

    try:
        query = """INSERT INTO Applicants 
                   (Adhar, Name, Father, Contact, Age, Cast, Education, Address, noofbf, appmonth, appdate, bankname, hname, acn, ifsc)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (adhar, name, father, contact, age, cast, education, address, noofbf, appmonth, appdate, bankname, hname, acn, ifsc)
        cursor.execute(query, values)
        connection.commit()
        messagebox.showinfo("Success", "Applicant information inserted successfully")
        fetch_data()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error inserting data: {err}")

# Function to fetch data from the Applicants table and display it in the Treeview
def fetch_data():
    try:
        cursor.execute("SELECT * FROM Applicants")
        rows = cursor.fetchall()

        for row in tree.get_children():
            tree.delete(row)

        for row in rows:
            tree.insert('', END, values=row)

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error fetching data: {err}")

# Function to update data in the Applicants table
def update_data():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Update Error", "Please select a record to update.")
        return

    adhar = entry_adhar.get()
    name = entry_name.get()
    father = entry_father.get()
    contact = entry_contact.get()
    age = entry_age.get()
    cast = entry_cast.get()
    education = entry_education.get()
    address = entry_address.get()
    noofbf = entry_noofbf.get()
    appmonth = entry_appmonth.get()
    appdate = entry_appdate.get()
    bankname = entry_bankname.get()
    hname = entry_hname.get()
    acn = entry_acn.get()
    ifsc = entry_ifsc.get()

    try:
        query = """UPDATE Applicants SET Name=%s, Father=%s, Contact=%s, Age=%s, Cast=%s, 
                   Education=%s, Address=%s, noofbf=%s, appmonth=%s, appdate=%s, 
                   bankname=%s, hname=%s, acn=%s, ifsc=%s WHERE Adhar=%s"""
        values = (name, father, contact, age, cast, education, address, noofbf, appmonth, appdate, bankname, hname, acn, ifsc, adhar)
        cursor.execute(query, values)
        connection.commit()
        messagebox.showinfo("Success", "Applicant information updated successfully")
        fetch_data()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error updating data: {err}")

# Function to delete data from the Applicants table
def delete_data():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Delete Error", "Please select a record to delete.")
        return

    adhar = tree.item(selected_item)['values'][0]  # Get the Adhar of the selected record

    try:
        query = "DELETE FROM Applicants WHERE Adhar=%s"
        cursor.execute(query, (adhar,))
        connection.commit()
        messagebox.showinfo("Success", "Applicant information deleted successfully")
        fetch_data()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error deleting data: {err}")

# Function to open the User Panel
def user_panel():
    
    root.geometry("565x750")

    root.minsize(565, 750)
    root.maxsize(565, 750)
    clear_frame()
    
    # Customize the header with a background color, padding, and rounded corners
    header_frame = Frame(root, bg="#007bff", bd=5, relief="solid")  # Frame for the header with blue background and a solid border
    header_frame.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")
    
    # Customize the label inside the header
    header_label = Label(header_frame, text="Application Form", font=("Helvetica", 24, "bold"), bg='#007bff', fg='white', padx=20, pady=10)
    header_label.pack(fill="x")  # This will make the label fill the entire width of the frame

    # Use a Frame to group form fields for a better layout
    form_frame = Frame(root, bg='#f9f9f9')  # Light grey background for form area
    form_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
    
    # Create form labels and entries with enhanced styling
    def create_label_entry(row, text):
        Label(form_frame, text=text, font=("Arial", 12), bg='#f9f9f9', fg='#333', anchor="w").grid(row=row, column=0, sticky='w', padx=10, pady=5)
        entry = Entry(form_frame, font=("Arial", 12), bd=2, width=30)
        entry.grid(row=row, column=1, padx=10, pady=5)
        return entry

    global entry_adhar, entry_name, entry_father, entry_contact, entry_age, entry_cast
    global entry_education, entry_address, entry_noofbf, entry_appmonth, entry_appdate
    global entry_bankname, entry_hname, entry_acn, entry_ifsc

    entry_adhar = create_label_entry(1, "Adhar Number")
    entry_name = create_label_entry(2, "Full Name")
    entry_father = create_label_entry(3, "Father's Name")
    entry_contact = create_label_entry(4, "Contact Number")
    
    # Age dropdown field with combobox
    Label(form_frame, text="Age", font=("Arial", 12), bg='#f9f9f9', fg='#333', anchor="w").grid(row=5, column=0, sticky='w', padx=10, pady=5)
    age_var = StringVar()
    age_options = [str(i) for i in range(18, 101)]  # Age options from 18 to 100
    entry_age = ttk.Combobox(form_frame, textvariable=age_var, values=age_options, font=("Arial", 12), width=28)
    entry_age.grid(row=5, column=1, padx=10, pady=5)
    entry_age.set("Select Age")
    
    entry_cast = create_label_entry(6, "Cast")
    entry_education = create_label_entry(7, "Education")
    entry_address = create_label_entry(8, "Current Address")
    entry_noofbf = create_label_entry(9, "No. of Beneficiaries in Family")
    
    # Application Month dropdown
    Label(form_frame, text="Application Month", font=("Arial", 12), bg='#f9f9f9', fg='#333', anchor="w").grid(row=10, column=0, sticky='w', padx=10, pady=5)
    appmonth_var = StringVar()
    appmonth_options = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    entry_appmonth = ttk.Combobox(form_frame, textvariable=appmonth_var, values=appmonth_options, font=("Arial", 12), width=28)
    entry_appmonth.grid(row=10, column=1, padx=10, pady=5)
    entry_appmonth.set("Select Month")

    # Application Date picker
    Label(form_frame, text="Application Date", font=("Arial", 12), bg='#f9f9f9', fg='#333', anchor="w").grid(row=11, column=0, sticky='w', padx=10, pady=5)
    entry_appdate = DateEntry(form_frame, font=("Arial", 12), width=28, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
    entry_appdate.grid(row=11, column=1, padx=10, pady=5)

    entry_bankname = create_label_entry(12, "Bank Name")
    entry_hname = create_label_entry(13, "Account Holder Name")
    entry_acn = create_label_entry(14, "Account Number")
    entry_ifsc = create_label_entry(15, "IFSC Code")

    # Submit button with modern styling
    submit_button = Button(root, text="Submit", command=insert_data, font=("Arial", 14, "bold"), bg='#28a745', fg='white', padx=10, pady=5)
    submit_button.grid(row=16, column=0, pady=30, padx=20, sticky="e")

    # Close button with modern styling
    close_button = Button(root, text="Close", command=root.destroy, font=("Arial", 14, "bold"), bg='#dc3545', fg='white', padx=10, pady=5)
    close_button.grid(row=16, column=1, pady=30, padx=20, sticky="w")
# Function to open the Admin Panel
def admin_panel():
    clear_frame()
    root.attributes('-fullscreen', True)
    # Header frame for the admin panel
    header_frame = Frame(root, bg='#007bff')
    header_frame.grid(row=0, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

    # Label for the header
    header_label = Label(header_frame, text="Admin Panel", font=("Arial", 20, "bold"), bg='#007bff', fg='white')
    header_label.pack(pady=20)

    # Border and shadow effect
    header_frame.configure(borderwidth=2, relief='groove')

    display_treeview()

# Function to display Treeview for admin with update and delete options
def display_treeview():
    global tree
    tree_frame = Frame(root)
    tree_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    # Treeview with all columns
    tree = ttk.Treeview(tree_frame, columns=("Adhar", "Name", "Father", "Contact", "Age", "Cast", "Education", "Address", "noofbf", "appmonth", "appdate", "bankname", "hname", "acn", "ifsc"), show='headings', height=10)

    # Create vertical scrollbar
    scrollbar = Scrollbar(tree_frame, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side="right", fill="y")
    tree.pack(side="left", fill="both", expand=True)

    # Configure headings and columns
    for col in tree['columns']:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    # Fetch data to populate the Treeview
    fetch_data()

    # Bind tree selection event to handle form population
    tree.bind("<<TreeviewSelect>>", lambda _ : messagebox.showinfo(message='Click On Update Buttton to update the record'))

    # Create Update and Delete buttons
    update_button = Button(root, text="Update", command=open_update_window, font=("Arial", 12), bg='#ffc107', fg='white', padx=10, pady=5)
    update_button.grid(row=2, column=0, padx=10, pady=20)

    delete_button = Button(root, text="Delete", command=delete_data, font=("Arial", 12), bg='#dc3545', fg='white', padx=10, pady=5)
    delete_button.grid(row=2, column=1, padx=10, pady=20)
    
    f_button = Button(root, text="Exit", command= lambda : root.attributes('-fullscreen', False), font=("Arial", 12), bg='#dc3545', fg='white', padx=10, pady=5)
    f_button.grid(row=3, column=1   , padx=10, pady=20)

# Function to open the update window with selected record details
def open_update_window():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a record to update.")
        return
    
    # Get selected item values
    item_values = tree.item(selected_item)['values']
    
    # Create a new window for updating the record
    update_window = Toplevel(root)
    update_window.title("Update Applicant Details")
    update_window.geometry("600x800")
    update_window.config(bg="#f2f2f2")  # Light grey background
    
    # Adding a title label
    title_label = tk.Label(update_window, text="Update Applicant Information", font=("Helvetica", 18, "bold"), bg="#3498db", fg="white", padx=20, pady=10)
    title_label.pack(fill=tk.X, pady=(10, 20))

    # Using a frame for better layout
    form_frame = tk.Frame(update_window, bg="#f2f2f2")
    form_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
    
    # Helper function to create form rows
    def create_form_row(label_text, entry_var, value):
        label = tk.Label(form_frame, text=label_text, font=("Arial", 12), bg="#f2f2f2")
        label.grid(row=create_form_row.row_num, column=0, pady=10, sticky=tk.W)
        entry = tk.Entry(form_frame, textvariable=entry_var, font=("Arial", 12), width=30)
        entry.grid(row=create_form_row.row_num, column=1, pady=10)
        entry.insert(0, value)
        create_form_row.row_num += 1
        return entry
    
    create_form_row.row_num = 0

    # Variables to hold updated data
    name_var = tk.StringVar()
    father_var = tk.StringVar()
    contact_var = tk.StringVar()
    age_var = tk.StringVar()
    cast_var = tk.StringVar()
    education_var = tk.StringVar()
    address_var = tk.StringVar()
    bankname_var = tk.StringVar()

    # Form fields
    adhar_label = tk.Label(form_frame, text="Adhar:", font=("Arial", 12), bg="#f2f2f2")
    adhar_label.grid(row=create_form_row.row_num, column=0, pady=10, sticky=tk.W)
    update_adhar = tk.Entry(form_frame, font=("Arial", 12), width=30)
    update_adhar.grid(row=create_form_row.row_num, column=1, pady=10)
    update_adhar.insert(0, item_values[0])  # Pre-fill with selected Adhar number
    update_adhar.config(state='readonly')  # Make Adhar readonly
    create_form_row.row_num += 1

    update_name = create_form_row("Name:", name_var, item_values[1])
    update_father = create_form_row("Father's Name:", father_var, item_values[2])
    update_contact = create_form_row("Contact:", contact_var, item_values[3])
    update_age = create_form_row("Age:", age_var, item_values[4])
    update_cast = create_form_row("Cast:", cast_var, item_values[5])
    update_education = create_form_row("Education:", education_var, item_values[6])
    update_address = create_form_row("Address:", address_var, item_values[7])
    update_bankname = create_form_row("Bank Name:", bankname_var, item_values[11])

    # Update button
    def submit_update():
        adhar = update_adhar.get()
        name = update_name.get()
        father = update_father.get()
        contact = update_contact.get()
        age = update_age.get()
        cast = update_cast.get()
        education = update_education.get()
        address = update_address.get()
        bankname = update_bankname.get()

        try:
            query = """UPDATE Applicants SET Name=%s, Father=%s, Contact=%s, Age=%s, Cast=%s, 
                       Education=%s, Address=%s, bankname=%s WHERE Adhar=%s"""
            values = (name, father, contact, age, cast, education, address, bankname, adhar)
            cursor.execute(query, values)
            connection.commit()
            messagebox.showinfo("Success", "Applicant information updated successfully")
            fetch_data()  # Refresh the data in the Treeview
            update_window.destroy()  # Close the update window
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error updating data: {err}")
    
    # Style the Update button
    update_btn = tk.Button(update_window, text="Update", font=("Arial", 14, "bold"), bg="#2ecc71", fg="white", padx=10, pady=5, command=submit_update)
    update_btn.pack(pady=20)

# Existing function to handle updating the data when "Update" is clicked
def update_data():
    global entry_adhar, entry_name, entry_father, entry_contact, entry_age
    global entry_cast, entry_education, entry_address, entry_noofbf
    global entry_appmonth, entry_appdate, entry_bankname, entry_hname, entry_acn, entry_ifsc

    selected_item = tree.selection()  # Get the selected item from the Treeview
    if not selected_item:
        messagebox.showwarning("Update Error", "Please select a record to update.")
        return

    # Get data from entry fields
    adhar = entry_adhar.get()
    name = entry_name.get()
    father = entry_father.get()
    contact = entry_contact.get()
    age = entry_age.get()
    cast = entry_cast.get()
    education = entry_education.get()
    address = entry_address.get()
    noofbf = entry_noofbf.get()
    appmonth = entry_appmonth.get()
    appdate = entry_appdate.get()
    bankname = entry_bankname.get()
    hname = entry_hname.get()
    acn = entry_acn.get()
    ifsc = entry_ifsc.get()

    try:
        # Update query
        query = """UPDATE Applicants SET Name=%s, Father=%s, Contact=%s, Age=%s, Cast=%s, 
                   Education=%s, Address=%s, noofbf=%s, appmonth=%s, appdate=%s, 
                   bankname=%s, hname=%s, acn=%s, ifsc=%s WHERE Adhar=%s"""
        values = (name, father, contact, age, cast, education, address, noofbf, appmonth, appdate, bankname, hname, acn, ifsc, adhar)
        cursor.execute(query, values)
        connection.commit()

        # Success message
        messagebox.showinfo("Success", "Applicant information updated successfully")
        fetch_data()  # Refresh data in the Treeview after updating
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error updating data: {err}")



    # Bind tree selection event
    tree.bind("<<TreeviewSelect>>", on_tree_select)

    # Create Update and Delete buttons
    update_button = Button(root, text="Update", command=update_data, font=("Arial", 12), bg='#ffc107', fg='white', padx=10, pady=5)
    update_button.grid(row=2, column=0, padx=10, pady=20)

    delete_button = Button(root, text="Delete", command=delete_data, font=("Arial", 12), bg='#dc3545', fg='white', padx=10, pady=5)
    delete_button.grid(row=2, column=1, padx=10, pady=20)

# Function to clear the current frame content
def clear_frame():
    for widget in root.winfo_children():
        widget.destroy()

# Create homepage with options
def homepage():
    root.geometry("600x650")
    clear_frame()
    
    # Create a main frame for padding and aesthetics
    main_frame = Frame(root, bg='#f0f0f0', padx=20, pady=20)
    main_frame.pack(fill=BOTH, expand=True)

    # Header Label
    header_label = Label(main_frame, text="Select an Option", font=("Arial", 24, "bold"), bg='#f0f0f0', fg='#333')
    header_label.pack(pady=(10, 20))  # Add vertical padding

    # Add a decorative line
    separator = ttk.Separator(main_frame, orient='horizontal')
    separator.pack(fill=X, pady=(0, 20))

    # User Button
    user_button = Button(main_frame, text="User", width=20, command=user_panel, 
                         font=("Arial", 12), bg='#007bff', fg='white', 
                         padx=10, pady=10, relief=FLAT)
    user_button.pack(pady=10)

    # Admin Button
    admin_button = Button(main_frame, text="Admin", width=20, command=admin_panel, 
                          font=("Arial", 12), bg='#28a745', fg='white', 
                          padx=10, pady=10, relief=FLAT)
    admin_button.pack(pady=10)

    # Add some decorative padding at the bottom
    bottom_padding = Label(main_frame, bg='#f0f0f0')
    bottom_padding.pack(fill=X, expand=True)


    # Optional: Add some instructions or info
    info_label = Label(main_frame, font=("Arial", 10), bg='#f0f0f0', fg='#666')
    info_label.pack(pady=(10, 20))

# Main window
root = Tk()
root.title("Applicant Management System")
root.configure(bg='#f0f0f0')

# Start with the homepage
homepage()

root.mainloop()