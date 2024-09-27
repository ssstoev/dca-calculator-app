from dash_callbacks.dca_calculator import calculate_dca, create_dca_visualization, add_asset_to_graph
from dash import callback, Input, Output, State, callback_context
import plotly.graph_objects as go
import datetime 

@callback(
    Output("dca-graph", "figure"),
    Output("total-invested-output", "value"),
    Output("portfolio-value", "value"),
    Output("profit", "value"),
    Input("submit-button", "n_clicks"),
    Input("compare-button", "n_clicks"),
    State("ticker-dropdown-compare", "value"),
    State("ticker-dropdown", "value"),
    State("initial-capital", "value"),
    State("interval-between-deposits", "value"),
    State("amount-of-deposit", "value"),
    State("start-date", "value"),
    State("end-date", "value"),

    preven_initial_call = True
)

def update_graph(n_clicks_submit, n_clicks_compare, ticker_compare, ticker, initial_capital, interval, amount, start_date, end_date):
    ctx = callback_context
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == "submit-button":
        print("submit button pressed")
        print(button_id)
        interval = str(interval) + "ME"
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        # print('button pressed')
        initial_capital = 0 if initial_capital is None else initial_capital
        investment_df = calculate_dca(ticker, initial_capital, interval, amount, start_date, end_date)
        figure = create_dca_visualization(investment_df)

        total_investment = investment_df["Total Investment"].iloc[-1]
        portfolio_value = investment_df["Portfolio Value"].iloc[-1]

        # calculate the profit in %
        profit = portfolio_value - total_investment
        profit_percentage= str((round(profit / total_investment, 2))* 100) + "%"
        
        return figure, round(total_investment, 2), round(portfolio_value, 2), profit_percentage
    
    elif button_id == "compare-button":
        print("compare button pressed")
        print(button_id)
        interval = str(interval) + "ME"
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        # print('button pressed')
        initial_capital = 0 if initial_capital is None else initial_capital
        investment_df = calculate_dca(ticker, initial_capital, interval, amount, start_date, end_date)

        current_figure = create_dca_visualization(investment_df)

        total_investment = investment_df["Total Investment"].iloc[-1]
        portfolio_value = investment_df["Portfolio Value"].iloc[-1]

        # calculate the profit in %
        profit = portfolio_value - total_investment
        profit_percentage= str((round(profit / total_investment, 2))* 100) + "%"

        ### add the new trace to the figure
        new_df = calculate_dca(ticker_compare, initial_capital, interval, amount, start_date, end_date)
        updated_figure = add_asset_to_graph(current_figure, new_df)

        return updated_figure, round(total_investment, 2), round(portfolio_value, 2), profit_percentage
    
    return go.Figure, None, None, None


# @callback(
#     Output("dca-graph", "figure"),
#     Output("total-invested-output", "value"),
#     Output("portfolio-value", "value"),
#     Output("profit", "value"),
#     Input("submit-button", "n_clicks"),
#     [State("ticker-dropdown", "value"),
#      State("initial-capital", "value"),
#     State("interval-between-deposits", "value"),
#     State("amount-of-deposit", "value"),
#     State("start-date", "value"),
#     State("end-date", "value")]
# )

# def update_graph(n_clicks, ticker, initial_capital, interval, amount, start_date, end_date):
#     if n_clicks > 0:
#         print("first submit button pressed")
#         interval = str(interval) + "ME"
#         start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
#         end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
#         # print('button pressed')
#         initial_capital = 0 if initial_capital is None else initial_capital
#         investment_df = calculate_dca(ticker, initial_capital, interval, amount, start_date, end_date)
#         figure = create_dca_visualization(investment_df)

#         total_investment = investment_df["Total Investment"].iloc[-1]
#         portfolio_value = investment_df["Portfolio Value"].iloc[-1]

#         # clculate the profit in %
#         profit = portfolio_value - total_investment
#         profit_percentage= str((round(profit / total_investment, 2))* 100) + "%"
        
#         return figure, round(total_investment, 2), round(portfolio_value, 2), profit_percentage
    
#     return go.Figure, None, None, None



# callback to add anther asset to the graph and compare
# @callback(
#     Output("dca-graph", "figure"),
#     Input("compare-button", "n_clicks"),
#     State("ticker-dropdown-compare", "value"),
#     State("dca-graph", "figure"),
#     State("initial-capital", "value"),
#     State("interval-between-deposits", "value"),
#     State("amount-of-deposit", "value"),
#     State("start-date", "value"),
#     State("end-date", "value")
# )

# def add_comparison(n_clicks, new_ticker, current_figure, initial_capital, period, amount, start_date, end_date):
#     if n_clicks > 0 :
#         new_df = calculate_dca(new_ticker, initial_capital, period, amount, start_date, end_date)
#         updated_figure = add_asset_to_graph(current_figure, new_df)

#         return updated_figure
    
#     return go.Figure