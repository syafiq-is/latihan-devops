# Gunakan image Python resmi
FROM python

# Set working directory dalam container
WORKDIR /app

# Salin semua file ke dalam container
COPY . /app

# Install dependensi
RUN pip install flask

# Jalankan aplikasi
CMD ["python3", "app.py"]
