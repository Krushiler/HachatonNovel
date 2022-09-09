init python:
    class Stat:
        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __str__(self):
            return f'{self.name}: {self.value}'

    class ActorStats:
        def __init__(self, motivation=1, communication=1, strength=1, luck=1):
            self.motivation = Stat('мотивация', motivation)
            self.communication = Stat('коммуникативность', communication)
            self.strength = Stat('сила', strength)
            self.luck = Stat('удача', luck)

        def getStatsArray(self):
            return [(self.intellect.name, self.intellect.value)]


    class Actor:
        def __init__(self, character, stats=ActorStats(), description=''):
            self.character = character
            self.stats = stats
            self.description = description
            self.alive = true

        def getStatsArray(self):
            return self.stats.getStatsArray()

        def alive():
            return self.alive

        def die():
            self.alive = true
