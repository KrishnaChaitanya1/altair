"""
Locations of US Airports
========================
This is a layered geographic visualization that shows the positions of US
airports on a background of US states.
"""
# category: geographic
import altair as alt
from vega_datasets import data

states = alt.topo_feature(data.us_10m.url, feature='states')
airports = data.airports.url

# US states background
background = alt.Chart(states).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    projection={'type': 'albersUsa'},
    width=500,
    height=300
)

# airport positions on background
points = alt.Chart(airports).mark_circle().encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    size=alt.value(10),
    color=alt.value('steelblue')
)

background + points
