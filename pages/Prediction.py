import pandas as pd
import streamlit as st
import pickle

from joblib import load

import time

st.markdown(
    """
    <div style="text-align: center;">
        <h2>🏠 Prediksi Harga Properti</h2>
    </div>
    """,
    unsafe_allow_html=True
)

# Read Data utama
properti = pd.read_csv('data_input/properti_jual.csv')

# Read model yang telah dibuat
# Buka file menggunakan 'rb' (read binary)
model = pd.read_pickle('harga_properti_model_3.12.pkl')
# model = load('harga_properti_model.joblib')

# Fungsi untuk melakukan prediksi
def prediksi_harga_properti(data_input):
    data = pd.DataFrame(data_input, index=[0])
    data = pd.get_dummies(data, columns=['Sertifikat', 'Tipe.Properti', 'Kota'])

    # Menambahkan kolom yang hilang dengan nilai nol
    missing_cols = [col for col in model.feature_names_in_.tolist() if col not in data.columns]

    for col in missing_cols:
        data[col] = 0

    # Pastikan urutan kolom sesuai dengan urutan saat pelatihan
    data = data[model.feature_names_in_.tolist()]

    prediksi = model.predict(data)
    return prediksi[0]


## Streamlit Layout
with st.container(border=True):
    st.markdown('### Masukkan spesifikasi rumah:')

    # input data
    ## Luas bangunan
    l_bangunan = st.select_slider(
        'Luas Bangunan',
        options=list(range(10,1001,10)),
        value=120,
        help= "Geser Nilai"
    )

    ## Kamar tidur
    k_tidur = st.number_input(
        'Jumlah kamar tidur',
        min_value = 1,
        max_value = 10,
        value = 2,
        help="Pilih Jumlah Kamar Tidur"

    )

    ## Kamar mandi
    k_mandi = st.number_input(
        'Jumlah kamar mandi',
        min_value = 1,
        max_value = 10,
        value = 1,
        help="Pilih Jumlah Kamar Mandi"
    )

    ## Sertifikat
    sertifikat = st.selectbox(
        'Jenis Sertifikat',
        options = properti['Sertifikat'].unique(),
        help = "Pilih Jenis Sertifikat"
    )

    ## Tipe Properti
    tipe_properti = st.selectbox(
        'Tipe Properti',
        options = properti['Tipe.Properti'].unique(),
        help = "Pilih Tipe Properti"
    )

    ## Kota
    kota = st.selectbox(
        'Kota',
        options = properti['Kota'].unique(),
        help = "Pilih Lokasi Kota"
    )

    # Tombol untuk memicu prediksi

    st.markdown("---")

    with st.sidebar:
        if st.button('Hitung Harga Prediksi', help="Klik untuk melihat hasil prediksi"):
            input_data = {
                'K.Mandi': k_mandi,
                'K.Tidur': k_tidur,
                'L.Bangunan': l_bangunan,
                'Sertifikat': sertifikat,
                'Tipe.Properti': tipe_properti,
                'Kota': kota
            }

            with st.spinner('Menghitung...'):
                harga = prediksi_harga_properti(input_data)
                time.sleep(2)
                
                # Menampilkan hasil dengan teks yang dipusatkan
                st.markdown(
                    f"""
                    <div style="text-align: center;">
                        <div style="background-color: #dff0d8; color: #3c763d; padding: 10px; border-radius: 4px;">
                            Hasil Prediksi: <strong>Rp {harga:,.0f}</strong>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.write("\n")

        


