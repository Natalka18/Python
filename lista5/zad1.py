import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# parametry
TOY_STORY_ID = 1


def linear_regression(m):
    # przygotowanie danych

    data = pd.read_csv('dane/ml-latest-small/ratings.csv')
    data = data[['userId', 'movieId', 'rating']]

    # lista zawierająca id użytkowników, którzy ocenili toy story
    users = [n for index, n in enumerate(data.userId)
             if data.movieId[index] == TOY_STORY_ID]
    condition = ((data.userId.isin(users)) & (data['movieId'] <= m))

    toy_story_data = data[condition]

    data_X = toy_story_data.pivot(index='userId', columns='movieId', values='rating').to_numpy()
    data_X = data_X[:, 1:]
    X = np.nan_to_num(data_X)
    Y = toy_story_data[toy_story_data['movieId'] == TOY_STORY_ID].rating.to_numpy()

    factors = np.linalg.lstsq(X, Y, rcond=None)[0]

    return users, X, Y, factors


# wykresy
ms = [10, 100, 1000]
for m in ms:
    _users, _X, _Y, _factors = linear_regression(m)
    x = np.array(list(range(len(_users))))
    y = np.absolute(_Y - np.matmul(_X, _factors))
    _ = plt.plot(x, y, 'o', label=f'Błędy dla m = {m}')
    _ = plt.xlabel('Numer użytkownika')
    _ = plt.ylabel('Błąd')
    _ = plt.legend()
    plt.show()

# predykcje

ms = [10, 100, 200, 500, 1000, 10000]
for m in ms:
    _users, _X, _Y, f = linear_regression(m)
    newX = _X[0:200]
    restX = _X[200:]
    newY = _Y[0:200]
    factors = np.linalg.lstsq(newX, newY, rcond=None)[0]
    x = np.array(list(range(len(_users) - 200)))
    predictions = np.matmul(restX, factors)
    y = _Y[200:]
    _ = plt.plot(x, predictions, 'o', label=f'Predykcje dla m = {m}')
    _ = plt.plot(x, y, 'o', label='Ocena')
    _ = plt.xlabel('Numer użytkownika')
    _ = plt.ylabel('Ocena')
    _ = plt.legend()
    plt.show()
