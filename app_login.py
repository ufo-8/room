from flask import session, redirect
import sqlite3


dbname = 'ROOM.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# SELECT文の発行
cur.execute('SELECT * FROM userlist')

# レコードを取得
USERLIST = cur.fetchall()

cur.close()
conn.close()

#↑ここまでSQLを試しているコード
#ログインしているか調べる
def is_login():
    return 'login' in session

#ログイン処理
def try_login(user, password):
    #該当ユーザーがいるか？
    for i in range(0, len(USERLIST)):
        if user == USERLIST[i][1]:
            if password == USERLIST[i][2]:
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
