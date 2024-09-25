from dash_callbacks.dca_calculator import calculate_dca
from dash import callback, Input, Output, State
import plotly.graph_objects as go
import datetime 
@callback(
    Output("dca-graph", "figure"),
    Input("submit-button", "n_clicks"),
    [State("ticker-dropdown", "value"),
     State("initial-capital", "value"),
    State("interval-between-deposits", "value"),
    State("amount-of-deposit", "value"),
    State("start-date", "value"),
    State("end-date", "value")]
)

def update_graph(n_clicks, ticker, initial_capital, interval, amount, start_date, end_date):
    if n_clicks > 0:
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        print('button pressed')
        figure = calculate_dca(ticker, initial_capital, interval, amount, start_date, end_date)
        print(figure)
        return figure
    
    return go.Figure
