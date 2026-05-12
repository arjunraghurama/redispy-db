# redispy-db


Start the Redis Server 
```bash
docker compose up --build
```

Connect using netcat and send a message
```bash
nc localhost 6379
Hello
```

Output
```
Attaching to db-1
db-1  | Starting redispy-db...
db-1  | Client connected: ('172.26.0.1', 57708)
db-1  | Data sent from client is : Hello
db-1  | 
```

TCP server will echo back the data sent from the client

Added the redis container also for testing.
Access the redis-cli using following command
```bash
docker compose exec redis redis-cli -h db -p 6379
```