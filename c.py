sudo ovs-vsctl set port s1-eth3 qos=@newqos -- \
--id=@newqos create QoS type=linux-htb \
other-config:max-rate=10000000 \
queues:123=@1q \
queues:234=@2q -- \
--id=@1q create queue other-config:min-rate=100 other-config:max-rate=5000000 -- \
--id=@2q create queue other-config:min-rate=100 other-config:max-rate=5000000

........................................................................................
sudo ovs-vsctl set port s1-eth1 qos=@newqos -- \
--id=@newqos create QoS type=linux-htb \
other-config:max-rate=10000000 \
queues:1=@1q \
queues:2=@2q -- \
--id=@1q create queue other-config:min-rate=100 other-config:max-rate=2500000 -- \
--id=@2q create queue other-config:min-rate=100 other-config:max-rate=2500000


sudo ovs-ofctl add-flow s1 ip,priority=65500,nw_src=10.0.1.2,nw_dst=10.0.4.2,idle_timeout=0,actions=set_queue:1,normal
sudo ovs-ofctl add-flow s1 ip,priority=65500,nw_src=10.0.2.2,nw_dst=10.0.5.2,idle_timeout=0,actions=set_queue:2,normal


sudo ovs-vsctl set port s1-eth1 qos=@newqos -- \
--id=@newqos create QoS type=linux-htb \
other-config:max-rate=10000000 \
queues:1=@1q \
