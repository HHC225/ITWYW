# Infrastructure: hosting and network access

Use these mappings when someone describes where an app should run, how people should reach it, or how incoming traffic should be handled. These are candidate names, not automatic diagnoses or vendor recommendations. A wish can require several concepts. Ask the distinguishing question before narrowing an ambiguous request.

Verified against the official sources below on 2026-10-25. **28 concepts.** Related references: [Delivery and operations](infra-delivery-operations.md), [Reliability and data](infra-reliability-data.md).

## Contents

- [Places to run an app](#places-to-run-an-app)
- [Names and encrypted connections](#names-and-encrypted-connections)
- [Traffic delivery and routing](#traffic-delivery-and-routing)
- [Location and private connectivity](#location-and-private-connectivity)
- [Traffic protection](#traffic-protection)
- [Ambiguity traps](#ambiguity-traps)
- [Sources](#sources)

## Places to run an app

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-HN-01 | Web hosting; application hosting | “Put my site on the internet.” / “Let people open it when my laptop is off.” | A computer service keeps your website available for people to visit. | Do you need a place to run the site, a memorable address, or both? | [INF-HN-S01] |
| INF-HN-02 | Static site hosting; static hosting | “Just publish these pages and pictures.” / “Serve the finished website files.” | A server hands out prepared files instead of making each page from scratch. | Are prepared files enough, or must a server calculate a new answer for each request? | [INF-HN-S02] |
| INF-HN-03 | Virtual machine; VM; virtual private server, VPS | “Give me my own cloud computer.” / “I need to install server software myself.” | One physical computer can act like several separate computers, each with its own operating system. | Do you need control of a whole operating system? | [INF-HN-S03] |
| INF-HN-04 | Container; containerization | “Package the app so it runs the same elsewhere.” / “Include the things the app needs in one bundle.” | The app travels in a package with its helper software. | Is the concern a repeatable app package, rather than a whole computer? | [INF-HN-S03] |
| INF-HN-05 | Container orchestration; container management | “Keep all these app containers running.” / “Replace failed containers and manage their copies.” | A manager keeps the right app packages running across computers. | Are you coordinating many running containers, beyond packaging one app? | [INF-HN-S04] |
| INF-HN-06 | Serverless computing; serverless hosting (functions as a service, FaaS, is one form) | “Run this code when something happens.” / “I do not want to look after a server.” | A provider looks after the computers that run your code. | Is the goal provider-managed compute, and is the work a short event task or a longer service? | [INF-HN-S05] |

## Names and encrypted connections

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-HN-07 | Custom domain; domain name registration | “I want my own website address.” / “Reserve this name for my business.” | You reserve a readable name people can use to find your site. | Do you already control the name, or still need to register it? | [INF-HN-S06] |
| INF-HN-08 | Subdomain | “Put the help center at help.myname.com.” / “Give the shop its own address under our name.” | An extra name in front of your domain gives one part its own address. | Do you mean `help.example.com` or a page path such as `example.com/help`? | [INF-HN-S07] |
| INF-HN-09 | Domain Name System; DNS; DNS hosting | “Make our name find the new server.” / “The address exists, but people cannot find the site.” | DNS helps computers look up where a website name points. | Is the name lookup wrong, or does the site fail after the lookup succeeds? | [INF-HN-S08] |
| INF-HN-10 | DNS record; A/AAAA record; CNAME alias; TXT verification record | “My host gave me a value to add to the domain.” / “Prove that I control this website name.” | A DNS record is one instruction attached to a domain name. | Are you pointing to an address, naming an alias, routing mail, or proving ownership? | [INF-HN-S09] |
| INF-HN-11 | HTTPS; TLS; TLS certificate; commonly called SSL certificate | “Give my website an encrypted connection.” / “Stop the browser warning about an untrusted certificate.” | The browser checks the site's certificate and protects messages while they travel. | Is this about the connection, rather than user login or stored data? | [INF-HN-S10] |
| INF-HN-12 | Automated certificate renewal; managed certificate lifecycle | “Do not let the website certificate expire.” / “Renew its connection certificate automatically.” | A helper replaces the site's certificate before it runs out. | Is a certificate missing now, or must an existing one keep renewing? | [INF-HN-S11] |

## Traffic delivery and routing

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-HN-13 | Content delivery network; CDN | “Send pictures from somewhere near each visitor.” / “People far away wait too long for our files.” | Copies of eligible content can be served from computers nearer to visitors. | Is the delay mainly delivering cacheable content across distance? | [INF-HN-S12] |
| INF-HN-14 | Reverse proxy | “Use one front door for several app servers.” / “Send each incoming request to the right service.” | A server receives visitors' requests and passes them to the app behind it. | Do you need request forwarding, load sharing, API policies, or several of these? | [INF-HN-S13] |
| INF-HN-15 | API gateway | “Give our APIs one entrance.” / “Apply common access rules to requests for our services.” | One entry point receives API calls and directs them to the right service. | Is the entrance specifically for APIs with shared routing or access policies? | [INF-HN-S14] |
| INF-HN-16 | Load balancer; load balancing | “Share visitors between our app servers.” / “Send requests to a healthy server.” | A traffic helper spreads requests across available app servers. | Do enough servers already exist, or must capacity also grow? | [INF-HN-S15] |
| INF-HN-27 | HTTP redirect; URL forwarding; permanent or temporary redirect | “Send old links to our new address.” / “Make visitors land on the HTTPS address.” | The server tells the browser to visit a different URL. | Should the browser's visible address change, rather than only its DNS destination? | [INF-HN-S23] |
| INF-HN-28 | HTTP caching; shared cache; edge cache | “Reuse the same answer instead of rebuilding it.” / “Keep popular files ready for the next visitor.” | A saved response can be reused while it is still suitable. | Can these responses safely be shared, and how quickly must changes appear? | [INF-HN-S24] |

## Location and private connectivity

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-HN-17 | Cloud region; hosting region | “Run the app near our customers.” / “Choose which part of the world holds the service.” | A region is a geographic area where a provider runs its computers. | Is the requirement location, latency, or a specific data-residency obligation? | [INF-HN-S16] |
| INF-HN-18 | Availability zone; AZ; zone | “Use separate locations inside the same region.” / “A problem in one facility should not affect every copy.” | A region has separate zones that help keep some failures apart. | Do you mean separate zones nearby or entirely different geographic regions? | [INF-HN-S16] |
| INF-HN-19 | Virtual private cloud; VPC; virtual network, VNet | “Give our cloud services their own network.” / “Keep internal machines on a separate cloud network.” | A private network connects your cloud resources using your network rules. | Do you need network isolation, or permission checks for people using the app? | [INF-HN-S17] |
| INF-HN-20 | Subnet; network segment | “Put the database in a different network section.” / “Separate public-facing machines from internal ones.” | A subnet is a smaller address area inside a network. | Which network sections need different routes or access rules? | [INF-HN-S17] |
| INF-HN-21 | Virtual private network; VPN; encrypted network tunnel | “Let staff reach internal services from home.” / “Reach the office network while I am away.” | A protected tunnel carries network traffic between connected places or devices. | Are you connecting people or networks, rather than publishing a public website? | [INF-HN-S18] |
| INF-HN-22 | Private endpoint; private service connection | “Reach that managed service using a private address.” / “Connect to cloud storage without its public entry point.” | A private doorway connects your network to a particular service. | Do you need private access to one service, rather than a general network tunnel? | [INF-HN-S19] |

## Traffic protection

| ID | Conventional name and aliases | Two everyday English phrases | Child-friendly explanation | Distinguishing cue or question | Source |
| --- | --- | --- | --- | --- | --- |
| INF-HN-23 | Network firewall; network access rule; security group | “Allow only these machines to reach this port.” / “Block unwanted network connections.” | Network rules decide which connections may enter or leave. | Are you filtering addresses and ports, rather than inspecting website request content? | [INF-HN-S20] |
| INF-HN-24 | Web application firewall; WAF | “Filter suspicious requests to the website.” / “Block known attack patterns in incoming web traffic.” | A filter checks web requests for patterns that may be harmful. | Is the concern the contents of HTTP requests rather than every kind of network traffic? | [INF-HN-S21] |
| INF-HN-25 | Rate limiting; request throttling | “Stop one caller from making too many requests.” / “Only allow this many attempts in a minute.” | A counter limits how often a caller can ask for something. | What is being counted, over what time, and for which caller or group? | [INF-HN-S22] |
| INF-HN-26 | DDoS protection; distributed denial-of-service mitigation | “Help the site survive a flood of fake traffic.” / “Filter a huge attack from many computers.” | Protection systems try to absorb or filter attack traffic that would overwhelm the service. | Is there a hostile traffic flood, or a legitimate increase in visitors? | [INF-HN-S25] |

## Ambiguity traps

- **“Put it online”** can mean hosting, domain registration, DNS, deployment, or all four. Start with what already exists. A domain is a name; it does not contain the website. [INF-HN-S01] [INF-HN-S06]
- **“Make it fast”** is a symptom, not a product name. Ask what action is slow, for whom, and whether it worsens under load. A CDN changes content delivery location; a cache reuses answers; load balancing distributes requests; scaling changes capacity. Do not jump directly to Redis, a CDN, or autoscaling. [INF-HN-S12] [INF-HN-S15] [INF-HN-S24] See [scaling and observability](infra-reliability-data.md).
- **“Point this name there”** may require a DNS record or an HTTP redirect. A CNAME alias does not itself tell the browser to show another URL. [INF-HN-S09] [INF-HN-S23]
- **“Make it private”** can mean a private network, a private endpoint, a VPN, or application permissions. Naming a network “private” does not establish the required routes and access rules. [INF-HN-S17] [INF-HN-S18] [INF-HN-S19] [INF-HN-S20]
- **“Secure the site”** does not identify one feature. TLS protects connections; a firewall limits network access; a WAF examines web requests; rate limits constrain request frequency. These do not promise invulnerability. [INF-HN-S10] [INF-HN-S20] [INF-HN-S21] [INF-HN-S22]
- **“Serverless”** still uses servers. Static hosting describes how content is served; containers describe packaging; serverless describes who handles much of the compute operation. These categories can overlap. [INF-HN-S02] [INF-HN-S03] [INF-HN-S05]

## Sources

Source links are evidence for terminology, not recommendations to select the named products. The everyday phrases and child-friendly explanations are original paraphrases.

| Source key | Official title and publisher | Verified topics |
| --- | --- | --- |
| [INF-HN-S01] | AWS — What is Web Hosting? | Hosting purpose; hosting versus a domain. |
| [INF-HN-S02] | GitHub Docs — What is GitHub Pages? | Serving prepared HTML, CSS, and JavaScript as static hosting. |
| [INF-HN-S03] | AWS — Containers vs VM: Difference Between Deployment Technologies | Containers package dependencies; virtual machines provide a machine environment. |
| [INF-HN-S04] | Kubernetes — Overview | Managing containerized workloads, desired state, replacement, and scaling. |
| [INF-HN-S05] | AWS — What is Serverless Computing? | Provider-managed server infrastructure; functions and other serverless forms. |
| [INF-HN-S06] | Cloudflare — What is a Domain Name? | Readable names; registration through a registrar; domain versus URL. |
| [INF-HN-S07] | Cloudflare DNS — Create subdomain records | Addresses such as `blog.example.com`; DNS records for subdomains. |
| [INF-HN-S08] | Cloudflare — What is DNS? | Name resolution and IP addresses. |
| [INF-HN-S09] | Cloudflare — DNS records | A, AAAA, CNAME, MX, and TXT record purposes. |
| [INF-HN-S10] | MDN — Transport Layer Security (TLS) | Connection encryption, integrity, authentication, and certificates. |
| [INF-HN-S11] | Let's Encrypt — Integration Guide | Automated certificate management and renewal timing. |
| [INF-HN-S12] | Cloudflare — What is a CDN? | Distributed content delivery and caching near visitors. |
| [INF-HN-S13] | Cloudflare — What is a reverse proxy? | Intermediary in front of servers; forwarding; optional caching and balancing. |
| [INF-HN-S14] | AWS — What is Amazon API Gateway? | API entry point, request routing, and API management capabilities. |
| [INF-HN-S15] | AWS — What is Elastic Load Balancing? | Traffic distribution and target health checks. |
| [INF-HN-S16] | AWS — AWS Regions and Availability Zones | Geographic regions and isolated zones within regions. |
| [INF-HN-S17] | AWS — What is Amazon VPC? | Virtual networks, subnets, addresses, and routing. |
| [INF-HN-S18] | AWS — What is AWS Client VPN? | Encrypted remote access to private network resources. |
| [INF-HN-S19] | Microsoft Learn — What is a private endpoint? | Private-address access from a virtual network to a service. |
| [INF-HN-S20] | AWS — Control traffic to your AWS resources using security groups | Network access rules by source, destination, protocol, and port. |
| [INF-HN-S21] | Cloudflare — What is a WAF? Web Application Firewall explained | HTTP request inspection and filtering. |
| [INF-HN-S22] | Cloudflare WAF — Rate limiting rules | Request counting, time periods, and actions at a limit. |
| [INF-HN-S23] | MDN — Redirections in HTTP | Changing the requested URL; old addresses; HTTPS redirects. |
| [INF-HN-S24] | MDN — HTTP caching | Reusing saved responses; freshness and shared caches. |
| [INF-HN-S25] | Cloudflare — What is DDoS mitigation? | Detecting, filtering, and absorbing attack traffic. |

[INF-HN-S01]: https://aws.amazon.com/what-is/web-hosting/
[INF-HN-S02]: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
[INF-HN-S03]: https://aws.amazon.com/compare/the-difference-between-containers-and-virtual-machines/
[INF-HN-S04]: https://kubernetes.io/docs/concepts/overview/
[INF-HN-S05]: https://aws.amazon.com/what-is/serverless-computing/
[INF-HN-S06]: https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/
[INF-HN-S07]: https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-subdomain/
[INF-HN-S08]: https://www.cloudflare.com/learning/dns/what-is-dns/
[INF-HN-S09]: https://www.cloudflare.com/learning/dns/dns-records/
[INF-HN-S10]: https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Transport_Layer_Security
[INF-HN-S11]: https://letsencrypt.org/docs/integration-guide/
[INF-HN-S12]: https://www.cloudflare.com/learning/cdn/what-is-a-cdn/
[INF-HN-S13]: https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/
[INF-HN-S14]: https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html
[INF-HN-S15]: https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html
[INF-HN-S16]: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions-availability-zones.html
[INF-HN-S17]: https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
[INF-HN-S18]: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html
[INF-HN-S19]: https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview
[INF-HN-S20]: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html
[INF-HN-S21]: https://www.cloudflare.com/learning/ddos/glossary/web-application-firewall-waf/
[INF-HN-S22]: https://developers.cloudflare.com/waf/rate-limiting-rules/
[INF-HN-S23]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Redirections
[INF-HN-S24]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching
[INF-HN-S25]: https://www.cloudflare.com/learning/ddos/ddos-mitigation/
