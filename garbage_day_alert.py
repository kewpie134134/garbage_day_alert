import datetime
import requests

# 発行されたトークン
ACCESS_TOKEN = "TYPE_YOUR_ACCESS_TOKEN"
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

# Line Notify API URL
url = "https://notify-api.line.me/api/notify"

# ゴミ出し曜日情報
DAILY_EVENT = {
    "月": "燃やすゴミ、燃えないゴミ、スプレー缶、乾電池",
    "火": "古紙・古布・段ボール",
    "水": None,
    "木": "プラスチック製容器包装",
    "金": "燃やすゴミ、燃えないゴミ、スプレー缶、乾電池",
    "土": "缶・ビン・ペットボトル、小さな金属類",
    "日": None,
}


def garbage_day():
    weekday = datetime.date.today().weekday()
    # Heroku側で時間指定起動をするには UST で指定しなければなりません。
    # そのため、JST(日本時間) で AM7:30 を指定したい場合は、
    # Heroku 側で 前日の PM22:30(UTC) を指定しますが、
    # その際に曜日が1 日ずれるので、その分を調整 (+1日) します。
    day, event = list(DAILY_EVENT.items())[weekday+1]
    event and send(f"\n{day}曜日は{event}の日です！")


def send(message):
    data = {"message": message}
    requests.post(
        url,
        headers=headers,
        data=data,
    )


if __name__ == "__main__":
    garbage_day()
