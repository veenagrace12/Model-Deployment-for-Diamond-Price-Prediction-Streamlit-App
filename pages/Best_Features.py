import streamlit as st
import pandas as pd
import plotly.express as px
from pickle import load


df=pd.read_csv('data/diamonds.csv')


# Dataset details
st.title('Diamond Dataset')
data = st.radio(label='Show DataFrame', options= ['Top 5','Columns'] )

if data=='Top 5':
    st.write(df.head(5))
else:
    st.write(set(df.columns))

# Data Description
st.subheader('Statistical Analysis')
dsrb = st.checkbox(label='Data Description')
if dsrb:
    st.write('Data Description')
    st.write(df.describe())  

# Loading pretrained models from pickle file
or_enc=load(open('models/ordinal_encoder.pkl','rb'))
scaler = load(open('models/StandardScaler.pkl', 'rb'))
features=df[['carat','cut','color','clarity','depth','table','x','y','z']]

# scaling categorical and numerical features
catg=features.select_dtypes(include=['object'])
num=features.select_dtypes(include=['int64', 'float64'])

rescaled_cat = or_enc.transform(catg)
rescaled_num=scaler.transform(num)
rescaled_feat=pd.concat([pd.DataFrame(rescaled_cat),pd.DataFrame(rescaled_num)],axis=1)


# Feature selection
st.header('Feature Selection')
st.markdown('Drop the unwanted features using Pearson Correlation')
features=df[['carat','cut','color','clarity','depth','table','x','y','z']]

data = features.corr()
st.write(px.imshow(data, text_auto = '.2f', aspect='auto', color_continuous_scale='viridis'))
st.markdown('From the above figure the features x,y,z are highly correlated')

# By using the function we can select highly correlated features

def pears_corr(data,threshold):
    corr_col=set() # set of names of correlated columns
    corr_matrix=data.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i,j]) > threshold:
                colname=corr_matrix.columns[i]
                corr_col.add(colname)
    return corr_col         
corr_features=pears_corr(features,0.5)
best_feat=features.drop(corr_features,axis=1)

st.header('Selecting Unwanted features')
button=st.button('Unwanted Features')
if button:
        st.subheader(f"{corr_features}")

st.header('Selecting best features')
button1=st.button('Best Features')
if button1:
        st.subheader(f"{set(best_feat.columns)}")

st.header('By using this Best Features Diamond Price is Predicted')

page_bg_img = '''
<style>
.stApp {
background-image: url("https://ak.picdn.net/shutterstock/videos/670441/thumb/1.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)