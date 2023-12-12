from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog  # Added for simpledialog
from tkinter import ttk # Import ttk module for Treeview

# Create an empty list to store entries
entries = []

class CourseRegistration:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Course Registration")
        self.master.geometry("500x400")
        self.master.configure(bg='#C78181') # Adding this line changes the background color
        self.entries = []

        # Create tree attribute
        self.tree = None
        self.tree = ttk.Treeview(self.master, columns=("Name", "Faculty", "Semester", "Course", "Credit Hours"), show="headings")



        # Entry labels
        Label(self.master, text="Name", pady=10, background='#C78181').grid(row=0, column=0)
        Label(self.master, text="Faculty", pady=10, background='#C78181').grid(row=1, column=0)
        Label(self.master, text="Semester", pady=10, background='#C78181').grid(row=2, column=0)
        Label(self.master, text="Course", pady=10, background='#C78181').grid(row=3, column=0)
        Label(self.master, text="Credit hours", pady=10, background='#C78181').grid(row=4, column=0)
        Label(self.master, text="Matrix Number", pady=10, background='#C78181').grid(row=5, column=0)

        # Entries
        self.name = Entry(self.master)
        self.faculty = Entry(self.master)
        self.semester = Entry(self.master)
        self.course = Entry(self.master)
        self.credit_hours = Entry(self.master)
        self.matrix_number = Entry(self.master)

        self.name.grid(row=0, column=1, pady=10)
        self.faculty.grid(row=1, column=1, pady=10)
        self.semester.grid(row=2, column=1, pady=10)
        self.course.grid(row=3, column=1, pady=10)
        self.credit_hours.grid(row=4, column=1, pady=10)
        self.matrix_number.grid(row=5, column=1, pady=10)

        # Initialize ViewData instance
        self.view_data_instance = None

        # Register Button
        Button(self.master, text="Register", command=self.register).grid(row=6, column=1, sticky=W+E)

        # Next Button
        Button(self.master, text="Next", command=self.show_delete_entry_page).grid(row=6, column=3, sticky=W+E)


    def register(self):
        global entries #declare entries as global
        name = self.name.get()
        faculty = self.faculty.get()
        semester = self.semester.get()
        course = self.course.get()
        credit_hours = self.credit_hours.get()
        matrix_number = self.matrix_number.get()

        if name == "" or faculty == "" or semester == "" or course == "" or credit_hours == "" or matrix_number == "":
            messagebox.showerror("Error", "All fields are required")
        else:
             # Assuming you have a list to store entries
            entry = {'name': name, 'faculty': faculty, 'semester': semester, 'course': course, 'credit_hours': credit_hours, 'matrix_number' : matrix_number}
            entries.append(entry)  # Add the entry to the list
            messagebox.showinfo("Success", "Registration successful")


    def show_view_data_page(self):
        self.master.withdraw()  # Hide the current window
        new_page = Toplevel(self.master)  # Create a new window
        self.view_data_instance = ViewData(new_page, entries, self.update_data_callback)

    def center_window(self):
        width = 500
        height = 400

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.master.geometry(f"{width}x{height}+{x}+{y}")

        self.show_delete_entry_page()
    
    def show_delete_entry_page(self):
        self.master.withdraw()  # Hide the current window
        new_page = Toplevel(self.master)  # Create a new window
        DeleteEntry(new_page, self.show_view_data_page, self.update_data_callback)

class DeleteEntry:
    def __init__(self, master, show_view_data_callback, update_data_callback):
        self.master = master
        self.master.title("Delete Student Course Registration")
        self.master.geometry("500x400")
        self.master.configure(bg='#C78181')
        
        # Entry labels for delete
        Label(self.master, text="Name",  pady=10, background='#C78181').grid(row=0, column=0)
        Label(self.master, text="Semester", pady=10, background='#C78181').grid(row=1, column=0)
        Label(self.master, text="Course", pady=10, background='#C78181').grid(row=2, column=0)

        # Entries
        self.name = Entry(self.master)
        self.semester = Entry(self.master)
        self.course = Entry(self.master)

        self.name.grid(row=0, column=1, pady=10)
        self.semester.grid(row=1, column=1, pady=10)
        self.course.grid(row=2, column=1, pady=10)

        # Delete Button
        Button(self.master, text="Delete", command=self.delete_entry).grid(row=3, column=1, sticky=W+E)

        # View Data Button
        Button(self.master, text="View Data", command=show_view_data_callback).grid(row=3, column=3, sticky=W+E)

    def delete_entry(self):
        global entries
        name_to_delete = simpledialog.askstring("Delete Entry", "Enter the name to delete:")
        if name_to_delete:
            found = False
            for entry in entries:
                if entry["name"] == name_to_delete:
                    entries.remove(entry)
                found = True
                break

        if found:
            messagebox.showinfo("Success", f"Entry for {name_to_delete} deleted successfully")
        else:
            messagebox.showerror("Error", f"No entry found for {name_to_delete}")
        
        self.show_view_data_page()
    
    def show_view_data_page(self):
        self.master.withdraw()  # Hide the current window
        new_page = Toplevel(self.master)  # Create a new window
        ViewData(new_page, entries, self.update_data_callback)

class ViewData:
    def __init__(self, master, entries, update_callback):
        self.master = master
        self.master.title("View Student Course Data")
        self.master.geometry("800x400")
        self.master.configure(bg='#C78181')

        # Labels
        Label(self.master, text="Student Records", pady=10, background='#C78181', font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=5, sticky="n")

        # Create a Treeview widget
        self.tree = ttk.Treeview(self.master, columns=("Name", "Faculty", "Semester", "Course", "Credit Hours"), show="headings")
      
        # Set column headings
        self.tree.heading("Name", text="Name")
        self.tree.heading("Faculty", text="Faculty")
        self.tree.heading("Semester", text="Semester")
        self.tree.heading("Course", text="Course")
        self.tree.heading("Credit Hours", text="Credit Hours")

        # Set column widths
        self.tree.column("Name", width=150)
        self.tree.column("Faculty", width=150)
        self.tree.column("Semester", width=100)
        self.tree.column("Course", width=150)
        self.tree.column("Credit Hours", width=100)

        for entry in entries:
            self.tree.insert("", "end", values=(entry['name'], entry['faculty'], entry['semester'], entry['course'], entry['credit_hours']))

        # Grid the Treeview widget
        self.tree.grid(row=1, column=0, sticky='n')

        # Create the "STUDENT RECORDS" headline
        headline = Label(self.master, text="STUDENT RECORDS", pady=10, background='#C78181', font=("Helvetica", 16, "bold"))
        headline.grid(row=0, column=0, columnspan=5, sticky="n")

        # Configure row and column weights for resizing
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

    def show_view_data_page(self):
        self.master.withdraw()  # Hide the current window
        new_page = Toplevel(self.master)  # Create a new window
        ViewData(new_page, entries, self.update_data_callback)

if __name__ == "__main__":
    root = Tk ()
    CourseRegistration(root)
    root.mainloop()