import numpy as np
from collections import Counter
def euclidean_distances(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))
def knn(training_pt, training_label, test_pt, k = 3):
    training_pt = np.array(training_pt)
    test_pt = np.array(test_pt)
    distance = np.sqrt(np.sum((test_pt - training_pt) ** 2, axis=1))
    k_indices = distance.argsort()[:k]
    k_nearest = [training_label[i] for i in k_indices]
    most_common = Counter(k_nearest).most_common(1)[0][0]
    return most_common

