import dash
import dash_bootstrap_components as dbc
from dash import html
from dash_layout.layout import create_layout
import dash_callbacks.callbacks

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR], title="DCA Calculator")

# Define the layout of the app
app.layout = create_layout()

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
