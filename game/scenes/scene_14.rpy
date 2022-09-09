label scene_14:

    scene scene_14 with fade

    'Вышка обвалилась и придавила [choosenCharacter.character.name]. Вы решаете попробовать вытащить его, но вам понадобится много сил, чтобы это сделать'

    'кто пойдет помогать?'
    $ tempChoosenCharacter = choosenCharacter
    menu:
        '[yuno.character.name]' if yuno.alive:
            $ choosenCharacter = yuno
        '[bobby.character.name]' if bobby.alive:
            $ choosenCharacter = bobby
        '[lakmus.character.name]' if lakmus.alive:
            $ choosenCharacter = lakmus
        '[shinji.character.name]' if shinji.alive:
            $ choosenCharacter = shinji

    if chance >= choosenCharacter.stats.strength.value:
        '[choosenCharacter.character.name] Удаётся спасти [tempChoosenCharacter.character.name].'
    else:
        '[choosenCharacter.character.name] Не удалось помочь [tempChoosenCharacter.character.name], вам придется продолжить путь без [tempChoosenCharacter.character.name]'
        $ tempChoosenCharacter.die()

    'Вы отправляетесь к колесу обозрения.'

    jump scene_15