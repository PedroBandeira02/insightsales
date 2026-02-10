from sklearn.metrics import accuracy_score

def avaliar_classificacao(y_true, y_pred):
    return {
        "accuracy": accuracy_score(y_true, y_pred)
    }

