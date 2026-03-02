from engine.db.queries import sales_over_time
from engine.ml.train import train_regression_pipeline

df = sales_over_time()

# Padroniza nome se necessário
df = df.rename(columns={"faturamento_total": "faturamento"})

print("Colunas recebidas:", df.columns)

results = train_regression_pipeline(df)

for model, metrics in results.items():
    print("\n", model)
    for k, v in metrics.items():
        print(f"{k}: {v:.6f}")