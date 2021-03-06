from entities.voucher import Voucher
from database_connection import get_database_connection

# This class handles all interactions with the database
class VoucerRepository():
    def __init__(self) -> None:
        pass

    # Methods to interact with table "vouchers"
    def save_new_voucher(self, v: Voucher):
        db = get_database_connection()
        db.isolation_level = None
        previous = db.execute("SELECT * FROM vouchers WHERE number == ?", [v.number]).fetchone()
        if previous:
            return False
        db.execute("INSERT INTO vouchers (number, costcentre, debitcredit, ammount, message) VALUES (?, ?, ?, ?, ?)", [v.number, v.cost_centre, v.debit_credit, v.ammount, v.message])
        return True
    
    def delete_voucher(self, n: int):
        db = get_database_connection()
        db.isolation_level = None
        db.execute("DELETE FROM vouchers WHERE number == ?", [n])

    def fetch_vouchers(self):
        vouchers = []
        db = get_database_connection()
        db.isolation_level = None
        data = db.execute("SELECT number, costcentre, debitcredit, ammount, message FROM vouchers").fetchall()
        for e in data:
            v = Voucher(e[0], e[1], e[2], e[3], e[4])
            vouchers.append(v)
        return vouchers
    
    # Methods to interact with table "accounts"
    def save_account(self, number: str, name: str):
        db = get_database_connection()
        db.isolation_level = None
        exists = db.execute("Select * FROM accounts WHERE number==?", [number]).fetchone()
        if exists:
            return False
        db.execute("INSERT INTO accounts (number, name) VALUES (?, ?)", [number, name])
        return True
    
    def find_account(self, number):
        db = get_database_connection()
        db.isolation_level = None
        exists = db.execute("Select number, name FROM accounts WHERE number==?", [number]).fetchone()
        if exists:
            return True
        return False

    def fetch_accounts(self):
        db = get_database_connection()
        db.isolation_level = None
        data = db.execute("Select number, name FROM accounts").fetchall()
        return data

