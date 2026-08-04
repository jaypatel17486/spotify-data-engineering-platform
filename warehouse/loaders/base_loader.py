from warehouse.loaders.database import get_connection


class BaseLoader:

    def __init__(self):

        self.conn = get_connection()
        self.cur = self.conn.cursor()

    def execute(self, query, values):

        self.cur.execute(query, values)

    def commit(self):

        self.conn.commit()

    def close(self):

        self.cur.close()
        self.conn.close()