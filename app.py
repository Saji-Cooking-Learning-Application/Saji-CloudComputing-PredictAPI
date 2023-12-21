import os
import io
import numpy as np
import tensorflow as tf
from werkzeug.utils import secure_filename
from flask import Flask, request, jsonify
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras.preprocessing import image
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in set(['png', 'jpg', 'jpeg'])

model_makanan = load_model('modelmakanan.h5')
model_bahan = load_model('modelbahan.h5')

# Fungsi untuk menghubungkan ke database MySQL
def mysql_connect():
    return mysql.connector.connect(
        host=os.environ.get('HOST'),
        user=os.environ.get('USER'),
        password=os.environ.get('PASSWORD'),
        database=os.environ.get('DATABASE')
    )

@app.route('/')
def hello_world():
    return jsonify('SAJI PREDICT API IS RUNNING !')


@app.route('/predict/makanan', methods=['POST'])
def predict_makanan():
    labels = {
        0: {'id': 5, 'nama_menu': 'Capcay'},
        1: {'id': 2, 'nama_menu': 'Kentang Goreng'},
        2: {'id': 4, 'nama_menu': 'Nasi Goreng'},
        3: {'id': 3, 'nama_menu': 'Tahu Fantasi'},
        4: {'id': 1, 'nama_menu': 'Terong Balado'},
    }
    
    imgFile = request.files.get('file')

    if imgFile and allowed_file(imgFile.filename):
        image_bytes = imgFile.read()
        img = image.load_img(io.BytesIO(image_bytes), target_size=(128,128))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0 

        prediction = model_makanan.predict(img_array)
        predicted_class = np.argmax(prediction)
        class_name = labels.get(predicted_class, 'Unknown')
        id = int(class_name.get('id'))
        
        # Simpan URL gambar ke database MySQL dan peroleh id_image yang baru saja dimasukkan
        conn = mysql_connect()
        cursor = conn.cursor()
        query = 'SELECT * FROM menu WHERE id = %s'
        cursor.execute(query, (id,))
        data = cursor.fetchall()
        result = data[0]
        
        confidence = float(prediction[0][predicted_class]) * 100
        
        if (confidence < 50) :
            return jsonify({
                "status": {
                    "code": 400,
                    "message": "Gambar yang anda masukkan kurang jelas / tidak terdeteksi"
                },
            })
        
        return jsonify({
            "status": {
                "code": 200,
                "message": "Success predicting"
            },
            "prediction": {
                "class_name": class_name,
                "confidence": f"{confidence:.2f}%"
            },
            "datas": {
                "id": result[0],
                "nama_menu": result[1],
                "deskripsi": result[2],
                "jumlah_kalori": result[3],
                "protein": result[4],
                "lemak": result[5],
                "karbohidrat": result[6],
                "serat": result[7],
                "vitamin_A": result[8],
                "vitamin_C": result[9],
                "dan_lain_lain": result[10]
            }
        })
        
        cursor.close()
        conn.close()

    return jsonify({
        "status": {
            "code": 400,
            "message": "No image uploaded"
        }
    })
    
@app.route('/predict/bahan', methods=['POST'])
def predict_bahan():
    imgFile = request.files.get('file')
    
    labels = {
        0: {'id': 26, 'nama_bahan': 'Bawang Bombay'},
        1: {'id': 3, 'nama_bahan': 'Bawang Merah'},
        2: {'id': 4, 'nama_bahan': 'Bawang Putih'},
        3: {'id': 27, 'nama_bahan': 'Bihun'},
        4: {'id': 28, 'nama_bahan': 'Cabai Keriting'},
        5: {'id': 29, 'nama_bahan': 'Cabai Merah Besar'},
        6: {'id': 30, 'nama_bahan': 'Daging Ayam'},
        7: {'id': 17, 'nama_bahan': 'Daun Bawang'},
        8: {'id': 12, 'nama_bahan': 'Kentang'},
        9: {'id': 31, 'nama_bahan': 'Kol Putih'},
        10: {'id': 2, 'nama_bahan': 'Nasi Putih'},
        11: {'id': 32, 'nama_bahan': 'Tahu'},
        12: {'id': 16, 'nama_bahan': 'Telur Ayam'},
        13: {'id': 1, 'nama_bahan': 'Terong Ungu'},
        14: {'id': 15, 'nama_bahan': 'Wortel'},
    }

    if imgFile and allowed_file(imgFile.filename):
        image_bytes = imgFile.read()
        img = image.load_img(io.BytesIO(image_bytes), target_size=(128,128))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0 

        prediction = model_bahan.predict(img_array)
        predicted_class = np.argmax(prediction)
        class_name = labels.get(predicted_class, 'Unknown') 
        id = int(class_name.get('id'))
        
        # Simpan URL gambar ke database MySQL dan peroleh id_image yang baru saja dimasukkan
        conn = mysql_connect()
        
        cursor1 = conn.cursor()
        query = 'SELECT * FROM bahan WHERE id = %s'
        cursor1.execute(query, (id,))
        data = cursor1.fetchall()
        result = data[0]
        
        cursor2 = conn.cursor()
        id_menu = int(result[0])
        rekomendasi_query = 'SELECT resep.id_menu, menu.nama_menu, MIN(foto_menu.foto) AS foto FROM resep INNER JOIN menu ON resep.id_menu = menu.id INNER JOIN foto_menu ON menu.id = foto_menu.id_menu WHERE id_bahan = %s GROUP BY menu.id'
        cursor2.execute(rekomendasi_query, (id_menu,))
        data_rekomendasi = cursor2.fetchall()
        result_rekomendasi = data_rekomendasi[0]
        
        confidence = float(prediction[0][predicted_class]) * 100
        
        if (confidence < 50) :
            return jsonify({
                "status": {
                    "code": 400,
                    "message": "Gambar yang  dimasukkan kurang jelas / tidak terdeteksi"
                },
            })
        
        return jsonify({
            "status": {
                "code": 200,
                "message": "Success predicting"
            },
            "prediction": {
                "class_name": class_name,
                "confidence": f"{confidence:.2f}%"
            },
            "datas": {
                "id": result[0],
                "nama_bahan": result[1],
                "deskripsi": result[2],
                "manfaat": result[3],
                "rekomendasi_resep": [
                    {
                        "id": i[0],
                        "nama_menu": i[1],
                        "foto": i[2]
                    }
                    for i in data_rekomendasi
                ]
            }
        })
        
        cursor1.close()
        cursor2.close()
        conn.close()

    return jsonify({
        "status": {
            "code": 400,
            "message": "No image uploaded"
        }
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))