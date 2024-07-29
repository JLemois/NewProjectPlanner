import ttkbootstrap as ttkbs
import psycopg2
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *


class Display(ttkbs.Window):
    def __init__(self):
        super().__init__(themename="sandstone")

        # Connection to partyplanner database
        self.conn = psycopg2.connect(database="partyplanner",
                                     user="postgres",
                                     host="localhost",
                                     password="",
                                     port="5432")
        self.cur = self.conn.cursor()

        # list for table
        self.row_data = []

        # select and for loop to return all table data to row_data
        self.cur.execute('SELECT id, firstname, lastname, membertype, menuchoice, amountpaid from attendance')
        for row in self.cur:
            self.row_data.append(row)
            print(f'{row[0]} | {row[1]}  {row[2]} | {row[3]} | {row[4]} | {row[5]}')
            print("_________________________________________________")

        self.col_data = [
            {'text': 'ID', "stretch": True},
            {'text': 'First Name', "stretch": True},
            {'text': 'Last Name', "stretch": True},
            {'text': 'Member Type', "stretch": True},
            {'text': 'Entree Choice', "stretch": True},
            {'text': "Amount Paid", "stretch": True}
        ]

        self.display_window = self
        self.colors = self.display_window.style.colors

        self.table_display_frame = ttkbs.Frame(self.display_window, borderwidth='1', padding='0.1i', relief='raised',
                                               style='info')

        self.table_display_frame.pack(side=RIGHT, expand=True, fill=BOTH)

        self.table = Tableview(
            master=self.table_display_frame,
            coldata=self.col_data,
            rowdata=self.row_data,
            paginated=True,
            pagesize=10,
            autofit=True,
            autoalign=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(self.colors.light, None))

        self.table.pack(side=TOP, expand=True, fill=BOTH)

        self.mainloop()

