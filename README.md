# 📊 InsightSales

InsightSales é um mini-SaaS de análise de vendas com geração de insights explicáveis, combinando:

- Engenharia de dados
- Estatística aplicada
- Regras determinísticas
- Machine Learning supervisionado (regressão)

O projeto foi desenvolvido com foco em arquitetura modular e decisão técnica consciente, evitando o uso de modelos como "caixa-preta".

---

## 🎯 Objetivo

Transformar dados de vendas em:

- Diagnósticos estruturais
- Alertas de risco
- Indicadores de estabilidade
- Projeções de variação futura

O Machine Learning atua como camada complementar, não substituindo regras explícitas.

---

## 🧠 Arquitetura do Pipeline


load_data
→ clean_data
→ persistência em SQLite
→ agregações SQL
→ estatística descritiva
→ regras determinísticas
→ regressão supervisionada
→ geração de insights


O ML opera apenas sobre dados já agregados e interpretados.

---

## 📦 Estrutura do Projeto


insightsales/
│
├── app/
│ └── main.py
│
├── engine/
│ ├── load_data.py
│ ├── clean_data.py
│ │
│ ├── db/
│ │ ├── schema.py
│ │ ├── ingest.py
│ │ └── queries.py
│ │
│ ├── statistics/
│ │ ├── temporal.py
│ │ └── distribution.py
│ │
│ ├── rules/
│ │ ├── temporal_rules.py
│ │ └── distribution_rules.py
│ │
│ ├── ml/
│ │ ├── features.py
│ │ ├── split.py
│ │ ├── models.py
│ │ ├── evaluation.py
│ │ ├── train.py
│ │ ├── train_and_save.py
│ │ └── predictor.py
│ │
│ └── insights/
│ └── generator.py
│
└── README.md


---

## 📊 Camada Estatística

Calcula métricas como:

- Variação percentual
- Índice de volatilidade
- Coeficiente de variação
- Participação percentual

Essas métricas alimentam as regras determinísticas.

---

## 📏 Regras Determinísticas

Representam conhecimento explícito:

- Alta volatilidade
- Baixa previsibilidade
- Quedas consecutivas
- Dependência excessiva
- Concentração estrutural

São totalmente auditáveis e explicáveis.

---

## 🤖 Machine Learning

### Modelo ativo
- Regressão Linear supervisionada
- Target: log-return do faturamento
- Validação com TimeSeriesSplit
- Métricas: MAE, RMSE, R²

### Decisão técnica

O modelo de classificação anteriormente testado foi congelado por instabilidade estrutural (dataset pequeno e alta variância).

A regressão foi integrada após:

- Superar baseline de persistência
- Apresentar R² positivo consistente
- Demonstrar coeficientes economicamente coerentes

O ML atua como sensor complementar para projeção de variação futura.

---

## ▶ Como Executar

Na raiz do projeto:

```bash
python -m app.main
📈 Exemplo de Output
🧠 INSIGHTS GERADOS PELO INSIGHTSALES:

- O crescimento do faturamento apresenta comportamento irregular ao longo do tempo.
- O volume de vendas apresenta baixa previsibilidade.
- Foram identificadas quedas consecutivas no crescimento.
- A projeção indica crescimento relevante no próximo período.
⚙ Requisitos

Python 3.10+

pandas

scikit-learn

sqlite3

🚧 Próximos Passos

Intervalo de incerteza baseado em RMSE

Camada de API (backend)

Estrutura SaaS

Automação de ingestão

Deploy em nuvem

📌 Filosofia do Projeto

SQL organiza.
Estatística descreve.
Regras explicam.
Regressão estima.
Backend serve.
Produto entrega.