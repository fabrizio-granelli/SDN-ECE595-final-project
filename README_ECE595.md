# Network Slicing ECE_595_final_project.n1 
## Harsh Kumar & Sriram Thotakura

### Project Goal

To implement in Comnetsemu VM a network slicing strategy to adapt to emergency situation

DETAILS: typically 2 slices are available, equally sharing the total capacity(e.g. 10Mbps divided in 5Mbps+5Mbps) but using only 50% of the respective capacity; a new slice is then built for emergency communications–requiring 4 Mbps, and then the other slices are reduced to 3+3Mbps. Once emergency is gone, capacity is back to the original

Here, we have used the network slicing topology having 6 hosts (h1, h2, h3, h4, h5 and h6) and 2 switches (s1, s2), operating as routers

```text
h1 ----                               ---- h3
      |  |                        |  |
      |  |                        |  |
h2 --- s1 ---------10Mbps----------s2 ---- h5
      |  |                        |  |
      |  |                        |  |
h3 ----                               ---- h6
``` 
This folder consists of the following files:

1. a.py: Script to build a network with six hosts and 2 switches, operating as routers, bandwidth is 10Mbps.

2. switch.py: Application to isolate the network topology into 2 slices. Inititally, the maximum bandwidth is 5Mbps for each slice, but they are working at 50% of the respectivecapacities. 
(h1 -> s1 -> s2 -> h3, 2.5Mbps) (h2 -> s1 -> s2 -> h5, 2.5Mbps). 

 In the emergency situation, the network topology into 3 slices 
 (h1 -> s1 -> s2 -> h3, 3Mbps) (h2 -> s1 -> s2 -> s4 -> h4, 3Mbps) and (h2 -> s1 -> s2 -> s4 -> h4, 4Mbps). 

#### How to run the project

1. To start mininet,

```bash
 sudo python3 a.py 
```
2. To load the application for running the switches as routers,
```bash
 ryu-manager rest_router.py 
```
3. This runs the default situation and the emergency situation for the service slicing, 
```bash
 python switch.py
```
### Result Verification 
```bash
To verify connectivity
```
```bash
mininet> pingall
*** Ping: testing ping reachability
h1 -> h2 h3 h4 h5 h6 
h2 -> h1 h3 h4 h5 h6 
h3 -> h1 h2 h4 h5 h6 
h4 -> h1 h2 h3 h5 h6 
h5 -> h1 h2 h3 h4 h6 
h6 -> h1 h2 h3 h4 h5 
*** Results: 0% dropped (30/30 received)
```
```bash
mininet> iperf h3 h6
*** Iperf: testing TCP bandwidth between h3 and h6 
*** Results: ['3.81 Mbits/sec', '4.85 Mbits/sec']
```
