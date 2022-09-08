init python:
    class Stat:
        def __init__(self, name, value):
            self.name = name
            self.value = value

        def __str__(self):
            return f'{self.name}: {self.value}'

    class ActorStats:
        def __init__(self, intellect=5):
            self.intellect = Stat("Интеллект", intellect)

        def getStatsArray(self):
            return [(self.intellect.name, self.intellect.value)]


    class Actor:
        def __init__(self, character, stats=ActorStats()):
            self.character = character
            self.stats = stats

        def getStatsArray(self):
            return self.stats.getStatsArray()
