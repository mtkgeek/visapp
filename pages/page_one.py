from nicegui import app, ui

app.add_static_files('/static', 'static')


def content() -> None:

    with ui.row().classes('flex justify-between w-full h-full'):
        with ui.column().classes('w-2/5'):
            with ui.card().classes('w-full mt-2'):
                ui.label('Course name and code').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label('Course Name: Geo-information Tools').classes(
                    'font-serif text-md pb-4')
                ui.label('Course Code: GRS20806').classes(
                    'font-serif text-md pb-4')
            # 2
            with ui.card().classes('w-full mt-2'):
                ui.label('Application description').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label('The product focuses on mapping the migration route and corridor of the Iberian Ibex around Álora, Spain. The goal is to identify and visualize the movement corridors preferred by the Iberian Ibex to ensure their safe migration between the National Park Sierra Nevada and the National Park Sierra de las Nieves. The visualization aims to assist in the planning and conservation efforts by highlighting the areas that need protection and those that pose potential obstacles or dangers to the Ibex population.').classes(
                    'font-serif text-md pb-4')
            # 3
            with ui.card().classes('w-full mt-2'):
                ui.label('User description and requirements (PEOPLE)').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label("Potential users of this product include wildlife conservation organizations, environmental planners, and local authorities responsible for managing the region's natural resources. They require a detailed visualization that clearly shows the preferred movement corridors of the Iberian Ibex, highlighting the areas that require protection and potential barriers to their migration.").classes(
                    'font-serif text-md pb-4')
            # 4
            with ui.card().classes('w-full mt-2'):
                ui.label('Purpose of your visualization').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label('The purpose of this visualization is to map and visualize the migration route and corridor of the Iberian Ibex around Álora, Spain. By representing the movement corridors preferred by the Ibex on a map, the visualization serves as a valuable tool for wildlife conservation organizations, environmental planners, and local authorities. They can understand the specific areas that the Ibex favors, identify potential barriers or risks to their migration, and plan conservation strategies accordingly. The visualization aids in decision-making related to land-use planning, habitat protection, and infrastructure development, ensuring the safe migration of the Iberian Ibex population.').classes(
                    'font-serif text-md pb-4')
            # # 5
            # with ui.card().classes('w-full mt-2'):
            #     ui.label('Dataset description').classes(
            #         'font-serif text-xl font-extrabold pb-8')
            #     ui.label('The datasets used in this project include both vector and raster data. The vector data contains information about the boundaries of the National Park Sierra Nevada and the National Park Sierra de las Nieves, as well as the locations of grazing grounds, abandoned orchards, agricultural areas, water bodies, human settlements, and infrastructure, including the high-speed railway connection. The raster data includes information on land cover and slope.').classes(
            #         'font-serif text-md pb-4')

            # 6
            with ui.card().classes('w-full mt-2 mb-6'):
                ui.label('Processing methods and tools').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label('The processing methods used in this project include spatial analysis techniques such as overlay analysis, proximity analysis, and suitability analysis. These techniques are used to identify and prioritize the areas preferred by the Iberian Ibex based on their specific habitat requirements and movement patterns. The processing also involves data integration, transformation, and visualization techniques to create a comprehensive map depicting the migration route and corridor.\n The project was implemented using ArcGIS. It provide a wide range of geospatial analysis and visualization capabilities, allowing for the integration and analysis of different thematic layers to create the desired geo-visualization map.').classes(
                    'font-serif text-md pb-4')

        with ui.column().classes('w-3/5 flex-1'):
            ui.image('/static/img/geotoolsmap.svg').classes('w-full')

            # Reflection
            with ui.card().classes('w-full mb-4n h-[57rem]'):
                ui.label('Reflection on final results').classes(
                    'font-serif text-xl font-extrabold pb-8')
                ui.label("The chosen visualization type, a combination of thematic map layers and spatial analysis, aligns well with the needs of wildlife conservation organizations, environmental planners, and local authorities responsible for managing the region's natural resources. The purpose of the product is to identify and visualize the preferred movement corridors of the Iberian Ibex, highlighting potential barriers and areas requiring protection. The chosen visualization type effectively combines various thematic layers, such as land cover, slope, infrastructure, and human settlements, to provide a comprehensive understanding of the Ibex migration patterns and guide conservation efforts.\n\n  ").classes('font-serif text-md pb-4')
                ui.label("The process aligns with the purpose of the visualization, as spatial analysis techniques were applied to identify and prioritize the preferred areas for the Ibex based on their habitat requirements and movement patterns. The integration of vector and raster datasets, along with the utilization of GIS tools, facilitated the analysis and creation of the final visualization.\nTo further enhance the alignment, additional data sources could be incorporated into the analysis. For example, including information on vegetation density, proximity to protected areas, or the presence of predators could provide a more comprehensive understanding of the Ibex migration behavior. Furthermore, involving stakeholders and experts in the process, such as local conservationists or field researchers, can provide valuable insights and ensure the visualization accurately reflects the real-world dynamics of the migration route and corridor.\n").classes('font-serif text-md pb-4')
                ui.label("The motivation for choosing the visualization type stems from its ability to holistically represent the complex factors influencing the Iberian Ibex migration. By combining multiple thematic layers, the visualization captures the interplay between land cover, slope, infrastructure, and human settlements, allowing for a more comprehensive assessment of the preferred movement corridors. This type of visualization enables stakeholders to identify potential risks and plan conservation strategies that align with the specific habitat requirements and behavior of the Iberian Ibex.").classes('font-serif text-md pb-4')
        # with ui.button('Next', on_click=lambda: ui.open('/2')).classes('absolute left-[3rem] bottom-[15rem]'):
        #     ui.icon('arrow_forward').classes('text-white')
