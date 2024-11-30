from flask import Flask, request, jsonify
from argostranslate import package, translate

app = Flask(__name__)

# 下载英语到中文的翻译模型
package.download("en_zh")
translator = translate.load_model("en_zh")

@app.route('/translate', methods=['POST'])
def translate_text():
    text = request.json.get('text')
    translated_text = translator.translate(text)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # 监听所有 IP 地址
