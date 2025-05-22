import requests
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

API_KEY = 'AIzaSyBiq-3W8DJDPLjblHtaMXbIUJiBGJRI6Ak'
CHANNEL_ID = 'UCJZjTHk7M6FgDLeGTVEDUjQ'

def get_subscriber_count():
    url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={CHANNEL_ID}&key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return int(data['items'][0]['statistics']['subscriberCount'])

def create_banner(subs):
    width, height = 1280, 720
    image = Image.new('RGB', (width, height), color=(230, 70, 30))  # rouge-orangé
    draw = ImageDraw.Draw(image)

    try:
        font_large = ImageFont.truetype("arial.ttf", 80)
        font_small = ImageFont.truetype("arial.ttf", 40)
    except:
        font_large = font_small = ImageFont.load_default()

    title = "JustePourRire"
    draw.text((50, 50), title, font=font_large, fill="white")

    text = f"Abonnés : {subs:,} / 1 000 000"
    draw.text((50, 180), text, font=font_small, fill="white")

    progress = subs / 1_000_000
    draw.rectangle((50, 250, 1230, 300), fill=(180, 180, 180))
    draw.rectangle((50, 250, 50 + int(1180 * progress), 300), fill=(255, 255, 255))

    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    draw.text((50, 350), f"Dernière mise à jour : {now}", font=font_small, fill="white")

    image.save("static/banner.png")

if __name__ == "__main__":
    subs = get_subscriber_count()
    create_banner(subs)
