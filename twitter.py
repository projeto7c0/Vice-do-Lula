import tweepy
import twitter_auth

def tweet(texto, imagem):
    api = twitter_auth.authenticate()
    if (imagem):
        status = api.update_with_media(imagem, status=texto)
    else:
        status = api.update_status(status=texto)
            
    return status