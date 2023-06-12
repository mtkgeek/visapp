from nicegui import app, ui, Client
from functions import extract_3d

app.add_static_files('/static', 'static')


def content() -> None:
    with ui.column():
        with ui.row().classes('flex justify-between w-full'):
            # left
            with ui.column().classes('w-2/5'):
                with ui.card().classes('w-full mt-2'):
                    ui.label('Course name and code').classes(
                        'font-serif text-xl font-extrabold pb-8')
                    ui.label('Course Name: Machine Learning').classes(
                        'font-serif text-md pb-4')
                    ui.label('Course Code: FTE35306').classes(
                        'font-serif text-md pb-4')
                # 2
                with ui.card().classes('w-full mt-2'):
                    ui.label('Application description').classes(
                        'font-serif text-xl font-extrabold pb-8')
                    ui.label('The product aims to visualize the predicted crop yields for potatoes in each Dutch province using two different regression models: simple linear regression and K-Nearest Neighbors Regression. The visualization will provide insights into the spatial distribution of predicted yields and help stakeholders in the agrifood chain make informed decisions.').classes(
                        'font-serif text-md pb-4')
                # 3
                with ui.card().classes('w-full mt-2'):
                    ui.label('User description and requirement').classes(
                        'font-serif text-xl font-extrabold pb-8')
                    ui.label('Potential users of this product include farmers, agricultural businesses, and policymakers in the agrifood chain. They require a clear and intuitive visualization that shows the predicted crop yields for each province and allows them to compare the performance of the two regression models.').classes(
                        'font-serif text-md pb-4')
                # 4
                with ui.card().classes('w-full mt-2'):
                    ui.label('Motivation for visualization type').classes(
                        'font-serif text-xl font-extrabold pb-8')
                    ui.label('The chosen visualization type is a choropleth map, as it is a common and effective way of visualizing regional data. Choropleth maps provide a quick and intuitive way of identifying patterns and trends in the data, making them an ideal choice for visualizing crop yields across different Dutch provinces.').classes(
                        'font-serif text-md pb-4')
                # 5
                with ui.card().classes('w-full mt-2'):
                    ui.label('Dataset description').classes(
                        'font-serif text-xl font-extrabold pb-8')
                    ui.label('The dataset used in this project is a spatio-temporal open dataset from the European Commission’s Joint Research Center (JRC). The dataset reports on eleven Dutch provinces for twenty years 1999-2018. It is a raster dataset that contains information on crop yields for different crops, including potatoes.').classes(
                        'font-serif text-md pb-4')
                # 6
                with ui.card().classes('w-full mt-2'):
                    ui.label('Processing methods and tools').classes(
                        'font-serif text-xl font-extrabold pb-8')
                    ui.label('The processing methods used in this project include data cleaning, data preprocessing, and model training. The data cleaning involves removing missing values, checking for outliers, and transforming the data into a format suitable for analysis. The data preprocessing includes feature selection, feature scaling, and data splitting into training and testing sets. The model training involves fitting the two regression models to the training data.').classes(
                        'font-serif text-md pb-4')
                # 7
                with ui.card().classes('w-full mt-2 mb-8'):
                    ui.label('Reflection on final results').classes(
                        'font-serif text-xl font-extrabold pb-8')
                    ui.label('The final result is a choropleth map that shows the predicted crop yields for potatoes in each Dutch province using the two regression models. The map is easy to interpret and provides useful insights into the spatial distribution of predicted yields. However, there are limitations to the analysis, \nas it only considers a limited number of features and does not account for all possible factors that may influence crop yields. Additionally, the accuracy of the predictions may be affected by errors in\n the dataset and the assumptions made in the regression models. Therefore, users should interpret the results with caution and consider other sources of information when making decisions.').classes(
                        'font-serif text-md pb-4')

            # right
            with ui.column().classes('w-3/5 flex-1 mt-2'):
                ui.label('MAP SHOWING SAMPLE REGIONAL CROP YIELD USING THE NUTS REGIONS').classes(
                    'font-serif w-full text-center text-lg pb-6')

                ui.html(extract_3d.readhtml3d()).classes(
                    'w-full border-solid rounded-lg w-full h-[32rem]')

                # with ui.card().classes('w-full mt-8 mb-4'):
                #     ui.label('Extra information').classes(
                #         'font-serif text-xl font-extrabold pb-8')
                #     ui.label('The final result is a choropleth map that shows the predicted crop yields for potatoes in each Dutch province using the two regression models. The map is easy to interpret and provides useful insights into the spatial distribution of predicted yields. However, there are limitations to the analysis, \nas it only considers a limited number of features and does not account for all possible factors that may influence crop yields. Additionally, the accuracy of the predictions may be affected by errors in\n the dataset and the assumptions made in the regression models. Therefore, users should interpret the results with caution and consider other sources of information when making decisions.').classes(
                #         'font-serif text-md pb-4')

        # with ui.button('Next', on_click=lambda: ui.open('/2')).classes('absolute left-[3rem] bottom-[15rem]'):
        #     ui.icon('arrow_forward').classes('text-white')
