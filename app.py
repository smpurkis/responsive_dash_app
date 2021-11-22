import dash
from dash import html, dcc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    name=__name__,
    external_stylesheets=external_stylesheets,
    meta_tags=[{'name': 'viewport',
                'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
)

server = app.server

center_style = {
    "text-align": "center",
    "padding": "1em",
    "max-width": "100%",
    "margin": "0 auto"
}

button_style = {
    "text-align": "center",
    "max-width": "20rem",
    "margin": "0 auto"
}


h1_style = {
    "color": "#ff3e00",
    "text-transform": "uppercase",
    "font-size": "4em",
    "font-weight": "100"
}

img_style = {
    "text-align": "center",
    "min-width": "200px",
    "width": "75%",
    "max-width": "600px",
    "margin": "0 auto"
}

app.layout = html.Div([
    html.H2('Hello World', style=h1_style),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in ['LA', 'NYC', 'MTL']],
        value='LA',
        style=button_style
    ),
    html.Div(id='display-value'),
    html.Br(),
    html.Img(id="example-image", src="https://placekitten.com/408/287", style=img_style)
], style=center_style)


@app.callback(dash.dependencies.Output('display-value', 'children'),
              [dash.dependencies.Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected "{value}"'


if __name__ == '__main__':
    app.run_server(debug=True)
