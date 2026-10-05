import os
import requests
import json
from datetime import datetime
def fetch_api_data():
    api_token = os.environ.get("API_TOKEN")
    url = "https://github.com"
    headers = {}
    if api_token:
        headers["Authorization"] = f"token {api_token}"      
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()   
        today = datetime.now().strftime("%Y%m%d")
        os.makedirs("data", exist_ok=True)
        with open(f"data/result_{today}.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("データの取得と保存に成功しました。")
    else:
        print(f"エラーが発生しました: {response.status_code}")
        print(response.text)
if __name__ == "__main__":
    fetch_api_data()

