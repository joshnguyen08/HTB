<img src="./assets/banner.png" style="max-width: 100%;" align=left />

# Template Writeup
8<sup>th</sup> February 2025

Prepared by: joshnguyen08		

Machine Author(s): joshnguyen08

Difficulty:<font color="Green">Easy</font> 

## Scenario
```
You are a cybersecurity analyst for a U.S.-based managed service provider (MSP) that uses Versa Director to manage client networks.

A recent security alert indicates suspicious activity on your Versa Director servers, with signs of zero-day exploitation and credential theft.

Your manager suspects Volt Typhoon is behind the attack, and you must investigate their tactics using MITRE ATT&CK to assess the breach and recommend mitigations.

```

## Initial Analysis

We are tasked with investigating Volt Typhoon, a China-based APT known for targeting U.S. critical infrastructure. The group primarily uses zero-day exploits, proxy-based C2, and living-off-the-land (LOTL) techniques to evade detection.

As a cyber threat intelligence analyst, your objective is to analyze Volt Typhoon’s tactics using MITRE ATT&CK, focusing on their recent Versa Director Zero-Day Exploitation campaign (August 2024).

We will use this source: https://attack.mitre.org/groups/G1017/ to perform our research on the APT.

## Questions 


1. What is the MITRE ATT&CK ID of the group associated with the Versa Director Zero Day Exploitation campaign?
 `G1017`
2. When did this group first appear / became active?
 `2021`
3. Which technique does Volt Typhoon use to execute commands stealthily without deploying traditional malware?
 `LOLBins`
4. Alongside zero-day vulnerabilities for initial access, Volt Typhoon exploits multiple internet-facing software and appliances such as?
 `Fortinet, Ivanti (Pulse Secure), NETGEAR, Citrix, Cisco`
5. Volt Typhoon routes malicious traffic through multiple intermediary devices before reaching its final target. What is the MITRE ATT&CK technique ID for this multi-hop proxy behavior?
 `T1090.003`
6. In the Lockheed Martin Cyber Kill Chain model, which phase does Volt Typhoon’s multi-hop proxy (T1090.003) fall under?
 `Command and Control`
7. Instead of deploying traditional malware, Volt Typhoon uses built-in system utilities for post-compromise activity. What is the MITRE ATT&CK technique ID for this approach?
 `T1218`
8. What technique did Volt Typhoon use to maintain persistence by modifying network settings on compromised devices?
 `T1090.001`
9. According to MITRE ATT&CK, Volt Typhoon was last seen in August 2024 conducting a campaign, what was the campaign called?
 `Versa Director Zero Day Exploitation`
10. What CVE did Volt Typhoon exploit in the latest campaign in question 9?
 `CVE-2024-39717`
11. What is the name of the Java Archive (JAR) file deployed by Volt Typhoon to capture credentials after exploiting Versa Director?
 `VersaMem`
12. Where did this JAR file capture local credentials?
 `/tmp/.temp.data`
13. Volt Typhoon attempts to extract credentials from three common password storage locations on compromised systems. Name them. 
 `OpenSSH, realvnc, and PuTTY`

