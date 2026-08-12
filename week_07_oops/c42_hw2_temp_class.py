# Ek Temperature class banao with _celsius; ek method set_celsius jo -273 se kam value reject kare.

class Temperature :
    def __init__(self,celsius):
        self._celsius = celsius

    def set_celsius(self,value):
        if value <= -273:
            print("invalied")
            return

        self._celsius = value
        print(f"Temp update {self._celsius}")


tem_ob_1 = Temperature(500)

tem_ob_1.set_celsius(273)

tem_ob_2 = Temperature(273)

tem_ob_1.set_celsius(20)

tem_ob_1.set_celsius(-300)

tem_ob_2.set_celsius(20)

tem_ob_2.set_celsius(-300)

