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


distinct_brands = parking_brand_df['Brand Name'].unique().tolist()
brands_list = st.multiselect("Brands:", [""] + distinct_brands)

st.write("Parking Coverage by Brand")

if brands_list:
    styled_brand_df = (
        parking_brand_df[parking_brand_df['Brand Name'].isin(brands_list)].style.apply(
            lambda x: ['background-color: #D7E8ED' if i % 2 == 0 else '' for i in range(len(x))], axis=0)
    )
    st.dataframe(styled_brand_df, use_container_width=True, hide_index=True)
else:
    styled_brand_df = (
        parking_brand_df.style.apply(lambda x: ['background-color: #D7E8ED' if i % 2 == 0 else '' for i in range(len(x))], axis=0)
    )
    st.dataframe(styled_brand_df, use_container_width=True, hide_index=True)

hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
'''
st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

css = '''
<style>
section.main > div:has(~ footer ) {
     padding-top: 0px;
    padding-bottom: 0px;
}

[data-testid="ScrollToBottomContainer"] {
    overflow: hidden;
}
</style>
'''

st.markdown(css, unsafe_allow_html=True)

# Keep-alive comment: 2025-03-28 09:32:39.588424

# Keep-alive comment: 2025-03-29 14:27:14.055875
# Keep-alive comment: 2025-03-31 15:59:14.175400
# Keep-alive comment: 2025-03-31 19:24:52.184447
# Keep-alive comment: 2025-04-01 06:22:33.182397
# Keep-alive comment: 2025-04-01 17:23:27.120806
# Keep-alive comment: 2025-04-02 04:23:12.745112
# Keep-alive comment: 2025-04-02 15:23:11.822012
# Keep-alive comment: 2025-04-03 02:22:46.263393
# Keep-alive comment: 2025-04-03 13:23:52.205973
# Keep-alive comment: 2025-04-04 00:24:13.695677
# Keep-alive comment: 2025-04-04 11:23:45.024836
# Keep-alive comment: 2025-04-04 22:22:56.504494
# Keep-alive comment: 2025-04-05 09:22:46.751631
# Keep-alive comment: 2025-04-05 20:24:02.156213
# Keep-alive comment: 2025-04-06 07:23:31.817406
# Keep-alive comment: 2025-04-06 18:23:03.471858
# Keep-alive comment: 2025-04-07 05:23:27.067215
# Keep-alive comment: 2025-04-07 16:24:26.271935
# Keep-alive comment: 2025-04-08 03:23:42.692484
# Keep-alive comment: 2025-04-08 14:24:02.024725
# Keep-alive comment: 2025-04-09 01:23:26.379945
# Keep-alive comment: 2025-04-09 12:23:07.504535
# Keep-alive comment: 2025-04-09 23:23:26.967353
# Keep-alive comment: 2025-04-10 10:22:35.877967
# Keep-alive comment: 2025-04-10 21:23:00.202615
# Keep-alive comment: 2025-04-11 08:25:11.120800
# Keep-alive comment: 2025-04-11 19:25:31.833868
# Keep-alive comment: 2025-04-12 06:23:07.391594