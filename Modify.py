import ttkbootstrap as ttkbs
import psycopg2
from ttkbootstrap.constants import *


class Modify(ttkbs.Window):
    def __init__(self):
        super().__init__(themename="sandstone")

        # Connection to partyplanner database
        self.conn = psycopg2.connect(database="partyplanner",
                                     user="postgres",
                                     host="localhost",
                                     password="",
                                     port="5432")
        self.cur = self.conn.cursor()

        self.modify_window = self
        self.modify_frame = ttkbs.Frame(self.modify_window, borderwidth='2', padding='0.2i',
                                        relief='raised', style='primary')

        self.names = []
        self.cur.execute('SELECT firstname, lastname FROM attendance')
        for row in self.cur:
            self.names.append(row)
            print(f'Name: {row[0]} {row[1]}')

        self.modify_frame.pack(side=RIGHT, expand=True)

        self.name_options = ttkbs.Combobox(self.modify_frame, values=self.names, state='readonly')
        self.name_options.bind('<<ComboboxSelected>>')
        self.name_options.pack(side=TOP, fill=BOTH, expand=True)

        self.mainloop()


def main():
    Modify()


if __name__ == "__main__":
    main()
