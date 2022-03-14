import math

class Spell:
    """ Spell parent class """
    def __init__(self, characters):
        for character in characters:
            self.effect(character)


class Rage(Spell):
    """ Rage spell class, doubles the damage and movement speed of the character """
    def __init__(self, characters):
        super().__init__(characters)

    def effect(self, character):
        character.damage *= 2
        character.ms *= 2

class Heal(Spell):
    """ Heal spell class, heals the character by a certain amount """
    def __init__(self, characters):
        super().__init__(characters)

    def effect(self, character):
        character.health += math.floor(character.health/2)
        if character.health > character.maxhealth:
            character.health = character.maxhealth