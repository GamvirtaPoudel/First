from classes.connection import MyDb


class Item:
    def __init__(self):
        self.my_db = MyDb()

    def add_item(self, name, types, rate):
        qry = "INSERT INTO items (name, type, price) VALUES (%s,%s,%s)"
        values = (name, types, rate)
        self.my_db.iud(qry, values)
        return True

    def show_item(self):
        qry = "SELECT * FROM items"
        all_items = self.my_db.show_data(qry)
        return all_items

    def search_item(self, key):
        qry = "SELECT * FROM items WHERE name LIKE '" + key + "%'"
        all_items = self.my_db.show_data(qry)
        return all_items

    def update_item(self, row, name, types, rate):
        qry = "UPDATE items SET name = %s, type = %s, price = %s WHERE id = %s"
        values = (name, types, rate, row)
        self.my_db.iud(qry, values)
        return True

    def delete_item(self):
        pass
