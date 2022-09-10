label scene_16:

    scene scene_16 with fade

    'Ваша кабинка поднимаетесь на вершину колеса'

    'Вам открывается вид на весь парк и лес за ним'

    'Вся компания успокаивается, ведь спустившись вы сможете покинуть это страшное место…'

    $ chance = renpy.random.randint(1, 3)

    if chance == 1 or chance == 2:
        jump scene_20
    else:
        'Колесо внезапно начинает трястись и вы летите вниз..'
        if bobby.alive:
            $ shinji.die()
            $ yuno.die()
            $ lakmus.die()

            jump scene_23
        else:
            jump scene_19