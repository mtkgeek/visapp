from nicegui import app, ui

app.add_static_files('/static', 'static')


def content() -> None:

    with ui.image('/static/img/bg.png').classes(replace='w-full h-screen'):
        with ui.column().classes('w-full h-full'):
            ui.label('Visualization Portfoilio').classes(
                'font-serif text-2xl font-extrabold absolute left-[3rem] bottom-[20rem] pb-8')
            ui.label('Moses Okolo').classes(
                'font-serif text-lg font-semibold  absolute left-[3rem] bottom-[18rem] pb-4')
            with ui.button('Shall We?', on_click=lambda: ui.open('/1')).classes('absolute left-[3rem] bottom-[15rem]'):
                ui.icon('arrow_forward').classes('text-white')
