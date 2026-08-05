import os
import glob
import streamlit as st
import pandas as pd
import kagglehub

# Configuração da página Streamlit
st.set_page_config(
    page_title="Dashboard Netflix",
    page_icon="🎬",
    layout="wide"
)

# Função para baixar e carregar os dados do Kaggle com cache
@st.cache_data
def carregar_dados():
    # Download do dataset via kagglehub
    path = kagglehub.dataset_download("debayank2024/netflix-movies-and-series")
    
    # Localiza o arquivo CSV dentro do repositório baixado
    arquivos_csv = glob.glob(os.path.join(path, "*.csv"))
    if arquivos_csv:
        return pd.read_csv(arquivos_csv[0])
    return pd.DataFrame()

# Título Principal
st.title("🎬 Painel Interativo: Netflix Filmes e Séries")
st.markdown("Análise exploratória do catálogo da Netflix utilizando dados do Kaggle (`kagglehub`).")

# Carregamento dos dados
with st.spinner("Baixando e carregando dados do Kaggle..."):
    df = carregar_dados()

if not df.empty:
    # Barra Lateral - Filtros Interativos
    st.sidebar.header("⚙️ Filtros")

    # Filtro por Tipo (Movie / TV Show)
    coluna_tipo = [col for col in df.columns if 'type' in col.lower()]
    if coluna_tipo:
        campo_tipo = coluna_tipo[0]
        opcoes_tipo = ["Todos"] + list(df[campo_tipo].dropna().unique())
        tipo_selecionado = st.sidebar.selectbox("Tipo de Conteúdo:", opcoes_tipo)
        if tipo_selecionado != "Todos":
            df = df[df[campo_tipo] == tipo_selecionado]

    # Filtro por Ano de Lançamento
    coluna_ano = [col for col in df.columns if 'year' in col.lower() or 'release' in col.lower()]
    if coluna_ano:
        campo_ano = coluna_ano[0]
        df[campo_ano] = pd.to_numeric(df[campo_ano], errors='coerce')
        min_ano = int(df[campo_ano].min())
        max_ano = int(df[campo_ano].max())
        intervalo_anos = st.sidebar.slider("Ano de Lançamento:", min_value=min_ano, max_value=max_ano, value=(min_ano, max_ano))
        df = df[(df[campo_ano] >= intervalo_anos[0]) & (df[campo_ano] <= intervalo_anos[1])]

    # Filtro de Busca por Título
    coluna_titulo = [col for col in df.columns if 'title' in col.lower()]
    if coluna_titulo:
        campo_titulo = coluna_titulo[0]
        termo_busca = st.sidebar.text_input("🔍 Buscar por Título:", "")
        if termo_busca:
            df = df[df[campo_titulo].astype(str).str.contains(termo_busca, case=False, na=False)]

    # Exibição de Métricas
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Títulos Exibidos", len(df))
    with col2:
        if coluna_tipo:
            filmes = len(df[df[campo_tipo].astype(str).str.lower().str.contains("movie")])
            st.metric("Filmes", filmes)
    with col3:
        if coluna_tipo:
            series = len(df[df[campo_tipo].astype(str).str.lower().str.contains("tv show|series|show")])
            st.metric("Séries / Shows", series)

    st.markdown("---")

    # Gráficos
    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        st.subheader("📊 Proporção por Tipo")
        if coluna_tipo:
            st.bar_chart(df[campo_tipo].value_counts())

    with col_graf2:
        st.subheader("📈 Lançamentos por Ano")
        if coluna_ano:
            contagem_anos = df[campo_ano].value_counts().sort_index()
            st.line_chart(contagem_anos)

    # Visualização da Tabela
    st.subheader("📋 Tabela de Dados")
    with st.expander("🔍 Expandir para visualizar todos os registros detalhados"):
        st.dataframe(df, use_container_width=True)

else:
    st.error("Não foi possível carregar os dados do Kaggle.")