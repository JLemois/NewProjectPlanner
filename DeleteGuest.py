import ttkbootstrap as ttkbs
import psycopg2
from ttkbootstrap.constants import *


class DeleteGuest(ttkbs.Window):
    def __init__(self):
        super().__init__(themename="sandstone")

        # Connection to partyplanner database
        self.conn = psycopg2.connect(database="partyplanner",
                                     user="postgres",
                                     host="localhost",
                                     password="",
                                     port="5432")
        self.cur = self.conn.cursor()

        self.delete_window = self
        self.delete_frame = ttkbs.Frame(self.delete_window, borderwidth='2', padding='0.2i',
                                        relief='raised', style='warning')

        self.delete_label = ttkbs.Label(self.delete_frame, text="Delete Guest", font="Helvetica 20 bold",
                                        style='primary-inverse')
        self.delete_label.pack(side="top", fill=X, expand=True, padx=2, pady=2)

        self.names = []
        self.cur.execute('SELECT firstname, lastname FROM attendance')
        for row in self.cur:
            self.names.append(row)
            print(f'Name: {row[0]} {row[1]}')

        self.delete_frame.pack(side=RIGHT, fill=BOTH, expand=True)

        self.name_options = ttkbs.Combobox(self.delete_frame, values=self.names, style='secondary')
        self.name_options.pack(side=TOP, fill=X, expand=True)

        self.delete_button = ttkbs.Button(self.delete_frame, text="Delete", style='danger')
        self.delete_button.pack(side=BOTTOM, fill=X, expand=True, padx=2, pady=2)

        self.mainloop()
