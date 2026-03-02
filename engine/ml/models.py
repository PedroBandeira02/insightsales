from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor


def get_models():

    models = {
        "linear": LinearRegression(),
        "ridge": Ridge(alpha=1.0),
        "lasso": Lasso(alpha=0.01),
        "tree": DecisionTreeRegressor(max_depth=3, random_state=0),
        "rf": RandomForestRegressor(
            n_estimators=50,
            max_depth=3,
            random_state=0
        ),
    }

    return models


















# from sklearn.compose import make_column_transformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.dummy import DummyClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.pipeline import Pipeline

# def definicao_encoder(colunas_categoricas = None):
#     if not colunas_categoricas:
#         return 'passthrough'
    
#     encoder = make_column_transformer((OneHotEncoder(drop= 'if_binary'),
#                                        colunas_categoricas),
#                                        remainder= 'passthrough',
#                                        sparse_threshold= 0)
#     return encoder

# def modelo_base ():
#     dummy = DummyClassifier(strategy= 'most_frequent')
#     return dummy

# def modelo_principal ():
#     tree = DecisionTreeClassifier(max_depth=4, min_samples_leaf=10, random_state=5)
#     return tree

# def formacao_pipeline (encoder, modelo):
#     pipeline = Pipeline(steps= [('encoder', encoder),
#                                 ('modelo', modelo)])
#     return pipeline

# from sklearn.tree import DecisionTreeClassifier

# def modelo_arvore_depth(depth):
#     return DecisionTreeClassifier(
#         max_depth=depth,
#         random_state=42
#     )
