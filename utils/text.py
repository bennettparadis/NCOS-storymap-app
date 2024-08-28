import streamlit as st

#tab display
def tab_display():
      st.set_page_config(page_title="NC Oyster Sanctuary Data", page_icon=":oyster:", layout="wide")

#text function
def display_text(content, font_size=20, font_weight= 'normal', align='center'):
    st.markdown(
        f"""
        <div style="text-align: {align};">
            <p style="font-size:{font_size}px;font-weight:{font_weight}">{content}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

#sidebar text function for pages labels/links
# Define the custom CSS
custom_css = """
<style>
    /* Change the color and font of the page titles in the sidebar */
    .eczjsme13 {
        color: #00647B !important; /* Replace with your desired color */
        font-weight: bold !important;
        font-size: 16px !important;
    }
</style>
"""

def pages_font():
       st.markdown(custom_css, unsafe_allow_html=True) 
