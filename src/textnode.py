from enum import Enum



class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"



class TextNode:
    text = ''
    text_type = ''
    url = None

    def __eq__(self, node2):
        if self == node2:
            return True
        return False


    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
        