label scene_12:

    scene scene_12 with fade

    'Вы заметили вышку, с которой можно осмотреть территорию всего парка.'

    'Подойдя ближе вы замечаете, что она выглядит ненадежно, должно очень повезти, чтобы она не развалилась под человеком. Кого отправите на разведку?'

    menu:
        '[yuno.character.name]' if yuno.alive:
            $ choosenCharacter = yuno
        '[bobby.character.name]' if bobby.alive:
            $ choosenCharacter = bobby
        '[lakmus.character.name]' if lakmus.alive:
            $ choosenCharacter = lakmus
        '[shinji.character.name]' if shinji.alive:
            $ choosenCharacter = shinji

    jump scene_13