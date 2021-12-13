# Prediksi Harapan Hidup Pasien Covid-19

Virus Corona atau COVID-19 ini merupakan jenis baru dari coronavirus yang menular ke manusia. 
Virus ini bisa menyerang siapa saja, bayi, anak-anak, orang dewasa, lansia, ibu hamil, maupun ibu 
menyusui.
Infeksi COVID-19 pertama kali ditemukan di kota Wuhan, Cina, akhir Desember 2019. Virus ini menular dengan cepat dan menyebar ke wilayah lain di Cina dan sebagian besar negara di dunia ini, termasuk Indonesia. Hal ini membuat beberapa negara menerapkan kebijakan lockdown untuk mencegah penyebarannya.
Infeksi virus Corona atau COVID-19 disebabkan oleh coronavirus, yaitu kelompok virus yang menginfeksi sistem pernapasan. Pada banyak kasus, virus ini hanya menyebabkan infeksi pernapasan ringan, seperti flu. Namun, virus ini juga bisa menyebabkan infeksi pernapasan berat, seperti infeksi paru-paru (pneumonia), Middle-East Respiratory Syndrome (MERS), Severe Acute Respiratory Syndrome (SARS), bahkan bisa menimbulkan kematian.

Dengan jumlah kasus yang dapat melonjak dengan signifikan sewaktu-waktu dan ketersediaan sumber daya medis yang terbatas kami rasa perlu langkah yang efektif dan efisien dalam mengobati pasien yang terinfeksi COVID-19, salah satunya dengan mengklasifikasikan status pasien. 
Tenaga medis memerlukan bantuan untuk mengklasifikasi status pasien berdasarkan data pasien secara otomatis untuk mengurangi kelelahan tenaga medis yang harus terus bertugas dan meminimalisir resiko penanganan yang terlambat terhadap pasien.
Oleh karena itu dibutuhkan solusi teknologi berbasis data secara otomatis yang dapat membantu mengklasifikasikan status kegawatan berdasarkan data pasien.
Dalam project ini kami akan membuat model prediktif yang dapat memprediksi status kematian akibat virus covid-19 secara akurat, mengidentifikasi predictor terpenting kematian akibat covid19 secara akurat, dan mengidentifikasikan predictor terpenting dari kematian covid-19.

Dataset digunakan adalah data pasien covid di negara Mexico yang kami peroleh dari Kaggle.com , dengan jumlah pasien kurang lebih sebanyak 50.000.
Data yang digunakan mengandung 23 atribut dan 566.602 baris. Tetapi pada project kali ini, kami akan menggunakan kurang dari 23 atribut yang berpengaruh terhadap prediksi status kematian akibat virus covid-19.

## Deskripsi Atribut
1. Id (numeric)
2. sex : jenis kelamin (kategorik)
3. patient_type : apakah dirawat di rs atau tidak (kategorik)
4. entry_date : tanggal masuk rs (numeric)
5. date_symptoms : tanggal mulai gejala (numeric)
6. date_died : apakah mati atau tidak (kategorik)
7. intubed : apakah pasien membutuhkan intubasi atau tidak (kategorik)
8. pneunomia : penderita pneunomia (kategorik)
9. age : usia dalam tahun (numeric)
10. pregnancy : kehamilan (kategorik)
11. copd : apakah pasien memiliki riwayat Chronic obstructive pulmonary disease
(COPD) (kategorik)
12. asthma : apakah pasien memiliki riwayat asthma (kategorik)
13. inmsupr : apakah pasien terindikasi immunosuppressed (kategorik)
14. hypertension : apakah pasien terindikasi hypertension (kategorik)
15. other_disease : apakah pasien memiliki riwayat penyakit lainnya (kategorik)
16. cardiovascular : apakah pasien terindikasi cardiovascular (kategorik)
17. obesity : apakah pasien mengalami obesitas (kategorik)
18. renal_chronic : apakah pasien memiliki riwayat penyakit chronic renal (kategorik)
19. tobacco : apakah pasien perokok (kategorik)
20. contact_other_covid : apakah pasien kontak dengan pasien positif COVID (kategorik)
21. covid_res : apakah pasien covid atau tidak (kategorik)
22. icu : apakah pasien perlu diberikan perawatan di ICU atau tidak (kategorik) 

## Keterangan
1 = YA  ;   2 = TIDAK   ;     97,98,99 = MISSING VALUE
Predict Variable : status(Y) = apakah pasien teridentifikasi meninggal atau tidak ? dengan kategori 1 = iya dan 0 = tidak
Diperoleh dari kolom "date_died" dengan membuat kolom baru untuk status pasien apakah meninggal (buruk) atau tidak (baik).Jika pada kolom date_died teridentifikasi tanggal meninggalnya maka pasien teridentifikasi sebagai meninggal dan sebaliknya pada variabel y.
