# 根拠と未確定事項

確認日：2026-11-27。公式資料は更新されるためリリース前に再確認する。

## 公式資料

- [Apple App Review Guidelines 5.1.1 / 5.1.2](https://developer.apple.com/app-store/review/guidelines/#privacy)：アプリ内とApp Store Connectのポリシーリンク、データ・取得方法・用途、第三者の同等以上の保護、保存/削除・同意撤回の説明が必要。第三者の保護を未検証のまま保証する記述はしていない。
- [Apple Manage app privacy](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy)：App PrivacyのPrivacy Policy→Edit→URL→Save。URLとプライバシーラベルは別の設定。URL変更は次バージョンとともに公開。
- [AdMob iOS data disclosure](https://developers.google.com/admob/ios/privacy/data-disclosure)：診断、性能、識別子、広告・操作情報、おおよその位置情報を説明。確認時の資料は13.12.0基準、添付アプリのロックは13.11.0。正確な収集は最終SDKと設定で照合する必要あり。
- [Google privacy policy](https://policies.google.com/privacy?hl=ja)：Googleでのデータ処理の参照先。
- [AdMob UMP](https://developers.google.com/admob/ios/privacy)：同意情報の更新と必要時のプライバシー選択画面。日本向けであることだけから同意画面不要とは判断しない。
- [RevenueCat Apple App Privacy](https://www.revenuecat.com/docs/platform-resources/apple-platform-resources/apple-app-privacy)：購入履歴の開示、分析・アプリ機能の用途。独自ID・広告ID・属性や連携は設定依存。匿名IDであることだけで他SDKも含めた非追跡とは判断しない。
- [RevenueCat Identifying Customers](https://www.revenuecat.com/docs/customers/identifying-customers)：ID未指定時の匿名App User ID。
- [RevenueCat privacy policy](https://www.revenuecat.com/privacy)：顧客のために処理するデータの削除依頼等は顧客（本件の運営者）が窓口。
- [Apple トラッキング設定](https://support.apple.com/ja-jp/102420)：iOSの許可変更手順。
- [GitHub Pages作成](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)：公開ソース・エントリポイント・公開範囲。

## 添付ソースから確認できたこと

対象：ユーザー添付の `sample/hitotobi`。参照のみでアプリは変更していない。

- `src/story.ts` / `capacitor.config.ts`：名称「打刻させて」、iOSアプリ。
- `src/save.ts`：Preferencesによる端末内保存。ステージ進行、ゴースト、設定、広告頻度管理の記録。独自サーバーへの送信処理はこの保存処理にない。
- `src/monetization.ts`：RevenueCatのconfigureにappUserID指定なし。購入・復元・権利確認。購入済み判定後は広告の準備を行わず、表示処理も抑止。すでに起動したSDKの全通信停止までは保証していない。
- 同ファイル：UMPによる同意情報確認、必要時のフォーム表示。`src/main.ts`：「広告のプライバシー設定」を条件付きで表示。
- `Package.resolved`：Google Mobile Ads 13.11.0、UMP 3.1.0、RevenueCat iOS 5.103.2。
- アプリ内のポリシーへのリンクは検索したソース中で見つからなかった。追加が必要。

## 2026-11-27の確定内容

- 運営者回答：AdMobメディエーション、RevenueCat Integrations/Webhooksはいずれも未設定。
- 方針決定：施行日2026-11-27。問い合わせ情報は対応完了から1年以内に削除。購入情報は権利提供・購入確認・復元に必要な期間保存し、本人と対象を確認できる削除依頼に対応。具体的な運用はOPERATIONS.md。
- `Info.plist` に `NSUserTrackingUsageDescription` がある。アプリ側からの明示的なATT要求呼び出しは見つからない。プラグインのinitializeもATTを直接要求しない。UMPのIDFAメッセージ設定による表示の可能性はあるが実機では未確認。
- `prepareInterstitial` に `npa` 指定がなく、プラグインの既定値はfalse。非パーソナライズ広告への固定とは記述しない。広告の種類が実際にパーソナライズされるかは許可・配信側判断にもよる。
- 顧客属性を設定する `setAttributes` 等、広告IDを収集する `collectDeviceIdentifiers`、App User IDを表示する `getAppUserID` の呼び出しはアプリのsrcに見つからない。
- [RevenueCat Customer Profile](https://www.revenuecat.com/docs/dashboard-and-metrics/customer-profile)：購入情報のほか、初回/最終接続・国情報がある。国判定後のIPアドレス自体は保存しないという説明を本文に反映。削除は非同期であり、Appleの履歴削除や返金とは異なる。
- [RevenueCat DPA](https://www.revenuecat.com/dpa) と [Google Adsデータ保護条項](https://business.safety.google/adscontrollerterms/) を参照した。公開文書の確認は個別契約への同意・適用状態・実運用の監査を意味しない。本文は同等以上の保護を要求して維持する運営方針として記載。
- [Google データ保持方針](https://policies.google.com/technologies/retention?hl=ja) を参照し、全広告データに共通する固定保存日数を推測して記載しない。

## 本文確定後も必要な動作確認

ATT・UMPの表示と許可の尊重、アプリ内ポリシーリンク、削除依頼用IDの確認導線、メールの実受信、最終ビルドのSDK構成は未検証。特に非購入ユーザーは現行のアプリUIとメールだけでは匿名顧客を確実に特定できない。本文では個別案内と特定できない場合の説明を定め、削除できるとの無条件な保証はしない。READMEの提出前手順を実施する。

将来追加される計測機能は現行機能として列挙していない。追加時に当該アプリのポリシー・App Privacy回答・同意処理を見直す。
