#IMPORTANDO AS BIBLIOTECAS
import tweepy
#PEGANDO AS CHAVES DE ACESSO
chave_consumidor = "hYsrRTxwOLHPpcr0RPFiXuJr8"
segredo_consumidor = "f8IdVbpeCD4FGBSx9AMAR7RcAAmgqCag7L65YvCMQ5QoIeRMdV"
token_acesso = "1131229409057431552-IIkgSBVBiHIUvgwDjhi1RjUxe8OEb5"
token_acesso_segredo = "6Yo4z1mVmEa7O0ZrNr1AQOQWHGgrmwbVv9mKfxDtjXVEI"

#GERANDO A AUTENTIFICAÇÃO
autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao.set_access_token(token_acesso, token_acesso_segredo)

#tweepy SE CONECTANDO COM A API DO TWITTER
twitter = tweepy.API(autenticacao)

#FAZENDO A BUSCA DOS TWEETS
#Munizxandinho
twitter.search(screen_name = "Munizxandinho")

#PARA VIZUALIZAR OS TWEETS
resultado = twitter.search(screen_name ="Munizxandinho")

# lista_separados = ["\\",'n','@','💙']

arquivo = open('‪‪Cientifico4.txt', 'a')
#IMPRIMINDO OS TWEETS NA TELA
for tweet in resultado:
    #usuario.append(tweet.user.screen_name)
    arquivo.write(tweet.text.replace('\n', '').replace('\\', '').replace('@', '').replace('💙', ''))
    arquivo.write('\n')
arquivo.close()
