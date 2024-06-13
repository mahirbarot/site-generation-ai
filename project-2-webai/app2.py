import streamlit as st
import requests
import webbrowser
from random import randint



st.title("News app by: Mahir Barot.")
data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=0708f1aaa69e4091898f3af7960ea177').json()


try:
    with st.empty():
        
        def load_news(index=6):
            st.empty()
            heading=data['articles'][index]['title']
            details=data['articles'][index]['description']
            author=data['articles'][index]['author']
            content=data['articles'][index]['content']
            url=data['articles'][index]['url']
            st.title(heading)
            st.write("")
            st.write("")

            # img_url = data['articles'][index]['urlToImage']
            # raw_data = urlopen(img_url).read()
            # im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            # photo = ImageTk.PhotoImage(im)
            # st.image(photo)
            img=data['articles'][index]['urlToImage']
            st.image(img)
            st.write(details)
            st.write(content)
            st.caption(author)
            col1, col2, col3 = st.columns(3)

            with col3:
                if st.button("Next",key=index+randint(0,333)):
                    # st.empty()
                    load_news(index+1)

            with col2:
                if st.button("Readmore",key=index+randint(4566,5000)):
                    webbrowser.open(url)
            #write code for readmore here
            
            with col1:
                if st.button("Prev",key=index+randint(373,888)):
                    # st.empty()
                    load_news(index-1)
except:
    st.write("We ran into an error... sorry :(")


  


load_news(randint(1,19))


