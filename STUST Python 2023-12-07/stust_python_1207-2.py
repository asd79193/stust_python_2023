#運動
class Sports:
    def __init__(self,name):
        self._name=name

    @property
    def sports_name(self):
        return self._name


    @sports_name.setter
    def sports_name(self, value):
        self._name=value

    def practice(self):
        print("Doing Sports practice")

#陸上運動
class LandSports(Sports):
    def __init__(self,name,field):
        super().__init__(name)
        self._field=field

    @property
    def landSports_field(self):
        return self._field
    
    def practice(self):
        print("Doing Land Sports practice")


#水上運動
class WaterSports(Sports):
    def __init__(self,name,activity):
        super().__init__(name)
        self._activity=activity

    @property
    def waterSports_activity(self):
        return self._activity
    
    def practice(self):
        print("Doing Water Sports practice")



if __name__ =="__main__":

    #棒球-陸上
    baseball=LandSports("baseball","baseball field")
    print(baseball.sports_name)
    print(baseball.landSports_field)

    #游泳-水上
    swim=WaterSports("swim","swim activity")
    print(swim.sports_name)
    print(swim.waterSports_activity)
    
