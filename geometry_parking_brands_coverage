import streamlit as st
from read_data import read_from_gsheets
import altair as alt
from datetime import datetime, timedelta
import pandas as pd
import streamlit.components.v1 as components
import plotly.express as px

st.set_page_config(
    page_title="Geometry Summary Statistics - Parking Brands Coverage",
    layout="wide"
)

#### Geometry Brand Category Stats ####


brand_stats_parking_df = read_from_gsheets('Parking - brands')\
    [["primary_brand","naics_code", "safegraph_category", "safegraph_subcategory", "pct_poi_with_parking", 'total_open_poi_count']]\
    .astype({'naics_code': str, 'total_open_poi_count':int})


brand_stats_parking_df = brand_stats_parking_df[brand_stats_parking_df['total_open_poi_count']>=100].drop(['total_open_poi_count'], axis=1)


brand_stats_parking_df['pct_poi_with_parking'] = [0 if (pd.isna(x)) or (x=="NaN") else float(x) for x in brand_stats_parking_df['pct_poi_with_parking'] ]
brand_stats_parking_df['naics_code'] = [x.split(".")[0] for x in brand_stats_parking_df['naics_code'] ]


parking_brand_df = (
    brand_stats_parking_df
    .rename(columns={"naics_code": "NAICS Code", "safegraph_category": "SafeGraph Category",\
                        "safegraph_subcategory": "SafeGraph Subcategory",  "pct_poi_with_parking":"Pct POI With Parking",\
                              "primary_brand":"Brand Name" })
    .assign(**{
        "Pct POI With Parking": lambda df: ((df["Pct POI With Parking"]) * 100).astype(float)
}).sort_values('Pct POI With Parking', ascending=False)
    .reset_index(drop=True)
)


parking_brand_df['Pct POI With Parking'] = parking_brand_df['Pct POI With Parking'].astype(float).apply(lambda x: "{:.01f}%".format(x))


styled_brand_df = (
    parking_brand_df.style.apply(lambda x: ['background-color: #D7E8ED' if i % 2 == 0 else '' for i in range(len(x))], axis=0)
)

st.write("Parking Coverage by Brand")
st.dataframe(styled_brand_df, use_container_width=True, hide_index=True)
