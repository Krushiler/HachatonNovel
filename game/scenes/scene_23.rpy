label scene_23:
    scene scene_8

    'Из всех персонажей выжил только Боби'

    'Бобби пытается вылезти из-под завала'

    $ chance = renpy.random.randint(1, 2)
    if chance >= choosenCharacter.stats.strength.value:
        'Успех – Боби выбирается и становится единственным уцелевшим'
    else:
        'у него не получилось, все погибли'

