from nicegui import ui


def my_classes(index: int, page_no: int):
    selected = 'border-2 border-white border-solid' if index == page_no else ''
    my_classes = f'text-white text-lg font-serif font-bold p-2 {selected}'
    return my_classes


def menu(index: int) -> None:

    ui.link('1', '/1').classes(replace=my_classes(index, 1))
    ui.link('2', '/2').classes(replace=my_classes(index, 2))
    # ui.link('3', '/3').classes(replace=my_classes(index, 3))
    # ui.link('4', '/4').classes(replace=my_classes(index, 4))
