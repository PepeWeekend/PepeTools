# PepeTools

PepeTools is the free and open sourc Blender Add-on.

This is a collection of tools for Blender designed to extend the Blender side panel and assist with various tasks in the 3D character model creation process. These tools are designed to improve Pepe_Weekend's efficiency in 3D model creation.

Support Blender 4.1.0

## 機能一覧

> [!WARNING]
> 常に破壊的な変更が発生する可能性があります。

|機能            |概要                               |状態     |
|----------------|-----------------------------------|:-------:|
|Blender終了 | アプリケーションを終了します(Add-onハンズオン) | 完了 |
|作業ファイルサイズ表示 | 3DViewに作業中のファイルサイズを表示す | 作成中 |
|ウェイト値設定 | ウェイト値を設定するためのパネル | 未着手 |
|ウェイト転写操作 | ウェイトモックとウェイト転写先メッシュを指定し、ウェイト値を転写する操作パネル | 未着手 |

## Release Note

### バージョン 0.0.0 (2024年X月XX日)

- まだありません

## 開発環境セットアップガイド

- Python 3.11.7をインストール

``` plain
Python 3.11.7 (tags/v3.11.7:fa7a6f2, Dec  4 2023, 19:24:49) [MSC v.1937 64 bit (AMD64)] on win32
```

- Blender bpy moduleをインストール(Blener 4.0向け)

``` bash
pip install fake-bpy-module-4.0
```

- Blender Development add-onをインストール
- 設定で「Blender: Addon Folders」に「PepeTools」格納パスを指定
- setting.jsonに以下を追加  
  ("Blender Install Path.ext"はBlenderのインストールパスを指定する)

``` json
    "blender.executables": [
        {
          "path": "Blender Install Path.exe",
          "name": "",
          "isDebug": false
        }
```

### デバッグ方法

- VSCodeでCtrl + Shift + Pを押して「Blender: start」を選択
- 起動するBlender.exeを選択(事前設定した"Blender Install Path.exe"が表示される)
- Blenderが起動し、VSCodeのデバッグツールでデバッグが可能になる

### トラブルシューティング

> 「fake-bpy-mmodule-4.0」をインストールしたがパスが通らない

- VSCodeで使用するPythonが「fake-bpy-mmodule-4.0」をインストールしたPythonと異なる可能性があります。VSCodeのPythonインタープリターを確認してください。
- VSCodeのPythonインタープリターを変更する方法
  1. VSCodeを開きます
  2. Ctrl + Shift + Pを押して「Python: Select Interpreter」を選択
  3. 「fake-bpy-mmodule-4.0」をインストールしたPythonを選択

## License

Licensed under the MIT License.

[!INCLUDE [License](../LICENSE.md)]
