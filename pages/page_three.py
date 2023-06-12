from nicegui import app, ui

app.add_static_files('/static', 'static')


def content() -> None:

    with ui.row().classes('flex justify-between w-full h-full'):
        with ui.column().classes('w-2/5'):
            with ui.card().classes('w-full mt-2'):
                ui.label('Course name and code').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label('Course Name: Advanced Earth Observation').classes(
                    'font-serif text-md pb-4')
                ui.label('Course Code: GRS32306').classes(
                    'font-serif text-md pb-4')
            # 2
            with ui.card().classes('w-full mt-2'):
                ui.label('Application description').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label('Iberian Ibex').classes(
                    'font-serif text-md pb-4')
            # 3
            with ui.card().classes('w-full mt-2'):
                ui.label('User description and requirement').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label('Iberian Ibex').classes(
                    'font-serif text-md pb-4')
            # 4
            with ui.card().classes('w-full mt-2'):
                ui.label('Motivation for visualization type').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label('Iberian Ibex').classes(
                    'font-serif text-md pb-4')
            # 5
            with ui.card().classes('w-full mt-2'):
                ui.label('Dataset description').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label('Iberian Ibex').classes(
                    'font-serif text-md pb-4')
            # 6
            with ui.card().classes('w-full mt-2 mb-6'):
                ui.label('Processing methods and tools').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label('Iberian Ibex').classes(
                    'font-serif text-md pb-4')

            # Reflection
            with ui.card().classes('w-full mt-4 mb-4'):
                ui.label('Reflection on final results').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label('Iberian Ibex').classes(
                    'font-serif text-md pb-4')

        with ui.column().classes('w-3/5 flex-1'):
            ui.label('MAP SHOWING LAND COVER CLASSIFICATION RESULTS, SUMATRA, INDONESIA').classes(
                'font-serif w-full text-center text-lg pb-6 pt-4')
            ui.image('/static/img/000.jpeg').classes('w-full')

        # with ui.button('Next', on_click=lambda: ui.open('/2')).classes('absolute left-[3rem] bottom-[15rem]'):
        #     ui.icon('arrow_forward').classes('text-white')
