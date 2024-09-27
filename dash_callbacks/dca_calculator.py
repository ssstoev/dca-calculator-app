import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

amount = 500
period = '3ME'
initial_deposit = 10000
ticker = 'AAPL'
start_date = '2017-01-01'
end_date = '2024-01-01'
# data = yf.download(ticker, start_date, end_date)
# data_resampled = data.resample(period).first()
# data_resampled.dropna(inplace=True)
# print(data_resampled)

def calculate_dca(ticker, initial_deposit, period, amount, start_date, end_date):

    data = yf.download(ticker, start_date, end_date)
    data_resampled = data.resample(period).first()
    data_resampled.dropna(inplace=True)

    total_shares = 0
    total_investement = 0

    investment_log = []

    for date, row in data_resampled.iterrows():
        price = row['Adj Close']
        if total_investement == 0:
            total_shares += initial_deposit / price
            total_investement += initial_deposit

        total_shares += amount / price
        total_investement += amount
        
        current_log = {
            'Ticker': ticker,
            'Date': date,
            'Price': price,
            'Total Shares': total_shares,
            'Total Investment': total_investement,
            'Portfolio Value': total_shares * price
        }

        investment_log.append(current_log) 


    investment_df = pd.DataFrame(investment_log)

    return investment_df

# calculate_dca(ticker, initial_deposit, period, amount, start_date, end_date)

def create_dca_visualization(investment_df):
    # Ensure 'Date' column is a datetime object if needed
    investment_df['Date'] = pd.to_datetime(investment_df['Date'])

    # get the vlue of the chosen ticker from the ticker column at row 0
    ticker = investment_df.iloc[0, 0]

    fig = go.Figure()
    fig = fig.add_trace(go.Scatter(x=investment_df['Date'], y=investment_df['Portfolio Value'], name=f"Portfolio Value in {ticker}", mode='lines', line=dict(color='lightgreen')))

    # fig = fig.add_trace(go.Scatter(x=investment_df['Date'], y=investment_df['Portfolio Value'], name=f"Portfolio Value in {ticker}", fill='tonexty', fillcolor='lightgreen'))
    fig = fig.add_trace(go.Scatter(x=investment_df['Date'], y=investment_df['Total Investment'], name="Total Investment"))
    fig.update_layout(showlegend=True, title=f'Portfolio Value for {ticker}', xaxis_title='Date', yaxis_title='Portfolio Value')

    return fig

def add_asset_to_graph(initial_graph, new_df):

    ticker = new_df.iloc[0, 0]
    new_graph = initial_graph.add_trace(go.Scatter(x = new_df['Date'], y = new_df['Portfolio Value'], name = f"Portfolio Value in {ticker}", mode='lines', line=dict(color='blue')))
    new_graph.update_layout(showlegend=True, title=f'Portfolio Value for Different Assets', xaxis_title='Date', yaxis_title='Portfolio Value')
    # new_graph.show()
    return new_graph

# add_asset_to_graph(create_dca_visualization(calculate_dca(ticker, initial_deposit, period, amount, start_date, end_date)),
#                    calculate_dca("MSFT", initial_deposit, period, amount, start_date, end_date))