# AI Auto Blur
**Latest Release:** v0.8 Face Beta

YOLO11 Segmentationを利用して、画像内の指定オブジェクトを自動検出し、
ぼかし処理を行うWindows向けGUIツールです。

## Features

- YOLO11による対象オブジェクトの自動検出
- 検出領域への自動ブラー処理
- Blur Sizeの調整
- Confidenceの調整
- 複数画像の一括処理
- 処理進捗の表示
- 処理ログの表示
- PNG / JPG / JPEG / WebP対応

## 使用技術

- Python
- CustomTkinter
- Ultralytics YOLO11
- OpenCV
- PyInstaller

## 使い方

1. `AI Auto Blur.exe` を起動
2. Input Folderで処理する画像フォルダを選択
3. Output Folderで保存先を選択
4. Blur Sizeを調整
5. Confidenceを調整
6. `Start` を押す

処理結果は指定したOutput Folderに保存されます。

## パラメータ

### Blur Size

検出領域に適用するぼかしの強さを設定します。

値を大きくすると、ぼかしが強くなります。

### Confidence

YOLOの検出信頼度の閾値を設定します。

値を下げると検出しやすくなりますが、
誤検出が増える可能性があります。

値を上げると誤検出を減らせますが、
対象を見逃す可能性があります。

## 対応画像

- PNG
- JPG
- JPEG
- WebP

## 学習済みモデルについて

本アプリでは独自に学習したYOLO11 Segmentationモデルを使用しています。

配布版には、動作に必要な学習済みモデルが含まれています。

学習済みモデルファイルは本リポジトリには含まれていません。

## 開発環境から実行する場合

```bash
pip install -r requirements.txt
python gui.py
```

## EXEのビルド

```bash
pyinstaller --onedir --windowed --name "AI Auto Blur" gui.py
```
生成されたアプリは `dist/AI Auto Blur/` に出力されます。

## License

本ソフトウェアのライセンスについては、使用している外部ライブラリおよび
学習済みモデルのライセンス条件を考慮した上で決定します。
