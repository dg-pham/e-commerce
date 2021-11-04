# Django e-commerce
## Cài đặt
####git clone https://github.com/lilbunnyfufuu/e-commerce.git
Vào thư mục vừa tải về

Tải docker, cài đặt và chạy docker

Tải PostgreSQL và tạo schema shopping

Tạo file .env và điền các biến cần thiết
####docker build .
####docker-compose build
####docker-compose up
Tạo một cửa sổ CMD khác và chạy tiếp:
####docker-compose exec web python manage.py makemigrations
####docker-compose exec web python manage.py migrate
Ứng dụng chạy tại 127.0.0.1:8000
