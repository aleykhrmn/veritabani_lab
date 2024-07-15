from flask import Flask, request, jsonify, render_template_string
import redis
from pymongo import MongoClient

app = Flask(__name__)

# Redis bağlantısı
try:
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    redis_info = redis_client.ping()
    if redis_info:
        print("Redis bağlantısı başarılı.")
    else:
        print("Redis sunucusuna bağlanılamadı.")
except Exception as e:
    print(f"Redis bağlantı hatası: {e}")
    exit()

# MongoDB bağlantısı
try:
    mongo_client = MongoClient('mongodb+srv://hakkituran:UCZYZMI0yegWM6qG@cluster0.juo4by4.mongodb.net/')
    db = mongo_client['omu_vtys_lab']
    collection = db['users']  # Örnek bir collection seçimi
    server_info = mongo_client.server_info()  # Bağlantı testi
    print("MongoDB bağlantısı başarılı.")
except Exception as e:
    print(f"MongoDB bağlantı hatası: {e}")
    exit()

# Redis CRUD İşlemleri
def redis_create(key, value):
    redis_client.set(key, value)
    return f"Redis: {key} -> {value} kaydedildi."

def redis_read(key):
    value = redis_client.get(key)
    if value:
        return f"Redis: {key} -> {value.decode('utf-8')}"
    else:
        return f"Redis: {key} bulunamadı."

def redis_update(key, value):
    if redis_client.exists(key):
        redis_client.set(key, value)
        return f"Redis: {key} -> {value} güncellendi."
    else:
        return f"Redis: {key} bulunamadı."

def redis_delete(key):
    if redis_client.delete(key):
        return f"Redis: {key} silindi."
    else:
        return f"Redis: {key} bulunamadı."

# MongoDB CRUD İşlemleri
def mongodb_create(data):
    result = collection.insert_one(data)
    return f'MongoDB: {data} kaydedildi. ID: {result.inserted_id}'

def mongodb_read(query):
    result = collection.find_one(query)
    if result:
        return f'MongoDB: {query} -> {result}'
    else:
        return f'MongoDB: {query} bulunamadı.'

def mongodb_update(query, new_values):
    result = collection.update_one(query, {'$set': new_values})
    if result.modified_count > 0:
        return f'MongoDB: {query} -> {new_values} güncellendi.'
    else:
        return f'MongoDB: {query} bulunamadı.'

def mongodb_delete(query):
    result = collection.delete_one(query)
    if result.deleted_count > 0:
        return f'MongoDB: {query} silindi.'
    else:
        return f'MongoDB: {query} bulunamadı.'

# Flask Routes
@app.route('/')
def index():
    return render_template_string('''
    <html>
    <head>
        <title>Veri Tabanı İşlemleri</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f0f8ff;
                font-family: Arial, sans-serif;
                color: #333;
            }
            .container {
                text-align: center;
                background: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #007BFF;
            }
            form {
                margin: 20px 0;
            }
            label, select, input {
                display: block;
                width: 100%;
                margin: 10px 0;
                padding: 10px;
                font-size: 16px;
            }
            input[type="submit"] {
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s;
            }
            input[type="submit"]:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Veri Tabanı İşlemleri</h1>
            <h2>Redis CRUD İşlemleri</h2>
            <form id="redis-form" action="/redis" method="post">
                <label for="redis-action">İşlem Seçiniz:</label>
                <select id="redis-action" name="action">
                    <option value="" selected disabled hidden></option>
                    <option value="create">Ekle</option>
                    <option value="read">Oku</option>
                    <option value="update">Güncelle</option>
                    <option value="delete">Sil</option>
                </select>
                <label for="redis-key">Anahtar:</label>
                <input type="text" id="redis-key" name="key">
                <label for="redis-value">Değer:</label>
                <input type="text" id="redis-value" name="value">
                <input type="submit" value="Gönder">
            </form>
            <h2>MongoDB CRUD İşlemleri</h2>
            <form id="mongodb-form" action="/mongodb" method="post">
                <label for="mongodb-action">İşlem Seçiniz:</label>
                <select id="mongodb-action" name="action">
                    <option value="" selected disabled hidden></option>
                    <option value="create">Ekle</option>
                    <option value="read">Oku</option>
                    <option value="update">Güncelle</option>
                    <option value="delete">Sil</option>
                </select>
                <label for="mongodb-name">İsim:</label>
                <input type="text" id="mongodb-name" name="name">
                <label for="mongodb-value">Değer:</label>
                <input type="text" id="mongodb-value" name="value">
                <input type="submit" value="Gönder">
            </form>
        </div>
    </body>
    </html>
    ''')

@app.route('/redis', methods=['POST'])
def redis_operations():
    action = request.form['action'].strip().lower()
    key = request.form['key'].strip()
    value = request.form.get('value', '').strip()
    
    if action == 'create':
        result = redis_create(key, value)
    elif action == 'read':
        result = redis_read(key)
    elif action == 'update':
        result = redis_update(key, value)
    elif action == 'delete':
        result = redis_delete(key)
    else:
        result = "Geçersiz işlem. Lütfen tekrar deneyin."
    
    return jsonify(result=result)

@app.route('/mongodb', methods=['POST'])
def mongodb_operations():
    action = request.form['action'].strip().lower()
    name = request.form['name'].strip()
    value = request.form.get('value', '').strip()
    
    if action == 'create':
        result = mongodb_create({"name": name, "value": value})
    elif action == 'read':
        result = mongodb_read({"name": name})
    elif action == 'update':
        result = mongodb_update({"name": name}, {"value": value})
    elif action == 'delete':
        result = mongodb_delete({"name": name})
    else:
        result = "Geçersiz işlem. Lütfen tekrar deneyin."
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
