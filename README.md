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

or 

```
docker compose exec -it redis sh
/data # redis-cli -h db -p 6379 PING
/data # redis-cli -h db -p 6379 SET K [1,2,3]
```


Benchmark using redis-benchmark
Actual redis
1. Single client, 10 requests
```bash
redis-benchmark -n 10 -q -t ping_mbulk -h localhost -p 6378
```

Our implementation
Single client, 10 requests
```bash
redis-benchmark -n 10 -c 1 -t ping_mbulk -h db -p 6379
```