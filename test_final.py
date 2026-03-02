# test_final_model.py

from engine.db.queries import sales_over_time
from engine.ml.train_and_save import train_and_save

df = sales_over_time()

df = df.rename(columns={"faturamento_total": "faturamento"})

train_and_save(df, model_name="linear")