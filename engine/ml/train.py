import pickle as pk
import pandas as pd

# ===============================
# ENGINE (fonte de dados)
# ===============================

from engine.db.queries import sales_over_time

# ===============================
# ML MODULES
# ===============================

from engine.ml.features import (
    ordenacao_temporal,
    media_faturamento_ultimos_periodos,
    tendencia_faturamento,
    volatilidade_faturamento,
    risco_queda_faturamento
)

from engine.ml.split import temporal_train_test_split
from engine.ml.predictor import baseline_persistencia, baseline_frequencia
from engine.ml.evaluation import avaliar_classificacao
from engine.ml.models import (
    definicao_encoder,
    modelo_base,
    modelo_principal,
    formacao_pipeline
)

# ===============================
# MAIN
# ===============================

def main():

    # ======================================================
    # 1️⃣ COLETA DE DADOS (ENGINE)
    # ======================================================

    df = sales_over_time()

    # validação mínima
    colunas_esperadas = ['data_venda', 'faturamento_total', 'numero_vendas']
    for col in colunas_esperadas:
        if col not in df.columns:
            raise KeyError(f"Coluna obrigatória ausente: {col}")

    # ======================================================
    # 2️⃣ FEATURE ENGINEERING (ML)
    # ======================================================

    df = ordenacao_temporal(df, coluna_temporal='data_venda')

    # renomear para padronizar ML
    df = df.rename(columns={'faturamento_total': 'faturamento'})

    df = media_faturamento_ultimos_periodos(df)
    df = tendencia_faturamento(df)
    df = volatilidade_faturamento(df)

    # ======================================================
    # 3️⃣ VARIÁVEL ALVO
    # ======================================================

    df = risco_queda_faturamento(df)

    # remover linhas inválidas (rolling / shift)
    df = df.dropna().reset_index(drop=True)

    # ======================================================
    # 4️⃣ SPLIT TEMPORAL
    # ======================================================

    X_train, X_test, y_train, y_test = temporal_train_test_split(
        df,
        coluna_alvo='risco_queda_faturamento',
        test_size=0.20,
        coluna_data='data_venda'
    )

    # ======================================================
    # 5️⃣ BASELINES
    # ======================================================

    # Dummy
    dummy = modelo_base()
    dummy.fit(X_train, y_train)
    y_pred_dummy = dummy.predict(X_test)

    # Persistência
    y_pred_persistencia = baseline_persistencia(
        y_train,
        tamanho_teste=len(y_test)
    )

    # Frequência
    y_pred_frequencia = baseline_frequencia(
        y_train,
        tamanho_teste=len(y_test)
    )

    print("\n📊 BASELINES")
    print("Dummy:", avaliar_classificacao(y_test, y_pred_dummy))
    print("Persistência:", avaliar_classificacao(y_test, y_pred_persistencia))
    print("Frequência:", avaliar_classificacao(y_test, y_pred_frequencia))

    # ======================================================
    # 6️⃣ MODELO PRINCIPAL (ÁRVORE)
    # ======================================================

    encoder = definicao_encoder(colunas_categoricas=None)
    arvore = modelo_principal()
    pipeline = formacao_pipeline(encoder, arvore)

    pipeline.fit(X_train, y_train)

    y_pred_modelo = pipeline.predict(X_test)
    resultado_modelo = avaliar_classificacao(y_test, y_pred_modelo)

    print("\n🌳 MODELO PRINCIPAL")
    print("Árvore:", resultado_modelo)

    # ======================================================
    # 7️⃣ EXPORTAÇÃO DO MODELO
    # ======================================================

    with open("engine/ml/modelo_insightsales.pkl", "wb") as f:
        pk.dump(pipeline, f)

    print("\n✅ Modelo ML salvo em engine/ml/modelo_insightsales.pkl")


if __name__ == "__main__":
    main()


