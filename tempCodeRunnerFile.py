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
