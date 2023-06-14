class Map:
    def __init__(self, x, y, name, file, difficulty, bpmscale, game):
        self.x = x
        self.y = y
        self.name = name
        self.file = file
        self.difficulty = difficulty
        self.bpmscale = bpmscale
        self.game = game
        self.r = 50
        self.g = 120
        self.b = 80
  
          
        if self.difficulty == "hard":
            self.r = 165
            self.g = 10
            self.b = 93
        
        
    
    def on_draw(self):
        if self.game.select:
            noStroke()
            fill(255, 255, 255)
            rect(self.x - 100, self.y - 20, self.x + 100, self.y + 20, 30)
            fill(self.r, self.g, self.b)
            rect(self.x - 95, self.y - 15 , self.x + 95, self.y + 15, 25)
            fill(255, 255, 255)
            textSize(20)
            text(str(self.name), self.x, self.y)
            noStroke()
        
    def on_update(self):
        if self.x - 100 < mouseX < self.x + 100 and self.y - 20 < mouseY < self.y + 20 and self.game.select:
            fill(255, 255, 255, 50)
            rect(self.x - 102, self.y - 22, self.x + 102, self.y + 22, 30)
        
    def on_mouse_clicked(self, mouseX, mouseY):
        if self.x - 100 < mouseX < self.x + 100 and self.y - 20 < mouseY < self.y + 20 and self.game.select:
            
            with open(str(self.file)) as file:
                u=[]
                for row in file:
                    row = row.strip()
                    self.game.j = row.split(",")
                    for c in range(len(self.game.j)):
                        self.game.j[c] = self.game.j[c]
                    self.game.j[2] = float(self.game.j[2])
                    self.game.j[2] = self.game.j[2] / self.bpmscale
                    u = self.game.j[5].split(":")
                    self.game.j[5]=int(u[0])
                    self.game.j[5] /= self.bpmscale
                    self.game.j[2] = int(self.game.j[2])
                    self.game.j[5] = int(self.game.j[5])
                    self.game.i.append(self.game.j)
                self.game.endtime = self.game.i[-1][2]
                    
            self.game.difficulty = "hard"
            self.game.menu = False
            self.game.play = True
            self.game.select = False
            self.game.notes = []
            self.game.count = -20
            self.game.notecount = 0
            self.game.hits = 0
            self.game.go = True
            self.game.hp = 500
            
            
