import 'package:flutter_py/flutter_py.dart';

Future<String> translateText(String text) async {
  final py = await FlutterPy.init();
  
  // 运行 Python 脚本
  final result = await py.run('''
import sys
from argostranslate import translate

# 加载英语到中文的翻译模型
package.download("en_zh")
translator = translate.load_model("en_zh")

text = "$text"
translated_text = translator.translate(text)
print(translated_text)
''');

  return result;
}
