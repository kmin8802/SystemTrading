import sqlite3

# conn = sqlite3.connect('universe_price.db')
# with문은 오토커밋, conn.close 자동 수행
with sqlite3.connect('universe_price.db') as conn:
    cur = conn.cursor()

# 1. 잔고 테이블 생성
cur.execute('''CREATE TABLE balance
(code varchar(6) PRIMARY KEY,
bid_price int(20),
quantity int (20),
created_at varchar(14),
will_clear_at varchar(14)
)'''
)
conn.commit()

# 2. 데이터 인서트
sql = "insert into balance(code, bid_price, quantity, created_at, will_clear_at) values (?, ?, ?, ?, ?)"
cur.execute(sql, ('005930', 70000, 10, '20220216', 'today'))
conn.commit()
print(cur.rowcount)

def check_table_exist(db_name, table_name):
    with sqlite3.connect('{}.db'.format(db_name)) as con:
        cur = con.cursor()
        sql = "SELECT name FROM sqlite_master WHERE type='table' and name=:table_name"
        cur.execute(sql, {"table_name": table_name})

        if len(cur.fetchall()) > 0:
            return True
        else:
            return False


def insert_df_to_db(db_name, table_name, df, option="replace"):
   with sqlite3.connect('{}.db'.format(db_name)) as con:
       df.to_sql(table_name, con, if_exists=option)


def execute_sql(db_name, sql, param={}):
   with sqlite3.connect('{}.db'.format(db_name)) as con:
       cur = con.cursor()
       cur.execute(sql, param)
       return cur


if __name__ == "__main__":
    pass