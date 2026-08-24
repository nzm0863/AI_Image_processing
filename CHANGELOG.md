# Changelog

## v0.8.2

### Fixed

* 日本語パス（OneDrive / デスクトップ / ドキュメント等）で顔検出モデルが読み込めない問題を修正。
* EXE を別フォルダへ移動した際に顔ぼかしが動作しない問題を修正。

### Refactoring

* `utils/resource.py` を追加。
* モデルファイルの読み込み処理を共通化（PyInstaller対応）。

---

## v0.8.1

### Fixed

* Input Folder と Output Folder に同じフォルダを指定できないように変更。
* 元画像を誤って上書きしてしまう問題を防止。

---

## v0.8-face-beta

### Added

* YuNetによる顔ぼかし追加。
* Detection Target チェックボックス追加。
* 顔・陰部の同時ぼかし対応。
* GUIレイアウト改善。
