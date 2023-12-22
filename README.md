# SAJI Machine Learning Model Detection API
# API DOCUMENTATION

### Endpoint

https://saji-cc-predict-api-2srtjzs7ba-et.a.run.app
<br><br>

### Predict Bahan

- URL
    
    - `/predict/bahan`
    
- METHOD
    
   - `POST`
    
- REQUEST BODY
  - `file` as `file`, must be image jpg, jpeg, png
     
- RESPONSE
    
```json
{
    "datas": {
        "deskripsi": "Terong (Solanum melongena), atau yang dikenal sebagai terong, adalah tanaman buah-buahan yang termasuk dalam keluarga Solanaceae. Terong biasanya memiliki bentuk bulat atau lonjong, dengan warna yang bervariasi dari ungu, merah, kuning, hijau, hingga putih.",
        "id": 1,
        "manfaat": "1. Kaya Nutrisi: Terong mengandung nutrisi penting seperti serat, vitamin C, vitamin K, vitamin B6, folat, dan potassium. Nutrisi ini berperan dalam mendukung kesehatan jantung, sistem pencernaan, dan tulang.\r\n\r\n2. Antioksidan: Terong mengandung senyawa antioksidan, seperti nasunin dan klorogenik asam, yang membantu melawan radikal bebas dalam tubuh. Antioksidan dapat melindungi sel-sel tubuh dari kerusakan dan peradangan.\r\n\r\n3. Menurunkan Risiko Penyakit Jantung: Konsumsi terong dapat membantu menurunkan tekanan darah dan kolesterol, yang dapat mengurangi risiko penyakit jantung.\r\n\r\n4. Pertahankan Berat Badan Sehat: Terong memiliki kandungan serat yang tinggi, sehingga dapat membantu menjaga perasaan kenyang lebih lama, mendukung manajemen berat badan, dan menjaga fungsi pencernaan yang sehat.\r\n\r\n5. Mendukung Kesehatan Otak: Beberapa komponen dalam terong, seperti nasunin, dikaitkan dengan manfaat bagi kesehatan otak, termasuk perlindungan terhadap kerusakan sel saraf.\r\n\r\n6. Sumber Antiinflamasi: Terong mengandung senyawa antiinflamasi yang dapat membantu mengurangi peradangan dalam tubuh, memberikan potensi manfaat untuk penderita arthritis atau kondisi inflamasi lainnya.\r\n\r\n7. Meningkatkan Kesehatan Mata: Kandungan vitamin A dalam terong dapat mendukung kesehatan mata dan mencegah masalah mata, seperti degenerasi makula.\r\n\r\n8. Dapat Digunakan dalam Berbagai Masakan: Terong dapat diolah dalam berbagai masakan, mulai dari tumis, curries, hingga hidangan panggang, sehingga memberikan variasi dalam konsumsi makanan sehari-hari.",
        "nama_bahan": "Terong",
        "rekomendasi_resep": [
            {
                "foto": "https://storage.googleapis.com/asset_saji/menu/terong%20balado%20(1).jpg",
                "id": 1,
                "nama_menu": "Terong Balado"
            }
        ]
    },
    "prediction": {
        "class_name": {
            "id": 1,
            "nama_bahan": "Terong Ungu"
        },
        "confidence": "99.98%"
    },
    "status": {
        "code": 200,
        "message": "Success predicting"
    }
}
```

### Predict Makanan

- URL
    
    - `/predict/makanan`
    
- METHOD
    
   - `POST`
    
- REQUEST BODY
  - `file` as `file`, must be image jpg, jpeg, png
     
- RESPONSE
    
```json
{
    "datas": {
        "dan_lain_lain": "Terong balado, selain memiliki rasa yang lezat, juga dapat memberikan beberapa kelebihan berdasarkan bahan-bahan yang digunakan dan karakteristiknya. ",
        "deskripsi": "\nTerong balado adalah hidangan khas Indonesia yang terdiri dari terong yang digoreng dan disajikan dengan sambal balado, yaitu sambal pedas yang terbuat dari cabai, bawang, tomat, dan bumbu-bumbu lainnya yang diuleg atau dihaluskan. Terong balado memiliki kombinasi rasa pedas, gurih, dan sedikit manis yang membuatnya lezat dan populer di meja makan Indonesia. Hidangan ini sering dihidangkan sebagai lauk pendamping nasi putih dan dapat ditemui dalam berbagai variasi tergantung pada selera dan kebiasaan lokal.",
        "id": 1,
        "jumlah_kalori": 100,
        "karbohidrat": 6,
        "lemak": 2,
        "nama_menu": "Terong Balado",
        "protein": 100,
        "serat": 3,
        "vitamin_A": 10,
        "vitamin_C": 3
    },
    "prediction": {
        "class_name": {
            "id": 1,
            "nama_menu": "Terong Balado"
        },
        "confidence": "99.99%"
    },
    "status": {
        "code": 200,
        "message": "Success predicting"
    }
}
```
