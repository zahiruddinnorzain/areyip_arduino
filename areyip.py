
projectName = "outfile"

def start():
    f = open(projectName + ".txt", "w")
    f.write("void main(){ \n\n")

        
def mid():
    f = open(projectName + ".txt", "a")
    f.write("\n\n}\n\nvoid loop(){ \n\n")
    
def end():
    f = open(projectName + ".txt", "a")
    f.write("\n\n}")
        
def delay(x):
    x=x*1000
    f = open(projectName + ".txt", "a")
    f.write("delay(" + str(x) + ");\n")


class SdeclarePin:
    def __init__(self, pin, kondisi):
        self.pin = pin
        self.kondisi = kondisi
        
    
    def WdeclarePin(self):
        f = open(projectName + ".txt", "a")
        f.write("pinMode(" + str(self.pin) + "," + self.kondisi + ");\n")
    
    def WdigitalPin(self, onoff):
        self.onoff = onoff
        
        if self.kondisi == "OUTPUT":
            f = open(projectName + ".txt", "a")
            f.write("pinMode(" + str(self.pin) + "," + self.onoff + ");\n")
        
        if self.kondisi != "OUTPUT":
            print("ERROR: CANNOT READ INPUT. CHANGE INPUT TO OUTPUT AT PIN " + str(self.pin) + "\n")
        
    #sensor = analogRead(pin)
    def WanalogRead(self, datain):
        self.datain = datain
        
        if self.kondisi == "INPUT":
        
            f = open(projectName + ".txt", "a")
            f.write(datain + " = analogRead(" + str(self.pin) + ");" )
            
        if self.kondisi != "INPUT":
            print("ERROR: CANNOT READ OUTPUT. CHANGE OUTPUT TO INPUT AT PIN " + str(self.pin) + "\n")