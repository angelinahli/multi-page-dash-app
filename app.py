# @author Angelina Li
# @modified 8/16/2018
# @filename app.py
# @description main application

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import flask

from templates import BootstrapBase

# setup
server = flask.Flask("app")
app = dash.Dash(server=server)
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

# defining general layout
app.layout = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Div(id="page-content")
])

# define base template for application
base_template = BootstrapBase(
    nav_brand=("/", "Test Dash Web App"),
    nav_items=[
        ("/page-1/", "Page 1"), 
        ("/page-2/", "Page 2")
    ],
    default_title="Test Dash Multi-App Webpage",
    default_footer = u"© Angelina Li 2018"
)

# import placed here to prevent circular imports
from apps import app1, app2

index = base_template.render_template()

# display pages based on url
@app.callback(Output("page-content", "children"),
    [Input("url", "pathname")])
def display_page(pathname):
    if pathname:
        pathname = pathname.strip("/")
    paths = {
        "page-1": app1.layout,
        "page-2": app2.layout 
    }
    return paths.get(pathname, index)

# run app
if __name__ == "__main__":
    app.run_server(debug=True)
