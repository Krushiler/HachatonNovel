label scene_10:

    scene scene_10 with fade

    'Вы попадаете в кафе «Вонючий ветер»'

    show shinji normal

    $ shinji.character 'АОАОАОАООАОА, ЧТО ЭТО????'

    hide shinji normal

    'На столе вы видите тарелку с отрубленными пальцами.'

    'Что будете делать?'

    menu:
        'Попробовать убежать из парка':
            jump scene_17
        'Пойти в комнату страха':
            jump scene_6