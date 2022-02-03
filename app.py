import pickle
import numpy as np
import streamlit as st

data = pickle.load(open('data.pkl','rb'))
model = pickle.load(open('random_forest.pkl','rb'))

st.title('LAPTOP PRICE PREDICTOR')

#company
company = st.selectbox('Laptop Brand', data['Company'].unique())

#laptop type
type = st.selectbox('Laptop Type', data['TypeName'].unique())

#ram
ram = st.selectbox('Ram', [2,4,6,8,12,16,24,32,64])

#weight
weight = st.number_input('Weight')

#GPU
gpu = st.selectbox('GPU', data['GPU'].unique())

#os
Os = st.selectbox('OS', data['OS'].unique())

#ips panel
ips_panel = st.selectbox('IPS_Panel', ['Yes','No'])

#touch screen
screen_touch = st.selectbox('Screen Touch', ['Yes','No'])

#screen size
size = st.selectbox('Screen Resolution', ['1920x1080','1366x768','1600x900','3200x1800','3840x2160','2560x1440','2256x1504','2304x1440'])

#size
screen_size = st.number_input('Screen size')

#cpu
cpu = st.selectbox('CPU', data['cpu'].unique())

#ssd
ssd = st.selectbox('SSD', [0,8, 16, 32, 64, 128, 256,512, 1024, 1000, 180, 240])

#hdd 
hdd = st.selectbox('HDD', [0, 8, 16, 32, 64, 128, 256, 512, 1024, 1000, 2000, 500])

if st.button('Check'):
    if ips_panel == 'Yes':
        ips_panel = 1
    else:
        ips_panel = 0
    if screen_touch == 'Yes':
        screen_touch = 1
    else:
        screen_touch = 0

    X_res = int(size.split('x')[0])
    y_res = int(size.split('x')[1])
    ppi = ((X_res**2 + y_res**2)**0.5)/screen_size
    query = np.array([company,type, ram,weight, gpu, Os,ips_panel, screen_touch,ppi,cpu,ssd,hdd])
    query = query.reshape(1,12)
    st.title('PREDICTED PRICE : {} INR'.format(int(np.exp(model.predict(query)))))