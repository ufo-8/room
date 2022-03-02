from flask import session, redirect
import sqlite3
#ログインに使うユーザ名とパスワード
#USERLIST = {
#    'taro': 'aaa',
#    'jiro': 'bbb',
#    'sabu': 'ccc',
#}

dbname = 'ROOM.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# 参考:https://qiita.com/wiwi7373/items/7d47decf85a77454074d
# dict_factoryの定義
def dict_factory(cursor, row):
   d = {}
   for idx, col in enumerate(cursor.description):
       d[col[0]] = row[idx]
   return d


# row_factoryの変更(dict_factoryに変更)
conn.row_factory = dict_factory

# SELECT文の発行
cur.execute('SELECT * FROM userlist')

       
conn.row_factory = dict_factory
# レコードを1行取得
USERLIST = cur.fetchall()


#ログインしているか調べる
def is_login():
    return 'login' in session

#ログイン処理
def try_login(user, password):
    #該当ユーザーがいるか？
    if user not in USERLIST: return False
    #パスワードが合っているか？
    if USERLIST[user] != password: return False
    #ログイン処理
    session['login'] = user
    return True

#ログアウトする
def try_logout():
    session.pop('login', None)
    return True

#セッションからユーザー名を得る
def get_user():
    if is_login(): return session['login']
    return 'not login'

cur.close()
conn.close()
