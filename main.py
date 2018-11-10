import areyip


areyip.projectName = "zero3"
r1 = areyip.SdeclarePin(13,"OUTPUT")


areyip.start()

r1.WdeclarePin()

areyip.mid()

r1.WdigitalPin("HIGH")
areyip.delay(2)
r1.WdigitalPin("LOW")

areyip.end()
