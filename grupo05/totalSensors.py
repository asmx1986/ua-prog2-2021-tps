class TotalSensors:
    ActiveSensors = []
    DesactiveSensors = []

    @classmethod
    def ActivateSensor(cls,sensor):
        cls.ActiveSensors.append(sensor)
        cls.DesactiveSensors.remove(sensor)

    @classmethod
    def DesactiveSensor(cls,sensor):
        cls.ActiveSensors.remove(sensor)
        cls.DesactiveSensors.append(sensor)

    @classmethod
    def searchActiveSensor(cls,sensor):
        for ActiveSensor in cls.ActiveSensors:
            if ActiveSensor == sensor:
                return ActiveSensor
            else:
                raise Exception


    @classmethod
    def searchDesactiveSensor(cls,sensor):
        for DesactiveSensor in cls.DesactiveSensors:
            if DesactiveSensor == sensor:
                return DesactiveSensor
            else:
                raise Exception

    @classmethod
    def existActiveSensor(cls,x,y):
        a = 0
        for sensor in cls.ActiveSensors:
            if str(sensor.location.getX()) == x and str(sensor.location.getY()) == y:
                a = 1
                return sensor
        if a == 0:
            return None


    @classmethod
    def addSensor(cls,sensor):
        cls.ActiveSensors.append(sensor)


