import numpy as np
import math
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

def CalculForce(a,normale,hauteur,Rho,masse):
    F_Archimede=0
    g=9.81
    Stot=0
    plan=[0,0,1,0]#coef de l'equation cartésienne du plan de l'eau
    """ajustement de la hauteur de la coque """
    translation(2,a,hauteur)

    for n in range(0,len(a)): #on parcour pour le nombre de facettes

        """Calcule de la surface total et de chaque facette"""

        DsVec,Ds=calculeSurface(a[n][0],a[n][1],a[n][2],normale[n])
        Stot+=Ds #surface totale de la coque


        """Calcule de la hauteur d'une facette """
        #Zfk=calculeHauteurFacette(a[n][0],a[n][1],a[n][2])

        """condition pour que une facette soit compté comme immergé """
        if a[n][0][2] <0 and a[n][1][2]<0 and a[n][2][2]<0 :#Totalement immergé
            #print("immergé")
            Zfk=calculeHauteurFacette(a[n][0],a[n][1],a[n][2])
            F_Archimede+=Rho*g*Zfk*DsVec

        elif a[n][0][2] >0 and a[n][1][2] >0 and a[n][2][2] >0:#Totalement non immergé
            F_Archimede+=0
            #print("pas immergé")

        elif a[n][0][2] >0 and a[n][1][2] <0 and a[n][2][2] <0:#seul le premier point de la facette n'est pas immergé
            #print("1")
            #on calcule les vecteurs driecteurs du premier point avec les autres
            D=DetPointPlanDroite(a[n][0],a[n][1],plan)
            #print("le point D ",D)
            E=DetPointPlanDroite(a[n][0],a[n][2],plan)
            #print("le point E ",E)
            #On calcule la surface des deux nouvelles facettes créées puis leur force d'archimede
            Zfk=calculeHauteurFacette(a[n][1],D,E)
            DsVec,Ds=calculeSurface(a[n][1],D,E,normale[n])
            F_Archimede+=Rho*g*Zfk*DsVec
            Zfk=calculeHauteurFacette(a[n][2],D,E)
            DsVec,Ds=calculeSurface(a[n][2],D,E,normale[n])
            F_Archimede+=Rho*g*Zfk*DsVec

        elif a[n][0][2] <0 and a[n][1][2] >0 and a[n][2][2] <0:#seul le deuxème point de la facette n'est pas immergé
            #print("2")
            D=DetPointPlanDroite(a[n][1],a[n][0],plan)
            E=DetPointPlanDroite(a[n][1],a[n][2],plan)
            Zfk=calculeHauteurFacette(a[n][0],D,E)
            DsVec,Ds=calculeSurface(a[n][0],D,E,normale[n])
            F_Archimede+=Rho*g*Zfk*DsVec
            Zfk=calculeHauteurFacette(a[n][2],D,E)
            DsVec,Ds=calculeSurface(a[n][2],D,E,normale[n])
            F_Archimede+=Rho*g*Zfk*DsVec


        elif a[n][0][2] <0 and a[n][1][2] <0 and a[n][2][2] >0:#seul le troisième point de la facette n'est pas immergé
            #print("3")
            D=DetPointPlanDroite(a[n][2],a[n][0],plan)
            E=DetPointPlanDroite(a[n][2],a[n][1],plan)
            Zfk=calculeHauteurFacette(a[n][0],D,E)
            DsVec,Ds=calculeSurface(a[n][0],D,E,normale[n])
            F_Archimede+=Rho*g*Zfk*DsVec
            Zfk=calculeHauteurFacette(a[n][1],D,E)
            DsVec,Ds=calculeSurface(a[n][1],D,E,normale[n])
            F_Archimede+=Rho*g*Zfk*DsVec

        elif a[n][0][2] >0 and a[n][1][2] >0 and a[n][2][2] <0:#seul le troisième point de la facette est immergé
            #print("4")
            D=DetPointPlanDroite(a[n][2],a[n][0],plan)
            E=DetPointPlanDroite(a[n][2],a[n][1],plan)
            Zfk=calculeHauteurFacette(a[n][2],D,E)
            DsVec,Ds=calculeSurface(a[n][2],D,E,normale[n])
            F_Archimede+=Rho*g*Zfk*DsVec

        elif a[n][0][2] >0 and a[n][1][2] <0 and a[n][2][2] >0:#seul le deuxième point de la facette est immergé
            #print("5")
            D=DetPointPlanDroite(a[n][1],a[n][0],plan)
            E=DetPointPlanDroite(a[n][1],a[n][2],plan)
            Zfk=calculeHauteurFacette(a[n][1],D,E)
            DsVec,Ds=calculeSurface(a[n][1],D,E,normale[n])
            F_Archimede+=Rho*g*Zfk*DsVec
        elif a[n][0][2] <0 and a[n][1][2] >0 and a[n][2][2] >0:#seul le premier point de la facette est immergé
            #print(6)
            D=DetPointPlanDroite(a[n][0],a[n][1],plan)
            E=DetPointPlanDroite(a[n][0],a[n][2],plan)
            Zfk=calculeHauteurFacette(a[n][0],D,E)
            DsVec,Ds=calculeSurface(a[n][0],D,E,normale[n])
            F_Archimede+=Rho*g*Zfk*DsVec

    """On remet la hauteur de la coque"""
    translation(2,a,-hauteur)

    """calcule du poid de la coque selon l'axe Oz"""


    F_Poid=(0,0,-1*masse*g)

    """On determine la norme de la resultante du poid plus d'archimède"""

    normeArchimede=np.linalg.norm(F_Archimede)
    print("archi ",F_Archimede)
    print("poid ",F_Poid)
    normePoid=np.linalg.norm(F_Poid)

    difference= normeArchimede-normePoid #Si <0 alors Poid < Archimede sinon >0 alors Poid > Archimede

    return difference


def signif(x, digit):
    ''' Permet de retourné un digit avec un nombre de chiffre significatif defini par digit
    Source : http://www.python-simple.com/python-langage/operations.php'''
    if x == 0:
        return 0
    return round(x, digit - int(math.floor(math.log10(abs(x)))) - 1)

def Dichotomie(Haut,Bas,Precision,a,normale,Rho,masse,potentiometre):
    print('precision : ',Precision,'rho : ',Rho,'masse : ',masse,'Haut,bas :',Haut,Bas)
    Haut+=1
    Bas-=1
    ecart=Bas-Haut
    nb_repetition=0
    listeZmilieu=[]
    while abs(ecart)>Precision:
        Zmilieu=(Haut+Bas)/2
        #print("ecart ",ecart," haut ",Haut," bas ",Bas," Zmilieu ",Zmilieu)

        difference=CalculForce(a,normale,Zmilieu-potentiometre,Rho,masse)
        #print("diff ",difference)
        nb_repetition+=1
        listeZmilieu.append(Zmilieu)
        if difference<0 :
            Haut=Zmilieu

        else : Bas=Zmilieu
        ecart=Haut-Bas
    print(Zmilieu)
    return Zmilieu,nb_repetition,listeZmilieu


def isfloat(str):
    '''retourne si le str est un nombre ou non
    https://www.developpez.net/forums/d1473466/autres-langages/python/general-python/python-verifier-variable-nombre/
    '''
    try:
        float(str)
    except ValueError:
        return False
    return True


def DetPointPlanDroite(A,B,plan):#A et B deux points de R3 un plan une equation cartésienne d'un plan de R3 de la forme ax+by+cz+d
    #plan est une liste des coef a b c d
    AB=calculVecteur(A,B)
    t=(-(plan[3]+plan[0]*A[0]+plan[1]*A[1]+plan[2]*A[2]))/(plan[0]*AB[0]+plan[1]*AB[1]+plan[2]*AB[2])
    #t=-(d+a*Xa+b*Ya+c*Za)/(a*Xab+b*Yab+c*Zab)
    C=(A[0]+AB[0]*t,A[1]+AB[1]*t,A[2]+AB[2]*t)
    return C


def calculeSurface(A,B,C,vec): # trois points sous forme de matrice avec 3 coords et un vecteur normal
    U=calculVecteur(A,B)
    V=calculVecteur(A,C)
    Ds=norme(produitVectoriel(U,V))
    DsVec=Ds*vec
    return DsVec,Ds
