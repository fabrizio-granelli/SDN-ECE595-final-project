from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink

class Harsh(Topo):
    """docstring forHarsh."""

    def __init__(self):
        Topo.__init__(self)


        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        h1 = self.addHost( 'h1', ip='10.0.1.2/24', defaultRoute='via 10.0.1.1' )
        h2 = self.addHost( 'h2', ip='10.0.2.2/24', defaultRoute='via 10.0.2.1' )
        h3 = self.addHost( 'h3', ip='10.0.3.2/24', defaultRoute='via 10.0.3.1' )
        h4 = self.addHost( 'h4', ip='10.0.4.2/24', defaultRoute='via 10.0.4.1' )
        h5 = self.addHost( 'h5', ip='10.0.5.2/24', defaultRoute='via 10.0.5.1' )
        h6 = self.addHost( 'h6', ip='10.0.6.2/24', defaultRoute='via 10.0.6.1' )

        self.addLink(s1, s2)
        self.addLink(s1, h1)
        self.addLink(s1, h2)
        self.addLink(s1, h3)
        self.addLink(s2, h4)
        self.addLink(s2, h5)
        self.addLink(s2, h6)
topos = {"Harxh": (lambda: Harsh())}

if __name__ == "__main__":
    topo = Harsh()
    net = Mininet(
        topo=topo,
        switch=OVSKernelSwitch,
        build=False,
        autoSetMacs=True,
        autoStaticArp=True,
        link=TCLink,
    )
    controller = RemoteController("c1", ip="127.0.0.1", port=6633)
    net.addController(controller)
    net.build()
    net.start()
    CLI(net)
    net.stop()
