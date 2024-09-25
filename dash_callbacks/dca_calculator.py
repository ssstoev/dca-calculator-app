import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

amount = 500
period = '3M'
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

    investement_log = []

    for date, row in data_resampled.iterrows():
        price = row['Adj Close']
        if total_investement == 0:
            total_shares += initial_deposit / price
            total_investement += initial_deposit
        print(total_investement)

        total_shares += amount / price
        total_investement += amount
        
        current_log = {
            'Date': date,
            'Price': price,
            'Total Shares': total_shares,
            'Total Investment': total_investement,
            'Portfolio Value': total_shares * price
        }

        investement_log.append(current_log) 


    investement_df = pd.DataFrame(investement_log)
    print(investement_df.columns)
    # Ensure 'Date' column is a datetime object if needed
    investement_df['Date'] = pd.to_datetime(investement_df['Date'])
    print(investement_df)

    fig = go.Figure()
    fig = fig.add_trace(go.Scatter(x=investement_df['Date'], y=investement_df['Portfolio Value'], fill='tozeroy'))
    fig = fig.add_trace(go.Scatter(x=investement_df['Date'], y=investement_df['Total Investment'], fill='tonexty'))
    fig.update_layout(showlegend=True, title=f'Portfolio Value for {ticker}', xaxis_title='Date', yaxis_title='Portfolio Value')

    return fig

# calculate_dca(ticker, initial_deposit, period, amount, start_date, end_date)
