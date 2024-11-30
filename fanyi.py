import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

// 翻译文本的函数
Future<String> translateText(String text) async {
  final response = await http.post(
    Uri.parse('http://192.168.31.123:5000/translate'),  // 替换成后端服务的地址
    headers: {'Content-Type': 'application/json'},
    body: json.encode({'text': text}),
  );

  if (response.statusCode == 200) {
    final data = json.decode(response.body);
    return data['translated_text'];  // 返回翻译后的文本
  } else {
    throw Exception('Failed to translate');
  }
}

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: TranslatePage(),
    );
  }
}

class TranslatePage extends StatefulWidget {
  @override
  _TranslatePageState createState() => _TranslatePageState();
}

class _TranslatePageState extends State<TranslatePage> {
  final TextEditingController _controller = TextEditingController();
  String _translatedText = '';

  void _translate() async {
    final text = _controller.text;
    try {
      // 调用 translateText 函数获取翻译
      final translated = await translateText(text);
      setState(() {
        _translatedText = translated;
      });
    } catch (e) {
      setState(() {
        _translatedText = 'Translation failed: $e';
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('翻译应用'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            TextField(
              controller: _controller,
              decoration: InputDecoration(labelText: '输入文本'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _translate,
              child: Text('翻译'),
            ),
            SizedBox(height: 20),
            Text(
              '翻译结果: $_translatedText',
              style: TextStyle(fontSize: 16),
            ),
          ],
        ),
      ),
    );
  }
}
