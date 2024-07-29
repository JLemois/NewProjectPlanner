import ttkbootstrap as ttkbs
import psycopg2
from ttkbootstrap.constants import *


class AddGuest(ttkbs.Window):
    def __init__(self):
        super().__init__(themename="sandstone")

        # Connection to partyplanner database
        self.conn = psycopg2.connect(database="partyplanner",
                                     user="postgres",
                                     host="localhost",
                                     password="",
                                     port="5432")
        self.cur = self.conn.cursor()

        self.add_window = self
        self.add_frame = ttkbs.Frame(self.add_window, borderwidth='2', padding='0.2i', relief='raised', style='success')
        self.add_frame.pack(side=RIGHT, expand=True, fill=BOTH)

        self.add_label = ttkbs.Label(self.add_frame, text='Add Guest Information', font='Arial 18 bold',
                                     borderwidth='.1i', style='primary-inverse', justify='center')
        self.add_label.pack(side=TOP, padx='2', pady='5', expand=True, fill=X)

        self.add_guest_btn = ttkbs.Button(self.add_frame, text='Add Guest', style='secondary')
        self.add_guest_btn.pack(side=BOTTOM, padx='2', pady='5', expand=True, fill=X)

        self.first_name_entry = ttkbs.Entry(self.add_frame, style='info')
        self.first_name_entry.insert(0, 'First Name')
        self.first_name_entry.pack(side=LEFT, padx='2', expand=True, fill=X)

        self.last_name_entry = ttkbs.Entry(self.add_frame, style='info')
        self.last_name_entry.insert(0, 'Last Name')
        self.last_name_entry.pack(side=LEFT, padx='2', expand=True, fill=X)

        self.member_type_entry = ttkbs.Entry(self.add_frame, style='info')
        self.member_type_entry.insert(0, 'ex. Member/guest/...')
        self.member_type_entry.pack(side=LEFT, padx='2', expand=True, fill=X)

        self.menu_choice_entry = ttkbs.Entry(self.add_frame, style='info')
        self.menu_choice_entry.insert(0, "ex. Chicken/Beef/...")
        self.menu_choice_entry.pack(side=LEFT, padx='2', expand=True, fill=X)

        self.payment_entry = ttkbs.Entry(self.add_frame, style='info')
        self.payment_entry.insert(0, 'ex. $15-$100')
        self.payment_entry.pack(side=LEFT, padx='2', expand=True, fill=X)

        self.mainloop()
