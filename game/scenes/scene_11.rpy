label scene_11:
    'Выберите персонажа, который пойдет успокаивать синдзи'

    menu:
        '[yuno.character.name]' if yuno.alive:
            $ choosenCharacter = yuno
        '[bobby.character.name]' if bobby.alive:
            $ choosenCharacter = bobby
        '[lakmus.character.name]' if lakmus.alive:
            $ choosenCharacter = lakmus
    '[choosenCharacter.character.name] пытается успокоить [shinji.character.name]'

    $ chance = renpy.random.randint(1,4)
    if chance >= choosenCharacter.stats.motivation.value:
        'Синдзи окончательно теряет рассудок, вам придется продолжить без него.'
        $ shinji.die()

    menu:
        'тык 17':
            jump scene_17
        'тык 20':
            jump scene_20


