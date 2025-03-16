from sklearn.neural_network import MLPRegressor

def build_model(input_dim):
    model = MLPRegressor(hidden_layer_sizes=(64, 64), activation='relu', max_iter=500)
    return model
