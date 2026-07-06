# Ransomware Incident Response Runbook
 
Organized around NIST SP 800-61 phases. Steps are checkable — mark `[x]` as completed. Adapt to your environment; assign an Incident Commander (IC) before execution begins.
 
---
 
## 1. Preparation
 
- [ ] 1.1 Maintain an offline/immutable backup strategy (3-2-1 rule) with regular restore testing.
- [ ] 1.2 Maintain an up-to-date asset inventory and network diagram, including data classification.
- [ ] 1.3 Define and staff an Incident Response Team (IR lead, IT/infra, legal, comms, HR, executive sponsor).
- [ ] 1.4 Establish 24/7 contact tree and escalation paths (internal + external: law enforcement, cyber insurer, outside counsel, IR retainer/vendor).
- [ ] 1.5 Pre-stage IR tooling: EDR/AV, forensic imaging tools, log aggregation (SIEM), isolated "clean" jump-host, out-of-band communication channel (e.g., Signal, phone tree) in case corporate email/chat is compromised.
- [ ] 1.6 Document and test an IR plan and this runbook via tabletop exercises at least annually.
- [ ] 1.7 Ensure logging is centralized, retained (≥90 days), and time-synchronized (NTP) across endpoints, servers, network devices, identity provider (AD/Entra), and cloud services.
- [ ] 1.8 Harden identity: enforce MFA everywhere, especially for VPN, admin, and email accounts; review privileged account inventory.
- [ ] 1.9 Confirm cyber insurance policy details, breach notification obligations, and legal/regulatory requirements (e.g., state breach laws, GDPR, HIPAA, SEC).
- [ ] 1.10 Pre-approve a communications template (customers, employees, regulators, press) for ransomware scenarios.
---
 
## 2. Detection & Analysis
 
- [ ] 2.1 Validate the alert/report (EDR detection, ransom note, encrypted files, help-desk reports, unusual outbound traffic).
- [ ] 2.2 Declare an incident and activate the IR team; assign an Incident Commander.
- [ ] 2.3 Establish the secure out-of-band communication channel immediately (assume email/chat may be compromised or monitored by the attacker).
- [ ] 2.4 Determine scope: which hosts, users, shares, and business services are affected. Check for lateral spread indicators (new admin accounts, disabled EDR/AV, mass file modification events).
- [ ] 2.5 Identify the ransomware family if possible (ransom note text, file extension, ID-ransomware/known IOCs) — informs known TTPs, decryptor availability, and whether data exfiltration is a known behavior of this group.
- [ ] 2.6 Preserve volatile evidence before powering off systems: memory captures, running process lists, network connections, scheduled tasks, and relevant logs.
- [ ] 2.7 Identify initial access vector and timeline (phishing, exposed RDP, VPN compromise, vulnerable public-facing app, supply chain).
- [ ] 2.8 Determine whether data was exfiltrated (large/unusual outbound transfers, staging directories, cloud storage/file-sharing tool usage, dark-web leak-site monitoring).
- [ ] 2.9 Classify severity/impact (systems down, data confidentiality, regulatory triggers, safety impact) and notify executive leadership and legal counsel.
- [ ] 2.10 Engage external IR firm and/or law enforcement (FBI/CISA or local equivalent) if not already engaged, per pre-established criteria.
- [ ] 2.11 Begin an incident timeline/log documenting every action taken, by whom, and when (for legal, insurance, and lessons-learned purposes).
---
 
## 3. Containment, Eradication & Recovery
 
### 3a. Containment
- [ ] 3.1 Isolate affected hosts from the network (disable network adapters, pull from switch, or use EDR network-isolation feature) — avoid powering off unless memory capture is complete or not feasible.
- [ ] 3.2 Disable or reset credentials for compromised/suspicious accounts, especially privileged and service accounts.
- [ ] 3.3 Block known malicious IOCs (IPs, domains, hashes) at firewall/proxy/EDR.
- [ ] 3.4 Segment or disable affected network segments/VLANs to halt lateral movement.
- [ ] 3.5 Disable remote access services if implicated (RDP, VPN) or enforce MFA immediately if not already required.
- [ ] 3.6 Preserve (do not delete) ransom notes, encrypted samples, and any attacker communication for forensics and negotiation/legal review.
- [ ] 3.7 Verify backup integrity and isolate backups further if not already offline/immutable — confirm backups themselves are not encrypted or compromised.
### 3b. Eradication
- [ ] 3.8 Identify and remove attacker persistence mechanisms (scheduled tasks, new services, registry run keys, web shells, rogue accounts).
- [ ] 3.9 Patch or remediate the confirmed initial access vector (e.g., patch vulnerability, close exposed RDP, revoke compromised credentials).
- [ ] 3.10 Rebuild compromised systems from known-good/gold images where feasible rather than "cleaning" in place.
- [ ] 3.11 Rotate all credentials domain-wide if broad compromise (especially krbtgt/AD, admin, and service accounts) is suspected.
- [ ] 3.12 Re-scan environment with EDR/AV and threat-hunt for remaining IOCs before reconnecting systems.
### 3c. Recovery
- [ ] 3.13 Decide on restoration path: restore from clean backups (preferred) vs. decryption tool (if available and vetted) vs. ransom payment (last resort, subject to legal/insurance/OFAC sanctions review).
- [ ] 3.14 Restore systems in priority order per business impact analysis; validate integrity before returning to production.
- [ ] 3.15 Reconnect systems incrementally with heightened monitoring; watch for reinfection or dwell-time attacker activity.
- [ ] 3.16 Confirm business services function correctly and data integrity is verified (checksums, application-level validation) before declaring recovery complete.
- [ ] 3.17 Communicate recovery status to stakeholders, customers, and regulators per legal guidance and communication plan.
---
 
## 4. Post-Incident Activity
 
- [ ] 4.1 Conduct a formal after-action review / lessons-learned meeting with all stakeholders within 1–2 weeks of recovery.
- [ ] 4.2 Finalize the incident timeline and root-cause analysis; document initial access vector, dwell time, and scope.
- [ ] 4.3 Update IR plan, runbooks, and playbooks based on identified gaps.
- [ ] 4.4 Complete all required regulatory, contractual, and insurance breach notifications and reporting.
- [ ] 4.5 Track remediation action items to closure (patching, architecture changes, policy updates, additional monitoring) with owners and deadlines.
- [ ] 4.6 Update detection rules/IOCs in SIEM/EDR based on attacker TTPs observed.
- [ ] 4.7 Reassess backup strategy, segmentation, and privileged access model in light of findings.
- [ ] 4.8 Retain forensic evidence and documentation per legal/insurance retention requirements.
- [ ] 4.9 Brief executive leadership/board on incident summary, cost, and risk-reduction roadmap.
- [ ] 4.10 Schedule a tabletop exercise to validate updated runbook within 3–6 months.
---
 
*This runbook is a general template. Validate legal, regulatory, and insurance obligations with counsel, and tailor technical steps to your specific environment.*