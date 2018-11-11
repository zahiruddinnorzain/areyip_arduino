import areyip


areyip.projectName = "zero33"
r1 = areyip.SdeclarePin(13,"OUTPUT")
r2 = areyip.SdeclarePin(12,"INPUT")
r3 = areyip.Sblynk("abc7","botak","ppkk")

r3.startBlynk()
#areyip.start()

r1.WdeclarePin()
r2.WdeclarePin()

areyip.mid()

r1.WdigitalPin("HIGH")
areyip.delay(2)
r1.WdigitalPin("LOW")
areyip.delay(1)
r2.WanalogRead("sensor")
areyip.show("sensor")

areyip.end()
