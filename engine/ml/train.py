import joblib
import numpy as np
import pandas as pd

from .features import build_regression_dataset
from .split import get_time_series_split
from .models import get_models
from .evaluation import evaluate, summarize


def persistence_baseline(y):
    return y.shift(1)


def train_regression_pipeline(df: pd.DataFrame):

    df_model = build_regression_dataset(df)

    X = df_model.drop(columns=["target"])
    y = df_model["target"]

    tscv = get_time_series_split(n_splits=5)
    models = get_models()

    all_results = {}

    # =============================
    # BASELINE
    # =============================

    baseline_results = []

    for train_idx, test_idx in tscv.split(X):

        y_test = y.iloc[test_idx]

        y_pred = persistence_baseline(y).iloc[test_idx]

        metrics = evaluate(y_test, y_pred)
        baseline_results.append(metrics)

    all_results["baseline"] = summarize(baseline_results)

    # =============================
    # MODELOS
    # =============================

    for name, model in models.items():

        fold_results = []

        for train_idx, test_idx in tscv.split(X):

            X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
            y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]

            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            metrics = evaluate(y_test, y_pred)
            fold_results.append(metrics)

        all_results[name] = summarize(fold_results)

    return all_results
































































































# import pickle as pk
# import pandas as pd

# # ===============================
# # ENGINE (fonte de dados)
# # ===============================

# from engine.db.queries import sales_over_time

# # ===============================
# # ML MODULES
# # ===============================

# from engine.ml.features import (
#     ordenacao_temporal,
#     media_faturamento_ultimos_periodos,
#     tendencia_faturamento,
#     volatilidade_faturamento,
#     risco_queda_faturamento
# )

# from engine.ml.split import temporal_train_test_split
# from engine.ml.predictor import baseline_persistencia, baseline_frequencia
# from engine.ml.evaluation import avaliar_classificacao, analyze_class_distribution
# from engine.ml.models import (
#     definicao_encoder,
#     modelo_base,
#     modelo_principal,
#     formacao_pipeline
# )
# from engine.ml.evaluation import evaluate_time_series_cv
# from engine.ml.models import modelo_arvore_depth


# # ===============================
# # MAIN
# # ===============================

# def main():

#     # ======================================================
#     # 1️⃣ COLETA DE DADOS
#     # ======================================================

#     df = sales_over_time()

#     colunas_esperadas = ['data_venda', 'faturamento_total', 'numero_vendas']
#     for col in colunas_esperadas:
#         if col not in df.columns:
#             raise KeyError(f"Coluna obrigatória ausente: {col}")

#     # ======================================================
#     # 2️⃣ FEATURE ENGINEERING
#     # ======================================================

#     df = ordenacao_temporal(df, coluna_temporal='data_venda')

#     df = df.rename(columns={'faturamento_total': 'faturamento'})

#     df = media_faturamento_ultimos_periodos(df)
#     df = tendencia_faturamento(df)
#     df = volatilidade_faturamento(df)

#     # ======================================================
#     # 3️⃣ VARIÁVEL ALVO
#     # ======================================================

#     df = risco_queda_faturamento(df)

#     df = df.dropna().reset_index(drop=True)

#     # ======================================================
#     # 🔎 FASE 1 — AUDITORIA DO DATASET COMPLETO
#     # ======================================================

#     print("\n===============================")
#     print("🔎 AUDITORIA INICIAL DO DATASET")
#     print("===============================")

#     analyze_class_distribution(df['risco_queda_faturamento'])

#     # ======================================================
#     # 🔁 VALIDAÇÃO TEMPORAL COMPLETA 
#     # ======================================================

#     encoder = definicao_encoder(colunas_categoricas=None)
#     arvore = modelo_principal()
#     pipeline = formacao_pipeline(encoder, arvore)

#     X_full = df.drop(columns=['risco_queda_faturamento', 'data_venda'])
#     y_full = df['risco_queda_faturamento']


#     print("\n===============================")
#     print("🔁 TESTE DE COMPLEXIDADE DA ÁRVORE")
#     print("===============================")

#     X_full = df.drop(columns=['risco_queda_faturamento', 'data_venda'])
#     y_full = df['risco_queda_faturamento']

#     for depth in [2, 3, 5]:

#         print(f"\n🌳 ÁRVORE max_depth={depth}")

#         encoder = definicao_encoder(colunas_categoricas=None)
#         arvore = modelo_arvore_depth(depth)
#         pipeline = formacao_pipeline(encoder, arvore)

#         evaluate_time_series_cv(
#             pipeline,
#             X_full,
#             y_full,
#             n_splits=5
#         )



#     # ======================================================
#     # 4️⃣ SPLIT TEMPORAL
#     # ======================================================

#     X_train, X_test, y_train, y_test = temporal_train_test_split(
#         df,
#         coluna_alvo='risco_queda_faturamento',
#         test_size=0.20,
#         coluna_data='data_venda'
#     )

#     # ======================================================
#     # 5️⃣ BASELINES
#     # ======================================================

#     dummy = modelo_base()
#     dummy.fit(X_train, y_train)
#     y_pred_dummy = dummy.predict(X_test)

#     y_pred_persistencia = baseline_persistencia(
#         y_train,
#         tamanho_teste=len(y_test)
#     )

#     y_pred_frequencia = baseline_frequencia(
#         y_train,
#         tamanho_teste=len(y_test)
#     )

#     print("\n📊 BASELINES")
#     print("Dummy:", avaliar_classificacao(y_test, y_pred_dummy))
#     print("Persistência:", avaliar_classificacao(y_test, y_pred_persistencia))
#     print("Frequência:", avaliar_classificacao(y_test, y_pred_frequencia))

#     # ======================================================
#     # 6️⃣ MODELO PRINCIPAL
#     # ======================================================

#     encoder = definicao_encoder(colunas_categoricas=None)
#     arvore = modelo_principal()
#     pipeline = formacao_pipeline(encoder, arvore)

#     pipeline.fit(X_train, y_train)

#     y_pred_modelo = pipeline.predict(X_test)
#     resultado_modelo = avaliar_classificacao(y_test, y_pred_modelo)

#     print("\n🌳 MODELO PRINCIPAL")
#     print("Árvore:", resultado_modelo)

#     # ======================================================
#     # 7️⃣ EXPORTAÇÃO
#     # ======================================================

#     with open("engine/ml/modelo_insightsales.pkl", "wb") as f:
#         pk.dump(pipeline, f)

#     print("\n✅ Modelo ML salvo em engine/ml/modelo_insightsales.pkl")


# if __name__ == "__main__":
#     main()




