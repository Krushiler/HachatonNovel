python:
    import random
label scene_11:
    'Выберите персонажа, который пойдет успокаивать синдзи'
    menu:
        if yuno.alive():
            "[yuno.character.name]":
                $ choosenCharacter = yuno
        if bobby.alive():
            "[bobby.character.name]":
                $ choosenCharacter = bobby
        if lakmus.alive():
            "[lakmus.character.name]":
                $ choosenCharacter = lakmus
    '[choosenCharacter.character.name] пытается успокоить [shinji.character.name]'
    python:
        chance = random.randint(1,4)
    if chance >= choosenCharacter.character.stats.motivation:
        "Синдзи окончательно теряет рассудок, вам придется продолжить без него."
        shinji.die()


