from pages import pages
import home_page

from nicegui import ui, Client


# here we use our custom page decorator directly and just put the content creation into a separate function
@ui.page('/')
def index_page(client: Client) -> None:
    client.content.classes('p-0 gap-0')
    home_page.content()


# this call shows that you can also move the whole page creation into a separate file
pages.create()


ui.run(title='Visualization Portfolio', show=False)
