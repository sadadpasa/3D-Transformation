import math
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.shape_base import block

transform_matrix = np.identity(4, dtype=float)

def translation(matrix, x, y, z):
    transform_matrix[0][3] = x
    transform_matrix[1][3] = y
    transform_matrix[2][3] = z
    new_matrix = np.dot(transform_matrix, matrix)
    return new_matrix

def scaling(matrix, x, y, z):
    transform_matrix[0][0] = x
    transform_matrix[1][1] = y
    transform_matrix[2][2] = z
    new_matrix = np.dot(transform_matrix, matrix)
    return new_matrix

def rotation_x(matrix, degree, x, y, z):
    transform_matrix[1][1], transform_matrix[2][2] = math.cos(math.radians(degree))
    transform_matrix[1][2] = -math.sin(math.radians(degree))
    transform_matrix[2][1] = math.sin(math.radians(degree))
    new_matrix = translation(new_matrix, -x, -y, -z)
    new_matrix = np.dot(transform_matrix, matrix)
    new_matrix = translation(new_matrix, x, y, z)
    return new_matrix

def rotation_y(matrix, degree, x, y, z):
    transform_matrix[0][0], transform_matrix[2][2] = math.cos(math.radians(degree))
    transform_matrix[0][2] = math.sin(math.radians(degree))
    transform_matrix[2][0] = -math.sin(math.radians(degree))
    new_matrix = translation(new_matrix, -x, -y, -z)
    new_matrix = np.dot(transform_matrix, matrix)
    new_matrix = translation(new_matrix, x, y, z)
    return new_matrix

def rotation_z(matrix, degree, x, y, z):
    transform_matrix[0][0], transform_matrix[1][1] = math.cos(math.radians(degree))
    transform_matrix[0][1] = -math.sin(math.radians(degree))
    transform_matrix[1][0] = math.sin(math.radians(degree))
    new_matrix = translation(new_matrix, -x, -y, -z)
    new_matrix = np.dot(transform_matrix, matrix)
    new_matrix = translation(new_matrix, x, y, z)
    return new_matrix

def shear_xy(matrix, x, y):
    transform_matrix[0][2] = x
    transform_matrix[1][2] = y
    new_matrix = np.dot(transform_matrix, matrix)
    return new_matrix

def shear_yz(matrix, y, z):
    transform_matrix[1][1] = y
    transform_matrix[2][1] = z
    new_matrix = np.dot(transform_matrix, matrix)
    return new_matrix

def shear_xz(matrix, x, z):
    transform_matrix[0][0] = x
    transform_matrix[2][0] = z
    new_matrix = np.dot(transform_matrix, matrix)
    return new_matrix

  
x_list = []
y_list = []
z_list = []
w_list = []

n = int(input("berapa titik yang akan di transformsi? "))
for i in range(n):
    print("titik ke-", i+1)
    x_list.append(int(input("x : ")))
    y_list.append(int(input("y : ")))
    z_list.append(int(input("z : ")))
    w_list.append(1)

    
matrix = []
matrix.append(x_list)
matrix.append(y_list)
matrix.append(z_list)
matrix.append(w_list)

new_matrix = matrix
lanjut = True
while lanjut == True:
    print("pilih metode transformasi yang ingin dilakukan : \n1. Translasi \n2. Scaling \n3. Rotasi \n4. Shear")
    methode = int(input("pilih sesuai nomor \n"))
    if methode == 1:
        x = int(input("geser x sejauh : "))
        y = int(input("geser y sejauh : "))
        z = int(input("geser z sejauh : "))
        new_matrix = translation(new_matrix, x, y, z)
    elif methode == 2:
        x = int(input("scale x sebanyak : "))
        y = int(input("scale y sebanyak : "))
        z = int(input("geser z sebanyak : "))
        new_matrix = scaling(new_matrix, x, y, z)
    elif methode == 3:
        print("pilih sumbu rotasi yang ingin dilakukan : \n1. x \n2. y \n3. z")
        axis = int(input("pilih sesuai nomor \n"))
        degree = int(input("putar sebanyak (derajat): "))
        x = int(input("titik pusat x : "))
        y = int(input("titik pusat y : "))
        z = int(input("titik pusat z : "))
        if axis == 1:
            new_matrix = rotation_x(new_matrix, degree, x, y, z)
        elif axis == 2:
            new_matrix = rotation_y(new_matrix, degree, x, y, z)
        elif axis == 3:
            new_matrix = rotation_z(new_matrix, degree, x, y, z)
    elif methode == 4:
        print("pilih sumbu rotasi yang ingin dilakukan : \n1. xy \n2. yz \n3. xz")
        shear = int(input("pilih sesuai nomor \n"))
        if shear == 1 or shear == 3:
            x = int(input("shear x sebesar : "))
        if shear == 1 or shear == 2:
            y = int(input("shear y sebesar : "))
        if shear == 2 or shear == 3:
            z = int(input("shear z sebesar : "))

        if axis == 1:
            new_matrix = shear_xy(new_matrix, x, y)
        elif axis == 2:
            new_matrix = shear_yz(new_matrix, y, z)
        elif axis == 3:
            new_matrix = shear_xz(new_matrix, x, z)
            

    print("matrix hasil transformasi : \n", new_matrix)

    # Creating figure
    fig = plt.figure(figsize = (10, 7))
    ax = plt.axes(projection ="3d")

    # Creating plot
    ax.scatter3D(new_matrix[0], new_matrix[1], new_matrix[2], color = "green")
    plt.title("simple 3D scatter plot")

    # show plot
    plt.show(block=True)

    state = input("lakukan transformasi lagi? (y/n)") 
    if state == "y":
        lanjut = True
    elif state == "n":
        lanjut = False
