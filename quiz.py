import random
from rich import print
from rich.console import Console
console = Console()
import os


questions = [
        {
            "question": "Which two traffic types use the Real-Time Transport Protocol (RTP)? (Choose two.)\n",
            "options": ["video", "web", "file transfer", "voice", "peer-to-peer"],
            "correct_answers": [0, 3],
            "multi_answer": True
        },
        {
            "question": "Which wireless technology has low-power and data rate requirements making it popular in home automation applications?\n",
            "options": ["ZigBee", "LoRaWAN", "5G", "Wi-Fi"],
            "correct_answers": [0],  
            "multi_answer": False
        },
        {
            "question": "Which layer of the TCP/IP model provides a route to forward messages through an internetwork?\n",
            "options": ["application", "network access", "internet", "transport"],
            "correct_answers": [2],  
            "multi_answer": False
        },
        {
            "question": "Which type of server relies on record types such as A, NS, AAAA, and MX in order to provide services?\n",
            "options": ["DNS", "email", "file", "web"],
            "correct_answers": [0],  
            "multi_answer": False
        },
        {
            "question": "What are proprietary protocols?\n",
            "options": ["protocols developed by private organizations to operate on any vendor hardware", "protocols that can be freely used by any organization or vendor", "protocols developed by organizations who have control over their definition and operation", "a collection of protocols known as the TCP/IP protocol suite\n"],
            "correct_answers": [2],  
            "multi_answer": False
        },
        {
            "question": "What service is provided by DNS?\n",
            "options": ["Resolves domain names, such as cisco.com, into IP addresses.", "A basic set of rules for exchanging text, graphic images, sound, video, and other multimedia files on the web.", "Allows for data transfers between a client and a file server.", "Uses encryption to secure the exchange of text, graphic images, sound, and video on the web.\n"],
            "correct_answers": [0],
            "multi_answer": False
        },
        {
            "question": "A client packet is received by a server. The packet has a destination port number of 110. What service is the client requesting?\n",
            "options": ["DNS", "DHCP", "SMTP", "POP3"],
            "correct_answers": [3],  
            "multi_answer": False
        },
        {
            "question": "What command can be used on a Windows PC to see the IP configuration of that computer?\n",
            "options": ["show ip interface brief", "ping", "show interfaces", "ipconfig"],
            "correct_answers": [3],
            "multi_answer": False
        },
        {
            "question": "A wired laser printer is attached to a home computer. That printer has been shared so that other computers on the home network can also use the printer. What networking model is in use?\n",
            "options": ["peer-to-peer (P2P)", "point-to-point", "master-slave", "client-based"],
            "correct_answers": [0],
            "multi_answer": False
        },
        {
            "question": "What characteristic describes a virus?\n",
            "options": ["a network device that filters access and traffic coming into a network", "the use of stolen credentials to access private data", "an attack that slows or crashes a device or network service", "malicious software or code running on an end device\n"],
            "correct_answers": [3],
            "multi_answer": False
        },
        {
            "question": "Three bank employees are using the corporate network. The first employee uses a web browser to view a company web page in order to read some announcements. The second employee accesses the corporate database to perform some financial transactions. The third employee participates in an important live audio conference with other corporate managers in branch offices. If QoS is implemented on this network, what will be the priorities from highest to lowest of the different data types?\n",
            "options": [
                "financial transactions, web page, audio conference",
                "audio conference, financial transactions, web page",
                "financial transactions, audio conference, web page",
                "audio conference, web page, financial transactions"
            ],
            "correct_answers": [1],
            "multi_answer": False
        },
        {
            "question": "What service is provided by Internet Messenger?\n",
            "options": [
                "An application that allows real-time chatting among remote users.",
                "Allows remote access to network devices and servers.",
                "Resolves domain names, such as cisco.com, into IP addresses.",
                "Uses encryption to provide secure remote access to network devices and servers."
            ],
            "correct_answers": [0],  # Zero-based index for "An application that allows real-time chatting among remote users."
            "multi_answer": False
        },
        {
            "question": "A network administrator notices that some newly installed Ethernet cabling is carrying corrupt and distorted data signals. The new cabling was installed in the ceiling close to fluorescent lights and electrical equipment. Which two factors may interfere with the copper cabling and result in signal distortion and data corruption? (Choose two.)\n",
            "options": [
                "crosstalk",
                "extended length of cabling",
                "RFI",
                "EMI",
                "signal attenuation"
            ],
            "correct_answers": [2, 3],  # Zero-based indices for "RFI" and "EMI"
            "multi_answer": True
        },
        {
            "question": "A host is trying to send a packet to a device on a remote LAN segment, but there are currently no mappings in its ARP cache. How will the device obtain a destination MAC address?\n",
            "options": [
                "It will send the frame and use its own MAC address as the destination.",
                "It will send an ARP request for the MAC address of the destination device.",
                "It will send the frame with a broadcast MAC address.",
                "It will send a request to the DNS server for the destination MAC address.",
                "It will send an ARP request for the MAC address of the default gateway."
            ],
            "correct_answers": [4],  # Zero-based index for "It will send an ARP request for the MAC address of the default gateway."
            "multi_answer": False
        },
        {
        "question": "A client packet is received by a server. The packet has a destination port number of 53. What service is the client requesting?\n",
        "options": [
            "DNS",
            "NetBIOS (NetBT)",
            "POP3",
            "IMAP"
        ],
        "correct_answers": [0],  # Zero-based index for "DNS"
        "multi_answer": False
    },
    {
    "question": "A network administrator is adding a new LAN to a branch office. The new LAN must support 25 connected devices. What is the smallest network mask that the network administrator can use for the new network?",
    "options": [
        "255.255.255.128",
        "255.255.255.192",
        "255.255.255.224",
        "255.255.255.240"
    ],
    "correct_answers": [2],  # Zero-based index for "255.255.255.224"
    "multi_answer": False
},
{
    "question": "What characteristic describes a Trojan horse?",
    "options": [
        "malicious software or code running on an end device",
        "an attack that slows or crashes a device or network service",
        "the use of stolen credentials to access private data",
        "a network device that filters access and traffic coming into a network"
    ],
    "correct_answers": [0],  # Zero-based index for "malicious software or code running on an end device"
    "multi_answer": False
},
{
    "question": "What service is provided by HTTPS?",
    "options": [
        "Uses encryption to provide secure remote access to network devices and servers.",
        "Resolves domain names, such as cisco.com, into IP addresses.",
        "Uses encryption to secure the exchange of text, graphic images, sound, and video on the web.",
        "Allows remote access to network devices and servers."
    ],
    "correct_answers": [2],  # Zero-based index for "Uses encryption to secure the exchange of text, graphic images, sound, and video on the web."
    "multi_answer": False
},
{
    "question": "A technician with a PC is using multiple applications while connected to the Internet. How is the PC able to keep track of the data flow between multiple application sessions and have each application receive the correct packet flows?",
    "options": [
        "The data flow is being tracked based on the destination MAC address of the technician PC.",
        "The data flow is being tracked based on the source port number that is used by each application.",
        "The data flow is being tracked based on the source IP address that is used by the PC of the technician.",
        "The data flow is being tracked based on the destination IP address that is used by the PC of the technician."
    ],
    "correct_answers": [1],  # Zero-based index for "The data flow is being tracked based on the source port number that is used by each application."
    "multi_answer": False
},
{
    "question": "A network administrator is adding a new LAN to a branch office. The new LAN must support 61 connected devices. What is the smallest network mask that the network administrator can use for the new network?",
    "options": [
        "255.255.255.240",
        "255.255.255.224",
        "255.255.255.192",
        "255.255.255.128"
    ],
    "correct_answers": [2],  # Zero-based index for "255.255.255.224"
    "multi_answer": False
},
{
    "question": "What characteristic describes a DoS attack?",
    "options": [
        "the use of stolen credentials to access private data",
        "a network device that filters access and traffic coming into a network",
        "software that is installed on a user device and collects information about the user",
        "an attack that slows or crashes a device or network service"
    ],
    "correct_answers": [3],  # Zero-based index for "an attack that slows or crashes a device or network service"
    "multi_answer": False
},
{
    "question": "What service is provided by SMTP?",
    "options": [
        "Allows clients to send email to a mail server and the servers to send email to other servers.",
        "Allows remote access to network devices and servers.",
        "Uses encryption to provide secure remote access to network devices and servers.",
        "An application that allows real-time chatting among remote users."
    ],
    "correct_answers": [0],  # Zero-based index for "Allows clients to send email to a mail server and the servers to send email to other servers."
    "multi_answer": False
},
{
    "question": "Which scenario describes a function provided by the transport layer?",
    "options": [
        "A student is using a classroom VoIP phone to call home. The unique identifier burned into the phone is a transport layer address used to contact another network device on the same network.",
        "A student is playing a short web-based movie with sound. The movie and sound are encoded within the transport layer header.",
        "A student has two web browser windows open in order to access two web sites. The transport layer ensures the correct web page is delivered to the correct browser window.",
        "A corporate worker is accessing a web server located on a corporate network. The transport layer formats the screen so the web page appears properly no matter what device is being used to view the web site."
    ],
    "correct_answers": [2],  # Zero-based index for "A student has two web browser windows open in order to access two web sites. The transport layer ensures the correct web page is delivered to the correct browser window."
    "multi_answer": False
},
{
    "question": "What does the term “attenuation” mean in data communication?",
    "options": [
        "strengthening of a signal by a networking device",
        "leakage of signals from one cable pair to another",
        "time for a signal to reach its destination",
        "loss of signal strength as distance increases"
    ],
    "correct_answers": [3],  # Zero-based index for "loss of signal strength as distance increases"
    "multi_answer": False
},
{
    "question": "Which two protocols operate at the top layer of the TCP/IP protocol suite? (Choose two.)",
    "options": [
        "TCP",
        "IP",
        "UDP",
        "POP",
        "DNS",
        "Ethernet"
    ],
    "correct_answers": [3, 4],  # Zero-based indices for "POP" and "DNS"
    "multi_answer": True
},
{
    "question": "A company has a file server that shares a folder named Public. The network security policy specifies that the Public folder is assigned Read-Only rights to anyone who can log into the server while the Edit rights are assigned only to the network admin group. Which component is addressed in the AAA network service framework?",
    "options": [
        "automation",
        "accounting",
        "authentication",
        "authorization"
    ],
    "correct_answers": [3],  # Zero-based index for "authentication"
    "multi_answer": False
},
{
    "question": "What three requirements are defined by the protocols used in network communications to allow message transmission across a network? (Choose three.)",
    "options": [
        "message size",
        "message encoding",
        "connector specifications",
        "media selection",
        "delivery options",
        "end-device installation"
    ],
    "correct_answers": [0, 1, 3],  # Zero-based indices for "message size", "message encoding", and "media selection"
    "multi_answer": True
},
{
    "question": "What are two characteristics of IP? (Choose two.)",
    "options": [
        "does not require a dedicated end-to-end connection",
        "operates independently of the network media",
        "retransmits packets if errors occur",
        "re-assembles out of order packets into the correct order at the receiver end",
        "guarantees delivery of packets"
    ],
    "correct_answers": [0, 1],  # Zero-based indices for "does not require a dedicated end-to-end connection" and "operates independently of the network media"
    "multi_answer": True
},
{
    "question": "An employee of a large corporation remotely logs into the company using the appropriate username and password. The employee is attending an important video conference with a customer concerning a large sale. It is important for the video quality to be excellent during the meeting. The employee is unaware that after a successful login, the connection to the company ISP failed. The secondary connection, however, activated within seconds. The disruption was not noticed by the employee or other employees. What three network characteristics are described in this scenario? (Choose three.)",
    "options": [
        "security",
        "quality of service",
        "scalability",
        "powerline networking",
        "integrity",
        "fault tolerance"
    ],
    "correct_answers": [0, 1, 5],  # Zero-based indices for "quality of service", "integrity", and "fault tolerance"
    "multi_answer": True
},
{
    "question": "What are two common causes of signal degradation when using UTP cabling? (Choose two.)",
    "options": [
        "improper termination",
        "low-quality shielding in cable",
        "installing cables in conduit",
        "low-quality cable or connectors",
        "loss of light over long distances"
    ],
    "correct_answers": [0, 3],  # Zero-based indices for "improper termination" and "low-quality cable or connectors"
    "multi_answer": True
},
{
    "question": "Which subnet would include the address 192.168.1.96 as a usable host address?",
    "options": [
        "192.168.1.64/26",
        "192.168.1.32/27",
        "192.168.1.32/28",
        "192.168.1.64/29"
    ],
    "correct_answers": [0],  # Zero-based index for "192.168.1.32/28"
    "multi_answer": False
},
{
    "question": "Which two statements describe how to assess traffic flow patterns and network traffic types using a protocol analyzer? (Choose two.)",
    "options": [
        "Capture traffic on the weekends when most employees are off work.",
        "Capture traffic during peak utilization times to get a good representation of the different traffic types.",
        "Only capture traffic in the areas of the network that receive most of the traffic such as the data center.",
        "Perform the capture on different network segments.",
        "Only capture WAN traffic because traffic to the web is responsible for the largest amount of traffic on a network."
    ],
    "correct_answers": [1, 3],  # Zero-based indices for "Capture traffic during peak utilization times to get a good representation of the different traffic types." and "Perform the capture on different network segments."
    "multi_answer": True
},
{
    "question": "What is the consequence of configuring a router with the ipv6 unicast-routing global configuration command?",
    "options": [
        "All router interfaces will be automatically activated.",
        "The IPv6 enabled router interfaces begin sending ICMPv6 Router Advertisement messages.",
        "Each router interface will generate an IPv6 link-local address.",
        "It statically creates a global unicast address on this router."
    ],
    "correct_answers": [1],  # Zero-based index for "The IPv6 enabled router interfaces begin sending ICMPv6 Router Advertisement messages."
    "multi_answer": False
},
{
    "question": "Which three layers of the OSI model map to the application layer of the TCP/IP model? (Choose three.)",
    "options": [
        "application",
        "network",
        "data link",
        "session",
        "presentation",
        "transport"
    ],
    "correct_answers": [0, 3, 4],  # Zero-based indices for "application", "presentation", and "transport"
    "multi_answer": True
},
{
    "question": "What will happen if the default gateway address is incorrectly configured on a host?",
    "options": [
        "The host cannot communicate with other hosts in the local network.",
        "The host cannot communicate with hosts in other networks.",
        "A ping from the host to 127.0.0.1 would not be successful.",
        "The host will have to use ARP to determine the correct address of the default gateway.",
        "The switch will not forward packets initiated by the host."
    ],
    "correct_answers": [1],  # Zero-based index for "The host cannot communicate with hosts in other networks."
    "multi_answer": False
},
{
    "question": "What are two features of ARP? (Choose two.)",
    "options": [
        "When a host is encapsulating a packet into a frame, it refers to the MAC address table to determine the mapping of IP addresses to MAC addresses.",
        "An ARP request is sent to all devices on the Ethernet LAN and contains the IP address of the destination host and its multicast MAC address.",
        "If a host is ready to send a packet to a local destination device and it has the IP address but not the MAC address of the destination, it generates an ARP broadcast.",
        "If no device responds to the ARP request, then the originating node will broadcast the data packet to all devices on the network segment.",
        "If a device receiving an ARP request has the destination IPv4 address, it responds with an ARP reply."
    ],
    "correct_answers": [2, 4],  # Zero-based indices for "If a host is ready to send a packet to a local destination device and it has the IP address but not the MAC address of the destination, it generates an ARP broadcast." and "If a device receiving an ARP request has the destination IPv4 address, it responds with an ARP reply."
    "multi_answer": True
},
{
    "question": "A network administrator is adding a new LAN to a branch office. The new LAN must support 90 connected devices. What is the smallest network mask that the network administrator can use for the new network?",
    "options": [
        "255.255.255.128",
        "255.255.255.240",
        "255.255.255.248",
        "255.255.255.224"
    ],
    "correct_answers": [0],  # Zero-based index for "255.255.255.248"
    "multi_answer": False
},
{
    "question": "What are two ICMPv6 messages that are not present in ICMP for IPv4? (Choose two.)",
    "options": [
        "Neighbor Solicitation",
        "Destination Unreachable",
        "Host Confirmation",
        "Time Exceeded",
        "Router Advertisement",
        "Route Redirection"
    ],
    "correct_answers": [0, 4],  # Zero-based indices for "Neighbor Solicitation" and "Router Advertisement"
    "multi_answer": True
},
{
    "question": "A client packet is received by a server. The packet has a destination port number of 80. What service is the client requesting?",
    "options": [
        "DHCP",
        "SMTP",
        "DNS",
        "HTTP"
    ],
    "correct_answers": [3],  # Zero-based index for "HTTP"
    "multi_answer": False
},
{
    "question": "What is an advantage for small organizations of adopting IMAP instead of POP?",
    "options": [
        "POP only allows the client to store messages in a centralized way, while IMAP allows distributed storage.",
        "Messages are kept in the mail servers until they are manually deleted from the email client.",
        "When the user connects to a POP server, copies of the messages are kept in the mail server for a short time, but IMAP keeps them for a long time.",
        "IMAP sends and retrieves email, but POP only retrieves email."
    ],
    "correct_answers": [1],  # Zero-based index for "POP only allows the client to store messages in a centralized way, while IMAP allows distributed storage."
    "multi_answer": False
},
{
    "question": "A technician can ping the IP address of the web server of a remote company but cannot successfully ping the URL address of the same web server. Which software utility can the technician use to diagnose the problem?",
    "options": [
        "tracert",
        "ipconfig",
        "netstat",
        "nslookup"
    ],
    "correct_answers": [3],  # Zero-based index for "nslookup"
    "multi_answer": False
},
{
    "question": "Which two functions are performed at the LLC sublayer of the OSI Data Link Layer to facilitate Ethernet communication? (Choose two.)",
    "options": [
        "implements CSMA/CD over legacy shared half-duplex media",
        "enables IPv4 and IPv6 to utilize the same physical medium",
        "integrates Layer 2 flows between 10 Gigabit Ethernet over fiber and 1 Gigabit Ethernet over copper",
        "implements a process to delimit fields within an Ethernet 2 frame",
        "places information in the Ethernet frame that identifies which network layer protocol is being encapsulated by the frame"
    ],
    "correct_answers": [1, 4],  # Zero-based indices for "implements a process to delimit fields within an Ethernet 2 frame" and "places information in the Ethernet frame that identifies which network layer protocol is being encapsulated by the frame"
    "multi_answer": True
},
{
    "question": "Which two functions are performed at the LLC sublayer of the OSI Data Link Layer to facilitate Ethernet communication? (Choose two.)",
    "options": [
        "responsible for internal structure of Ethernet frame",
        "applies source and destination MAC addresses to Ethernet frame",
        "handles communication between upper layer networking software and Ethernet NIC hardware",
        "adds Ethernet control information to network protocol data",
        "implements trailer with frame check sequence for error detection"
    ],
    "correct_answers": [2, 3],  # Zero-based indices for "responsible for internal structure of Ethernet frame" and "handles communication between upper layer networking software and Ethernet NIC hardware"
    "multi_answer": True
},
{
    "question": "Which two functions are performed at the LLC sublayer of the OSI Data Link Layer to facilitate Ethernet communication? (Choose two.)",
    "options": [
        "integrates Layer 2 flows between 10 Gigabit Ethernet over fiber and 1 Gigabit Ethernet over copper",
        "places information in the Ethernet frame that identifies which network layer protocol is being encapsulated by the frame",
        "implements CSMA/CD over legacy shared half-duplex media",
        "adds Ethernet control information to network protocol data",
        "applies source and destination MAC addresses to Ethernet frame"
    ],
    "correct_answers": [1, 3],  # Zero-based indices for "places information in the Ethernet frame that identifies which network layer protocol is being encapsulated by the frame" and "applies source and destination MAC addresses to Ethernet frame"
    "multi_answer": True
},
{
    "question": "Which two functions are performed at the LLC sublayer of the OSI Data Link Layer to facilitate Ethernet communication? (Choose two.)",
    "options": [
        "enables IPv4 and IPv6 to utilize the same physical medium",
        "adds Ethernet control information to network protocol data",
        "applies source and destination MAC addresses to Ethernet frame",
        "responsible for the internal structure of Ethernet frame",
        "implements trailer with frame check sequence for error detection"
    ],
    "correct_answers": [0, 1],  # Zero-based indices for "adds Ethernet control information to network protocol data" and "applies source and destination MAC addresses to Ethernet frame"
    "multi_answer": True
},
{
    "question": "Which two functions are performed at the LLC sublayer of the OSI Data Link Layer to facilitate Ethernet communication? (Choose two.)",
    "options": [
        "enables IPv4 and IPv6 to utilize the same physical medium",
        "applies source and destination MAC addresses to Ethernet frame",
        "integrates Layer 2 flows between 10 Gigabit Ethernet over fiber and 1 Gigabit Ethernet over copper",
        "handles communication between upper layer networking software and Ethernet NIC hardware",
        "responsible for internal structure of Ethernet frame"
    ],
    "correct_answers": [0, 3],  # Zero-based indices for "applies source and destination MAC addresses to Ethernet frame" and "handles communication between upper layer networking software and Ethernet NIC hardware"
    "multi_answer": True
},
{
    "question": "The global configuration command ip default-gateway 172.16.100.1 is applied to a switch. What is the effect of this command?",
    "options": [
        "The switch can communicate with other hosts on the 172.16.100.0 network.",
        "The switch can be remotely managed from a host on another network.",
        "The switch is limited to sending and receiving frames to and from the gateway 172.16.100.1.",
        "The switch will have a management interface with the address 172.16.100.1."
    ],
    "correct_answers": [1],  # Zero-based index for "The switch can communicate with other hosts on the 172.16.100.0 network."
    "multi_answer": False
},
{
    "question": "What happens when the transport input ssh command is entered on the switch vty lines?",
    "options": [
        "The SSH client on the switch is enabled.",
        "The switch requires a username/password combination for remote access.",
        "Communication between the switch and remote users is encrypted.",
        "The switch requires remote connections via a proprietary client software."
    ],
    "correct_answers": [2],  # Zero-based index for "Communication between the switch and remote users is encrypted."
    "multi_answer": False
},
{
    "question": "A disgruntled employee is using some free wireless networking tools to determine information about the enterprise wireless networks. This person is planning on using this information to hack the wireless network. What type of attack is this?",
    "options": [
        "DoS",
        "access",
        "reconnaissance",
        "Trojan horse"
    ],
    "correct_answers": [2],  # Zero-based index for "reconnaissance"
    "multi_answer": False
},
{
    "question": "What service is provided by HTTP?",
    "options": [
        "Uses encryption to secure the exchange of text, graphic images, sound, and video on the web.",
        "Allows for data transfers between a client and a file server.",
        "An application that allows real-time chatting among remote users.",
        "A basic set of rules for exchanging text, graphic images, sound, video, and other multimedia files on the web."
    ],
    "correct_answers": [3],  # Zero-based index for "A basic set of rules for exchanging text, graphic images, sound, video, and other multimedia files on the web."
    "multi_answer": False
},
{
    "question": "A client packet is received by a server. The packet has a destination port number of 67. What service is the client requesting?",
    "options": [
        "FTP",
        "DHCP",
        "Telnet",
        "SSH"
    ],
    "correct_answers": [1],  # Zero-based index for "DHCP"
    "multi_answer": False
},
{
    "question": "What are two problems that can be caused by a large number of ARP request and reply messages? (Choose two.)",
    "options": [
        "Switches become overloaded because they concentrate all the traffic from the attached subnets.",
        "The ARP request is sent as a broadcast, and will flood the entire subnet.",
        "The network may become overloaded because ARP reply messages have a very large payload due to the 48-bit MAC address and 32-bit IP address that they contain.",
        "A large number of ARP request and reply messages may slow down the switching process, leading the switch to make many changes in its MAC table.",
        "All ARP request messages must be processed by all nodes on the local network."
    ],
    "correct_answers": [1, 4],  # Zero-based indices for "The ARP request is sent as a broadcast, and will flood the entire subnet." and "A large number of ARP request and reply messages may slow down the switching process, leading the switch to make many changes in its MAC table."
    "multi_answer": True
},
{
    "question": "A group of Windows PCs in a new subnet has been added to an Ethernet network. When testing the connectivity, a technician finds that these PCs can access local network resources but not the Internet resources. To troubleshoot the problem, the technician wants to initially confirm the IP address and DNS configurations on the PCs, and also verify connectivity to the local router. Which three Windows CLI commands and utilities will provide the necessary information? (Choose three.)",
    "options": [
        "netsh interface ipv6 show neighbor",
        "arp -a",
        "tracert",
        "ping",
        "ipconfig",
        "nslookup",
        "telnet"
    ],
    "correct_answers": [3, 4, 5],  # Zero-based indices for "arp -a", "tracert", and "ping"
    "multi_answer": True
},
{
    "question": "During the process of forwarding traffic, what will the router do immediately after matching the destination IP address to a network on a directly connected routing table entry?",
    "options": [
        "analyze the destination IP address",
        "switch the packet to the directly connected interface",
        "look up the next-hop address for the packet",
        "discard the traffic after consulting the route table"
    ],
    "correct_answers": [1],  # Zero-based index for "switch the packet to the directly connected interface"
    "multi_answer": False
},
{
    "question": "What characteristic describes antispyware?",
    "options": [
        "applications that protect end devices from becoming infected with malicious software",
        "a network device that filters access and traffic coming into a network",
        "software on a router that filters traffic based on IP addresses or applications",
        "a tunneling protocol that provides remote users with secure access into the network of an organization"
    ],
    "correct_answers": [0],  # Zero-based index for "applications that protect end devices from becoming infected with malicious software"
    "multi_answer": False
},
{
    "question": "A network administrator needs to keep the user ID, password, and session contents private when establishing remote CLI connectivity with a switch to manage it. Which access method should be chosen?",
    "options": [
        "Telnet",
        "AUX",
        "SSH",
        "Console"
    ],
    "correct_answers": [2],  # Zero-based index for "SSH"
    "multi_answer": False
},
{
    "question": "What are the two most effective ways to defend against malware? (Choose two.)",
    "options": [
        "Implement a VPN.",
        "Implement network firewalls.",
        "Implement RAID.",
        "Implement strong passwords.",
        "Update the operating system and other application software.",
        "Install and update antivirus software."
    ],
    "correct_answers": [4, 5],  # Zero-based index for "Implement network firewalls." and "Install and update antivirus software."
    "multi_answer": True
},
{
    "question": "Which type of security threat would be responsible if a spreadsheet add-on disables the local software firewall?",
    "options": [
        "brute-force attack",
        "Trojan horse",
        "DoS",
        "buffer overflow"
    ],
    "correct_answers": [1],  # Zero-based index for "Trojan horse"
    "multi_answer": False
},
{
    "question": "Which frame field is created by a source node and used by a destination node to ensure that a transmitted data signal has not been altered by interference, distortion, or signal loss?",
    "options": [
        "User Datagram Protocol field",
        "transport layer error check field",
        "flow control field",
        "frame check sequence field",
        "error correction process field"
    ],
    "correct_answers": [3],  # Zero-based index for "frame check sequence field"
    "multi_answer": False
},
{
    "question": "A network administrator is adding a new LAN to a branch office. The new LAN must support 4 connected devices. What is the smallest network mask that the network administrator can use for the new network?",
    "options": [
        "255.255.255.248",
        "255.255.255.0",
        "255.255.255.128",
        "255.255.255.192"
    ],
    "correct_answers": [0],  # Zero-based index for "255.255.255.248"
    "multi_answer": False
},
{
    "question": "What service is provided by POP3?",
    "options": [
        "Retrieves email from the server by downloading the email to the local mail application of the client.",
        "An application that allows real-time chatting among remote users.",
        "Allows remote access to network devices and servers.",
        "Uses encryption to provide secure remote access to network devices and servers."
    ],
    "correct_answers": [0],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "What two security solutions are most likely to be used only in a corporate environment? (Choose two.)",
    "options": [
        "antispyware",
        "virtual private networks",
        "intrusion prevention systems",
        "strong passwords",
        "antivirus software"
    ],
    "correct_answers": [1, 2],  # Zero-based indices for the correct answers
    "multi_answer": True
},
{
    "question": "What characteristic describes antivirus software?",
    "options": [
        "applications that protect end devices from becoming infected with malicious software",
        "a network device that filters access and traffic coming into a network",
        "a tunneling protocol that provides remote users with secure access into the network of an organization",
        "software on a router that filters traffic based on IP addresses or applications"
    ],
    "correct_answers": [0],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "What mechanism is used by a router to prevent a received IPv4 packet from traveling endlessly on a network?",
    "options": [
        "It checks the value of the TTL field and if it is 0, it discards the packet and sends a Destination Unreachable message to the source host.",
        "It checks the value of the TTL field and if it is 100, it discards the packet and sends a Destination Unreachable message to the source host.",
        "It decrements the value of the TTL field by 1 and if the result is 0, it discards the packet and sends a Time Exceeded message to the source host.",
        "It increments the value of the TTL field by 1 and if the result is 100, it discards the packet and sends a Parameter Problem message to the source host."
    ],
    "correct_answers": [2],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "A client packet is received by a server. The packet has a destination port number of 69. What service is the client requesting?",
    "options": [
        "DNS",
        "DHCP",
        "SMTP",
        "TFTP"
    ],
    "correct_answers": [3],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "An administrator defined a local user account with a secret password on router R1 for use with SSH. Which three additional steps are required to configure R1 to accept only encrypted SSH connections? (Choose three.)",
    "options": [
        "Configure DNS on the router.",
        "Generate two-way pre-shared keys.",
        "Configure the IP domain name on the router.",
        "Generate the SSH keys.",
        "Enable inbound vty SSH sessions.",
        "Enable inbound vty Telnet sessions."
    ],
    "correct_answers": [2, 3, 4],  # Zero-based indices for the correct answers
    "multi_answer": True
},
{
    "question": "Which two functions are performed at the MAC sublayer of the OSI Data Link Layer to facilitate Ethernet communication? (Choose two.)",
    "options": [
        "handles communication between upper layer networking software and Ethernet NIC hardware",
        "implements trailer with frame check sequence for error detection",
        "places information in the Ethernet frame that identifies which network layer protocol is being encapsulated by the frame",
        "implements a process to delimit fields within an Ethernet 2 frame",
        "adds Ethernet control information to network protocol data"
    ],
    "correct_answers": [1, 3],  # Zero-based indices for the correct answers
    "multi_answer": True
},
{
    "question": "Which two functions are performed at the MAC sublayer of the OSI Data Link Layer to facilitate Ethernet communication? (Choose two.)",
    "options": [
        "places information in the Ethernet frame that identifies which network layer protocol is being encapsulated by the frame",
        "adds Ethernet control information to network protocol data",
        "responsible for internal structure of Ethernet frame",
        "enables IPv4 and IPv6 to utilize the same physical medium",
        "implements trailer with frame check sequence for error detection"
    ],
    "correct_answers": [2, 4],  # Zero-based indices for the correct answers
    "multi_answer": True
},
{
    "question": "Which two functions are performed at the MAC sublayer of the OSI Data Link Layer to facilitate Ethernet communication? (Choose two.)",
    "options": [
        "integrates Layer 2 flows between 10 Gigabit Ethernet over fiber and 1 Gigabit Ethernet over copper",
        "enables IPv4 and IPv6 to utilize the same physical medium",
        "handles communication between upper layer networking software and Ethernet NIC hardware",
        "adds Ethernet control information to network protocol data",
        "implements CSMA/CD over legacy shared half-duplex media"
    ],
    "correct_answers": [0, 4],  # Zero-based indices for the correct answers
    "multi_answer": True
},
{
    "question": "Which two functions are performed at the MAC sublayer of the OSI Data Link Layer to facilitate Ethernet communication? (Choose two.)",
    "options": [
        "applies delimiting of Ethernet frame fields to synchronize communication between nodes",
        "places information in the Ethernet frame that identifies which network layer protocol is being encapsulated by the frame",
        "adds Ethernet control information to network protocol data",
        "implements trailer with frame check sequence for error detection",
        "handles communication between upper layer networking software and Ethernet NIC hardware"
    ],
    "correct_answers": [0, 3],  # Zero-based indices for the correct answers
    "multi_answer": True
},
{
    "question": "An IPv6 enabled device sends a data packet with the destination address of FF02::2. What is the target of this packet?",
    "options": [
        "all IPv6 enabled devices on the local link",
        "all IPv6 DHCP servers",
        "all IPv6 enabled devices across the network",
        "all IPv6 configured routers on the local link"
    ],
    "correct_answers": [3],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "What are the three parts of an IPv6 global unicast address? (Choose three.)",
    "options": [
        "subnet ID",
        "subnet mask",
        "broadcast address",
        "global routing prefix",
        "interface ID"
    ],
    "correct_answers": [0, 3, 4],  # Zero-based index for the correct answers
    "multi_answer": True
},
{
    "question": "A network administrator is designing the layout of a new wireless network. Which three areas of concern should be accounted for when building a wireless network? (Choose three.)",
    "options": [
        "extensive cabling",
        "mobility options",
        "packet collision",
        "interference",
        "security",
        "coverage area"
    ],
    "correct_answers": [3, 4, 5],  # Zero-based index for the correct answers
    "multi_answer": True
},
{
    "question": "A new network administrator has been asked to enter a banner message on a Cisco device. What is the fastest way a network administrator could test whether the banner is properly configured?",
    "options": [
        "Enter CTRL-Z at the privileged mode prompt.",
        "Exit global configuration mode.",
        "Power cycle the device.",
        "Reboot the device.",
        "Exit privileged EXEC mode and press Enter."
    ],
    "correct_answers": [4],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "What method is used to manage contention-based access on a wireless network?",
    "options": [
        "token passing",
        "CSMA/CA",
        "priority ordering",
        "CSMA/CD"
    ],
    "correct_answers": [1],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "What is a function of the data link layer?",
    "options": [
        "provides the formatting of data",
        "provides end-to-end delivery of data between hosts",
        "provides delivery of data between two applications",
        "provides for the exchange of frames over a common local media"
    ],
    "correct_answers": [3],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "What is the purpose of the TCP sliding window?",
    "options": [
        "to ensure that segments arrive in order at the destination",
        "to end communication when data transmission is complete",
        "to inform a source to retransmit data from a specific point forward",
        "to request that a source decrease the rate at which it transmits data"
    ],
    "correct_answers": [3],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "What characteristic describes spyware?",
    "options": [
        "a network device that filters access and traffic coming into a network",
        "software that is installed on a user device and collects information about the user",
        "an attack that slows or crashes a device or network service",
        "the use of stolen credentials to access private data"
    ],
    "correct_answers": [1],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "Which switching method drops frames that fail the FCS check?",
    "options": [
        "store-and-forward switching",
        "borderless switching",
        "ingress port buffering",
        "cut-through switching"
    ],
    "correct_answers": [0],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "Which range of link-local addresses can be assigned to an IPv6-enabled interface?",
    "options": [
        "FEC0::/10",
        "FDEE::/7",
        "FE80::/10",
        "FF00::/8"
    ],
    "correct_answers": [2],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "What service is provided by FTP?",
    "options": [
        "A basic set of rules for exchanging text, graphic images, sound, video, and other multimedia files on the web.",
        "An application that allows real-time chatting among remote users.",
        "Allows for data transfers between a client and a file server.",
        "Uses encryption to secure the exchange of text, graphic images, sound, and video on the web."
    ],
    "correct_answers": [2],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "A user is attempting to access http://www.cisco.com/ without success. Which two configuration values must be set on the host to allow this access? (Choose two.)",
    "options": [
        "DNS server",
        "source port number",
        "HTTP server",
        "source MAC address",
        "default gateway"
    ],
    "correct_answers": [0, 4],  # Zero-based indices for the correct answers
    "multi_answer": True
},
{
    "question": "Which two statements accurately describe an advantage or a disadvantage when deploying NAT for IPv4 in a network? (Choose two.)",
    "options": [
        "NAT adds authentication capability to IPv4.",
        "NAT introduces problems for some applications that require end-to-end connectivity.",
        "NAT will impact negatively on switch performance.",
        "NAT provides a solution to slow down the IPv4 address depletion.",
        "NAT improves packet handling.",
        "NAT causes routing tables to include more information."
    ],
    "correct_answers": [1, 3],  # Zero-based indices for the correct answers
    "multi_answer": True
},
{
    "question": "What would be the interface ID of an IPv6 enabled interface with a MAC address of 1C-6F-65-C2-BD-F8 when the interface ID is generated by using the EUI-64 process?",
    "options": [
        "0C6F:65FF:FEC2:BDF8",
        "1E6F:65FF:FEC2:BDF8",
        "C16F:65FF:FEC2:BDF8",
        "106F:65FF:FEC2:BDF8"
    ],
    "correct_answers": [1],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "What service is provided by BOOTP?",
    "options": [
        "Uses encryption to secure the exchange of text, graphic images, sound, and video on the web.",
        "Allows for data transfers between a client and a file server.",
        "Legacy application that enables a diskless workstation to discover its own IP address and find a BOOTP server on the network.",
        "A basic set of rules for exchanging text, graphic images, sound, video, and other multimedia files on the web."
    ],
    "correct_answers": [2],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "What characteristic describes adware?",
    "options": [
        "a network device that filters access and traffic coming into a network",
        "software that is installed on a user device and collects information about the user",
        "the use of stolen credentials to access private data",
        "an attack that slows or crashes a device or network service"
    ],
    "correct_answers": [1],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "When a switch configuration includes a user-defined error threshold on a per-port basis, to which switching method will the switch revert when the error threshold is reached?",
    "options": [
        "cut-through",
        "store-and-forward",
        "fast-forward",
        "fragment-free"
    ],
    "correct_answers": [1],  # Zero-based index for the correct answer
    "multi_answer": False
},
{
    "question": "What are two primary responsibilities of the Ethernet MAC sublayer? (Choose two.)",
    "options": [
        "error detection",
        "frame delimiting",
        "accessing the media",
        "data encapsulation",
        "logical addressing"
    ],
    "correct_answers": [2, 3],  # Zero-based indices for the correct answers
    "multi_answer": True
},
{
    "question": "What is the subnet ID associated with the IPv6 address 2001:DA48:FC5:A4:3D1B::1/64?",
    "options": [
        "2001:DA48::/64​",
        "2001:DA48:FC5::A4:/64​",
        "2001:DA48:FC5:A4::/64​",
        "2001::/64"
    ],
    "correct_answers": [2],
    "multi_answer": False
},
{
    "question": "Users are reporting longer delays in authentication and in accessing network resources during certain time periods of the week. What kind of information should network engineers check to find out if this situation is part of a normal network behavior?",
    "options": [
        "syslog records and messages",
        "the network performance baseline",
        "debug output and packet captures",
        "network configuration files"
    ],
    "correct_answers": [1],
    "multi_answer": False
},
{
    "question": "How does the service password-encryption command enhance password security on Cisco routers and switches?",
    "options": [
        "It requires encrypted passwords to be used when connecting remotely to a router or switch with Telnet.",
        "It encrypts passwords that are stored in router or switch configuration files.",
        "It requires that a user type encrypted passwords to gain console access to a router or switch.",
        "It encrypts passwords as they are sent across the network."
    ],
    "correct_answers": [1],
    "multi_answer": False
},
{
    "question": "Which two statements are correct in a comparison of IPv4 and IPv6 packet headers? (Choose two.)",
    "options": [
        "The Source Address field name from IPv4 is kept in IPv6.",
        "The Version field from IPv4 is not kept in IPv6.",
        "The Destination Address field is new in IPv6.",
        "The Header Checksum field name from IPv4 is kept in IPv6.",
        "The Time-to-Live field from IPv4 has been replaced by the Hop Limit field in IPv6."
    ],
    "correct_answers": [0, 4],
    "multi_answer": True
},
{
    "question": "What characteristic describes identity theft?",
    "options": [
        "the use of stolen credentials to access private data",
        "software on a router that filters traffic based on IP addresses or applications",
        "software that identifies fast-spreading threats",
        "a tunneling protocol that provides remote users with secure access into the network of an organization"
    ],
    "correct_answers": [0],
    "multi_answer": False
},
{
    "question": "A network administrator is adding a new LAN to a branch office. The new LAN must support 200 connected devices. What is the smallest network mask that the network administrator can use for the new network?",
    "options": [
        "255.255.255.240",
        "255.255.255.0",
        "255.255.255.248",
        "255.255.255.224"
    ],
    "correct_answers": [1],
    "multi_answer": False
},
{
    "question": "What are three commonly followed standards for constructing and installing cabling? (Choose three.)",
    "options": [
        "cost per meter (foot)",
        "cable lengths",
        "connector color",
        "pinouts",
        "connector types",
        "tensile strength of plastic insulator"
    ],
    "correct_answers": [1, 3, 4],
    "multi_answer": True
},
{
    "question": "A client packet is received by a server. The packet has a destination port number of 143. What service is the client requesting?",
    "options": [
    "IMAP",
    "FTP",
    "SSH",
    "Telnet"
    ],
    "correct_answers": [0],
    "multi_answer": False
},
{
    "question": "What are two characteristics shared by TCP and UDP? (Choose two.)",
    "options": [
    "default window size",
    "connectionless communication",
    "port numbering",
    "3-way handshake",
    "ability to to carry digitized voice",
    "use of checksum"
    ],
    "correct_answers": [2, 5],
    "multi_answer": True
},
{
    "question": "A client packet is received by a server. The packet has a destination port number of 21. What service is the client requesting?",
    "options": [
        "FTP",
        "LDAP",
        "SLP",
        "SNMP"
    ],
    "correct_answers": [0],
    "multi_answer": False
},
{
    "question": "What attribute of a NIC would place it at the data link layer of the OSI model?",
    "options": [
        "attached Ethernet cable",
        "IP address",
        "MAC address",
        "RJ-45 port",
        "TCP/IP protocol stack"
    ],
    "correct_answers": [2],
    "multi_answer": False
},
{
    "question": "A network administrator is adding a new LAN to a branch office. The new LAN must support 10 connected devices. What is the smallest network mask that the network administrator can use for the new network?",
    "options": [
        "255.255.255.192",
        "255.255.255.248",
        "255.255.255.224",
        "255.255.255.240"
    ],
    "correct_answers": [3],
    "multi_answer": False
},
{
    "question": "What technique is used with UTP cable to help protect against signal interference from crosstalk?",
    "options": [
        "wrapping a foil shield around the wire pairs",
        "twisting the wires together into pairs",
        "terminating the cable with special grounded connectors",
        "encasing the cables within a flexible plastic sheath"
    ],
    "correct_answers": [1],
    "multi_answer": False
},
{
    "question": "A client packet is received by a server. The packet has a destination port number of 22. What service is the client requesting?",
    "options": [
        "SSH",
        "SMB/CIFS",
        "HTTPS",
        "SLP"
    ],
    "correct_answers": [0],
    "multi_answer": False
},
{
    "question": "What characteristic describes an IPS?",
    "options": [
        "a tunneling protocol that provides remote users with secure access into the network of an organization",
        "a network device that filters access and traffic coming into a network",
        "software that identifies fast-spreading threats",
        "software on a router that filters traffic based on IP addresses or applications"
    ],
    "correct_answers": [1],
    "multi_answer": False
},
{
    "question": "What two ICMPv6 message types must be permitted through IPv6 access control lists to allow resolution of Layer 3 addresses to Layer 2 MAC addresses? (Choose two.)",
    "options": [
        "neighbor solicitations",
        "echo requests",
        "neighbor advertisements",
        "echo replies",
        "router solicitations",
        "router advertisements"
    ],
    "correct_answers": [0, 2],
    "multi_answer": True
},
{
    "question": "A client is using SLAAC to obtain an IPv6 address for its interface. After an address has been generated and applied to the interface, what must the client do before it can begin to use this IPv6 address?",
    "options": [
        "It must send a DHCPv6 INFORMATION-REQUEST message to request the address of the DNS server.",
        "It must send a DHCPv6 REQUEST message to the DHCPv6 server to request permission to use this address.",
        "It must send an ICMPv6 Router Solicitation message to determine what default gateway it should use.",
        "It must send an ICMPv6 Neighbor Solicitation message to ensure that the address is not already in use on the network."
    ],
    "correct_answers": [3],
    "multi_answer": False
},
{
    "question": "Two pings were issued from a host on a local network. The first ping was issued to the IP address of the default gateway of the host and it failed. The second ping was issued to the IP address of a host outside the local network and it was successful. What is a possible cause for the failed ping?",
    "options": [
        "The default gateway is not operational.",
        "The default gateway device is configured with the wrong IP address.",
        "Security rules are applied to the default gateway device, preventing it from processing ping requests.",
        "The TCP/IP stack on the default gateway is not working properly."
    ],
    "correct_answers": [2],
    "multi_answer": False
},
{
    "question": "An organization is assigned an IPv6 address block of 2001:db8:0:ca00::/56. How many subnets can be created without using bits in the interface ID space?",
    "options": [
        "256",
        "512",
        "1024",
        "4096"
    ],
    "correct_answers": [0],
    "multi_answer": False
},
{
    "question": "What subnet mask is needed if an IPv4 network has 40 devices that need IP addresses and address space is not to be wasted?",
    "options": [
        "255.255.255.0",
        "255.255.255.240",
        "255.255.255.128",
        "255.255.255.192",
        "255.255.255.224"
    ],
    "correct_answers": [3],
    "multi_answer": False
},
{
    "question": "What is a benefit of using cloud computing in networking?",
    "options": [
        "Technology is integrated into every-day appliances allowing them to interconnect with other devices, making them more ‘smart’ or automated.",
        "Network capabilities are extended without requiring investment in new infrastructure, personnel, or software.",
        "End users have the freedom to use personal tools to access information and communicate across a business network.",
        "Home networking uses existing electrical wiring to connect devices to the network wherever there is an electrical outlet, saving the cost of installing data cables."
    ],
    "correct_answers": [1],
    "multi_answer": False
},
{
    "question": "Which two statements are correct about MAC and IP addresses during data transmission if NAT is not involved? (Choose two.)",
    "options": [
        "Destination IP addresses in a packet header remain constant along the entire path to a target host.",
        "Destination MAC addresses will never change in a frame that goes across seven routers.",
        "Every time a frame is encapsulated with a new destination MAC address, a new destination IP address is needed.",
        "Destination and source MAC addresses have local significance and change every time a frame goes from one LAN to another.",
        "A packet that has crossed four routers has changed the destination IP address four times."
    ],
    "correct_answers": [0, 3],
    "multi_answer": True
},
{
    "question": "What is one main characteristic of the data link layer?",
    "options": [
        "It generates the electrical or optical signals that represent the 1 and 0 on the media.",
        "It converts a stream of data bits into a predefined code.",
        "It shields the upper layer protocol from being aware of the physical medium to be used in the communication.",
        "It accepts Layer 3 packets and decides the path by which to forward the packet to a remote network."
    ],
    "correct_answers": [2],
    "multi_answer": False
},
{
    "question": "What are three characteristics of the CSMA/CD process? (Choose three.)",
    "options": [
        "The device with the electronic token is the only one that can transmit after a collision.",
        "A device listens and waits until the media is not busy before transmitting.",
        "After detecting a collision, hosts can attempt to resume transmission after a random time delay has expired.",
        "All of the devices on a segment see data that passes on the network medium.",
        "A jam signal indicates that the collision has cleared and the media is not busy.",
        "Devices can be configured with a higher transmission priority."
    ],
    "correct_answers": [1, 2, 3],
    "multi_answer": True
},
{
    "question": "Which two commands can be used on a Windows host to display the routing table? (Choose two.)",
    "options": [
        "netstat -s",
        "route print",
        "show ip route",
        "netstat -r",
        "tracert"
    ],
    "correct_answers": [1, 3],
    "multi_answer": True
},
{
    "question": "What are two functions that are provided by the network layer? (Choose two.)",
    "options": [
        "directing data packets to destination hosts on other networks",
        "placing data on the network medium",
        "carrying data between processes that are running on source and destination hosts",
        "providing dedicated end-to-end connections",
        "providing end devices with a unique network identifier"
    ],
    "correct_answers": [0, 4],
    "multi_answer": True
},
{
    "question": "Which two statements describe features of an IPv4 routing table on a router? (Choose two.)",
    "options": [
        "Directly connected interfaces will have two route source codes in the routing table: C and S.",
        "If there are two or more possible routes to the same destination, the route associated with the higher metric value is included in the routing table.",
        "The netstat -r command can be used to display the routing table of a router.",
        "The routing table lists the MAC addresses of each active interface.",
        "It stores information about routes derived from the active router interfaces.",
        "If a default static route is configured in the router, an entry will be included in the routing table with source code S."
    ],
    "correct_answers": [4, 5],
    "multi_answer": True
},
{
    "question": "What characteristic describes a VPN?",
    "options": [
        "software on a router that filters traffic based on IP addresses or applications",
        "software that identifies fast-spreading threats",
        "a tunneling protocol that provides remote users with secure access into the network of an organization",
        "a network device that filters access and traffic coming into a network"
    ],
    "correct_answers": [2],
    "multi_answer": False
},
{
    "question": "A user sends an HTTP request to a web server on a remote network. During encapsulation for this request, what information is added to the address field of a frame to indicate the destination?",
    "options": [
        "the network domain of the destination host",
        "the IP address of the default gateway",
        "the MAC address of the destination host",
        "the MAC address of the default gateway"
    ],
    "correct_answers": [3],
    "multi_answer": False
},
{
    "question": "What is an advantage to using a protocol that is defined by an open standard?",
    "options": [
        "A company can monopolize the market.",
        "The protocol can only be run on equipment from a specific vendor.",
        "An open standard protocol is not controlled or regulated by standards organizations.",
        "It encourages competition and promotes choices."
    ],
    "correct_answers": [3],
    "multi_answer": False
},
{
    "question": "Data is being sent from a source PC to a destination server. Which three statements correctly describe the function of TCP or UDP in this situation? (Choose three.)",
    "options": [
        "The source port field identifies the running application or service that will handle data returning to the PC.",
        "The TCP process running on the PC randomly selects the destination port when establishing a session with the server.",
        "UDP segments are encapsulated within IP packets for transport across the network.",
        "The UDP destination port number identifies the application or service on the server which will handle the data.",
        "TCP is the preferred protocol when a function requires lower network overhead.",
        "The TCP source port number identifies the sending host on the network."
    ],
    "correct_answers": [0, 2, 3],
    "multi_answer": True
},
{
    "question": "What two pieces of information are displayed in the output of the show ip interface brief command? (Choose two.)",
    "options": [
        "IP addresses",
        "interface descriptions",
        "MAC addresses",
        "next-hop addresses",
        "Layer 1 statuses",
        "speed and duplex settings"
    ],
    "correct_answers": [0, 4],
    "multi_answer": True
},
{
    "question": "A user is complaining that an external web page is taking longer than normal to load. The web page does eventually load on the user machine. Which tool should the technician use with administrator privileges in order to locate where the issue is in the network?",
    "options": [
        "ping",
        "nslookup",
        "tracert",
        "ipconfig /displaydns"
    ],
    "correct_answers": [2],
    "multi_answer": False
},
{
    "question": "A network technician is researching the use of fiber optic cabling in a new technology center. Which two issues should be considered before implementing fiber optic media? (Choose two.)",
    "options": [
        "Fiber optic cabling requires different termination and splicing expertise from what copper cabling requires.",
        "Fiber optic cabling requires specific grounding to be immune to EMI.",
        "Fiber optic cabling is susceptible to loss of signal due to RFI.",
        "Fiber optic cable is able to withstand rough handling.",
        "Fiber optic provides higher data capacity but is more expensive than copper cabling."
    ],
    "correct_answers": [0, 4],
    "multi_answer": True
},
{
    "question": "A user is executing a tracert to a remote device. At what point would a router, which is in the path to the destination device, stop forwarding the packet?",
    "options": [
        "when the router receives an ICMP Time Exceeded message",
        "when the RTT value reaches zero",
        "when the host responds with an ICMP Echo Reply message",
        "when the value in the TTL field reaches zero",
        "when the values of both the Echo Request and Echo Reply messages reach zero"
    ],
    "correct_answers": [3],
    "multi_answer": False
},
{
    "question": "Users report that the network access is slow. After questioning the employees, the network administrator learned that one employee downloaded a third-party scanning program for the printer. What type of malware might be introduced that causes slow performance of the network?",
    "options": [
        "virus",
        "worm",
        "phishing",
        "spam"
    ],
    "correct_answers": [1],
    "multi_answer": False
},
]



def ask_question(question, options, correct_answer_indices, multi_answer=False):
    """
    Function to ask a question and validate the user's response.
    Returns True if the response is correct, False otherwise.
    """
    console.print(f"{question}\n", style="bold yellow")
    for i, option in enumerate(options):
        console.print(f"{i + 1}. {option}\n")

    if multi_answer:
        console.print("\nPlease enter your answers separated by a comma (e.g., 1,3):")
    else:
        console.print("\nPlease enter the number of your answer (1-4):")

    while True:
        try:
            if multi_answer:
                answers = input("Your answers: ").split(',')
                answers = [int(a.strip()) for a in answers]
                if all(1 <= a <= len(options) for a in answers):
                    return set(answers) == set(correct_answer_indices)
                else:
                    console.print(f"Please enter numbers between 1 and {len(options)} separated by commas.")
            else:
                answer = int(input("Your answer: "))
                if 1 <= answer <= len(options):
                    return answer == correct_answer_indices[0]
                else:
                    console.print(f"Please enter a number between 1 and {len(options)}.")
        except ValueError:
            console.print("Invalid input. Please enter the correct format.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    # Your list of questions and answers goes here

    # Shuffle the questions
    random.shuffle(questions)

    score = 0
    console.print("Welcome to the quiz! Answer the following questions:\n", style="bold yellow")

    for q in questions:
        question = q["question"]
        options = q["options"]
        correct_answers = q["correct_answers"]
        multi_answer = q["multi_answer"]

        # Shuffle the options and find the new indices of the correct answers
        combined = list(zip(options, range(len(options))))
        random.shuffle(combined)
        shuffled_options, original_indices = zip(*combined)
        shuffled_correct_indices = [original_indices.index(i) + 1 for i in correct_answers]  # Convert to 1-based

        if ask_question(question, shuffled_options, shuffled_correct_indices, multi_answer):
            console.print("Correct!\n", style="green")
            score += 1
            input("Press Enter to continue...")
            clear_screen()
        else:
            console.print("Incorrect. The correct answer is:", style="red")
            if len(correct_answers) == 1:
                console.print(f"{correct_answers[0] + 1}. {options[correct_answers[0]]}", style="bold")
            else:
                console.print("The correct answers are:\n", style="bold")
                for i in correct_answers:
                    console.print(f"{options[i]}\n", style="bold")
            input("Press Enter to continue...")
            clear_screen()
            console.print()  # Add an empty line for spacing

    console.print(f"You scored {score} out of {len(questions)}.", style="bold cyan")

if __name__ == "__main__":
    main()

