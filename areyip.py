def projectName(filename):
    open(filename + ".txt", "w")
    return filename

projectName = "outfile"

def start():
    f = open(projectName + ".txt", "a")
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
        f = open(projectName + ".txt", "a")
        f.write("pinMode(" + str(self.pin) + "," + self.onoff + ");\n")