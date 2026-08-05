# 📊 Protótipo Interativo Streamlit - Netflix Dataset

Este repositório contém um protótipo de aplicativo web interativo desenvolvido em Python com a biblioteca **Streamlit** e implantado na **Streamlit Community Cloud**. 

O aplicativo consome dados do dataset **Netflix Movies and Series** do Kaggle em tempo real utilizando a biblioteca `kagglehub`.

## 📁 Estrutura do Repositório

```text
StreamlitPPII/
├── 📄 .gitignore          # Arquivos e pastas ignorados pelo Git
├── 📄 README.md           # Documentação e instruções do projeto
├── 🐍 app.py              # Código-fonte da aplicação Streamlit com dados do Kaggle
└── 📋 requirements.txt    # Dependências do projeto (streamlit, pandas, numpy, kagglehub)
```

## 🚀 Como Executar Localmente

1. Clone este repositório:
```bash
git clone https://github.com/anabiasena/StreamlitPPII.git
cd StreamlitPPII

```


2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

```


3. Instale as dependências:
```bash
pip install -r requirements.txt

```


4. Inicie o aplicativo:
```bash
streamlit run app.py

```
