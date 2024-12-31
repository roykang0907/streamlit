import streamlit as st
import random
from PIL import Image
from time import sleep
st.write("""
    # Welcome to my Python website!
    ## Made by ROY
    """)
#statistics=[20]
#chart_holder=st.empty()
#image_holder=st.empty()
#statistics=[]
#for i in range(87):
#    a=random.randint(20,80)
#   statistics.append(a)
#    option=st.selectbox("Plese select one!",
#    ('bar_chart', 'line_chart', 'area_chart'))
    #st.write("## random line chart")
#    st.write("## random" , option)
#    if option=='bar_chart':
#        chart_holder.bar_chart(statistics)
#    elif option=='line_chart':
#        chart_holder.line_chart(statistics)
#    elif option=='area_chart':
#        chart_holder.area_chart(statistics)
#chart_holder.line_chart(statistics)
#images=['monkey.jpg', 'laughing_son_with_lupi.jpg', 'programmer.jpeg']
#k=random.randint(0,2)
#ima=images[k]
#image=Image.open("%s" % ima)
#image_holder.image(image)
#st.write("## Uploading random images")
#if st.button("Click!"):
#    st.success("Another random line chart is summoned!")
#image_option=st.selectbox("Please select one jpg or jpeg file!",
#('monkey.jpg', 'laughing_son_with_lupi.jpeg', 'programmer.jpeg'))
#if image_option=='monkey.jpg':
#    image=Image.open("monkey.jpg")
#    st.image(image)
#elif image_option=='laughing_son_with_lupi.jpeg':
#    image=Image.open("laughing_son_with_lupi.jpg")
#    st.image(image)
#elif image_option=='programmer.jpeg':
#    image=Image.open('programmer.jpeg')
#    st.image(image)

#    image_placeholder = st.empty()
#    images=['monkey.jpg', 'laughing_son_with_lupi.jpg', 'programmer.jpeg']
#    while True:
#        k=random.randint(0,2)
#        ima=images[k]
#        image=Image.open("%s" % ima)
#        image_placeholder.image(image)
#        sleep(2.0)

#st.write('# -----------------------------------')
#st.write('# *Advertisement*')
st.write('# Information of Spavy')
st.write('''
## Spavy is a browser that easily navigates spatial data in one place.
## From 3D and 2D files to Reality Capture files, rvt, skp, nwd, fbx, las, and more, you can easily see and explore different formats on a single platform.
''')
st.link_button('Go to Spavy homepage', 'https://www.spavy.com/')