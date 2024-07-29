import psycopg2
import ttkbootstrap as tbs
from ttkbootstrap import *
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

# Connection to partyplanner database
conn = psycopg2.connect(database="partyplanner",
                        user="postgres",
                        host="localhost",
                        password="",
                        port="5432")
cur = conn.cursor()

# list for table
row_data = []

# select and for loop to return all table data to row_data

cur.execute('SELECT id, firstname, lastname, membertype, menuchoice, amountpaid from attendance')
for row in cur:
    row_data.append(row)
    print(f'{row[0]} | {row[1]}  {row[2]} | {row[3]} | {row[4]} | {row[5]}')
    print("_________________________________________________")

col_data = [
    {'text': 'ID', "stretch": False},
    {'text': 'First Name', "stretch": False},
    {'text': 'Last Name', "stretch": False},
    {'text': 'Member Type', "stretch": False},
    {'text': 'Entree Choice', "stretch": False},
    {'text': "Amount Paid", "stretch": False}
]

names = []
cur.execute('SELECT firstname, lastname FROM attendance')
for row in cur:
    names.append(row)
    print(f'Name: {row[0]} {row[1]}')


main_display = tbs.Window(themename="sandstone", position=(440, 150))
main_display.title("Party Planner")
colors = main_display.style.colors

"""     Frames Creation     """
outline_frame = ttk.Frame(main_display, borderwidth='3', padding='0.1i', relief='raised', style='light')
outline_frame.pack(fill='both', expand=True)

# Host Frame contains both menu and displays
host_frame = ttk.Frame(outline_frame, borderwidth='2', padding='0.1i', relief='raised', style='dark')
host_frame.pack(fill='both', expand=True)

# Menu frame will contain the buttons
menu_frame = ttk.Frame(host_frame, borderwidth='2', padding='0.2i', relief='raised', style='secondary')
menu_frame.pack(side=LEFT, expand=True, fill=BOTH)

# Display will dynamically change based on user button press
display_frame = ttk.Frame(host_frame, borderwidth='2', padding='0.2i', relief='raised', style='info')
display_frame.pack(side=RIGHT, expand=True, fill=BOTH)

# Button frames
table_display_frame = ttk.Frame(master=display_frame, borderwidth='2', padding='0.2i', relief='raised',
                                style='secondary')
modify_frame = ttk.Frame(master=display_frame, borderwidth='2', padding='0.2i', relief='raised', style='info')
add_frame = ttk.Frame(master=display_frame, borderwidth='2', padding='0.2i', relief='raised', style='success')
delete_frame = ttk.Frame(master=display_frame, borderwidth='2', padding='0.2i', relief='raised', style='warning')

"""     Clear Frames    """


def clear_frames():
    for widget in display_frame.winfo_children():
        widget.pack_forget()


"""     Button Functionality    """


def display_guests():
    clear_frames()
    table_display_frame.pack(side=RIGHT, expand=True, fill=BOTH)

    table = Tableview(
        master=table_display_frame,
        coldata=col_data,
        rowdata=row_data,
        paginated=True,
        pagesize=10,
        autofit=True,
        autoalign=True,
        searchable=True,
        bootstyle=PRIMARY,
        stripecolor=(colors.light, None))

    table.pack(fill=BOTH, expand=True)


def modify():
    clear_frames()

    modify_frame.pack(side=RIGHT, expand=True)

    name_options = ttk.Combobox(modify_frame, values=names)
    name_options.pack(side=TOP, fill=BOTH, expand=True)


def add_guest():
    clear_frames()

    add_frame.pack(side=RIGHT, expand=True, fill=BOTH)

    add_label = ttk.Label(add_frame, text='Add Guest Information', font='Arial 18 bold', borderwidth='.1i',
                          style='primary', justify='center')
    add_label.pack(side=TOP, padx='2', pady='2', expand=True, fill=X)

    add_guest_btn = ttk.Button(add_frame, text='Add Guest', style='secondary')
    add_guest_btn.pack(side=BOTTOM, padx='2', expand=True, fill=X)

    first_name_entry = ttk.Entry(add_frame, style='info')
    first_name_entry.insert(0, 'First Name')
    first_name_entry.pack(side=LEFT, padx='2', expand=True, fill=X)

    last_name_entry = ttk.Entry(add_frame, style='info')
    last_name_entry.insert(0, 'Last Name')
    last_name_entry.pack(side=LEFT, padx='2', expand=True, fill=X)

    member_type_entry = ttk.Entry(add_frame, style='info')
    member_type_entry.insert(0, 'ex. Member/guest/...')
    member_type_entry.pack(side=LEFT, padx='2', expand=True, fill=X)

    menu_choice_entry = ttk.Entry(add_frame, style='info')
    menu_choice_entry.insert(0, "ex. Chicken/Beef/...")
    menu_choice_entry.pack(side=LEFT, padx='2', expand=True, fill=X)

    payment_entry = ttk.Entry(add_frame, style='info')
    payment_entry.insert(0, 'ex. $15-$100')
    payment_entry.pack(side=LEFT, padx='2', expand=True, fill=X)


"""     Buttons     """
# Display all guests and info in a table
display_button = ttk.Button(menu_frame, text="Display", padding='0.1i', style='info', command=display_guests)
display_button.pack(expand=True, fill=BOTH, padx=2, pady=2)

# Modify Guest Entries in table
modify_button = ttk.Button(menu_frame, text="Modify", padding='0.1i', style='primary', command=modify)
modify_button.pack(expand=True, fill=BOTH, padx=2, pady=2)

# Add Guests to table
add_button = ttk.Button(menu_frame, text="Add", padding='0.1i', style='success', command=add_guest)
add_button.pack(expand=True, fill=BOTH, padx=2, pady=2)

# Delete Guests from table
delete_button = ttk.Button(menu_frame, text="Delete", padding='0.1i', style='warning')
delete_button.pack(expand=True, fill=BOTH, padx=2, pady=2)

# Exit program
exit_button = ttk.Button(menu_frame, text="Exit", padding='0.1i', style='danger', command=quit)
exit_button.pack(expand=True, fill=BOTH, padx=2, pady=2)

conn.commit()
conn.close()
main_display.mainloop()
