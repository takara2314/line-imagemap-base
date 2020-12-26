import os
from flask import Flask, send_file

app = Flask(__name__)

# 画像の名前 (ディレクトリ名)
image_list = ["takaran"]

# https://example.com/image/画像の名前/解像度 にアクセスされたら
#   「画像の名前」には任意の文字列、「解像度」には任意の整数が入る
#   それぞれimage_name、resolutionという変数に任意の値が格納される
@app.route("/image/<image_name>/<int:resolution>")
# app.route内の変数に代入されてきた値は、関数の引数に入る
def takaranImage(image_name, resolution):
    # 「画像の名前」が7行目のリストの中に入っているなら
    if image_name in image_list:
        # ローカルのパス
        img_url = "image/" + image_name + "/"

        if resolution == 240:
            # 指定したローカルのパスの画像をpng形式で送る
            # 例えば「画像の名前」が「takaran」、「解像度」が「240」なら、
            # https://example.com/image/takaran/240 にアクセスすれば画像が表示される
            return send_file(img_url+"240.png", mimetype="image/png")
        elif resolution == 300:
            return send_file(img_url+"240.png", mimetype="image/png")
        elif resolution == 460:
            return send_file(img_url+"240.png", mimetype="image/png")
        elif resolution == 700:
            return send_file(img_url+"240.png", mimetype="image/png")
        elif resolution == 1040:
            return send_file(img_url+"240.png", mimetype="image/png")
        else:
            # ファイルが見つからなかったら、「404 Not Found」という文字列と、
            # 404というファイルが見つからなかったということを示すコードを送る (HTTP Status Code)
            return "404 Not Found", 404

    else:
        return "404 Not Found", 404

# ポート番号をHerokuの実行設定から取得
port = os.getenv("PORT")
app.run(host="0.0.0.0", port=port)