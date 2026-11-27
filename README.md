# アプリのプライバシーポリシー

開発するアプリのプライバシーポリシーを掲載する静的サイトです。各アプリのデータの取扱いは個別ページに記載します。

- [アプリ一覧](https://st-sugawara-daiki.github.io/privacy/)
- [打刻させて](https://st-sugawara-daiki.github.io/privacy/dakoku/)


## アプリを追加する

1. `site/<slug>/index.html` を作り、アプリ固有の保存データ、SDK、利用目的、削除方法を記載する。
2. `site/index.html` に個別ページへのリンクを追加する。
3. `python3 scripts/check_site.py --release` でリンクと公開前の確認箇所を検査する。
4. `main` にpushし、公開ページを確認してからアプリ内とApp Store ConnectのプライバシーポリシーURLに登録する。

運用方針と確認記録は [OPERATIONS.md](OPERATIONS.md)、[RESEARCH.md](RESEARCH.md)、[VERIFICATION.md](VERIFICATION.md) を参照してください。
