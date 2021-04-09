import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
from functools import partial 
from scipy import signal
import fnc.matching
import fnc.extractFeature

class Olho:

    def __init__(self,caminho,id):
        print("Construir Objeto .. {}".format(self))
        self.caminho = caminho
        self.id = id
    
    def extrairCodigo(self):

        img = cv2.imread(self.caminho,0)
        

        info1 = fnc.extractFeature.extractFeature(self.caminho,80,True)
                


        return info1


def compararHd(info1,info2):

    hd = fnc.matching.calHammingDist(info1[0],info1[1],info2[0],info2[1])
        
    print(hd)


   



    





