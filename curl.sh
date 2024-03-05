#/bin/bash

function rand_string {
    cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1
}


curl -X GET http://localhost:8000/api/todos/get-all-todos/

for i in {1..10}
do
    echo "Request $i"
    curl -X POST -H "Content-Type: application/json" -d '{"title": "Awesome"}' http://localhost:8000/api/todos/create-todo/
    echo "\n"
    sleep 1
done

curl -X PUT -H "Content-Type: application/json" -d '{"title": "Awesome", "description": "nice"}' http://localhost:8000/api/todos/4/update-todo/

curl -X DELETE http://localhost:8000/api/todos/4/delete-todo/