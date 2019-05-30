Lab 4 
=================
### Requirements ###
[Java9 or later](https://www.oracle.com/technetwork/java/javase/downloads/index.html)<br />
[Apache Kafka](https://kafka.apache.org)<br />
[Redis](https://redis.io/download)<br />
[Python3.6 or later](https://www.python.org/downloads/)<br />



### Step 1: Download the code ###
```bash
    > git clone https://github.com/Agipas/Documentation-of-software-and-design-patterns/tree/lab4
```

### Step 2: First bootstrap envirement ###
```bash
    > tar -xzf kafka_2.12-2.2.0.tgz
    > cd kafka_2.12-2.2.0
```

Kafka uses ZooKeeper so you need to first start a ZooKeeper server if you don't already have one.
You can use the convenience script packaged with kafka to get a quick-and-dirty single-node ZooKeeper instance.
```bash
    > bin/zookeeper-server-start.sh config/zookeeper.properties
    [2019-05-26 15:01:37,495] INFO Reading configuration from: config/zookeeper.properties (org.apache.zookeeper.server.quorum.QuorumPeerConfig)
    ...
 ```
 
 Now start the Kafka server:
 ```bash
    > bin/kafka-server-start.sh config/server.properties
    [2019-05-26 15:01:47,028] INFO Verifying properties (kafka.utils.VerifiableProperties)
    [2019-05-26 15:01:47,051] INFO Property socket.send.buffer.bytes is overridden to 1048576 (kafka.utils.VerifiableProperties)
    ...
```

### Step 3: Create a topic ###
```bash
    > bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic lab4
```

### Step 5: Start a consumer ###
```bash
    > bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic lab4 --from-beginning
    This is a message
    This is another message
```

### Step 6: Get data to terminal/kafka ###
```bash
    > cd lab4
    > python main.py
```
---
#### If you want get data to logs in your [IDE](https://www.jetbrains.com/pycharm/?var=landing&gclid=Cj0KCQjw_r3nBRDxARIsAJljleGYSElcURFr917nYDwhMSGtS5wmZpvIW-n4jm0maW1XjpsF815cTtMaAvB5EALw_wcB)<br> ####
 - In 'server.conf' change EXPORT_SOURCE<br>
    ~~EXPORT_SOURCE=kafka~~ on EXPORT_SOURCE=logs<br>
 - Delete redis key  <br>
```bash
    > redis-5.0.5/src 
    > redis-cli
    127.0.0.1:6379 > del https://data.cityofnewyork.us/resource/uvxr-2jwn.json
```
 - Repeat [Step 6](https://github.com/Agipas/Documentation-of-software-and-design-patterns/new/lab4?readme=1#step-6-get-data-to-terminalkafka)

