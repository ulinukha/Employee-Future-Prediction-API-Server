install requirements
jalankan CLI atau bisa dengan postman

curl --location --request POST 'http://127.0.0.1:5000/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "data": [0, 2015, 2, 28, 1, 0, 3]
}'
