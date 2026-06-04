# jellyfin_client.py
import requests

JELLYFIN_URL = "http://localhost:8096"  # Jellyfin 서버 주소
API_KEY = "d58c4cc15a2342b69418ef87bcdd3cd5"  # 실제 API_KEY 입력
USER_ID = "6c0df3d86054432f8aacc0fed8b7a87b"  # 실제 USER_ID 입력

def get_my_music(limit=5):
    """
    브라우저에서 바로 재생 가능한 5곡만 가져오기
    """
    url = f"{JELLYFIN_URL}/Users/{USER_ID}/Items"
    params = {
        "IncludeItemTypes": "Audio",
        "Recursive": True,
        "Limit": limit,
        "SortBy": "DateCreated",
        "SortOrder": "Descending",
        "api_key": API_KEY
    }

    res = requests.get(url, params=params)
    if res.status_code != 200:
        return []

    items = res.json().get("Items", [])
    music_list = []

    for item in items:
        music_list.append({
            "id": item["Id"],
            "title": item["Name"],
            "artist": item.get("AlbumArtist", ["Unknown"])[0] if item.get("AlbumArtist") else "Unknown",
            "url": (
                f"{JELLYFIN_URL}/Audio/{item['Id']}/universal"
                f"?api_key={API_KEY}"
                f"&UserId={USER_ID}"
                f"&DeviceId=web"
                f"&Container=mp3"
                f"&MaxAudioChannels=2"
            ),
            "image": f"{JELLYFIN_URL}/Items/{item['Id']}/Images/Primary?api_key={API_KEY}"
        })

    return music_list