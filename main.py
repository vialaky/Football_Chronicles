import tweepy
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Авторизация
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Публикация поста
try:
    api.update_status("Hello!")
    print("Пост успешно опубликован!")
except tweepy.TweepyException as e:
    print(f"Ошибка при публикации поста: {e}")