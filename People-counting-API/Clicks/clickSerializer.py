from json import JSONEncoder

class ClickEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__  
