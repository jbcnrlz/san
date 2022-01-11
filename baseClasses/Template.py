from PIL import Image as im
from helper.functions import loadOBJ
import numpy as np, sys, os

class Template:

    def saveImageTraining(self,avgImageSave=True):
        pass

    def loadImage(self):
        pass

    def save(self):
        pass

    def getRawRepr(self):
        return self.__rawRepr

    def setRawRepr(self,value):
        self.__rawRepr = value
        if not self.lazyLoading:
            self.loadImageData()

    def isFileExists(self,pathImage):
        pass

    def existsPreProcessingFile(self):
        pass

    def loadImageData(self):
        if (self.__rawRepr[-3:] == 'obj'):
            self.imageLoaded = True
            imageFace = None
            if str(type(self)) == "<class 'LFWTemplate.LFWTemplate'>":
                a, b, imageFace, y, facets = loadOBJ(self.__rawRepr,True)
                self.facets = facets
            else:
                a, b, imageFace, y = loadOBJ(self.__rawRepr)
            self.image = imageFace
        elif (self.__rawRepr[-3:] == 'jpg'):
            self.imageLoaded = True
            self.image = im.open(self.__rawRepr)
        elif (self.__rawRepr[-3:] == 'bmp'):
            self.imageLoaded = True
            self.image = im.open(self.__rawRepr).convert('L')

    rawRepr = property(getRawRepr,setRawRepr)

    def getItemClass(self):
        return self.__itemClass

    def setItemClass(self,value):
        self.__itemClass = int(value)

    itemClass = property(getItemClass,setItemClass)

    def getImage(self):
        if self.lazyLoading and not self.imageLoaded:
            self.loadImageData()     

        return self.__image

    def setImage(self,value):
        if not value is None:
            self.imageLoaded = True
        self.__image = value

    image = property(getImage,setImage)

    __itemClass = None
    __rawRepr = None
    typeTemplate = None
    features = None
    __image = None
    probability = None
    lazyLoading = None
    modelDatabase = None
    dataset = None

    def __init__(self,pathFile,typeTemplate,lazy=False,dataset=None):
        self.imageLoaded = not lazy
        self.lazyLoading = lazy
        self.rawRepr = pathFile
        self.typeTemplate = typeTemplate
        self.dataset = dataset
        #self.modelDatabase = self.getModel()


    def saveMasks(self,folder,type):
        pass