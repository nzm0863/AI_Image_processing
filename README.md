# AI Auto Blur

**Latest Release:** v0.8.2

YOLO11 Segmentation と YuNet を利用して、画像内の指定オブジェクトを自動検出し、ぼかし処理を行う Windows 向け GUI ツールです。

## Features

* YOLO11 Segmentation による対象オブジェクトの自動検出
* YuNet による顔検出（写真対応）
* Face (Photo) / Private Parts (Illustration) の検出対象切り替え
* 複数の検出対象を同時にぼかし可能
* Blur Size の調整
* Confidence の調整
* 複数画像の一括処理
* 処理進捗の表示
* 処理ログの表示
* PNG / JPG / JPEG / WebP 対応
* 入力フォルダと出力フォルダの同一指定を防止（v0.8.1）

## 使用技術

* Python
* CustomTkinter
* Ultralytics YOLO11 Segmentation
* OpenCV
* YuNet Face Detection
* NumPy
* Pillow
* PyInstaller

## 使い方

1. `AI Auto Blur.exe` を起動
2. **Input Folder** で処理する画像フォルダを選択
3. **Output Folder** で保存先フォルダを選択
4. **Detection Target** を選択

   * **Face (Photo)**：実写写真の顔ぼかし
   * **Private Parts (Illustration)**：イラスト向け陰部ぼかし
5. Blur Size を調整
6. Confidence を調整
7. **Start** を押す

処理結果は指定した Output Folder に保存されます。

> **注意:** Input Folder と Output Folder に同じフォルダは指定できません。元画像の上書きを防ぐためです。

## パラメータ

### Blur Size

検出領域に適用するぼかしの強さを設定します。

値を大きくすると、ぼかしが強くなります。

### Confidence

YOLO の検出信頼度の閾値を設定します。

* 値を下げる：検出しやすくなる（誤検出が増える可能性あり）
* 値を上げる：誤検出を減らせる（見逃しが増える可能性あり）

## 対応画像

* PNG
* JPG
* JPEG
* WebP

## 学習済みモデルについて

本アプリでは独自に学習した YOLO11 Segmentation モデルを使用しています。

配布版には動作に必要な学習済みモデルが含まれています。

学習済みモデルファイルは GitHub リポジトリには含まれていません。

## 開発環境から実行する場合

```bash
pip install -r requirements.txt
python gui.py
```

## EXE のビルド

```bash
pyinstaller --clean --noconfirm --onedir --windowed \
  --name "AI Auto Blur" \
  --add-data "models/best.pt;models" \
  --add-data "models/face_detection_yunet_2026may.onnx;models" \
  gui.py
```

生成されたアプリは `dist/AI Auto Blur/` に出力されます。

## Changelog

## v0.8.2

### Fixed

* 日本語パス（OneDrive / デスクトップ / ドキュメント等）で顔検出モデルが読み込めない問題を修正。
* EXE を別フォルダへ移動した際に顔ぼかしが動作しない問題を修正。

### Refactoring

* `utils/resource.py` を追加。
* モデルファイルの読み込み処理を共通化（PyInstaller対応）。


### v0.8.1

* Input Folder と Output Folder の同一指定を防止。
* 元画像の誤上書きを防止。
* 学習済みモデル（best.pt）を最新版に更新。

### v0.8 Face Beta

* YuNet による顔ぼかし機能を追加。
* Face / Private Parts の検出対象切り替えを追加。
* 顔・陰部の同時ぼかしに対応。
* GUI レイアウトを改善。

## License

本ソフトウェアのライセンスは、使用している外部ライブラリおよび学習済みモデルのライセンス条件に従います。

商用配布・販売についてはライセンス条件を確認した上で対応します。
