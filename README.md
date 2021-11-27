# Response Dash App

This is an example template of how to make a response Dash app.

Please see a demo [here](https://responsive-dash-app.herokuapp.com/), deployed on [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python) (follow this [tutorial](https://dash.plotly.com/deployment)).
You can see, if you view the app in mobile/responsive view, that it is responsive and looks 
as expected.

The responsiveness is achieved by using the `<meta>` tag. Specifically, the meta parameter passed:
```python
meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
```