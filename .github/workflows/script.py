import os
import time
import requests
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}
def call_github_api(url):
    while True:
        response = requests.get(url, headers=headers)
        remaining = int(response.headers.get("X-RateLimit-Remaining", 1))
        reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
        print(f"API残回数: {remaining}")
        if remaining <= 5:
            now = time.time()
            sleep_duration = max(reset_time - now + 5, 10)
            print(f" レート制限が近づいたため、{int(sleep_duration)}秒間スリープします...")
            time.sleep(sleep_duration)
            continue
        if response.status_code != 200:
            print(f"エラーが発生しました: {response.status_code}")
            return None   
        return response.json()
url = "https://github.com"
data = call_github_api(url)
if data:
    print(f"取得成功: {data.get('full_name')}")
