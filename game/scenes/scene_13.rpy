label scene_13:
    scene scene_13 with fade

    '[choosenCharacter.character.name] взбирается на вышку и замечает неподалеку колесо обозрения, о чем сообщает группе'

    'Осталось самое сложное – безопасно слезть'

    $ chance = renpy.random.randint(1,4)

    if chance >= choosenCharacter.stats.luck.value:
        '[choosenCharacter.character.name] удаётся слезть с вышки'
        jump scene_15
    else:
        jump scene_14


