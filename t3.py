import streamlit as st
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

st.write("This is my first App in ISTM635")
st.title("My first app in ISTM635")

df = pd.DataFrame(np.random.randn(10,2), columns = ["Product A", "Product B"])

data = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(data)

print(df)
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)


#fig, ax = plt.subplots()
#ax.hist(data, bins=15, color = "blue")
#st.pyplot(fig)
#st.pyplot(np.random.normal(1, 2, size = 5000))


st.progress(50)
st.spinner("This is a spinner")

st.sidebar.title("This is a sidebar title") 
st.sidebar.header("This is a sidebar text")

st.image("chart_t1.png")
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.checkbox("This is a checkbox")
st.button("This is a button")
st.radio("This is a radio button", ("Option 1", "Option 2", "Option 3"))
st.selectbox("This is a select box", ("Choice A", "Choice B", "Choice C"))
st.multiselect("This is a multi select", ("Item 1", "Item 2", "Item 3"))
st.slider("This is a slider", 0, 100, 50)
st.select_slider("This is a select slider", ["Low", "Medium", "High"])
st.text_input("This is a text input")
st.text_area("This is a text area")
st.date_input("This is a date input")   
st.time_input("This is a time input")

st.header("This is a header")
st.markdown("This is a markdown cell")

st.latex("e=mc^2")



