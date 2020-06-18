# pip install dash==0.21.1  
# install dash-renderer==0.13.0  
# pip install dash-html-components==0.11.0
# pip install dash-core-components==0.23.0  
# pip install plotly --upgrade


# Import Data Wrangling components
import matplotlib.pyplot as plt
plt.style.use('classic')
#%matplotlib inline
import numpy as np
import pandas as pd

import seaborn as sns
sns.set()


filename1 = '/Users/pbanerjee/Documents/CBU/CBU_Projects/CBU_Internal/Data_Report_Redcap/df_report.csv'
df_report = pd.read_csv(filename1)
analysis_count = df_report.Analysis_Type.value_counts(sort=True)
# print(analysis_count)
sorted_analysis_count = analysis_count.sort_index()
# print(sorted_analysis_count)

# # Count for all coulms corresponding to Analysis_Type
# test_count = df_report.apply(pd.value_counts).fillna(0)
# print(test_count)

analysis_types = df_report.Analysis_Type.unique()
# print(analysis_types)
# print(sorted(analysis_types))

# Import DASH Components
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='CBU Projects',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='A web application to visulaize CBU projects.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Graph1',
        figure={
            'data': [
                {'x': sorted(analysis_types), 'y': sorted_analysis_count, 'type': 'bar', 'name': 'Analysis_Type'},
            ],
            'layout': {
                'title': 'CBU Analysis Types'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=False, port=8050)