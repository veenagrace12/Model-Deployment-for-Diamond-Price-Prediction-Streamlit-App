import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(
    page_title="Diamond App",
    page_icon="💎",
)




st.title("🏠Home Page")
st.header("💠 Welcome to Diamond Price Application 💠 ")
st.sidebar.success("Select a page above.")

################################## DATA LOADING #######################################
df=pd.read_csv('data/diamonds.csv')

st.subheader('About Diamond')
st.markdown('Diamond is a solid form of the element carbon with its atoms arranged in a crystal structure called diamond cubic. At room temperature and pressure, another solid form of carbon known as graphite is the chemically stable form of carbon, but diamond converts to it extremely slowly. Diamond has the highest hardness and thermal conductivity of any natural material, properties that are used in major industrial applications such as cutting and polishing tools.')

st.subheader("Understanding 4C's")
st.markdown('The value of diamonds depends upon their structure, cut, inclusions (impurity), carats, and many other features. They are graded and certified based on the "four Cs", which are COLOR, CUT, CLARITY, and CARAT. These are the only metrics that are being used to the quality of diamonds and sets the price of the diamond.')

st.subheader("1.CUT")
st.markdown("Cut is the only diamond component not influenced by nature, and Mills considers this the most important of the 4Cs. This factor refers to the quality of the diamond's cut, not the shape or size, and how well the stone is faceted, proportioned, and polished.")
img1 = Image.open("images/cut.jpg")
st.image(img1, width=700)
st.markdown('Details of cut')
img2 = Image.open("images/diamond-cut-details.jpg")
st.image(img2, width=700)


st.subheader("2.COLOR")
st.markdown("Diamond colors fall under a D-Z scale, with D meaning completely colorless (and the most expensive), and Z having a light yellow hue.")
img3 = Image.open("images/color.jpg")
st.image(img3, width=700)
st.markdown('Details of all colors')
img4 = Image.open("images/colors.jpg")
st.image(img4, width=700)


st.subheader("3.CLARITY")
st.markdown("This C involves the number of natural imperfections, called inclusions, present in the diamond, and whether you can see them with the unaided eye.")
img5 = Image.open("images/clarity.jpg")
st.image(img5, width=700)
st.markdown("For all other shapes, starting at SI1 [Slightly Included] clarity and up, you should not normally see any imperfections visible to the naked eye. Sometimes even SI2 diamonds can be very eye-clean, as well, but generally stick with SI1 and up.")


st.subheader("4.CARAT")
st.markdown("Carat refers to a measurement of the actual weight of the diamond. According to GIA, one carat converts to 0.2 grams, which is essentially the same weight as a paper clip. Naturally, the larger the carat, the more expensive the diamond.")
img6 = Image.open("images/carat.jpg")
st.image(img6, width=700)


################################## BACKGROUND IMAGE CODE #######################################
page_bg_img = '''
<style>
.stApp {
background-image: url("https://www.pixelstalk.net/wp-content/uploads/2016/10/Black-diamond-images-high-resolution-2560x1440.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
