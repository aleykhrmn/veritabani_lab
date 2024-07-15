import redis
import time

# Redis'e bağlan
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Benchmark değişkenleri
num_operations = 100000
write_times = []
read_times = []

# yazma işlemi
for i in range(num_operations):
    start_time = time.time()
    redis_client.set(f"aleyna_{i}", "kahraman")
    end_time = time.time()
    
    write_times.append(end_time - start_time)

# okuma işlemi
for i in range(num_operations):
    start_time = time.time()
    redis_value = redis_client.get(f"aleyna_{i}")
    end_time = time.time()
    
    if redis_value is not None:
        read_times.append(end_time - start_time)
    else:
        print(f"Okuma işlemi başarısız: aleyna_{i}")

# Ortalama süreleri hesapla
average_write_time = sum(write_times) / num_operations
average_read_time = sum(read_times) / num_operations

print(f"Redis - Ortalama yazma süresi: {average_write_time:.6f} saniye")
print(f"Redis - Ortalama okuma süresi: {average_read_time:.6f} saniye")
