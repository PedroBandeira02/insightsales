# InsightSales 📊

Mini-SaaS de **Data Science** para análise de dados de vendas e geração de insights de negócio.  
Este projeto está sendo desenvolvido de forma **incremental**, mês a mês, com foco em **análise de dados**, utilizando **IA como aliada estratégica**.

> ⚠️ No momento, o projeto encontra-se na **fase de motor analítico (Mês 2)**.  
> Interface web, banco de dados e modelos avançados serão adicionados progressivamente.

---

## 🎯 Objetivo do Projeto

O **InsightSales** tem como objetivo ajudar pequenas e médias empresas a:
- entender seus dados de vendas
- identificar padrões
- gerar métricas de negócio
- apoiar a tomada de decisão baseada em dados

Tudo isso a partir de **arquivos CSV simples**, sem exigir conhecimento técnico do usuário final.

---

## 🧠 Escopo Atual (Mês 2)

Nesta fase, o projeto entrega:

- Leitura e padronização de dados de vendas
- Limpeza básica dos dados
- Cálculo de métricas essenciais de negócio:
  - faturamento total
  - ticket médio
  - vendas por produto
  - vendas ao longo do tempo
- Estrutura modular e reutilizável do motor analítico

❌ Ainda NÃO incluído:
- Interface web
- Banco de dados
- Machine Learning
- Deploy

---

## 📁 Estrutura do Projeto

insightsales/
│
├── app/
│ └── main.py
│
├── data/
│ └── raw/
│
├── engine/
│ ├── init.py
│ ├── load_data.py
│ ├── clean_data.py
│ └── metrics.py
│
├── notebooks/
│ └── eda_mes2.ipynb
│
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore


---

## ▶️ Como Executar (local)

### 1️⃣ Criar ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate

2️⃣ Instalar dependências
pip install -r requirements.txt

3️⃣ Executar o projeto
python app/main.py

📊 Formato esperado do CSV
Coluna	Descrição
data	Data da venda
categoria Categoria do produto. Exemplo: móveis
produto	Nome do produto
valor	Valor da venda
quantidade Quantidade de produtos por venda
canal_de_venda Canal utilizado para a venda
vendedor Nome do vendedor


👤 Autor

Projeto desenvolvido por Pedro Arantes,
como parte de um plano estruturado de estudos em Data Science.


