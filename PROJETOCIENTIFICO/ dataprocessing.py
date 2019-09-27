import tweepy
import re
import csv


chave_consumidor = "hYsrRTxwOLHPpcr0RPFiXuJr8"
segredo_consumidor = "f8IdVbpeCD4FGBSx9AMAR7RcAAmgqCag7L65YvCMQ5QoIeRMdV"
token_acesso = "1131229409057431552-IIkgSBVBiHIUvgwDjhi1RjUxe8OEb5"
token_acesso_segredo = "6Yo4z1mVmEa7O0ZrNr1AQOQWHGgrmwbVv9mKfxDtjXVEI"

auth = tweepy.OAuthHandler(chave_consumidor,segredo_consumidor )
auth.set_access_token(token_acesso, token_acesso_segredo)

api = tweepy.API(auth)

def obter_tweets(usuario, limite=10):
    resultados = api.user_timeline(screen_name=usuario, count=limite, tweet_mode='extended')
    tweets = []
    for r in resultados:
        tweet = re.sub(r'http\S+', '', r.full_text)
        tweets.append(tweet.replace('\n', ' ').replace('\\', '').replace('@', '').replace('💙', '').replace('🇦','').replace('🇺','').replace('🇱','').replace('🇵','').replace('👍','').replace('🤝','').replace('🏻','').replace('🇮','').replace('🇷','').replace('🇨','').replace('🇸','').replace('🇯','').replace('🏼','').replace('⚽️','').replace('🇧',''))
    return tweets
tweets = obter_tweets(usuario='jairbolsonaro', limite=500)

with open('‪jairbolsonaro.txt', 'a') as f:
    f.write('\n'.join(tweets))

with open('‪jairbolsonaro.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('‪jairbolsonaro.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)