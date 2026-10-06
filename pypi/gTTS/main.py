from gtts import gTTS

# texto = input("Digite o texto que deseja converter em áudio: ")
# tts = gTTS(text=texto, lang='pt') 
texto = " Meu nome é Barry Allen e eu sou o homem mais rápido do mundo. Para o mundo exterior, sou apenas um cientista forense comum, mas secretamente, com a ajuda dos meus amigos nos Laboratórios S.T.A.R., eu combato o crime e encontro outros metahumanos como eu. Eu fui o único que viu o impossível. Minha mãe foi assassinada por uma mancha. Meu pai foi preso pelo assassinato dela. A velocidade é a chave para a justiça. Eu sou o Flash."
#criar o objeto gTTS com o texto e o idioma desejado
tts = gTTS(text=texto, lang='pt', slow=False)

#salvar o arquivo de áudio
tts.save("exemplo.mp3")

print("Arquivo de áudio 'exemplo.mp3' criado com sucesso!")