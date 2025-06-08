# journal_bot.py
# -*- coding: utf-8 -*-

from textblob import TextBlob
from googletrans import Translator
import datetime
import os
import json

def analyze_sentiment(text):
    translator = Translator()
    try:
        translated = translator.translate(text, dest='en')
        print(f"[翻譯後內容] {translated.text}")
        blob = TextBlob(translated.text)
        return blob.sentiment.polarity
    except Exception as e:
        print(f"[翻譯錯誤] {e}")
        return 0.0

def respond_to_sentiment(polarity):
    if polarity > 0.2:
        return "聽起來你今天心情不錯呢！繼續保持！🌞"
    elif polarity < -0.2:
        return "我聽到你有些難過，願意說更多嗎？我會陪你聊聊。🌧️"
    else:
        return "謝謝你分享今天的心情，如果你願意，我會一直在這裡。🌙"

def save_journal_entry(entry, polarity):
    today = datetime.date.today().isoformat()
    filename = os.path.join("logs", f"{today}.json")
    os.makedirs("logs", exist_ok=True)
    data = {"text": entry, "polarity": polarity}

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    print("📝 歡迎來到反思日記機器人。請輸入今天的心情記錄：")
    user_input = input("> ")
    polarity = analyze_sentiment(user_input)
    response = respond_to_sentiment(polarity)
    print(f"🤖 {response}")
    save_journal_entry(user_input, polarity)

if __name__ == "__main__":
    main()

