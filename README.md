# 個人開発アプリのプライバシーポリシー

日本語の静的HTML/CSS。JavaScript・外部フォント・サイト側の広告/解析SDKなし。公開対象は `site/` のみ。共有CSSを使い、収集情報とSDKの説明はアプリ別のHTMLに記載します。

## 現在の状態

- 運営者・連絡先：菅原大樹 / gaku.dev88@gmail.com（本人提供）。住所・電話番号は掲載していません。
- `site/index.html`：アプリ一覧、`site/dakoku/index.html`：「打刻させて」。
- 本文は確認済みソース、公式資料、運営者による「追加連携なし」の回答に基づいて確定しました。施行日・最終更新日は2026-11-27。保存・削除の運用は [OPERATIONS.md](OPERATIONS.md) に定めています。今後 `data-publish-blocker` を追加した場合は公開を停止します。
- GitHubの公開先は未指定です。アカウント名、公開URL、公開成功は未確定です。

## 公開・アプリ提出前の実施事項

本文中の未入力箇所は解消済みです。以下は設定・実機の検証事項であり、実施済みとはしていません。

1. [OPERATIONS.md](OPERATIONS.md) に沿ってメールの保存・削除受付を運用する。メールの実受信とRevenueCat管理画面での対象検索を確認する。
2. [RESEARCH.md](RESEARCH.md) の確認済みSDKを最終ビルドと照合する。構成を変えた場合は本文とApp Privacyの回答も更新する。
3. アプリ内の設定等に実際の公開URLへのリンクを追加する。匿名App User IDの表示・コピー導線も追加して削除依頼の対象を確実に確認できるようにする。現在の添付アプリにこれらの導線は見つかっていない。非購入ユーザーは特にメールだけでは対象を特定できない。
4. ATTを必要とするトラッキングは許可前に行わない。AdMobのIDFAメッセージ設定と、初回・拒否・許可・取消し時の動作を実機確認する。Info.plistの説明文やUMP導入だけで動作済みとはしない。
5. `python3 scripts/check_site.py --release` を実行し成功を確認する。

## GitHub Pagesへの公開

希望のURLを `https://OWNER.github.io/privacy/dakoku/` とするため、リポジトリ名を **privacy** にします。OWNERは実際のGitHubユーザー名または組織名に置き換えてください。手元のフォルダ名からアカウント名は推定していません。

1. GitHubへログインし、新しい空のリポジトリ `privacy` を作成。GitHub Freeの場合はPublicを選択。README等の自動作成はオフにする。
2. このフォルダで以下を実行（OWNERを置換）。既存リポジトリへ追加する場合はその履歴を取得し、以下の初期化手順をそのまま使わないでください。

   ```sh
   git init -b main
   git add .
   git commit -m "Add Japanese app privacy site"
   git remote add origin https://github.com/OWNER/privacy.git
   git push -u origin main
   ```

3. GitHubの対象リポジトリ → **Settings → Pages → Build and deployment → Source → GitHub Actions** を選択する。Actionsの実行許可やEnvironmentの承認が表示される場合は、画面の案内に従って許可する。
4. **Actions → Publish privacy site → Run workflow → main** を実行する。通常は以降のmainへのpushで自動更新される。`--release` で失敗した場合は未確定箇所を解消する。公開設定で失敗した場合は手順3を確認し、再実行する。
5. 成功後、Settings → PagesのURLを実際に開く。次の一覧・個別ページがログイン不要のHTTPSで開き、CSS、目次、一覧への戻り、外部リンク、メールリンクが動くことを確認する。

| 用途 | 公開後に確認するURL（未公開のテンプレート） |
| --- | --- |
| アプリ一覧 | `https://OWNER.github.io/privacy/` |
| 打刻させて / App Store登録用 | `https://OWNER.github.io/privacy/dakoku/` |

`site/` 自体が公開ルートです。`site/privacy/` を追加すると `/privacy/privacy/` になるため追加しないでください。リポジトリ名・所有者・`dakoku` フォルダ名は公開後に変更しない運用とし、文章の改訂では同じURLを維持します。独自ドメインは設定していません。

## App Store Connectへの登録

公開確認後、Account Holder、Admin、App ManagerまたはMarketing権限のアカウントで操作します。

1. App Store Connect → **アプリ → 打刻させて → アプリのプライバシー（App Privacy）**。
2. **プライバシーポリシー（Privacy Policy）→ 編集（Edit）** を選ぶ。
3. 日本語の **プライバシーポリシーURL** に `https://OWNER.github.io/privacy/dakoku/` の実際の公開URLを入力して保存する。一覧ページのURLは使わない。
4. URL登録とは別にApp Privacyの収集データの回答を、第三者SDKを含めて入力・公開する。RevenueCatの購入履歴（アプリ機能・分析）とAdMobの情報を確認する。「データを収集しない」は選ばない。個人との紐付け・トラッキングは実設定で判断する。

Appleの案内ではURLの変更は次のアプリバージョンとともに公開されます。編集可能なアプリ状態も確認してください。アプリ内から同じページへアクセスできることも実機で確認します。

## アプリを1本追加する（4ステップ）

1. 固定の英小文字スラッグを決め、`site/dakoku/index.html` を `site/<slug>/index.html` にコピーする。
2. アプリ名・ページタイトル・日付・保存データ・SDK・目的・削除と同意の方法を、そのアプリの実装と公式資料に基づいて書き直す。AdMob/RevenueCatを使わないアプリにはその記述を残さない。未確認部分には `data-publish-blocker` を付ける。
3. `site/index.html` に `<slug>/` へのカードを追加し、`RESEARCH.md` に根拠を記録する。CSSは共通の `assets/style.css` を使う。
4. ブラウザ表示・リンクと `python3 scripts/check_site.py --release` を確認しmainへpushする。公開後に個別URLを確認して、対象アプリのApp Store Connectとアプリ内リンクに登録する。

## ローカル確認

```sh
python3 scripts/check_site.py
python3 -m http.server 8000 --directory site --bind 127.0.0.1
```

`http://127.0.0.1:8000/` と `/dakoku/` を確認します。320px・390px・デスクトップ幅、文字拡大、キーボード操作、目次を確認してください。検証結果と未確認点は [VERIFICATION.md](VERIFICATION.md) に記録します。
