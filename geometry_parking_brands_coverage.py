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
# Keep-alive comment: 2025-07-16 14:22:35.308386
# Keep-alive comment: 2025-07-17 01:22:30.723342
# Keep-alive comment: 2025-07-17 12:22:36.375486
# Keep-alive comment: 2025-07-17 23:22:29.205316
# Keep-alive comment: 2025-07-18 10:22:50.222855
# Keep-alive comment: 2025-07-18 21:22:30.348231
# Keep-alive comment: 2025-07-19 08:23:11.069188
# Keep-alive comment: 2025-07-19 19:22:15.783936
# Keep-alive comment: 2025-07-20 06:22:40.428436
# Keep-alive comment: 2025-07-20 17:22:46.117143
# Keep-alive comment: 2025-07-21 04:22:40.665968
# Keep-alive comment: 2025-07-21 15:22:26.384744
# Keep-alive comment: 2025-07-22 02:22:50.136684
# Keep-alive comment: 2025-07-22 13:23:02.290653
# Keep-alive comment: 2025-07-23 00:22:37.042155
# Keep-alive comment: 2025-07-23 11:22:25.963154
# Keep-alive comment: 2025-07-23 22:22:29.734922
# Keep-alive comment: 2025-07-24 09:22:45.681648
# Keep-alive comment: 2025-07-24 20:22:31.098748
# Keep-alive comment: 2025-07-25 07:22:25.728295
# Keep-alive comment: 2025-07-25 18:22:30.428831
# Keep-alive comment: 2025-07-26 05:22:26.239285
# Keep-alive comment: 2025-07-26 16:22:30.287271
# Keep-alive comment: 2025-07-27 03:22:25.630823
# Keep-alive comment: 2025-07-27 14:22:16.151290
# Keep-alive comment: 2025-07-28 01:22:36.589739
# Keep-alive comment: 2025-07-28 12:22:31.541614
# Keep-alive comment: 2025-07-28 23:22:30.153836
# Keep-alive comment: 2025-07-29 10:22:04.901809
# Keep-alive comment: 2025-07-29 21:22:35.982341
# Keep-alive comment: 2025-07-30 08:22:31.806760
# Keep-alive comment: 2025-07-30 19:22:40.148700
# Keep-alive comment: 2025-07-31 06:22:45.378807
# Keep-alive comment: 2025-07-31 17:22:30.956633
# Keep-alive comment: 2025-08-01 04:22:29.801208
# Keep-alive comment: 2025-08-01 15:22:40.225973
# Keep-alive comment: 2025-08-02 02:22:25.621178
# Keep-alive comment: 2025-08-02 13:22:36.018150
# Keep-alive comment: 2025-08-03 00:22:31.548638
# Keep-alive comment: 2025-08-03 11:22:36.421721
# Keep-alive comment: 2025-08-03 22:22:30.982549
# Keep-alive comment: 2025-08-04 09:22:27.108935
# Keep-alive comment: 2025-08-04 20:22:30.643171
# Keep-alive comment: 2025-08-05 07:22:33.887155
# Keep-alive comment: 2025-08-05 18:22:35.095754
# Keep-alive comment: 2025-08-06 05:22:30.641486
# Keep-alive comment: 2025-08-06 16:24:20.687975
# Keep-alive comment: 2025-08-07 03:22:35.060068
# Keep-alive comment: 2025-08-07 14:22:35.914005
# Keep-alive comment: 2025-08-08 01:22:25.264938
# Keep-alive comment: 2025-08-08 12:22:36.030714
# Keep-alive comment: 2025-08-08 23:22:36.830082
# Keep-alive comment: 2025-08-09 10:22:30.718108
# Keep-alive comment: 2025-08-09 21:22:52.089697
# Keep-alive comment: 2025-08-10 08:22:36.835427
# Keep-alive comment: 2025-08-10 19:22:36.813851
# Keep-alive comment: 2025-08-11 06:22:30.710824
# Keep-alive comment: 2025-08-11 17:22:35.750906
# Keep-alive comment: 2025-08-12 04:22:35.161097
# Keep-alive comment: 2025-08-12 15:22:26.568533
# Keep-alive comment: 2025-08-13 02:22:35.910444
# Keep-alive comment: 2025-08-13 13:22:30.880079
# Keep-alive comment: 2025-08-14 00:22:29.776528
# Keep-alive comment: 2025-08-14 11:22:36.657528
# Keep-alive comment: 2025-08-14 22:22:30.435781
# Keep-alive comment: 2025-08-15 09:22:30.044565
# Keep-alive comment: 2025-08-15 20:22:19.826104
# Keep-alive comment: 2025-08-16 07:22:45.100807
# Keep-alive comment: 2025-08-16 18:22:30.387186
# Keep-alive comment: 2025-08-17 05:22:34.609336
# Keep-alive comment: 2025-08-17 16:22:29.907319
# Keep-alive comment: 2025-08-18 03:22:30.809899
# Keep-alive comment: 2025-08-18 14:22:30.912861
# Keep-alive comment: 2025-08-19 01:22:30.972249
# Keep-alive comment: 2025-08-19 12:22:35.832279
# Keep-alive comment: 2025-08-19 23:22:57.687318
# Keep-alive comment: 2025-08-20 10:22:31.090868
# Keep-alive comment: 2025-08-20 21:22:35.615524
# Keep-alive comment: 2025-08-21 08:22:32.101629
# Keep-alive comment: 2025-08-21 19:22:36.268698
# Keep-alive comment: 2025-08-22 06:22:35.915321
# Keep-alive comment: 2025-08-22 17:22:31.076117
# Keep-alive comment: 2025-08-23 04:22:40.815287
# Keep-alive comment: 2025-08-23 15:22:29.789878
# Keep-alive comment: 2025-08-24 02:22:29.916435
# Keep-alive comment: 2025-08-24 13:22:30.564498
# Keep-alive comment: 2025-08-25 00:22:36.562182
# Keep-alive comment: 2025-08-25 11:22:35.684768
# Keep-alive comment: 2025-08-25 22:22:30.644504
# Keep-alive comment: 2025-08-26 09:22:31.110185
# Keep-alive comment: 2025-08-26 20:22:35.329504
# Keep-alive comment: 2025-08-27 07:22:40.529204
# Keep-alive comment: 2025-08-27 18:22:10.233644
# Keep-alive comment: 2025-08-28 05:22:40.812221
# Keep-alive comment: 2025-08-28 16:22:30.725551
# Keep-alive comment: 2025-08-29 03:22:14.950244
# Keep-alive comment: 2025-08-29 14:22:20.509394
# Keep-alive comment: 2025-08-30 01:22:20.097345
# Keep-alive comment: 2025-08-30 12:22:15.938664
# Keep-alive comment: 2025-08-30 23:22:19.485070
# Keep-alive comment: 2025-08-31 10:22:15.152770
# Keep-alive comment: 2025-08-31 21:22:26.786964
# Keep-alive comment: 2025-09-01 08:22:27.823367
# Keep-alive comment: 2025-09-01 19:22:26.996949
# Keep-alive comment: 2025-09-02 06:22:15.195443
# Keep-alive comment: 2025-09-02 17:22:26.290133
# Keep-alive comment: 2025-09-03 04:22:19.518535
# Keep-alive comment: 2025-09-03 15:22:21.049483
# Keep-alive comment: 2025-09-04 02:22:25.206846
# Keep-alive comment: 2025-09-04 13:22:29.249535
# Keep-alive comment: 2025-09-05 00:22:16.001440
# Keep-alive comment: 2025-09-05 11:22:10.831781
# Keep-alive comment: 2025-09-05 22:22:20.274892
# Keep-alive comment: 2025-09-06 09:22:16.685564
# Keep-alive comment: 2025-09-06 20:22:15.625002
# Keep-alive comment: 2025-09-07 07:22:21.264187
# Keep-alive comment: 2025-09-07 18:22:21.300046
# Keep-alive comment: 2025-09-08 05:22:17.231107
# Keep-alive comment: 2025-09-08 16:22:21.460877
# Keep-alive comment: 2025-09-09 03:22:46.630898
# Keep-alive comment: 2025-09-09 14:22:21.416519
# Keep-alive comment: 2025-09-10 01:22:14.842625
# Keep-alive comment: 2025-09-10 12:22:26.284503
# Keep-alive comment: 2025-09-10 23:22:15.545848
# Keep-alive comment: 2025-09-11 10:22:18.159586
# Keep-alive comment: 2025-09-11 21:22:15.981795
# Keep-alive comment: 2025-09-12 08:22:30.468397
# Keep-alive comment: 2025-09-12 19:22:21.005605
# Keep-alive comment: 2025-09-13 06:22:10.133946
# Keep-alive comment: 2025-09-13 17:22:16.772151
# Keep-alive comment: 2025-09-14 04:22:06.549197
# Keep-alive comment: 2025-09-14 15:22:17.972133
# Keep-alive comment: 2025-09-15 02:22:15.320038
# Keep-alive comment: 2025-09-15 13:22:16.663771
# Keep-alive comment: 2025-09-16 00:22:15.821188
# Keep-alive comment: 2025-09-16 11:22:21.023782
# Keep-alive comment: 2025-09-16 22:22:15.169617
# Keep-alive comment: 2025-09-17 09:22:16.793140
# Keep-alive comment: 2025-09-17 20:22:26.164723
# Keep-alive comment: 2025-09-18 07:22:22.851048
# Keep-alive comment: 2025-09-18 18:22:22.120704
# Keep-alive comment: 2025-09-19 05:22:16.926131
# Keep-alive comment: 2025-09-19 16:22:50.817490
# Keep-alive comment: 2025-09-20 03:22:21.181130
# Keep-alive comment: 2025-09-20 14:22:22.044387
# Keep-alive comment: 2025-09-21 01:22:21.455801
# Keep-alive comment: 2025-09-21 12:22:21.119989
# Keep-alive comment: 2025-09-21 23:22:16.508261
# Keep-alive comment: 2025-09-22 10:22:18.526008
# Keep-alive comment: 2025-09-22 21:22:15.266425
# Keep-alive comment: 2025-09-23 08:22:16.593928
# Keep-alive comment: 2025-09-23 19:22:22.084370
# Keep-alive comment: 2025-09-24 06:22:15.942551
# Keep-alive comment: 2025-09-24 17:22:20.602345
# Keep-alive comment: 2025-09-25 04:22:25.954087
# Keep-alive comment: 2025-09-25 15:22:25.762612
# Keep-alive comment: 2025-09-26 02:22:21.661770
# Keep-alive comment: 2025-09-26 13:22:25.558653
# Keep-alive comment: 2025-09-26 19:30:52.789121
# Keep-alive comment: 2025-09-27 05:30:59.115516
# Keep-alive comment: 2025-09-27 15:30:53.183548
# Keep-alive comment: 2025-09-28 01:30:57.351309
# Keep-alive comment: 2025-09-28 11:30:58.177268
# Keep-alive comment: 2025-09-28 21:30:57.787659
# Keep-alive comment: 2025-09-29 07:31:03.713491
# Keep-alive comment: 2025-09-29 17:31:13.738553
# Keep-alive comment: 2025-09-30 03:30:52.301592
# Keep-alive comment: 2025-09-30 13:30:58.308507
# Keep-alive comment: 2025-09-30 23:31:17.938967
# Keep-alive comment: 2025-10-01 09:31:23.943109
# Keep-alive comment: 2025-10-01 19:30:57.741550
# Keep-alive comment: 2025-10-02 05:31:27.082546
# Keep-alive comment: 2025-10-02 15:31:24.002565
# Keep-alive comment: 2025-10-03 01:30:57.561693
# Keep-alive comment: 2025-10-03 11:31:18.513451
# Keep-alive comment: 2025-10-03 21:30:52.646893
# Keep-alive comment: 2025-10-04 07:30:53.180305
# Keep-alive comment: 2025-10-04 17:31:03.040723
# Keep-alive comment: 2025-10-05 03:30:58.108404
# Keep-alive comment: 2025-10-05 13:31:02.792607
# Keep-alive comment: 2025-10-05 23:31:23.248064
# Keep-alive comment: 2025-10-06 09:31:28.538674
# Keep-alive comment: 2025-10-06 19:30:58.679984
# Keep-alive comment: 2025-10-07 05:30:59.915325
# Keep-alive comment: 2025-10-07 15:31:20.733876
# Keep-alive comment: 2025-10-08 01:30:58.563010
# Keep-alive comment: 2025-10-08 11:30:59.205685
# Keep-alive comment: 2025-10-08 21:30:58.602771
# Keep-alive comment: 2025-10-09 07:31:00.979000
# Keep-alive comment: 2025-10-09 17:31:00.196931
# Keep-alive comment: 2025-10-10 03:30:48.868895
# Keep-alive comment: 2025-10-10 13:30:39.708931
# Keep-alive comment: 2025-10-10 23:30:53.290006
# Keep-alive comment: 2025-10-11 09:30:59.194125
# Keep-alive comment: 2025-10-11 19:30:52.953538
# Keep-alive comment: 2025-10-12 05:30:56.042720
# Keep-alive comment: 2025-10-12 15:31:00.194832
# Keep-alive comment: 2025-10-13 01:30:54.761615
# Keep-alive comment: 2025-10-13 11:31:26.147073
# Keep-alive comment: 2025-10-13 21:30:48.977537
# Keep-alive comment: 2025-10-14 07:30:52.681180
# Keep-alive comment: 2025-10-14 17:30:55.547517
# Keep-alive comment: 2025-10-15 03:30:53.121960
# Keep-alive comment: 2025-10-15 13:30:54.300780
# Keep-alive comment: 2025-10-15 23:30:58.562769
# Keep-alive comment: 2025-10-16 09:30:54.123168
# Keep-alive comment: 2025-10-16 19:30:59.734327
# Keep-alive comment: 2025-10-17 05:30:58.946504
# Keep-alive comment: 2025-10-17 15:31:15.096614
# Keep-alive comment: 2025-10-18 01:30:54.423624
# Keep-alive comment: 2025-10-18 11:31:19.512464
# Keep-alive comment: 2025-10-18 21:31:29.151910
# Keep-alive comment: 2025-10-19 07:30:48.989250
# Keep-alive comment: 2025-10-19 17:31:23.892538
# Keep-alive comment: 2025-10-20 03:31:21.263733
# Keep-alive comment: 2025-10-20 13:30:59.383441
# Keep-alive comment: 2025-10-20 23:30:53.848274
# Keep-alive comment: 2025-10-21 09:30:59.464351
# Keep-alive comment: 2025-10-21 19:32:59.578358
# Keep-alive comment: 2025-10-22 05:30:54.966102
# Keep-alive comment: 2025-10-22 15:31:59.488920
# Keep-alive comment: 2025-10-23 01:30:54.136177
# Keep-alive comment: 2025-10-23 11:31:06.334952
# Keep-alive comment: 2025-10-23 21:30:55.256089
# Keep-alive comment: 2025-10-24 07:32:15.122252
# Keep-alive comment: 2025-10-24 17:31:04.834153
# Keep-alive comment: 2025-10-25 03:30:59.683784
# Keep-alive comment: 2025-10-25 13:31:23.814200
# Keep-alive comment: 2025-10-25 23:30:55.218499
# Keep-alive comment: 2025-10-26 09:30:49.018355
# Keep-alive comment: 2025-10-26 19:31:25.696497
# Keep-alive comment: 2025-10-27 05:31:05.785801
# Keep-alive comment: 2025-10-27 15:31:20.018601
# Keep-alive comment: 2025-10-28 01:30:58.503696
# Keep-alive comment: 2025-10-28 11:31:00.455996
# Keep-alive comment: 2025-10-28 21:30:48.956920
# Keep-alive comment: 2025-10-29 07:30:56.076958
# Keep-alive comment: 2025-10-29 17:31:04.102765
# Keep-alive comment: 2025-10-30 03:30:54.731266
# Keep-alive comment: 2025-10-30 13:31:25.679892
# Keep-alive comment: 2025-10-30 23:31:00.411404
# Keep-alive comment: 2025-10-31 09:32:15.200310
# Keep-alive comment: 2025-10-31 19:30:50.483407
# Keep-alive comment: 2025-11-01 05:30:59.302174
# Keep-alive comment: 2025-11-01 15:30:48.438645
# Keep-alive comment: 2025-11-02 01:30:59.618515
# Keep-alive comment: 2025-11-02 11:31:01.075988
# Keep-alive comment: 2025-11-02 21:31:15.701329
# Keep-alive comment: 2025-11-03 07:30:55.430102
# Keep-alive comment: 2025-11-03 17:30:59.002275
# Keep-alive comment: 2025-11-04 03:30:59.609445
# Keep-alive comment: 2025-11-04 13:31:26.871279
# Keep-alive comment: 2025-11-04 23:31:18.702407
# Keep-alive comment: 2025-11-05 09:31:30.124599
# Keep-alive comment: 2025-11-05 19:30:59.583532
# Keep-alive comment: 2025-11-06 05:31:25.217280
# Keep-alive comment: 2025-11-06 15:31:12.291476
# Keep-alive comment: 2025-11-07 01:30:57.571292
# Keep-alive comment: 2025-11-07 11:31:00.647116
# Keep-alive comment: 2025-11-07 21:31:00.956673
# Keep-alive comment: 2025-11-08 07:30:49.778441
# Keep-alive comment: 2025-11-08 17:31:05.428854
# Keep-alive comment: 2025-11-09 03:31:39.660210
# Keep-alive comment: 2025-11-09 13:31:00.233031
# Keep-alive comment: 2025-11-09 23:30:50.035552
# Keep-alive comment: 2025-11-10 09:30:55.093841
# Keep-alive comment: 2025-11-10 19:31:10.636268
# Keep-alive comment: 2025-11-11 05:30:56.622715
# Keep-alive comment: 2025-11-11 15:30:53.968262
# Keep-alive comment: 2025-11-12 01:31:02.059189
# Keep-alive comment: 2025-11-12 11:31:03.447282
# Keep-alive comment: 2025-11-12 21:31:20.220652
# Keep-alive comment: 2025-11-13 07:30:43.190370
# Keep-alive comment: 2025-11-13 17:30:55.360252
# Keep-alive comment: 2025-11-14 03:31:02.403907
# Keep-alive comment: 2025-11-14 13:31:23.307104
# Keep-alive comment: 2025-11-14 23:30:55.485751
# Keep-alive comment: 2025-11-15 09:30:59.502109
# Keep-alive comment: 2025-11-15 19:31:04.795547
# Keep-alive comment: 2025-11-16 05:30:55.926947
# Keep-alive comment: 2025-11-16 15:31:01.066857
# Keep-alive comment: 2025-11-17 01:30:50.365314
# Keep-alive comment: 2025-11-17 11:31:24.448726
# Keep-alive comment: 2025-11-17 21:30:50.492208
# Keep-alive comment: 2025-11-18 07:30:54.518813
# Keep-alive comment: 2025-11-18 17:30:54.461314
# Keep-alive comment: 2025-11-19 03:30:58.959990
# Keep-alive comment: 2025-11-19 13:30:50.591408
# Keep-alive comment: 2025-11-19 23:30:53.529656
# Keep-alive comment: 2025-11-20 09:31:00.582434
# Keep-alive comment: 2025-11-20 19:32:50.114052
# Keep-alive comment: 2025-11-21 05:30:55.983766
# Keep-alive comment: 2025-11-21 15:31:00.170528
# Keep-alive comment: 2025-11-22 01:31:04.860199
# Keep-alive comment: 2025-11-22 11:30:50.009319
# Keep-alive comment: 2025-11-22 21:31:00.381012
# Keep-alive comment: 2025-11-23 07:31:01.156876
# Keep-alive comment: 2025-11-23 17:31:01.364500
# Keep-alive comment: 2025-11-24 03:30:54.820559
# Keep-alive comment: 2025-11-24 13:30:49.805249
# Keep-alive comment: 2025-11-24 23:31:00.740019
# Keep-alive comment: 2025-11-25 09:31:20.962615
# Keep-alive comment: 2025-11-25 19:30:55.656755
# Keep-alive comment: 2025-11-26 15:31:02.567854
# Keep-alive comment: 2025-11-27 01:30:59.562373
# Keep-alive comment: 2025-11-27 11:30:56.291493
# Keep-alive comment: 2025-11-27 21:30:50.964001
# Keep-alive comment: 2025-11-28 07:30:49.727416
# Keep-alive comment: 2025-11-28 17:31:00.857020
# Keep-alive comment: 2025-11-29 03:30:55.829496
# Keep-alive comment: 2025-11-29 13:31:05.958664
# Keep-alive comment: 2025-11-29 23:30:55.412011
# Keep-alive comment: 2025-11-30 09:30:57.627921
# Keep-alive comment: 2025-11-30 19:30:46.031897
# Keep-alive comment: 2025-12-01 05:30:45.243846
# Keep-alive comment: 2025-12-01 15:30:50.244372
# Keep-alive comment: 2025-12-02 01:30:35.541080
# Keep-alive comment: 2025-12-02 11:30:57.242412
# Keep-alive comment: 2025-12-02 21:30:59.020042
# Keep-alive comment: 2025-12-03 07:30:57.044039
# Keep-alive comment: 2025-12-03 17:31:04.086795
# Keep-alive comment: 2025-12-04 03:30:54.333753
# Keep-alive comment: 2025-12-04 13:30:51.909126
# Keep-alive comment: 2025-12-04 23:30:54.895820
# Keep-alive comment: 2025-12-05 09:30:54.781294
# Keep-alive comment: 2025-12-05 19:30:49.609313
# Keep-alive comment: 2025-12-06 05:30:56.049072
# Keep-alive comment: 2025-12-06 15:30:42.852624
# Keep-alive comment: 2025-12-07 01:30:51.879469
# Keep-alive comment: 2025-12-07 11:30:55.575297
# Keep-alive comment: 2025-12-07 21:30:51.748010
# Keep-alive comment: 2025-12-08 07:31:05.009720
# Keep-alive comment: 2025-12-08 17:30:49.734492
# Keep-alive comment: 2025-12-09 03:30:54.973190
# Keep-alive comment: 2025-12-09 13:30:53.334582
# Keep-alive comment: 2025-12-09 23:30:55.410900
# Keep-alive comment: 2025-12-10 09:30:56.434237
# Keep-alive comment: 2025-12-10 19:31:01.039036
# Keep-alive comment: 2025-12-11 05:30:36.031875
# Keep-alive comment: 2025-12-11 15:30:56.896177
# Keep-alive comment: 2025-12-12 01:30:55.099649
# Keep-alive comment: 2025-12-12 11:30:41.057866
# Keep-alive comment: 2025-12-12 21:31:00.298666
# Keep-alive comment: 2025-12-13 07:30:54.888009
# Keep-alive comment: 2025-12-13 17:30:56.636811
# Keep-alive comment: 2025-12-14 03:30:58.888928
# Keep-alive comment: 2025-12-14 13:30:53.870831
# Keep-alive comment: 2025-12-14 23:30:49.483989
# Keep-alive comment: 2025-12-15 09:30:54.561263
# Keep-alive comment: 2025-12-15 19:30:54.148842
# Keep-alive comment: 2025-12-16 05:31:02.109748
# Keep-alive comment: 2025-12-16 15:30:49.235619
# Keep-alive comment: 2025-12-17 01:31:20.503337
# Keep-alive comment: 2025-12-17 11:30:49.443683
# Keep-alive comment: 2025-12-17 21:34:04.602048
# Keep-alive comment: 2025-12-18 07:30:55.857346
# Keep-alive comment: 2025-12-18 17:31:02.471207
# Keep-alive comment: 2025-12-19 03:30:57.582865
# Keep-alive comment: 2025-12-19 13:30:52.687957
# Keep-alive comment: 2025-12-19 23:31:34.304555
# Keep-alive comment: 2025-12-20 09:30:40.175438
# Keep-alive comment: 2025-12-20 19:30:55.568175
# Keep-alive comment: 2025-12-21 05:30:54.240905
# Keep-alive comment: 2025-12-21 15:30:38.888813
# Keep-alive comment: 2025-12-22 01:30:53.418101
# Keep-alive comment: 2025-12-22 11:30:56.187715
# Keep-alive comment: 2025-12-22 21:30:39.909123
# Keep-alive comment: 2025-12-23 07:30:56.686612
# Keep-alive comment: 2025-12-23 17:30:58.599955
# Keep-alive comment: 2025-12-24 03:30:45.596309
# Keep-alive comment: 2025-12-24 13:30:40.566148
# Keep-alive comment: 2025-12-24 23:30:47.973881
# Keep-alive comment: 2025-12-25 09:31:01.151926
# Keep-alive comment: 2025-12-25 19:30:54.884216
# Keep-alive comment: 2025-12-26 05:30:55.115389
# Keep-alive comment: 2025-12-26 15:30:54.226907
# Keep-alive comment: 2025-12-27 01:30:48.319515
# Keep-alive comment: 2025-12-27 11:30:53.725638
# Keep-alive comment: 2025-12-27 21:30:54.609661
# Keep-alive comment: 2025-12-28 07:30:54.170762
# Keep-alive comment: 2025-12-28 17:31:01.251458
# Keep-alive comment: 2025-12-29 03:30:49.194835
# Keep-alive comment: 2025-12-29 13:30:55.527306
# Keep-alive comment: 2025-12-29 23:30:49.569693
# Keep-alive comment: 2025-12-30 09:30:39.821978
# Keep-alive comment: 2025-12-30 19:30:58.449245
# Keep-alive comment: 2025-12-31 05:30:50.952217
# Keep-alive comment: 2025-12-31 15:30:51.678592
# Keep-alive comment: 2026-01-01 01:31:00.698739
# Keep-alive comment: 2026-01-01 11:30:55.974338
# Keep-alive comment: 2026-01-01 21:31:06.819195
# Keep-alive comment: 2026-01-02 07:30:57.198941
# Keep-alive comment: 2026-01-02 17:30:54.194929