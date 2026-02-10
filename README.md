# InsightSales

InsightSales é um mini-SaaS de **análise de vendas e geração de insights**, construído de forma incremental com foco em **engenharia de dados, estatística aplicada e machine learning**.

O projeto foi estruturado para refletir um **pipeline real de dados**, indo do carregamento bruto até a geração de insights acionáveis, com **regras determinísticas e ML coexistindo**.

---

## 🎯 Objetivo do projeto

- Analisar o comportamento de vendas ao longo do tempo
- Detectar padrões de risco, concentração e volatilidade
- Gerar insights explicáveis para apoio à decisão
- Explorar Machine Learning como **camada complementar**, não substituta das regras

---

## 🧠 Arquitetura geral

load_data
→ clean_data
→ persistência em SQL
→ agregações via SQL
→ estatística aplicada
→ regras determinísticas
→ machine learning (opcional)
→ geração de insights


O ML **não atua sobre dados brutos**, mas sobre **dados já agregados e entendidos**, garantindo robustez e interpretabilidade.

---

## 📦 Estrutura do projeto

engine/
├── load_data.py
├── clean_data.py
├── db/
│ ├── schema.py
│ ├── ingest.py
│ └── queries.py
├── statistics/
│ ├── temporal.py
│ └── distribution.py
├── rules/
│ ├── temporal_rules.py
│ └── distribution_rules.py
├── insights/
│ └── generator.py
└── ml/
├── features.py
├── split.py
├── models.py
├── predictor.py
├── evaluation.py
├── train.py
└── modelo_insightsales.pkl


---

## 📊 Camada estatística

A camada estatística calcula métricas como:
- variação percentual
- volatilidade
- coeficiente de variação
- participação percentual

Essas métricas alimentam tanto:
- regras determinísticas  
- quanto features para Machine Learning

---

## 📐 Regras determinísticas

As regras representam **conhecimento explícito**, como:
- alta volatilidade
- baixa previsibilidade
- quedas consecutivas
- concentração excessiva

São totalmente explicáveis e auditáveis.

---

## 🤖 Machine Learning

O Machine Learning atua como **sensor estatístico complementar**, treinado para:

- antecipar risco de queda de faturamento
- com base no comportamento recente (nível, tendência e estabilidade)

### Características:
- aprendizado supervisionado
- comparação com baselines (dummy, persistência, frequência)
- modelo inicial: árvore de decisão
- ML não substitui regras — **complementa**

O treinamento é executado separadamente via:

```bash
python -m engine.ml.train
🧪 Estado atual do ML
Pipeline completo de ML implementado

Modelo supera baselines de forma consistente

Avaliação inicial baseada em accuracy

Próximo passo planejado:

métricas de classificação (precision, recall, F1)

interpretação do modelo

decisão consciente de integração no produto

🚧 Próximos passos
Avaliação avançada do modelo

Interpretação das decisões do ML

Definição do papel do ML no InsightSales

Possível integração como alerta complementar

📌 Observação final
Este projeto prioriza arquitetura, clareza e decisão consciente, não apenas métricas altas.

Machine Learning é tratado como ferramenta de apoio, não como solução mágic
