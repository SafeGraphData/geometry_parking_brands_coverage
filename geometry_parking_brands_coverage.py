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
# Keep-alive comment: 2025-04-12 17:23:20.748227
# Keep-alive comment: 2025-04-13 04:22:36.697577
# Keep-alive comment: 2025-04-13 15:23:35.115393
# Keep-alive comment: 2025-04-14 02:23:56.301538
# Keep-alive comment: 2025-04-14 13:23:20.098162
# Keep-alive comment: 2025-04-15 00:23:05.345893
# Keep-alive comment: 2025-04-15 11:23:27.325044
# Keep-alive comment: 2025-04-15 22:23:10.890755
# Keep-alive comment: 2025-04-16 09:23:50.176302
# Keep-alive comment: 2025-04-16 20:23:40.516057
# Keep-alive comment: 2025-04-17 07:23:11.557528
# Keep-alive comment: 2025-04-17 18:25:35.081944
# Keep-alive comment: 2025-04-18 05:22:55.874883
# Keep-alive comment: 2025-04-18 16:23:01.247961
# Keep-alive comment: 2025-04-19 03:23:26.234134
# Keep-alive comment: 2025-04-19 14:22:36.980702
# Keep-alive comment: 2025-04-20 01:22:35.729256
# Keep-alive comment: 2025-04-20 12:23:30.609051
# Keep-alive comment: 2025-04-20 23:23:05.371409
# Keep-alive comment: 2025-04-21 10:23:51.615686
# Keep-alive comment: 2025-04-21 21:23:15.196086
# Keep-alive comment: 2025-04-22 08:23:26.005337
# Keep-alive comment: 2025-04-22 19:23:26.022093
# Keep-alive comment: 2025-04-23 06:23:00.145363
# Keep-alive comment: 2025-04-23 17:23:01.912658
# Keep-alive comment: 2025-04-24 04:23:06.354774
# Keep-alive comment: 2025-04-24 15:24:02.127088
# Keep-alive comment: 2025-04-25 02:22:40.122120
# Keep-alive comment: 2025-04-25 13:24:01.080789
# Keep-alive comment: 2025-04-25 16:08:12.400981
# Keep-alive comment: 2025-04-25 16:18:07.308856
# Keep-alive comment: 2025-04-26 00:23:41.252414
# Keep-alive comment: 2025-04-26 11:23:36.919976
# Keep-alive comment: 2025-04-26 22:22:36.083230
# Keep-alive comment: 2025-04-27 09:23:06.706838
# Keep-alive comment: 2025-04-27 20:23:01.540091
# Keep-alive comment: 2025-04-28 07:23:15.261716
# Keep-alive comment: 2025-04-28 18:23:51.530787
# Keep-alive comment: 2025-04-29 05:23:21.457284
# Keep-alive comment: 2025-04-29 16:24:05.449741
# Keep-alive comment: 2025-04-30 03:22:56.308716
# Keep-alive comment: 2025-04-30 14:23:06.114172
# Keep-alive comment: 2025-05-01 01:23:35.576159
# Keep-alive comment: 2025-05-01 12:23:06.245651
# Keep-alive comment: 2025-05-01 23:22:39.451587
# Keep-alive comment: 2025-05-02 10:23:25.357576
# Keep-alive comment: 2025-05-02 21:22:35.583036
# Keep-alive comment: 2025-05-03 08:23:00.247402
# Keep-alive comment: 2025-05-03 19:23:20.132552
# Keep-alive comment: 2025-05-04 06:23:25.517475
# Keep-alive comment: 2025-05-04 17:22:34.851096
# Keep-alive comment: 2025-05-05 04:23:45.115961
# Keep-alive comment: 2025-05-05 15:23:00.584727
# Keep-alive comment: 2025-05-06 02:23:55.048880
# Keep-alive comment: 2025-05-06 13:22:56.016945
# Keep-alive comment: 2025-05-07 00:22:55.938811
# Keep-alive comment: 2025-05-07 11:22:55.822066
# Keep-alive comment: 2025-05-07 22:23:05.536665
# Keep-alive comment: 2025-05-08 09:22:55.721679
# Keep-alive comment: 2025-05-08 20:22:55.627005
# Keep-alive comment: 2025-05-09 07:23:06.201719
# Keep-alive comment: 2025-05-09 18:23:26.560802
# Keep-alive comment: 2025-05-10 05:23:05.402531
# Keep-alive comment: 2025-05-10 16:22:59.665365
# Keep-alive comment: 2025-05-11 03:22:59.867341
# Keep-alive comment: 2025-05-11 14:22:51.762734
# Keep-alive comment: 2025-05-12 01:22:56.989787
# Keep-alive comment: 2025-05-12 12:23:26.307162
# Keep-alive comment: 2025-05-12 23:23:00.270424
# Keep-alive comment: 2025-05-13 10:23:56.577267
# Keep-alive comment: 2025-05-13 21:23:00.491859
# Keep-alive comment: 2025-05-14 08:23:22.548710
# Keep-alive comment: 2025-05-14 19:23:25.851929
# Keep-alive comment: 2025-05-15 06:23:26.807995
# Keep-alive comment: 2025-05-15 17:23:50.788782
# Keep-alive comment: 2025-05-16 04:23:12.492491
# Keep-alive comment: 2025-05-16 15:22:11.661755
# Keep-alive comment: 2025-05-17 02:22:30.579084
# Keep-alive comment: 2025-05-17 13:23:07.607605
# Keep-alive comment: 2025-05-18 00:22:31.580294
# Keep-alive comment: 2025-05-18 11:23:00.723417
# Keep-alive comment: 2025-05-18 22:22:57.986379
# Keep-alive comment: 2025-05-19 09:23:29.057948
# Keep-alive comment: 2025-05-19 20:22:30.889011
# Keep-alive comment: 2025-05-20 07:22:48.236471
# Keep-alive comment: 2025-05-20 18:24:00.436876
# Keep-alive comment: 2025-05-21 05:22:33.050432
# Keep-alive comment: 2025-05-21 16:22:41.106487
# Keep-alive comment: 2025-05-22 03:22:35.397037
# Keep-alive comment: 2025-05-22 14:22:31.856919
# Keep-alive comment: 2025-05-23 01:22:37.927753
# Keep-alive comment: 2025-05-23 12:22:38.097798
# Keep-alive comment: 2025-05-23 23:22:42.854512
# Keep-alive comment: 2025-05-24 10:22:40.899318
# Keep-alive comment: 2025-05-24 21:22:37.594987
# Keep-alive comment: 2025-05-25 08:22:36.593903
# Keep-alive comment: 2025-05-25 19:22:42.770346
# Keep-alive comment: 2025-05-26 06:22:27.673538
# Keep-alive comment: 2025-05-26 17:22:32.089900
# Keep-alive comment: 2025-05-27 04:22:37.902062
# Keep-alive comment: 2025-05-27 15:22:41.514715
# Keep-alive comment: 2025-05-28 02:22:51.561627
# Keep-alive comment: 2025-05-28 13:22:39.595773
# Keep-alive comment: 2025-05-29 00:22:35.985152
# Keep-alive comment: 2025-05-29 11:22:30.774283
# Keep-alive comment: 2025-05-29 22:22:45.570958
# Keep-alive comment: 2025-05-30 09:22:30.068338
# Keep-alive comment: 2025-05-30 20:22:31.197108
# Keep-alive comment: 2025-05-31 07:22:42.965376
# Keep-alive comment: 2025-05-31 18:22:38.576655
# Keep-alive comment: 2025-06-01 05:22:37.072242
# Keep-alive comment: 2025-06-01 16:22:50.444830
# Keep-alive comment: 2025-06-02 03:22:51.894407
# Keep-alive comment: 2025-06-02 14:22:41.821182
# Keep-alive comment: 2025-06-03 01:22:32.862642
# Keep-alive comment: 2025-06-03 12:22:46.500729
# Keep-alive comment: 2025-06-03 23:22:40.761236
# Keep-alive comment: 2025-06-04 10:22:41.932476
# Keep-alive comment: 2025-06-04 21:22:20.698483
# Keep-alive comment: 2025-06-05 08:22:43.496307
# Keep-alive comment: 2025-06-05 19:22:33.426042
# Keep-alive comment: 2025-06-06 06:22:32.559859
# Keep-alive comment: 2025-06-06 17:22:15.572062
# Keep-alive comment: 2025-06-07 04:22:17.493625
# Keep-alive comment: 2025-06-07 15:22:27.021875
# Keep-alive comment: 2025-06-08 02:22:32.343547
# Keep-alive comment: 2025-06-08 13:22:33.873173
# Keep-alive comment: 2025-06-09 00:22:16.615994
# Keep-alive comment: 2025-06-09 11:22:30.917153
# Keep-alive comment: 2025-06-09 22:22:39.038922
# Keep-alive comment: 2025-06-10 09:22:41.049877
# Keep-alive comment: 2025-06-10 20:22:35.430807
# Keep-alive comment: 2025-06-11 07:22:36.392905
# Keep-alive comment: 2025-06-11 18:24:22.753615
# Keep-alive comment: 2025-06-12 05:22:33.599280
# Keep-alive comment: 2025-06-12 16:22:36.729369
# Keep-alive comment: 2025-06-13 03:22:37.971273
# Keep-alive comment: 2025-06-13 14:22:26.931608
# Keep-alive comment: 2025-06-14 01:22:46.791197
# Keep-alive comment: 2025-06-14 12:22:34.553909
# Keep-alive comment: 2025-06-14 23:22:25.399064
# Keep-alive comment: 2025-06-15 10:22:11.236577
# Keep-alive comment: 2025-06-15 21:22:46.475369
# Keep-alive comment: 2025-06-16 08:22:42.378212
# Keep-alive comment: 2025-06-16 19:22:26.583228
# Keep-alive comment: 2025-06-17 06:23:03.684330
# Keep-alive comment: 2025-06-17 17:22:31.204382
# Keep-alive comment: 2025-06-18 04:22:38.387868
# Keep-alive comment: 2025-06-18 15:22:34.047582
# Keep-alive comment: 2025-06-19 02:22:35.569728
# Keep-alive comment: 2025-06-19 13:22:34.469690
# Keep-alive comment: 2025-06-20 00:22:32.106717
# Keep-alive comment: 2025-06-20 11:23:21.169013
# Keep-alive comment: 2025-06-20 22:22:41.180538
# Keep-alive comment: 2025-06-21 09:22:26.782122
# Keep-alive comment: 2025-06-21 20:22:38.523175
# Keep-alive comment: 2025-06-22 07:22:31.775195
# Keep-alive comment: 2025-06-22 18:22:22.286927
# Keep-alive comment: 2025-06-23 05:22:38.922787
# Keep-alive comment: 2025-06-23 16:22:31.303034
# Keep-alive comment: 2025-06-24 03:22:37.972444
# Keep-alive comment: 2025-06-24 14:22:16.488361
# Keep-alive comment: 2025-06-25 01:22:10.770576
# Keep-alive comment: 2025-06-25 12:22:32.651995
# Keep-alive comment: 2025-06-25 23:22:36.131944
# Keep-alive comment: 2025-06-26 10:22:43.667275
# Keep-alive comment: 2025-06-26 21:24:06.913638
# Keep-alive comment: 2025-06-27 08:22:36.789118
# Keep-alive comment: 2025-06-27 19:22:33.516412
# Keep-alive comment: 2025-06-28 06:22:41.438623
# Keep-alive comment: 2025-06-28 17:22:31.823454
# Keep-alive comment: 2025-06-29 04:22:20.660497
# Keep-alive comment: 2025-06-29 15:22:11.437619
# Keep-alive comment: 2025-06-30 02:22:32.666033
# Keep-alive comment: 2025-06-30 13:22:13.058068
# Keep-alive comment: 2025-07-01 00:24:18.388644
# Keep-alive comment: 2025-07-01 11:22:32.935093
# Keep-alive comment: 2025-07-01 22:22:37.855058
# Keep-alive comment: 2025-07-02 09:22:31.375157
# Keep-alive comment: 2025-07-02 20:24:20.095061
# Keep-alive comment: 2025-07-03 07:22:46.207942
# Keep-alive comment: 2025-07-03 18:22:10.545506
# Keep-alive comment: 2025-07-04 05:22:34.951474
# Keep-alive comment: 2025-07-04 16:22:31.153412
# Keep-alive comment: 2025-07-05 03:22:30.403073
# Keep-alive comment: 2025-07-05 14:22:35.658833
# Keep-alive comment: 2025-07-06 01:22:32.321588
# Keep-alive comment: 2025-07-06 12:22:30.087732
# Keep-alive comment: 2025-07-06 23:22:31.051365
# Keep-alive comment: 2025-07-07 10:22:31.191363
# Keep-alive comment: 2025-07-07 21:22:29.772223
# Keep-alive comment: 2025-07-08 08:22:35.245507
# Keep-alive comment: 2025-07-08 19:22:30.312574
# Keep-alive comment: 2025-07-09 06:22:42.272024
# Keep-alive comment: 2025-07-09 17:23:14.522396
# Keep-alive comment: 2025-07-10 04:22:30.663182
# Keep-alive comment: 2025-07-10 15:22:35.200679
# Keep-alive comment: 2025-07-11 02:22:29.828425
# Keep-alive comment: 2025-07-11 13:22:30.144654
# Keep-alive comment: 2025-07-12 00:22:16.753584
# Keep-alive comment: 2025-07-12 11:22:35.295388
# Keep-alive comment: 2025-07-12 22:22:31.346735
# Keep-alive comment: 2025-07-13 09:22:31.360664
# Keep-alive comment: 2025-07-13 20:22:15.559664
# Keep-alive comment: 2025-07-14 07:22:26.628130
# Keep-alive comment: 2025-07-14 18:22:50.171692
# Keep-alive comment: 2025-07-15 05:22:41.242671
# Keep-alive comment: 2025-07-15 16:22:35.153835
# Keep-alive comment: 2025-07-16 03:22:35.337508