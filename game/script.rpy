# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define shinji = Actor(Character('Синдзи', color='#ffffff'), ActorStats(luck=3), 'некое описание')
define bobby = Actor(Character('Бобби', color='#00ff00'), ActorStats(strength=3), 'некое описание')
define yuno = Actor(Character('Юно Гасай', color='#0000ff'), ActorStats(motivation=3), 'некое описание')
define lakmus = Actor(Character('Лакмус', color='#ff00ff'), ActorStats(communication=3), 'некое описание')


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    call transforms
    call scenes_bg

    jump scene_2

    return
