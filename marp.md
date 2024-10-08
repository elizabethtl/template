---

marp: true
theme: default
paginate: true

---

<style>
section {
  text-align: left;
  background-color: #ededed;
}
h1, h4 {
  text-align: right;
}
h2 {
  color: #0270bf;
  position: absolute;
  top: 8%;
}
h3 {
  color: #02717d;
  position: absolute;
  top: 12%;
}
img{
  display: block;
  margin-left:30%;
}
</style>


# Securing Public Safety Communications on Commercial and Tactical 5G Networks

#### 資科四 林子恩

---

public safety actors (law enforcement, border control, etc.) have traditionlly used closed networks with high-security and narrow-bandwidth properties

costs of maintaining a dedicated communication infrastructrue are high

potential advantages of emerging applications

&rarr; necessitate upgrading the network

---

<style scoped>
  p, ul{
    position: relative;
    top: 10%;
  }
  img{
    display: block;
    margin-left:30%;
  }
</style>

## next generation of public safety networks 

expected to be based on 3GPP (protocols for mobile telecommunications)

follow hybrid architecture 
* commercial mobile operator network infrastructure
* rapidly deployable tactical network bubbles
  * extra capacity in remote locations
  * availability where commercial network is distrupted

![width:500px](./screenshots/infrastructure.png)

---

## next generation of public safety networks 

hybrid infrastructure promises cost effective means to achieve communication with good quality

but, sharing infrastructure between civilian and public safety users introduces new challenges
* availability
* trustworthiness
* security

threat landscape larger than closed networks

---

## complement existing research by providing

an analysis of public safety communication related security requirements and characteristics

insights and observations on challenges arising from 
* utilization of 5G communication standards and civilian infrastructure
* emergence of IoT equipment
* tactical communications in remote locations with potentially limited or disconnected backhaul
* distributed mission-critical application architectures

---

## public safety network evolution and use cases

* characteristics of technologies
* highlight typical use cases and requirements involved
  
---
<style scoped>
  p, ul{
    position: relative;
    top: 10%;
  }
</style>

## public safety network evolution and use cases

### authorities in commercial operators' access networks

public safety users typically require priority over other users

&rarr; operators may provide service levels with diverse availability guarantees and QoS properties

provides dynamically request availability guarantees for traffic flows through policy control functions

based on agreements between operators and public safety organizations
* contractual agreements
* service level agreements

---

<style scoped>
  p, ul{
    position: relative;
    top: 12%;
  }
</style>

## public safety network evolution and use cases

### tactical bubbles

movable, stand-alone, rapidly deployable networks that provide connectivity to network

minimal configuration time and efforts, automation and self-configuration are essential

may increase security when securely isolated from commercial infrastructure

![width:500px](./screenshots/Topology-of-the-tactical-bubble-system-with-three-interconnected-bubbles.png)

---

## public safety network evolution and use cases

### tactical bubbles

three main modes

1. **tactical access bubble** - has own access network functions, core network and application services are external (from cloud or other bubble)
2. **regular bubble** - own access and core functions, application services from cloud or other bubble
3. **isolated bubble** - works independently with its own access, core, application functions

---

## public safety network evolution and use cases

### use cases and assets - video surveillance within tactical bubble

capable of transmitting large data streams within isolated tactical network

requires broadband access and core, video servers, local edge acceleration (optional)

---

## public safety network evolution and use cases

### use cases and assets - mission-critical services in the cloud

application servers and database operate in remote location

cloud services and tactical bubble connected with backhaul (commercial mobile network or satellite)

---

## public safety network evolution and use cases

### use cases and assets - access through a civilian private network

provide public safety users an alternative access network, can be utilized when dedicated or commercial networks are unavailable

requires federation and cooperation between private network operators and public safety organizations

---

## threat landscape

### root vulnerabilities

implementation failures - can be minimized with testing but cannot be completely removed

architectural failures - related to design and planning of public safety communication and security architecture

operational failures - caused by normal end-users, can be minimized with standards

configuration failures - intentional or non-intentional mistakes made by administrators

---

## threat landscape

### attack vectors and types

- open air interface or local radio attacks - can be made within coverage of radio access network
- physical adversaries can intrude on equipment or devices
- remove cyber-adversaries advancing through different interfaces or with the help of malware

---

## public safety scenario analysis

### threat scenrios in the access network

part of the control plane communication is *unprotected* → exposed to eavesdropping, tracking, tampering, man-in-the-middle attacks

Operational information of public safety actors’ capabilities can be leaked to eavesdroppers
* device capability information and temporary identifiers are still transmitted in clear text both in 4G and 5G 

---

## public safety scenario analysis

### threat scenrios in the access network

DoS adversaries can exploit the few public safety specific mechanisms

* total bandwidth is limited, some UEs have higher priority, malicious UEs with higher priority have potential to cause harm
* information on who is given priority or access may not be available from centralized database when under network attack
  &rarr; some tactical bubbles may become ‘orphans’

---

## public safety scenario analysis

### threat scenrios in the network domain - core network services

authentication server function (AUSF) requires extensive protection

authentication database distributed to tactical bubbles

5G's APIs introduces new opportunities, but also more vulnerable

opened services, such as policy control functions must be secured

---

## public safety scenario analysis

### threat scenrios in the network domain - infrastructure

critical functions typically not hosted on infrastructure shared with civilian users

in isolated situations, core services are brought to tactical bubbles &rarr; risk of attack or unathorized access

power supply, heating/cooling, hosting base stations are also attack paths

--- 

## security enablers

the security requirements and solutions proposed and researched for 5G networks and public safety communications

--- 

<style scoped>
  p, ul{
    position: relative;
    top: 12%;
  }
</style>

## security enablers

### network security

based on 3GPP protocol, user credentials stored in a USIM application

the concealing of UE identifiers when transmitted in the open air when reaching the UE

monitoring and trusted computing to verify and enforce that devices are running in the expected software configuration and are providing desired security level

![width:500px](screenshots/SIM.jpg)

--- 

<style scoped>
  p, ul{
    position: relative;
    top: 12%;
  }
  img{
    display: block;
    margin-left:35%;
  }
</style>

## security enablers

### network security

security required when connecting tactical bubbles, base stations, or base stations

firewalls mandatory in communication perimeters

backhaul communication usually encapsulated using GPRS tunneling protocol (GTP), secured with internet protocol security (IPsec)

architectures designed to tolerate against DoS - mesh architecture, dynamic backhaul

![width:300px](./screenshots/mesh.png)

---


## security enablers

### mission-critical applications

Application layer security is needed for critical applications where network layer mechanisms are not trusted to provide sufficient security level

* identity and access management
* confidentiality and integrity (key management and cryptographic protocols)

---

## security enablers

### mission-critical applications

security framework specified by 3GPP is distributed and service-based

* identity management service enables federated authentication
* key management server provides cryptographic keys
* group management server controls group communication
  * ensure that only legitimate users have access to group communication

---

## security enablers

### mission-critical applications

Identity and access management services can in principle be centralized and locate in the cloud or distributed to the tactical bubble

synchronizing information in distributed scenarios requires federation

&rarr; more exposed to data breaches

---

<style scoped>
  p, ul, ol{
    position: relative;
    top: 12%;
  }
</style>

## security enablers

### hardened devices

harden UEs (cellphones, IoT devices) to minimize risk of security breaches and threats towards the network through UEs

prevent untrusted features and configurations

1. whitelisting of applications, services, and system software versions,
2. protecting physical interfaces (e.g., USB) by whitelisting devices and accessories that can be cnnected,
3. protecting network interfaces, e.g., with firewalls
4. securing critical information, software, and credentials with secure hardware solutions (root-of-trusts).

---

## security enablers

### hardened devices

protection and verification of software integrity
* assuring software configuration with secure boot, where each layer of the system verifies integrity of next layer before execution, establishing a chain of trust

Device integrity measurements can function as evidence of the trustworthiness of a UE
* remote attestation: remote agent challenges device to report identity and software configuration, agent then verifies integrity of device

---

## security enablers

### hardened devices

In a mobile network, the security is typically based on hardware tokens (USIM)

A new alternative, which provides more flexibility for public safety users, is the virtualized credential platform eSIM

eSIM architecture enables network to push eSIM profiles automatically to compatible devices with bootstrap profiles that are pre-registered to the network

---

<style scoped>
  img{
  display: block;
  margin-left:10%;
  margin-top:10%;
  }
</style>
## security solutions in pubilc safety trials

![](./screenshots/security%20enablers.png)

---

<style scoped>
  p, ul{
    position: relative;
    top: 13%;
  }
  img{
  display: block;
  margin-left:25%;
  }
</style>

## security solutions in pubilc safety trials

### remote attestation enhanced access management within tactical bubbles

devices susceptible to cyber-adversaries &rarr; use remote attestation to verify integrity of device and detect unauthorized changes in device firmware

backend services verify devices in tactical bubble using OpenID Connect and OAuth 2.0- based authentication and authoriztion framework

![width:600px](./screenshots/OAuth2.0.png)

---

<style scoped>
  p, ul{
    position: relative;
    top: 10%;
  }
</style>

## security solutions in pubilc safety trials

### securing satellite backhaul for tactical bubbles

wireless backhaul is sometimes the only solution for connecting the tactical bubble to the core network or application server

the downlink (satellite-to-ground) traffic can be intercepted and signal tampered at any location within the spot beam with roughly equal signal quality using low-cost commercial equipment

confidentiality and integrity of the satellite link traffic are of paramount importance

a commercial GEO satellite link must be treated as an inherently unsecure transmission medium, requiring at the very minimum a strong end-to-end security solution
