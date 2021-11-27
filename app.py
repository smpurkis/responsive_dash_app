import dash
from dash import html, dcc
from styles import *

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    name=__name__,
    external_stylesheets=external_stylesheets,
    meta_tags=[{'name': 'viewport',
                'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
)

server = app.server

img_srcs = {
    "cat": "https://placekitten.com/408/287",
    "dog": "https://place-puppy.com/300x300"
}

app.layout = html.Div([
    html.H2('Hello World', style=h2_style),
    html.Div([
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
            value='LA',
            style=dropdown_style
        ),
        html.Div(id='display-value'),
    ], style=div_style),
    html.Br(),
    html.Div([
        html.Img(id="example-image", src=img_srcs["cat"], style=img_style),
        html.Button('Switch Img', id='switch-image-button', style=button_style),
    ], style=div_style)
], style=center_style)


@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected "{value}"'


@app.callback(dash.dependencies.Output('example-image', 'src'),
              [dash.dependencies.Input('switch-image-button', 'n_clicks')])
def switch_img_src(n_clicks):
    if n_clicks is None:
        return img_srcs["cat"]
    if n_clicks % 2 == 0:
        return img_srcs["cat"]
    else:
        return img_srcs["dog"]


if __name__ == '__main__':
    app.run_server(debug=False)
