import numpy as np
from matplotlib import pyplot as plt


# for apple
mean_01 = np.array([3.0,4.0])
cov_01 = np.array([[1.0,-0.5],[-0.5,1.0]])
#for leman(sweetness and color)
# Red is higher and yello is lower value
# sweetnes is higher and surness in lesser value

#  for Lemon
mean_02 = np.array([0.0,0.0])
cov_02 = np.array([[1.5,0.5],[0.5,0.6]])
#2x2 identity matrix
# Arrays of array


dist_01 = np.random.multivariate_normal(mean_01,cov_01,200)
dist_02 = np.random.multivariate_normal(mean_02,cov_02,200)


print dist_01.shape
print dist_02.shape
#print  dist_01


# Try to make scatter plot

plt.figure(0)

for x in range(dist_01.shape[0]):
    plt.scatter(dist_01[x,0],dist_01[x,1],color='red')
    plt.scatter(dist_02[x, 0], dist_02[x, 1], color='yellow')
#plt.show()


# Training data preperation of apples and lemons

# Using 400 Samples (200 for Apples and 200 for Lemons )

labels = np.zeros((400,1))
labels[200:] = 1.0

X_data = np.zeros((400,2))
X_data[:200, :] = dist_01
X_data[200:, :] = dist_02

print X_data
print labels



# KNN  Algorithm :)



#Dist of the query_point to all other points in the space ( O(N)) time for every point + sorting


#Euclidean Distance

def dist( x1 , x2):
    return np.sqrt(((x1-x2)**2).sum())

x1 = np.array([0.0,0.0])
x2 = np.array([1.0,1.0])

print dist(x1,x2)





def knn(X_train, query_point, y_train, k=5):
    vals = []

    for ix in range(X_train.shape[0]):
        v = [dist(query_point, X_train[ix, :]), y_train[ix]]
        vals.append(v)
    # vals is a list containing distances and their labels

    updated_vals = sorted(vals)

    # Lets us pick up top K values

    pred_arr = np.asarray(updated_vals[:k])
    pred_arr = np.unique(pred_arr[:, 1], return_counts=True)
    # Largest Occurence
    print pred_arr

# q = np.array([2.0,2.0])
# knn(X_data,q,labels)

    # Largest Occurence

    index = pred_arr[1].argmax()     # Index of largest freq
    return pred_arr[0][index]


q = np.array([0.0, 4.0])

predicted_label = knn(X_data, q, labels)

#if predicted label is 0.0 then apple else lemon

print predicted_label
#
# ## Run a Loop over a testing data(Split the original data into 2 sets - Training, Testing)
#
# # FInd predictions for Q Query points
#
# # If predicted outcome = actual outcome -> Sucess else Failure
#
# # Accuracy =  (Successes)/ (Total no of testing points) * 100