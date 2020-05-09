# ARP-Spoofer
  This program spoofs the target machine's ARP table under same network. It changes the MAC address of router for the target machine and MAC address of target machine for the Router to MAC address of attacking machine.

### Syntax:
  ./arp-spoof \<ip-address-of-target\> <br>
  ./arp-spoof \<ip-address-of-target\> \<ip-address-of-router\>
  
### Features:
 * It provides help if the syntax or IP Address is wrong.
 * This program automatically takes the MAC address of the router and target from previously assigned ARP tables. 
 * This program also assigns router’s IP address automatically if not specified.
 * This program also takes two arguments if there is a specific router’s IP.
