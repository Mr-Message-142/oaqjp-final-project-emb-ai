import requests


def emotion_detector(text_to_analyze):
    url = "http://localhost:5000/model/predict"

    response = requests.post(
        url,
        json={"text": text_to_analyze}
    )

    if response.status_code == 200:
        return response.json()

    return None