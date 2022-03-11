import math

class Spell:
    def __init__(self, characters):
        for character in characters:
            self.effect(character)


class Rage(Spell):
    def __init__(self, characters):
        super().__init__(characters)

    def effect(self, character):
        character.damage *= 2
        character.ms *= 2

class Heal(Spell):
    def __init__(self, characters):
        super().__init__(characters)

    def effect(self, character):
        character.health += math.floor(character.health/2)
        if character.health > character.maxhealth:
            character.health = character.maxhealth