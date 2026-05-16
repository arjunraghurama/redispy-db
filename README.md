# 

<h1 align="center">
   redispy-db
   <br/>
   <h4 align="center">
    A re-mplementation of redis in python 
   </h4>
</h1>




<br/>

## Tests
[![Unit Test](https://github.com/arjunraghurama/redispy-db/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/arjunraghurama/redispy-db/actions/workflows/ci.yaml)

## Getting started
Start the Redis Server 
```bash
docker compose up --build
```

There are two docker containers running.
1. redispy-db : Our implementation of redis at port `6379`
2. redis : Actual redis for comparison at port `6378`

<br/>

To test our server we use the redis-cli and redis-benchmark tools.<br>
Access the redis-cli using following command
```bash
docker compose exec redis redis-cli -h redispy-db -p 6379
```

or 

```
docker compose exec -it redis sh
/data # redis-cli -h redispy-db -p 6379 PING
/data # redis-cli -h localhost -p 6378 PING
/data # redis-cli -h localhost -p 6378 SET K [1,2,3]
```

## Benchmark
we are using redis-benchmark tool

Actual redis, single client, 10 requests
```bash
redis-benchmark -n 10 -q -c 1 -t ping_mbulk -h localhost -p 6378
```

Our implementation, single client, 10 requests
```bash
redis-benchmark -n 10 -q -c 1 -t ping_mbulk -h redispy-db -p 6379
```

Here is the benchmark after the initial implementation of `PING` command

![](/assets/1.benchmark_synchronus_server.png)

We were able to achieve a decent speed of `3333.3` rps where as Redis achieved `10000` rps

## Credits
This implementation is based on the `Redis Internals` series by [`Arpit Bhayani`](https://github.com/arpitbbhayani).<br/> Original implementation is in golang and can be found [here](https://github.com/dicedb/dicedb)
YouTube playlist where he explains the concepts can be found [here](https://www.youtube.com/watch?v=h30k7YixrMo&list=PLsdq-3Z1EPT0eElcdOON9fdaeaQjlyXDt)