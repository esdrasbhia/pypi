import flet as ft

def main(page: ft.Page):
    # Configurações da Janela / Página
    page.title = "App Contador em Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK  # Suporte a tema escuro/claro

    # Texto que exibe a contagem
    txt_numero = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    # Funções dos botões
    def diminuir(e):
        txt_numero.value = str(int(txt_numero.value) - 1)
        page.update()  # Atualiza a interface gráfica

    def aumentar(e):
        txt_numero.value = str(int(txt_numero.value) + 1)
        page.update()

    # Adiciona os elementos no layout da página
    page.add(
        ft.Row(
            controls=[
                ft.IconButton(ft.icons.REMOVE, on_click=diminuir),
                txt_numero,
                ft.IconButton(ft.icons.ADD, on_click=aumentar),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# Inicializa o aplicativo (como Janela Desktop por padrão)
ft.app(target=main)
