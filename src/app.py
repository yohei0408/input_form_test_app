# 必要なモジュールのインポート
from flask import Flask, request, render_template
from wtforms import Form, StringField, validators, SubmitField

# app という変数名で Flask オブジェクトをインスタンス化
app = Flask(__name__)

# WTForms を使い、index.html 側で表示させるフォームを構築します。
class InputForm(Form):
    InputFormTest = StringField('文字を入力してください',
                    [validators.InputRequired()])

    # HTML 側で表示する submit ボタンの表示
    submit = SubmitField('送信')

# URL にアクセスがあった場合の挙動の設定
@app.route('/', methods = ['GET', 'POST'])
def input():
    # WTForms で構築したフォームをインスタンス化
    form = InputForm(request.form)

    # POST メソッドの条件の定義
    if request.method == 'POST':

        # 条件に当てはまる場合
        if form.validate() == False:
            return render_template('index.html', forms=form)
        # 条件に当てはまらない場合の、処理の実行を定義
        else:
            outputname_ = request.form['InputFormTest']
            return render_template('result.html', outputname=outputname_)

    # GET メソッドの定義
    elif request.method == 'GET':
        return render_template('index.html', forms=form)

# アプリケーションの実行の定義
if __name__ == '__main__':
    app.run(debug=True)

