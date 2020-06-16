import numpy as np

def produitVectoriel(u,v):
    w=np.cross(u,v)
    return w


def norme(u):
    return np.linalg.norm(u)


def translation(axe,matriceCoord,translation):#axe : 0=x; 1=y; 2=z
    for i in range(len(matriceCoord)):#on parcout les lignes de la matrice
        matriceCoord[i][0][axe]+=translation
        matriceCoord[i][1][axe]+=translation
        matriceCoord[i][2][axe]+=translation


def calculVecteur(A,B):#deux points avec trois coords sous forme de matrice
    vecteur=(B[0]-A[0],B[1]-A[1],B[2]-A[2])
    return vecteur


def calculeHauteurFacette(A,B,C): # trois points sous forme de matrice avec 3 coords
    hauteur=(A[2]+B[2]+C[2])/3
    return hauteur


