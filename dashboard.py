from dash import Dash, dcc, Input, Output, callback, dash, html
import dash_mantine_components as dmc
import requests
import plotly.graph_objs as go

dash._dash_renderer._set_react_version('18.2.0')

# Fetch the list of sectors from the Flask API
_sectors = requests.get('http://127.0.0.1:5000/Sector').json()

def get_ebitda(sector):
    ebitda_by_sector = requests.get(f'http://127.0.0.1:5000/EBITDA?Sector={sector}')
    return ebitda_by_sector.json()

app = Dash()

app.layout = dmc.MantineProvider(
    [
        dcc.Graph(id='ebitda-output'),
        dmc.Flex(
            children=[
                dmc.MultiSelect(
                    label="Select Sectors",
                    id="multi-select",
                    value=[sector for sector in _sectors],
                    data=[{'label': sector, 'value': sector} for sector in _sectors],
                    w=400,
                )
            ],
            direction="row",
            align="center",
            justify="center",
        )
    ]
)

@callback(
    Output('ebitda-output', 'figure'),
    Input('multi-select', 'value')
)
def update_ebitda(selected_sectors):
    if not selected_sectors:
        return go.Figure()

    ebitda_values = []
    for sector in selected_sectors:
        ebitda = get_ebitda(sector)
        total_ebitda_sector = sum(ebitda)
        ebitda_values.append({'sector': sector, 'ebitda': total_ebitda_sector})

    total_ebitda = sum(item['ebitda'] for item in ebitda_values)

    # Pie chart
    fig = go.Figure(
        data=[go.Pie(
            labels=[item['sector'] for item in ebitda_values],
            values=[item['ebitda'] for item in ebitda_values],
            textinfo='label+percent',
            hole=0.3
        )]
    )

    fig.update_layout(title=f'EBITDA Contribution by Sector (Total EBITDA: {total_ebitda})')

    return fig

if __name__ == '__main__':
    app.run(debug=True, port=3000)