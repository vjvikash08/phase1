class ToyBox:
    def __init__(self,toys):
        self.toys = toys
        
    def __len__(self):
        return len(self.toys)
    
boy = ToyBox(["Mouse","Laser point","Catpins"])
print(len(boy))