# redispy-db


Start the Redis Server 
```bash
python3 main.py
```

Connect using netcat and send a message
```bash
nc localhost 6379
Hello
```

Output
```
Starting redispy-db...
Client connected: ('127.0.0.1', 57842)
Data sent from client is : Hello
```

TCP server will echo back the data sent from the client