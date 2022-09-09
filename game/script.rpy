# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define shinji = Actor(Character('Синдзи', color='#B592E1'), ActorStats(luck=3), 'Везучий, но очень боязливый парнишка со слабой психикой')
define bobby = Actor(Character('Бобби', color='#F7C649'), ActorStats(strength=3), 'Дувчушка-веселушка, способная замотивировать кого и на что угодно.')
define yuno = Actor(Character('Юно Гасай', color='#60C6E7'), ActorStats(motivation=3), 'Коммуникативный паренек, который может уговорить почти любого')
define lakmus = Actor(Character('Лакмус', color='#B3D358'), ActorStats(communication=3), 'Кто не курит и не пьет - ровно дышит, сильно бьёт. Силач, за друзей и свободу полезет на проволоку')

define smanduk = Character('Шмандюк', color='#FF0000')

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.


# Игра начинается здесь:
label start:

    call transforms

    jump scene_2

    return
