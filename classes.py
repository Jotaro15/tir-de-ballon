class Impact:
    """ classe permettant d'enregistrer l'emplacement des impact pour les "bliter" ensuite"""
    def __init__(self,fenetre,image):
        self.mf = fenetre
        self.nb = 0
        self.impact = image
        self.list_x = []
        self.list_y = []
        
        self.i = -1
        self.nb = -1
    def enregistrer(self, x_centre_viseur, y_centre_viseur):
        self.x_centre_viseur = x_centre_viseur
        self.y_centre_viseur = y_centre_viseur
        
        self.list_x.append(self.x_centre_viseur)
        self.list_y.append(self.y_centre_viseur)

        self.nb += 1
    def afficher(self, x_centre_viseur, y_centre_viseur):
        self.x_centre_viseur = x_centre_viseur
        self.y_centre_viseur = y_centre_viseur
        
        while self.i < self.nb:
            self.i += 1
            self.mf.blit(self.impact,(self.list_x[self.i],self.list_y[self.i]))
        #self.mf.blit(self.impact,(self.x_centre_viseur,self.y_centre_viseur))
        self.i = -1

