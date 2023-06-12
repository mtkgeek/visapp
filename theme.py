from contextlib import contextmanager

from menu import menu

from nicegui import ui


@contextmanager
def frame(navtitle: str, index: int):
    '''Custom page frame to share the same styling and behavior across all pages'''
    ui.colors(primary='#6E93D6', secondary='#53B689',
              accent='#111B1E', positive='#53B689')
    with ui.header().classes('justify-between items-center text-white'):
        ui.link('Visualization Portfolio', '/').classes(
            replace='text-white text-lg font-bold font-serif')
        ui.image(navtitle).classes(f"{'w-24' if index==2 else 'w-20'} h-20")
        with ui.row().classes('ml-4'):
            menu(index)
    with ui.row().classes(replace='w-full h-screen'):
        yield
