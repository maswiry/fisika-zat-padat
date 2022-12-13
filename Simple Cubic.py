import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Permodelan sederhana struktur kristal Simple Cubic
#maswiryy

#Menentukan jumlah atom pada kekisi
n = int(input("Masukkan jumlah atom pada kekisi (biasanya 2):"))

#Membuat array 3D dari zeros untuk menyimpan posisi atom pada kekisi
kekisi = np.zeros((n,n,n,3))

# Loop through the lattice and assign the positions of the atoms
#Loop melewati kekisi dan memasukkan posisi dari atom
for i in range(n):
    for j in range(n):
        for k in range(n):
            kekisi[i,j,k,0] = i
            kekisi[i,j,k,1] = j
            kekisi[i,j,k,2] = k

#membuat figure untuk memplotkan struktur kristal
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


#Memplot posisi atom-atom pada kekisi
ax.scatter(kekisi[:,:,:,0], kekisi[:,:,:,1], kekisi[:,:,:,2])

#menunjukkan plot
plt.show()