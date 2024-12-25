
import streamlit as st 

st.write(
    """
    # My Dashboard : Bike Sharing Datasets Analysis
    Informasi Pengguna

- Nama: Inggit Insani
- Email: insyninggittt@gmail.com
- Github: [Klik Disini](https://github.com/Insynigittt/Bike-Sharing-Datasets/tree/main)""")


st.write(
    '''
    # Analisis Akan Menjawab Pertanyaan Berikut:
- Bagaimana perbedaan pola peminjaman sepeda antara pengguna umum (casual) dibandingkan dengan pengguna terdaftar (registered)?
- Pada jam-jam berapakah dalam sehari terdapat konsentrasi penyewaan sepeda tertinggi untuk pengguna umum dan pengguna terdaftar?
- Bisakah kita mengenali anomali atau kejadian besar (seperti cuaca ekstrem atau hari libur nasional) berdasarkan lonjakan atau penurunan tiba-tiba dalam jumlah penyewaan sepeda (cnt)?   
    '''
)

st.write(
    """
    # Kesimpulan
    ***Pertanyaan 1 :*** **Bagaimana perbedaan pola peminjaman sepeda antara pengguna umum (casual) dibandingkan dengan pengguna terdaftar (registered)?**
    - **Data ini** memperlihatkan pentingnya peran layanan sepeda sebagai alat transportasi harian bagi **pelanggan terdaftar (registered)**, 
      sementara bagi **pelanggan umum (casual)**, sepeda lebih banyak digunakan untuk aktivitas rekreasi.
    - **Peningkatan fasilitas** dan ketersediaan sepeda selama **hari kerja** mungkin lebih penting untuk memenuhi kebutuhan pengguna terdaftar.
    - Pada **akhir pekan**, fokus pada pelanggan umum, seperti promosi atau kampanye wisata bersepeda, dapat menarik lebih banyak pengguna.
    """

 )

st.write(
    """
    ***Pertanyaan 2 :*** **Pada jam-jam berapakah dalam sehari terdapat konsentrasi penyewaan sepeda tertinggi untuk pengguna umum dan pengguna terdaftar?**

    - **Pelanggan terdaftar (registered)** mendominasi penyewaan selama jam sibuk (pagi dan sore), mengindikasikan penggunaan layanan sebagai alat transportasi utama.
    - **Pelanggan umum (casual)** memiliki volume penyewaan yang jauh lebih rendah dibandingkan pengguna terdaftar, tetapi konsisten sepanjang hari.
    - **Perbedaan pola ini** mengindikasikan bahwa pengguna terdaftar lebih terikat pada jadwal harian (misalnya, pekerjaan atau sekolah), sementara pelanggan umum lebih fleksibel dalam memilih waktu penyewaan.
    - Untuk memberi pelayanan maksimal kepada **pelanggan terdaftar (registered)**, ketersediaan sepeda selama **jam sibuk (pagi dan sore)** sangat penting.
    - Untuk **pelanggan umum (casual)**, bisa digunakan promosi dan layanan tambahan di sore hari atau akhir pekan agar dapat meningkatkan penyewaan.
    """
 )

st.write(
    """
    ***Pertanyaan 3 :*** **Bisakah kita mengenali anomali atau kejadian besar (seperti cuaca ekstrem atau hari libur nasional) berdasarkan lonjakan atau penurunan tiba-tiba dalam jumlah penyewaan sepeda (cnt)?**

    - Cuaca cerah cenderung meningkatkan penyewaan meskipun ada anomali, sementara cuaca buruk menurunkan penyewaan.
    - Kecepatan angin berpengaruh sedikit, hanya ketika dikombinasikan dengan kondisi cuaca tertentu.
    """
 )