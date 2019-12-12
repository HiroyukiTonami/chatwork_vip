# chatwork_vip

[社内chatworkにVIPチャンネルを作った話](https://qiita.com/TonamiH/items/07dfabb4bbe321f5c12f)
で作ったAWS lambda関数に署名検証を追加した版を自分用に置いておく。  
qiitaのエントリ通りに設定を行い、本リポジトリのソースコードをLambdaに転載すれば多分動く。  

## 環境変数

| key | description |
|---|---|
|CW_HOOK_TOKEN|chatwork WebHookの署名検証用トークン|
|CW_API_KEY|chatworkに発言を投稿するためのAPIキー|
|ROOM_ID|発言先のルームID|