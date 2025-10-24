import math
from collections import Counter

def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def knn(test_pt, training_label, training_pt, k=3):
    distances = []
    for i in range(len(training_pt)):
        dist = euclidean_distance(test_pt, training_pt[i])
        distances.append((dist, training_label[i]))

    distances.sort(key=lambda x: x[0])

    k_nearest = distances[ :k]

    labels = (label for (_, label) in k_nearest)
    most_common = Counter(labels).most_common(1)[0][0]
    return most_common

train_X = [[1,2],[2,3],[3,3],[6,5],[7,7],[8,6]]
train_y = ['A','A','A','B','B','B']

print(knn([5,5], train_y, train_X, k=3))

