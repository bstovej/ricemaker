This document is an excerpt from the **CrowdStrike 2024 Global Threat Report**. It details significant shifts in cyber adversary behavior throughout 2023, focusing on cloud exploitation, supply chain attacks, and the intersection of geopolitics and cyber warfare.

The following are the key insights and facts categorized by theme:

### 1. The Surge in Cloud-Targeted Attacks
The report highlights a massive increase in attacks targeting cloud environments, characterized by a shift toward "cloud-conscious" adversaries.

*   **Key Statistics:**
    *   **75% increase** in overall cloud environment intrusions from 2022 to 2023.
    *   **110% increase** in "cloud-conscious" cases (attackers who actively exploit cloud-specific features).
    *   **60% increase** in "cloud-agnostic" cases (attackers who compromise cloud environments but don't specifically target cloud features).
*   **Adversary Profiles:** 
    *   **eCrime actors** are the primary drivers, accounting for **84%** of cloud-conscious intrusions.
    *   **SCATTERED SPIDER** is a dominant threat, responsible for **29%** of total cloud-conscious cases, using sophisticated techniques for persistence and lateral movement.
*   **Tactical Trends:** Attackers are moving away from traditional endpoints and focusing on **identity-based techniques** (e.g., abusing Entra ID, Okta, and Azure Key Vault) to maintain access and escalate privileges.

### 2. Third-Party and Supply Chain Exploitation
Adversaries are increasingly targeting the "trusted relationships" between vendors and clients to achieve massive scale with minimal effort.

*   **High ROI Strategy:** Compromising a single software vendor or IT service provider allows an attacker to reach hundreds or thousands of downstream targets simultaneously.
*    **China-Nexus Activity:** 
    *   **JACKPOT PANDA and CASCADE PANDA** targeted Chinese-speaking victims through trojanized software and "actor-in-the-middle" attacks on legitimate update traffic.
    *   Other actors linked to China-nexus groups (e.g., **WET PANDA**) have compromised software vendors in India to distribute malware globally.
*   **North Korea (DPRK) Activity:**
    *   **LABYRINTH CHOLLIMA** demonstrated high proficiency in supply chain attacks, specifically targeting software like **3CX (VoIP)** and **CyberLink (media player)** to deploy malware.
*   **Sector Risk:** The **technology sector** is at the highest risk, as nearly all identified third-party compromises in 2023 originated from intrusions into commercial software providers.

### 3. The Vulnerability Landscape: "Under the Radar"
As organizations improve visibility on managed endpoints (laptops/servers) via EDR (Endpoint Detection and Response), attackers are shifting to unmanaged network periphery.

*   **Primary Targets:** Unmanaged network appliances, specifically **Edge Gateway devices** (firewalls and VPNs), are the most frequent initial access vectors.
*   **Exploited Vendors:** Notable vulnerabilities were exploited in **Cisco, Citrix, F5, and Ivanti** products.
*   **The EOL Threat:** Attackers are actively developing exploits for **End-of-Life (EOL) products** because these legacy systems cannot be patched and often lack modern security sensors.

### 4. Geopolitical Conflict: The Israel-Hamas Cyber War
The report analyzes the cyber dimension of the 2023 Israel-Hamas conflict, noting a focus on disruption and psychological influence.

*   **Nature of Operations:** Activity primarily consists of **DDoS attacks**, **destructive wipers**, and **"hack-and-leak"** operations.
*   **Faketivism vs. Hacktivism:** The report introduces the concept of **"Faketivism"**—inauthentic personas created by state-nexus actors to mimic hacktivists, providing state governments with plausible deniability.
*   **Key Actors:** 
    *   Groups like **Cyber Av3ngers** and **Rights Seekers** (pro-Iranian) targeted critical infrastructure and warning systems.
    *   **Hamas-nexus groups** (e.g., **RENEGADE JACKAL**) were active, though their impact was significantly hindered by the degradation of internet and power infrastructure in the Gaza Strip.

### Summary Table of Notable Adversaries
| Adversary Group | Primary Focus/Tactic |
| :--- | :--- |
| **SCATTERED SPIDER** | Cloud-conscious identity theft, lateral movement, and data exfiltration. |
| **JACKPOT PANDA** | Supply chain compromise via trojanized installers (e.g., CloudChat). |
| **LABYRINTH CHOLLIMA** | High-scale supply chain attacks via trusted software vendors (e.g., 3CX). |
| **Cyber Av3ngers** | Targeting critical infrastructure and ICS (Industrial Control Systems). |
| **Akira Ransomware** | Exploiting vulnerabilities in backup infrastructure (Veeam). |