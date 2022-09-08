# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

define clownDemid = Actor(Character('Клоун Демид'), ActorStats(intellect = 0))

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.



# Игра начинается здесь:
label start:

    scene bg room

    show eileen happy

    clownDemid.character "Вы создали новую игру Ren'Py."

    clownDemid.character "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    $ clownDemid.stats.intellect.value=-1

    $ clownDemid.character(str(clownDemid.stats.intellect))

    jump ochko_demida

    return
