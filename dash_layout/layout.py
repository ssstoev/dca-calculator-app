import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
import plotly.graph_objects as go
from dash_callbacks.dca_calculator import calculate_dca

tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'BRK.B', 'TSLA', 'META', 
    'UNH', 'LLY', 'JNJ', 'V', 'XOM', 'WMT', 'JPM', 'PG', 'MA', 'NVO', 
    'HD', 'MRK', 'CVX', 'SHEL', 'KO', 'ABBV', 'PEP', 'AVGO', 'ORCL', 
    'AZN', 'COST', 'MCD', 'BAC', 'TMO', 'ASML', 'PFE', 'NFLX', 'TM', 
    'ABT', 'LIN', 'CSCO', 'DHR', 'DIS', 'ADBE', 'NKE', 'BHP', 'PM', 
    'VZ', 'NEE', 'INTC', 'RTX', 'SAP', 'SCHW'
]

def create_layout():
    return dbc.Container([
                dbc.Row(
                    dbc.Navbar(
                        dbc.Container(
                            [
                            dbc.NavbarBrand(html.B("DCA Calculator", style={"fontSize": "2rem"}), className="ms-2"),  # App title
                            # dbc.Nav(
                            #     dbc.NavItem(dbc.Button("Create Post", id='create-post-button', color="primary", className="ms-2")),  # Create Post button
                            #     className="ms-auto",  # Push the button to the right
                            # ),
                            ]
                        ),
                        color="primary",  # Set the navbar color
                        dark=True,  # Make the text light to contrast the dark background
                        className="mb-4",  # Margin below the navbar
                        fixed="top"
                    )
                ),

                dbc.Row([
                    dbc.Col(
                        html.P("Select a Ticker"), 
                        className="d-flex justify-content-center align-items-center",
                        width=2
                    ),
                    
                    dbc.Col(
                        html.P("Initial Capital"), 
                        className="d-flex justify-content-center align-items-center",
                        width=2
                    ),

                    dbc.Col(
                        html.P("Interval Between Deposits (Months)"), 
                        className="d-flex justify-content-center align-items-center", 
                        width=2
                    ),

                    dbc.Col(
                        html.P("Amount of Deposit"), 
                        className="d-flex justify-content-center align-items-center", 
                        width=2
                    ),

                    dbc.Col(
                        html.P("Start Date"), 
                        className="d-flex justify-content-center align-items-center", 
                        width=2
                        ),

                    dbc.Col(
                        html.P("End Date"), 
                        className="d-flex justify-content-center align-items-center", 
                        width=2
                        )
                ], style={"padding-top": "100px"}),

                dbc.Row([
                    dbc.Col(
                        dcc.Dropdown(
                            id='ticker-dropdown',
                            options=[
                                {"label": ticker,
                                 "value": ticker}
                                 for ticker in tickers
                            ],
                            placeholder="Select a ticker",
                            searchable=True,  # Enable searching
                            multi=False,      # Set to True for multi-select dropdown
                        ), width=2
                    ),
                    
                    dbc.Col(
                        dbc.Input(id='initial-capital', placeholder='e.g. 1000, 10000...', type="number"), width=2
                    ),
                    dbc.Col(
                        dbc.Input(id='interval-between-deposits', placeholder='e.g. 1M, 2M...', type="text"), width=2
                    ),
                    dbc.Col(
                        dbc.Input(id='amount-of-deposit', placeholder='e.g. 100, 200...', type='number'), width=2
                    ),
                    dbc.Col(
                        dbc.Input(id='start-date', type="date"), width=2
                    ),
                    dbc.Col(
                        dbc.Input(id='end-date', type="date"), width=2
                    )
                ], style={"padding-top": "5px"}),

                dbc.Row([
                    dbc.Col(
                        dbc.Button("Submit", id='submit-button', n_clicks=0),
                        className="d-flex justify-content-end"
                    )
                ], style={"padding-top": "20px"}),

                dbc.Row([
                    dbc.Col(dcc.Graph(id="dca-graph"), width=8),
                    dbc.Col([
                        dbc.Row([
                            dbc.Col(html.P(html.B("Total Invested")), width=4),
                            dbc.Col(dbc.Input(id="total-invested-output", disabled=True))
                        ], style={"padding-top": "100px"}),

                        dbc.Row([
                            dbc.Col(html.P(html.B("Portfolio Value")), width=4),
                            dbc.Col(dbc.Input(id="portfolio-value", disabled=True))
                        ], style={'padding-top': "20px"})
                ])
                ], style={"padding-top": "20px"})
    ])