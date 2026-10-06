import streamlit as st
import pandas as pd
import numpy as np

# Título do App
st.title("📊 Meu Primeiro Dashboard em Streamlit")

# Barra lateral (Sidebar)
st.sidebar.header("Configurações")
nome = st.sidebar.text_input("Digite seu nome:", "Usuário")
opcao = st.sidebar.selectbox("Escolha uma opção:", ["Vendas", "Metas", "Relatórios"])

st.write(f"Olá, **{nome}**! Exibindo dados de: **{opcao}**.")

# Exibindo métricas (KPIs)
col1, col2, col3 = st.columns(3)
col1.metric("Faturamento", "R$ 45.000", "12%")
col2.metric("Pedidos", "1.230", "-3%")
col3.metric("Ticket Médio", "R$ 36,50", "5%")

# Criando dados aleatórios para gráfico
dados_grafico = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Produto A", "Produto B", "Produto C"]
)

# Gráfico de linha nativo do Streamlit
st.subheader("Evolução das Vendas")
st.line_chart(dados_grafico)

# Exibindo uma tabela interativa
st.subheader("Tabela de Dados")
st.dataframe(dados_grafico)