from tkinter import *
from tkinter.messagebox import showerror, showinfo, askokcancel
from tkinter.scrolledtext import ScrolledText
from pymongo import MongoClient

def create_todo_list():
    create.deiconify()

def update_todo_list():
    update.deiconify()from tkinter import *
from tkinter.messagebox import showerror, showinfo, askokcancel
from tkinter.scrolledtext import ScrolledText
from pymongo import MongoClient

def create_todo_list():
    create.deiconify()

def update_todo_list():
    update.deiconify()

def view_to_do():
    view_window.deiconify()
    populate_view_list() 

def populate_view_list():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["ToDo"]
        coll = db["ToDo"]
        tasks = coll.find()

        view_list.delete('1.0', END)

        for task in tasks:
            view_list.insert(INSERT, f"Task {task['_t_no']}: {task['task']}\n\n")

    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

def create_to_do():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["ToDo"]
        coll = db["ToDo"]
        taskno = Task_1_Entry.get()
        list_item = List_2_Entry.get()
        if (taskno == "") or (not taskno.isdigit()):
            showerror("Issue", "Enter only a number for the task number")
            Task_1_Entry.delete(0, END)
            Task_1_Entry.focus()
            return

        if list_item == "":
            showerror("Issue", "Do not keep the to-do list empty")
            List_2_Entry.delete(0, END)
            List_2_Entry.focus()
            return

        doc = {"_t_no": taskno, "task": list_item}
        coll.insert_one(doc)
        showinfo("Success", "To-Do List item created")
        Task_1_Entry.delete(0, END)
        List_2_Entry.delete(0, END)
        Task_1_Entry.focus()

    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

def update_to_do():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["ToDo"]
        coll = db["ToDo"]
        taskno = Task_1_Update_Entry.get()
        updated_task = Updated_Task_Entry.get()

        if (taskno == "") or (not taskno.isdigit()):
            showerror("Issue", "Enter only a number for the task number")
            Task_1_Update_Entry.delete(0, END)
            Task_1_Update_Entry.focus()
            return

        if updated_task == "":
            showerror("Issue", "Updated task description cannot be empty")
            Updated_Task_Entry.delete(0, END)
            Updated_Task_Entry.focus()
            return

        coll.update_one({"_t_no": taskno}, {"$set": {"task": updated_task}})
        showinfo("Success", "To-Do List item updated")
        Task_1_Update_Entry.delete(0, END)
        Updated_Task_Entry.delete(0, END)
        Task_1_Update_Entry.focus()

    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

root = Tk()
root.title("To Do List")
root.geometry("500x500+34+35")
f = ("Arial", 30, "bold", "italic")

header_label = Label(root, text="To Do List", font=f)
header_label.pack(pady=5)

create_button = Button(root, text="Create To Do List", font=f, command=create_todo_list)
update_button = Button(root, text="Update the To Do List", font=f, command=update_todo_list)
view_button = Button(root, text="View To Do List", font=f, command=view_to_do)
create_button.pack(pady=2)
update_button.pack(pady=3)
view_button.pack(pady=4)

create = Tk()
create.title("Create To Do List")
create.geometry("600x600+50+50")

def back():
    create.withdraw()
    root.deiconify()

Task_1_Label = Label(create, text="Enter the task number:", font=f, width=20)
Task_1_Entry = Entry(create, font=f)
List_2_Label = Label(create, text="Enter the task description:", font=f, width=20)
List_2_Entry = Entry(create, font=f)
create_btn = Button(create, text="Save", font=f, command=create_to_do)
back_btn = Button(create, text="Back", font=f, command=back)
Task_1_Label.pack(pady=5)
Task_1_Entry.pack(pady=5)
List_2_Label.pack(pady=5)
List_2_Entry.pack(pady=5)
create_btn.pack(pady=5)
back_btn.pack(pady=5)
create.withdraw()

view_window = Tk()
view_window.title("View To Do List")
view_window.geometry("600x600+50+50")
view_window.withdraw()

def back2():
    view_window.withdraw()
    root.deiconify()

back2_btn = Button(view_window, text="Back", font=f, command=back2)
back2_btn.pack(pady=5)

view_list = ScrolledText(view_window, font=f, height=10, width=50)
view_list.pack(pady=5)

update = Tk()
update.title("Update To Do List")
update.geometry("700x700+50+50")

def back3():
    update.withdraw()
    root.deiconify()

Task_1_Update_Label = Label(update, text="Enter the task number to update:", font=f)
Task_1_Update_Entry = Entry(update, font=f)
Updated_Task_Label = Label(update, text="Enter the updated task description:", font=f, width=20)
Updated_Task_Entry = Entry(update, font=f)
update_btn = Button(update, text="Update", font=f, command=update_to_do)
back3_btn = Button(update, text="Back", font=f, command=back3)
Task_1_Update_Label.pack(pady=5)
Task_1_Update_Entry.pack(pady=5)
Updated_Task_Label.pack(pady=5)
Updated_Task_Entry.pack(pady=5)
update_btn.pack(pady=5)
back3_btn.pack(pady=5)
update.withdraw()

def f9():
    if askokcancel("Quit", "Do you want to exit?"):
        root.destroy()
        view_window.destroy()
        update.destroy()

root.protocol("WM_DELETE_WINDOW", f9)
view_window.protocol("WM_DELETE_WINDOW", f9)
update.protocol("WM_DELETE_WINDOW", f9)

root.mainloop()

def view_to_do():
    view_window.deiconify()
    populate_view_list() 

def populate_view_list():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["ToDo"]
        coll = db["ToDo"]
        tasks = coll.find()

        view_list.delete('1.0', END)

        for task in tasks:
            view_list.insert(INSERT, f"Task {task['_t_no']}: {task['task']}\n\n")

    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

def create_to_do():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["ToDo"]
        coll = db["ToDo"]
        taskno = Task_1_Entry.get()
        list_item = List_2_Entry.get()
        if (taskno == "") or (not taskno.isdigit()):
            showerror("Issue", "Enter only a number for the task number")
            Task_1_Entry.delete(0, END)
            Task_1_Entry.focus()
            return

        if list_item == "":
            showerror("Issue", "Do not keep the to-do list empty")
            List_2_Entry.delete(0, END)
            List_2_Entry.focus()
            return

        doc = {"_t_no": taskno, "task": list_item}
        coll.insert_one(doc)
        showinfo("Success", "To-Do List item created")
        Task_1_Entry.delete(0, END)
        List_2_Entry.delete(0, END)
        Task_1_Entry.focus()

    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

def delete_to_do():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["ToDo"]
        coll = db["ToDo"]
        taskno = Task_1_Delete_Entry.get()
        if (taskno == "") or (not taskno.isdigit()):
            showerror("Issue", "Enter only a number for the task number")
            Task_1_Delete_Entry.delete(0, END)
            Task_1_Delete_Entry focus()
            return

        coll.delete_one({"_t_no": taskno})
        showinfo("Success", "To-Do List item deleted")
        Task_1_Delete_Entry.delete(0, END)
        Task_1_Delete_Entry.focus()

    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

def update_to_do():
    con = None
    try:
        con = MongoClient("localhost", 27017)
        db = con["ToDo"]
        coll = db["ToDo"]
        taskno = Task_1_Update_Entry.get()
        updated_task = Updated_Task_Entry.get()

        if (taskno == "") or (not taskno.isdigit()):
            showerror("Issue", "Enter only a number for the task number")
            Task_1_Update_Entry.delete(0, END)
            Task_1_Update_Entry.focus()
            return

        if updated_task == "":
            showerror("Issue", "Updated task description cannot be empty")
            Updated_Task_Entry.delete(0, END)
            Updated_Task_Entry.focus()
            return

        coll.update_one({"_t_no": taskno}, {"$set": {"task": updated_task}})
        showinfo("Success", "To-Do List item updated")
        Task_1_Update_Entry.delete(0, END)
        Updated_Task_Entry.delete(0, END)
        Task_1_Update_Entry.focus()

    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

root = Tk()
root.title("To Do List")
root.geometry("500x500+34+35")
f = ("Arial", 30, "bold", "italic")

header_label = Label(root, text="To Do List", font=f)
header_label.pack(pady=5)

create_button = Button(root, text="Create To Do List", font=f, command=create_todo_list)
update_button = Button(root, text="Update the To Do List", font=f, command=update_todo_list)
view_button = Button(root, text="View To Do List", font=f, command=view_to_do)
create_button.pack(pady=2)
update_button.pack(pady=3)
view_button.pack(pady=4)

create = Tk()
create.title("Create To Do List")
create.geometry("600x600+50+50")

def back():
    create.withdraw()
    root.deiconify()

Task_1_Label = Label(create, text="Enter the task number:", font=f, width=20)
Task_1_Entry = Entry(create, font=f)
List_2_Label = Label(create, text="Enter the task description:", font=f, width=20)
List_2_Entry = Entry(create, font=f)
create_btn = Button(create, text="Save", font=f, command=create_to_do)
back_btn = Button(create, text="Back", font=f, command=back)
Task_1_Label.pack(pady=5)
Task_1_Entry.pack(pady=5)
List_2_Label.pack(pady=5)
List_2_Entry.pack(pady=5)
create_btn.pack(pady=5)
back_btn.pack(pady=5)
create.withdraw()

view_window = Tk()
view_window.title("View To Do List")
view_window.geometry("600x600+50+50")
view_window.withdraw()

def back2():
    view_window.withdraw()
    root.deiconify()

back2_btn = Button(view_window, text="Back", font=f, command=back2)
back2_btn.pack(pady=5)

view_list = ScrolledText(view_window, font=f, height=10, width=50)
view_list.pack(pady=5)

update = Tk()
update.title("Update To Do List")
update.geometry("700x700+50+50")

def back3():
    update.withdraw()
    root.deiconify()

Task_1_Update_Label = Label(update, text="Enter the task number to update:", font=f)
Task_1_Update_Entry = Entry(update, font=f)
Updated_Task_Label = Label(update, text="Enter the updated task description:", font=f, width=20)
Updated_Task_Entry = Entry(update, font=f)
update_btn = Button(update, text="Update", font=f, command=update_to_do)
back3_btn = Button(update, text="Back", font=f, command=back3)
Task_1_Update_Label.pack(pady=5)
Task_1_Update_Entry.pack(pady=5)
Updated_Task_Label.pack(pady=5)
Updated_Task_Entry.pack(pady=5)
update_btn.pack(pady=5)
back3_btn.pack(pady=5)
update.withdraw()

def f9():
    if askokcancel("Quit", "Do you want to exit?"):
        root.destroy()
        view_window.destroy()
        update.destroy()

root.protocol("WM_DELETE_WINDOW", f9)
view_window.protocol("WM_DELETE_WINDOW", f9)
update.protocol("WM_DELETE_WINDOW", f9)

root.mainloop()
