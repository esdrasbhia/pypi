import easygui as eg
# caixa de mensagem simples
eg.msgbox("Bem-vindo ao EasyGUI!", title="Mensagem de Boas-Vindas")
# caixa de entrada de texto
nome = eg.enterbox("Qual é o seu nome?", title="Entrada de Nome")
#pergunta de sim ou não
resposta = eg.ynbox(f"Olá, {nome}! Você gosta de Python?", title="Pergunta", choices=["Sim", "Não"])
if resposta:
    eg.msgbox("Que bom! Python é uma linguagem incrível!", title="Resposta")
else:
    eg.msgbox("Que pena! Talvez você mude de ideia no futuro.", title="Resposta")