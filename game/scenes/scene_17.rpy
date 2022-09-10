label scene_17:
    $ wasHere = False

    scene scene_18 with fade

    if wasHere:
        jump scene_12
    else:
        $ wasHere = True

        'Вы отправились в сторону из которой пришли.'

        'Показались ворота входа в парк, но тут…'

        show shmanduk angry at right

        'Откуда ни возьмись появляется Мистер Шмандюк, а в руках у него..'

        show yuno normal at left

        yuno.character 'У него ружье!'

        hide yuno

        smanduk 'Я же говорил вам, что не выпущу вас, пока вы не посетите все аттракционы!'

        'Что будете делать?'
        menu:
            'Попробовать договориться':
                'Кого отправите на зарубу?'
                menu:
                    '[yuno.character.name]' if yuno.alive:
                        $ choosenCharacter = yuno
                    '[bobby.character.name]' if bobby.alive:
                        $ choosenCharacter = bobby
                    '[lakmus.character.name]' if lakmus.alive:
                        $ choosenCharacter = lakmus
                    '[shinji.character.name]' if shinji.alive:
                        $ choosenCharacter = shinji

                $ chance = renpy.random.randint(1,4)
                if chance <= choosenCharacter.stats.strength.value:
                    hide shmanduk
                    'Ура, вам удалось одолеть смотрителя'
                    'Вы покидаете луна-парк «Unluck`ич»'
                else:
                    '[choosenCharacter.character.name] не удалось победить Шмандюка, ружье оказалось сильнее..'
                    $ choosenCharacter.die()
                    'Вы спасаетесь бегством..'
                    jump scene_12

            'Убежать в сторону кафе ':
                jump scene_12

        jump scene_19