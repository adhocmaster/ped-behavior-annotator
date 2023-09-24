from enum import Enum

class PedestrianTag(Enum):
    Flinch = "Flinch"
    Crash = "Crash"
    Jaywalking = "Jaywalking"
    Distracted = "Distracted"

# PedestrianTag.Flinch == this is an object
# PedestrianTag.Flinch.value == "Flinch" this is a string