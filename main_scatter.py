import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
from utils import text

# Tab display 
st.set_page_config(page_title="NC Oyster Sanctuary Data", page_icon=":oyster:", layout="wide")

#Instruction text

with st.expander("Scatterplot Instructions"):
    st.info("""
            **Each point is a density estimate collected during Sanctuary sampling. Hover over each sample to view the observed oyster density, material type & age, and collection date.**
            
            **Remove materials from your analysis by clicking on them in the legend. Double click a material to isolate it. Double click the legend again to reset the plot.**

            **Draw a square on the plot to zoom in on a particular set of data points. Double click to reset the plot.** 

            **Select a filter to view the densities for all oysters, or only legal (>75mm), sublegal (25mm < x < 75mm), spat (≤25mm), or non-spat (legal + sublegal).**
""")

#import data
df = pd.read_csv("data/2019-2023_oyster_densities.csv")


# Calculate Lowess trendline for the selected data
lowess = sm.nonparametric.lowess
trendline = lowess(df['total'], df['Material_Age'], frac=0.25)


# Create scatter plot
fig1 = px.scatter(df, 
                x='Material_Age', 
                y='total', 
                color="Material", 
                color_discrete_map={
                    'Marl':'#636EFA',
                    'Granite':'#EF553B',
                    'Basalt':'#00CC96',
                    'Crushed Concrete': '#AB63FA',
                    'Shell':'#FFA15A',
                    'Reef Ball':'#19D3F3',
                    'Consolidated Concrete':'#FF6692'
                },
                hover_data=['OS_Name', 'Year'],
                size_max=15,  # Set the maximum size of the markers
                height=450,
                width=950)

# Add Lowess trendline to the plot
fig1.add_trace(
    go.Scatter(
        x=trendline[:, 0], 
        y=trendline[:, 1], 
        mode='lines', 
        line=dict(color='black', width=2), 
        name='Lowess Trendline'
    )
)

fig1.update_traces(
    marker=dict(
        size=15,  # Set the size of the markers
        opacity=0.7,  # Adjust the transparency of the markers
        line=dict(color='black', width=1)  # Add a black outline
    ),
    selector=dict(type='scatter'),
    hoverlabel=dict(bgcolor='white', font=dict(color='black', size=16))
)

fig1.update_layout(
    yaxis_range=[-500,4700],
    xaxis_range=[0,30],
    paper_bgcolor='#D6F2F4', 
    plot_bgcolor='white',
    font=dict(color='black', size=18),  # Update general font settings
    xaxis=dict(
        title=dict(text='Material Age (years)', font=dict(color='black', size=22)),
        tickfont=dict(color='black', size=16)  # Update tick font size for x-axis
    ),
    yaxis=dict(
        title=dict(text=f'Oyster Density (per m²)', font=dict(color='black', size=22)),
        tickfont=dict(color='black', size=16)  # Update tick font size for y-axis
    ),
    legend=dict(
                title= dict(
                    text='Material',
                    font= dict(color='black', size=16)
                ),
                font=dict(color='black', size=16),
                orientation="v",
                yanchor='top',
                y=0.95,
                xanchor='right',
                x=0.99,
                bgcolor='rgba(255, 255, 255, 0.6)'
            ),
            margin=dict(l=0, r=0, t=0, b=0)
    )

st.plotly_chart(fig1, use_container_width=True, use_container_height=True)

