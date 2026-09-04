import numpy as np
from vectors import rescale, similarity

names =np.genfromtxt('state_facts-1.csv', delimiter = ',' ,  skip_header=1, usecols=0, dtype=str)
data = np.genfromtxt('state_facts-1.csv', delimiter = ',' ,  skip_header=1)

#drop column
data = data[:, 1:]
#rescale
data_rescaled = rescale(data)
#find va
va_index = np.where(names == 'Virginia')[0][0]
#rescale va
va_vector = data_rescaled[va_index]

similar_state = None

most_similar = -1

for i in range(data_rescaled.shape[0]):
    if names[i] == 'Virginia':
        continue #ignores va index
    sim = similarity(va_vector, data_rescaled[i])
    if sim > most_similar:
        most_similar = sim
        similar_state = names[i] #finds similarity

print(f"The state most similar to Virginia is {similar_state} cosine similarity = {most_similar:.4f})")

#The state most similar to Virginia is Maryland cosine similarity = 0.9185)
