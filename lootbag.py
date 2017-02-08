import sys
import sqlite3

class LootBag():

    def __init__(self):
        self.good_children = dict()

    def add_toy_for_child(self, child, toy):
        with sqlite3.connect('lootbag.db') as conn:
            c = conn.cursor()

            try:
                c.execute("INSERT INTO Child VALUES (?, ?, ?)", (None, child, 0))
            except sqlite3.OperationalError:
                print("OPERATION ERROR TRIGGERRRRRED")
                pass

            c.execute("SELECT idChild FROM Child WHERE Name='{}'".format(child))
            child_id = c.fetchall()
            try:
                c.execute("INSERT INTO Toy VALUES (?, ?, ?)",
                    (None, toy, child_id[0][0]))
            except sqlite3.OperationalError:
                print("OPERATION ERROR TRIGGERRRRRED")
                pass

    def remove_toy_for_child(self, child, toy):

        with sqlite3.connect('lootbag.db') as conn:
            c = conn.cursor()

            c.execute("SELECT idChild FROM Child WHERE Name='{}'".format(child))
            child_id = c.fetchall()

            try:
                c.execute("DELETE FROM Toy WHERE idChild={} AND Name='{}'".format(child_id[0][0], toy))
            except sqlite3.OperationalError:
                print("OPERATION ERROR TRIGGERRRRRED")
                pass

    def get_by_child(self, child):

        with sqlite3.connect('lootbag.db') as conn:
            c = conn.cursor()

            c.execute("""SELECT t.Name
                FROM Toy t, Child c
                WHERE c.Name='{}'
                """.format(child))

        return c.fetchall()
        # return self.good_children[child]['toys']

    def get_list_of_kids(self):

        return [kid for kid in self.good_children.keys()]

    def is_child_happy(self, child):
        
        return self.good_children[child]['delivered']

    def deliver_toys_to_child(self, child):
        self.good_children[child]['delivered'] = True

if __name__ == "__main__":
    bag = LootBag()
    if sys.argv[1] == "add":
        print("adding {} for {}".format(sys.argv[3], sys.argv[2]))
        bag.add_toy_for_child(sys.argv[2], sys.argv[3])

    elif sys.argv[1] == 'remove':
        print("removing {} from {}".format(sys.argv[3], sys.argv[2]))
        bag.remove_toy_for_child(sys.argv[2], sys.argv[3])