import streamlit as st
from plotly.express import pie
from pandas import DataFrame
from requests import get

st.title('Распределение книг по жанрам')
st.markdown('Перейти к [Книжному каталогу](http://1.cshse.beget.tech/books "click")')

api_resp = get('http://1.cshse.beget.tech/action/get_genres_stats')
df = DataFrame(data=dict(api_resp.json()))
chart = pie(
        df,
        title='Круговая диаграмма',
        values='genre_weights',
        names='genre_names'
    )

st.plotly_chart(chart)
