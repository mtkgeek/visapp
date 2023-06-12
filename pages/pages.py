import theme

from nicegui import ui
from pages import page_one, page_two, page_three, page_four


def create() -> None:

    @ui.page('/1')
    def page_one_create():
        with theme.frame('/static/img/ibex.png', 1):
            page_one.content()

    @ui.page('/2')
    def page_two_create():
        with theme.frame('/static/img/potaflag.png', 2):
            page_two.content()

    @ui.page('/3')
    def page_three_create():
        with theme.frame('/static/img/satellite.png', 3):
            page_three.content()

    @ui.page('/4')
    def page_four_create():
        with theme.frame('/static/img/satellite.png', 4):
            page_four.content()

    @ui.page('/thanks')
    def page_thanks_create():
        with theme.frame('- Thank you -', 5):
            ui.label('Example C').classes('text-h4 text-grey-8')
