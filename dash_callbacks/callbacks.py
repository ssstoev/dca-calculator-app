from dash_callbacks.dca_calculator import calculate_dca, create_dca_visualization
from dash import callback, Input, Output, State
import plotly.graph_objects as go
import datetime 
@callback(
    Output("dca-graph", "figure"),
    Output("total-invested-output", "value"),
    Output("portfolio-value", "value"),
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
        # print('button pressed')
        initial_capital = 0 if initial_capital is None else initial_capital
        investment_df = calculate_dca(ticker, initial_capital, interval, amount, start_date, end_date)
        figure = create_dca_visualization(investment_df)

        total_investment = investment_df["Total Investment"].iloc[-1]
        portfolio_value = investment_df["Portfolio Value"].iloc[-1]
        # print(figure)
        return figure, round(total_investment, 2), round(portfolio_value, 2)
    
    return go.Figure, None, None

