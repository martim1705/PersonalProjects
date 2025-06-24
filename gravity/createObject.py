class Object: 
    
    def __init__(self, radius: float, color: str, posX: float, posY: float):
        self._radius = radius
        self._color = color
        self.posX = posX
        self.posY = posY

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY
    
    def getColor(self):
        return self._color
    
    def getRadius(self): 
        return self._radius
    
    def pos(self):
        return (self.posX, self.posY)
    
    