import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


m=Object()
m.name = "praveen"
m.age="27"
m.address=Object()
m.address.village='Adiralu'
m.address.city="hiriyuru"
m.finish="Finished"
print (m.toJSON())
