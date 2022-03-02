from flask import Flask, request, session, redirect, render_template
import app_login
app = Flask(__name__)
app.secret_key = '9KStWezC'

#メイン画面
@app.route('/')
def myroom():
    #ログインが必要
    if not app_login.is_login():
        return redirect('/login')
    return render_template('myroom.html',
            user=app_login.get_user())

#ログイン画面を表示
@app.route('/login')
def login():
    return render_template('login.html')

#ログイン処理
@app.route('/try_login', methods=['POST'])
def try_login():
    # フォームの値を取得
    user, pw = (None, None)
    if 'user' in request.form:
        user = request.form['user']
    if 'pw' in request.form:
        pw = request.form['pw']
    if (user is None) or (pw is None):
        return show_msg('ユーザー名かパスワードの間違い')
    #ログインに成功したらルートページに飛ぶ
    if app_login.try_login(user, pw):
        return redirect('/')

@app.route('/logout')
def logout():
    app_login.try_logout()
    return show_msg('ログアウトしました')

#テンプレートを利用してメッセージを出力
def show_msg(msg):
    return render_template('msg.html', msg=msg)

#livingへ
@app.route('/living')
def living_room():
    return render_template('living.html', user=user)

@app.route('/write')
def write():
    return render_template('write.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
