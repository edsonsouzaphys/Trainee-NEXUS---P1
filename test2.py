import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

L = 20
redeSpins = np.random.randint(0, 2, size=(L, L)) * 2 - 1

im = ax.imshow(redeSpins)



plt.show()

"""print(redeSpins)
 #Conferir -1 +1
print("Network Size:", redeSpins.shape)
print("Actual Values:", np.unique(redeSpins))"""

#Tipos de Spin
negative_quatities = np.sum(redeSpins == -1)
positive_quantities = np.sum(redeSpins == 1)


print("Spins -1:", negative_quatities)
print("Spins +1:", positive_quantities)

#Contador de Posições L aleatórios da Matriz +1 e -1
i = np.random.randint(0, L)
j = np.random.randint(0, L)

print("Choosen Position:", i, j)
print("Chosen spin:", redeSpins[i, j])

        

