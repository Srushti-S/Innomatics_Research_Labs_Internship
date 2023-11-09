import streamlit as st
import prediction
import time
if __name__ == '__main__':

 
    st.title("Laptop Price Prediction Model")
    processor_opt = tuple(())
    os_opt = tuple(())
    ram_opt = tuple(())
    brand = st.selectbox('Select brand:',
        ('Lenovo', 'ASUS', 'HP', 'DELL', 'RedmiBook', 'realme', 'acer',
       'MSI', 'APPLE', 'Infinix', 'SAMSUNG', 'Ultimus', 'Vaio',
       'GIGABYTE', 'Nokia', 'ALIENWARE'))
    if brand == 'APPLE':
        processor_opt = ('Apple M1', 'Apple M2', 'Apple M1 Pro', 'Apple M1 Max')
        os_opt = ('Mac',)
        ram_opt = ('LPDDR3', 'DDR4', 'LPDDR4', 'LPDDR4X', 'DDR5', 'LPDDR5', 'Unified')
    else:
        processor_opt = ('Intel Core i3', 'AMD Ryzen 5', 'Intel Core i5', 'AMD Ryzen 7',
       'AMD Ryzen 9', 'Intel Celeron', 'AMD Ryzen 3', 'AMD Athlon', 'Intel Core i7',
        'Qualcomm Snapdragon 7c Gen 2', 'Intel Pentium', 'Intel Core i9', 'AMD')
        os_opt = ('Windows', 'DOS', 'Chrome')
        ram_opt = ('LPDDR3', 'DDR4', 'LPDDR4', 'LPDDR4X', 'DDR5', 'LPDDR5')
    processor = st.selectbox('Select any Processor:',
                             processor_opt)
    os = st.selectbox('Select OS:',
                                    os_opt)
    display = st.select_slider('Choose display(inches):',
                               (11.6, 13., 13.3, 13.4, 13.5, 13.6, 14., 14.1, 14.2, 14.96, 15., 15.6, 16., 16.1, 16.2, 16.6, 17.3))
    ram_size = st.selectbox('Choose RAM size',
                            (4, 8, 16, 32))
    ram_type = st.selectbox('Select RAM type(GB):',
                            ram_opt)
    hd_size = st.selectbox('Choose HD size(GB):',
                           (32, 64, 128, 256, 512, 1000, 1128, 1256, 1512, 2000))
    hd_type = st.selectbox('Select HD type',
                           ('HDD', 'EMMC', 'SSD', 'Hybrid'))

    data = [[brand, processor, os, display, ram_size, ram_type, hd_type, hd_size]]
    if st.button('Predict the price'):
        data = prediction.data_transform(data)
        data = prediction.predict(data)
        st.subheader(u'\u20B9' + str(data))

