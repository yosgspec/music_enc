# 音楽ファイル変換
![music_encs](https://github.com/yosgspec/music_enc/blob/master/music_encs.png)

音楽ファイルを簡単に変換するソフト。  
FFmpegをバックエンドとして利用しています。  

# 動作環境
大体のWindowsで動作します。  

FFmepgのインストールが必要です。  
https://www.ffmpeg.org/  
Chocolateyを使うとインストールが簡単です。  
https://chocolatey.org/packages/ffmpeg  
Chocolatyについては下記記事などを参照してください。 
https://qiita.com/konta220/items/95b40b4647a737cb51aa  

なお、C#版の実行には.NET Core 3以上のRuntimeが必要です。
https://dotnet.microsoft.com/download

# ライセンス
## 本体(各srcディレクトリ)
CC0  

## HSP3用ライブラリ(hsp/src/hspext.dll)
BSDライセンス  
http://dev.onionsoft.net/trac/openhsp/wiki/RuleLicense  

## バイナリ配布用ライセンス
### NW.js
MITライセンス他(含有モジュール除く)  
生成したされたバイナリにライセンスファイルが含有されています。  

### PyInstaller
生成したexeへのライセンス追加は不要とのことです。  
https://github.com/pyinstaller/pyinstaller/wiki/FAQ  

# 作成者
YOS G-spec  
[ブログ](http://yosgspec.blog103.fc2.com/) 
[twitter](https://twitter.com/yosgspec) 
[メールアドレス](yos.g.spec@gmail.com)  
