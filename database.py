import sqlite3 as sql


class DatabaseManager:
    def __init__(self, db_name="stok.db"):
        self.db_name = db_name
        self.conn = sql.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS stok (id INTEGER PRIMARY KEY AUTOINCREMENT, urun_adi TEXT, kategori TEXT, stok_miktari INTEGER, birim_fiyat REAL, tarih TEXT)"
        )
        self.conn.commit()

    def show_all_products(self):
        self.cur.execute("SELECT * FROM ÜRÜNLER")
        print(self.cur.fetchall())
        return self.cur.fetchall()

    def add_product(self, urun_adi, kategori, stok_miktari, birim_fiyat, tarih):
        self.cur.execute(
            "INSERT INTO ÜRÜNLER (urun_adi, kategori, stok_miktari, birim_fiyat, tarih) VALUES (?,?,?,?,?)",
            (urun_adi, kategori, stok_miktari, birim_fiyat, tarih),
        )
        self.conn.commit()

    def close_connection(self):
        self.conn.close()


db = DatabaseManager()
db.show_all_products()
