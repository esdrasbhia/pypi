import gradio as gr
# Função que recebe um texto e um valor numérico
def saudar(nome, intensidade):
    return "Olá, " + nome + "!" * int(intensidade)
# Conecta a função à interface gráfica
demo = gr.Interface(
    fn=saudar,
    inputs=["text", gr.Slider(1, 5, value=1, step=1, label="Repetições")],
    outputs="text",
    title="Gerador de Saudação",
    description="Exemplo simples usando Gradio"
)
# Executa o aplicativo
demo.launch()