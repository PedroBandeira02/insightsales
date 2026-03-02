import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def evaluate(y_true, y_pred):

    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }


def summarize(results_list):

    summary = {}

    for metric in ["MAE", "RMSE", "R2"]:
        values = [res[metric] for res in results_list]

        summary[f"{metric}_mean"] = np.mean(values)
        summary[f"{metric}_std"] = np.std(values)

    return summary

































# from sklearn.metrics import accuracy_score
# import numpy as np

# def avaliar_classificacao(y_true, y_pred):
#     return {
#         "accuracy": accuracy_score(y_true, y_pred)
#     }


# def analyze_class_distribution(y, verbose=True):
#     y = np.array(y)
#     total = len(y)

#     unique, counts = np.unique(y, return_counts=True)
#     distribution = dict(zip(unique, counts))

#     results = {}

#     for cls in [0, 1]:
#         count = distribution.get(cls, 0)
#         pct = count / total if total > 0 else 0

#         results[cls] = {
#             "count": count,
#             "percentage": round(pct * 100, 2)
#         }

#     imbalance_ratio = (
#         min(results[0]["count"], results[1]["count"]) /
#         max(results[0]["count"], results[1]["count"])
#         if max(results[0]["count"], results[1]["count"]) > 0
#         else 0
#     )

#     results["imbalance_ratio"] = round(imbalance_ratio, 3)

#     if verbose:
#         print("\n📊 DISTRIBUIÇÃO DA VARIÁVEL TARGET")
#         print("-" * 40)
#         print(f"Total de observações: {total}")
#         print(f"Não queda (0): {results[0]['count']} ({results[0]['percentage']}%)")
#         print(f"Queda (1): {results[1]['count']} ({results[1]['percentage']}%)")
#         print(f"Razão de desbalanceamento: {results['imbalance_ratio']}")
#         print("-" * 40)

#         if results["imbalance_ratio"] < 0.5:
#             print("⚠ Dataset consideravelmente desbalanceado.")
#         else:
#             print("✔ Dataset relativamente equilibrado.")

#     return results


# from sklearn.model_selection import TimeSeriesSplit
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# def evaluate_time_series_cv(model_pipeline, X, y, n_splits=5):

#     tscv = TimeSeriesSplit(n_splits=n_splits)

#     accuracies = []
#     precisions = []
#     recalls = []
#     f1s = []

#     print("\n🔁 VALIDAÇÃO CRUZADA TEMPORAL")
#     print("-" * 40)

#     split_number = 1

#     for train_index, test_index in tscv.split(X):

#         X_train, X_test = X.iloc[train_index], X.iloc[test_index]
#         y_train, y_test = y.iloc[train_index], y.iloc[test_index]

#         model_pipeline.fit(X_train, y_train)
#         y_pred = model_pipeline.predict(X_test)

#         acc = accuracy_score(y_test, y_pred)
#         prec = precision_score(y_test, y_pred, zero_division=0)
#         rec = recall_score(y_test, y_pred, zero_division=0)
#         f1 = f1_score(y_test, y_pred, zero_division=0)

#         accuracies.append(acc)
#         precisions.append(prec)
#         recalls.append(rec)
#         f1s.append(f1)

#         print(f"\nSplit {split_number}")
#         print(f"Accuracy: {round(acc, 3)}")
#         print(f"Precision: {round(prec, 3)}")
#         print(f"Recall: {round(rec, 3)}")
#         print(f"F1-score: {round(f1, 3)}")

#         split_number += 1

#     print("\n📊 MÉDIAS")
#     print("-" * 40)
#     print(f"Accuracy média: {round(np.mean(accuracies), 3)} ± {round(np.std(accuracies), 3)}")
#     print(f"Precision média: {round(np.mean(precisions), 3)} ± {round(np.std(precisions), 3)}")
#     print(f"Recall média: {round(np.mean(recalls), 3)} ± {round(np.std(recalls), 3)}")
#     print(f"F1 média: {round(np.mean(f1s), 3)} ± {round(np.std(f1s), 3)}")

#     return {
#         "accuracy_mean": np.mean(accuracies),
#         "accuracy_std": np.std(accuracies),
#         "precision_mean": np.mean(precisions),
#         "precision_std": np.std(precisions),
#         "recall_mean": np.mean(recalls),
#         "recall_std": np.std(recalls),
#         "f1_mean": np.mean(f1s),
#         "f1_std": np.std(f1s)
#     }
