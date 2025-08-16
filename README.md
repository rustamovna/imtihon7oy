# Imtihon7oy Shop API

## Products API
- GET /api/products/products/ — barcha mahsulotlar
- POST /api/products/products/ — yangi mahsulot qo‘shish
- GET /api/products/products/<id>/ — mahsulotni ko‘rish
- PUT/PATCH /api/products/products/<id>/ — mahsulotni yangilash
- DELETE /api/products/products/<id>/ — mahsulotni o‘chirish

## Comments API
- GET /api/products/<product_id>/comments/ — mahsulot kommentlarini ko‘rish
- POST /api/products/<product_id>/comments/ — komment qo‘shish
- PUT/PATCH /api/comments/<id>/ — kommentni yangilash
- DELETE /api/comments/<id>/ — kommentni o‘chirish

## Cart API
- GET /api/cart/ — savatni ko‘rish
- POST /api/cart/add/ — mahsulot qo‘shish
- POST /api/cart/remove/ — mahsulotni o‘chirish
- POST /api/cart/clear/ — savatni tozalash
- PATCH /api/cart/update/ — savatdagi mahsulot sonini yangilash

## Orders API
- POST /api/orders/order/create/ — order yaratish
- GET /api/orders/orders/ — foydalanuvchi orderlarini ko‘rish
- GET /api/orders/orders/<id>/ — orderni ko‘rish
- PATCH /api/orders/orders/<id>/status/ — order statusini yangilash (admin)
- DELETE /api/orders/orders/<id>/cancel/ — orderni bekor qilish


<!-- Swagger UI: -->
-  [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) 

<!-- Redoc UI: -->
-  [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

<!-- Postman -->
- [https://documenter.getpostman.com/view/40449474/2sB3BHkTvN](https://documenter.getpostman.com/view/40449474/2sB3BHkTvN)
---