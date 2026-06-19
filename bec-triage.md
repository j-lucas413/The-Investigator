# BEC Triage — Meridian Group wire-transfer email

## Verdict
**Spoofed (external impersonation). Confidence: ~95% — high.**

The email was not sent from Meridian Group's mail infrastructure.
It was composed through a personal Gmail account and relayed via
Google's servers from an IP address (41.223.57.188) geolocating to a
Nigerian ISP — not Singapore, where the sender claims to be. All three
cryptographic/policy email-authentication checks fail simultaneously,
which is the strongest technical signal possible that the From address
has been forged. The presence of a Reply-To pointing to a disposable
Gmail account is not a mistake — it is the core fraud mechanism.

---

## Red flags found

### Technical (headers)
- **DKIM fail** — the email carries no valid cryptographic signature
  from meridiangroup.com. Any legitimate email sent from Marcus Webb's
  corporate account would pass this. Failure proves the message did not
  originate from Meridian's mail server.
- **SPF softfail** — Meridian's DNS does not authorize Gmail
  (209.85.208.201) to send on its behalf. The domain itself is
  declaring "we didn't send this."
- **DMARC fail (p=none)** — both SPF and DKIM failed alignment, so
  DMARC fails too. The `p=none` policy meant the mail was delivered
  anyway (monitor-only, no enforcement) — a gap the attacker likely
  checked for in advance.
- **Reply-To: mwebb.ceo2026@gmail.com** — the From address displays
  the CEO's corporate address, but any reply silently routes to an
  attacker-controlled Gmail inbox. The real Marcus Webb would never
  see Sandra's response. This is the defining mechanic of BEC fraud.
- **Originating IP 41.223.57.188** — this IP block is allocated to
  Nigeria (AFRINIC), not Singapore. The internal hop shows a private
  LAN device (192.168.43.7) behind a consumer router, consistent with
  a personal laptop or phone, not corporate infrastructure.

### Behavioral (email body)
- **Urgency** — "immediately," "hard deadline of 5 PM today," time
  pressure engineered to bypass deliberate decision-making.
- **Secrecy** — "Do not discuss this with anyone else on the team."
  This instruction exists specifically to prevent Sandra from reaching
  a colleague who might question the request or verify independently.
- **Authority** — impersonating the CEO ensures the target feels
  unable to push back or escalate without seeming insubordinate.
- **Isolation/unavailability** — "in meetings in Singapore and cannot
  be reached by phone until Monday" pre-empts the most obvious
  verification step (calling the boss back).
- **New, unverified payee** — Apex Consulting Group and First National
  Bank of Nevada are not established vendors; the account number has
  never been used before.
- **Plausible cover story** — "confidential acquisition" is
  sophisticated social engineering; it gives Sandra a reason to feel
  the secrecy is legitimate rather than suspicious.

---

## Verification steps — checked against raw headers

The AI's analysis was checked point-by-point against the raw headers:

| Claim | Verified? | Notes |
|---|---|---|
| DKIM = fail | ✅ | `dkim=fail (signature did not verify)` — exact match |
| SPF = softfail | ✅ | `spf=softfail (domain of transitioning sender)` — exact match |
| DMARC = fail, p=none | ✅ | `dmarc=fail (p=none) header.from=meridiangroup.com` — exact match |
| Reply-To is Gmail | ✅ | `Reply-To: mwebb.ceo2026@gmail.com` — confirmed in headers |
| Origin IP 41.223.57.188 | ✅ | Present in `X-Originating-IP` and `Received` chain |
| Routed through Gmail | ✅ | `mail-lj1-f201.google.com` in Received header |
| IP is Nigerian ISP | ⚠️ | Geolocation is probabilistic; 41.223.x.x is an AFRINIC block; a VPN could spoof this. Confirmed as not Meridian infrastructure regardless. |

No fabricated claims were found. The one item requiring independent
verification is the IP geolocation, which should be confirmed via
AFRINIC WHOIS or a threat-intel platform before being cited formally.
Even without geolocation, the combination of all other failures is
sufficient to block the transfer.

---

## Verification checklist (before wiring money)

1. **Call the requester on a known, pre-existing number** — not a
   number from the email, not a callback number the caller provides.
   Use the corporate directory or a number saved before this request
   arrived. If unreachable, treat that as a red flag, not a reason
   to proceed.

2. **Check email authentication headers** — view full/raw headers and
   confirm SPF, DKIM, and DMARC all pass. Any combination of failures
   on a financial request is a stop signal.

3. **Verify the Reply-To matches the From domain** — a From address
   at the company domain paired with a Reply-To at Gmail or any
   external service is a hard stop.

4. **Require a second approver for any new payee or wire above
   threshold** — no single person should be able to authorize a wire
   to an account not already in the approved vendor list.

5. **Confirm the payee through an independent source** — look up
   "Apex Consulting Group" and "First National Bank of Nevada" through
   official channels (state registry, known company contact page), not
   through links or numbers in the email.

6. **Never treat secrecy instructions as legitimate** — any request
   that tells you not to involve a colleague or manager before moving
   money is a behavioral red flag, not a policy to follow.

7. **When in doubt, delay** — a real CEO will understand a 24-hour
   hold for verification. An attacker will pressure, escalate, and
   invent new urgency. That escalation is itself evidence of fraud.

---

## Extend the method — what changes for vishing (voice phishing)?

In a vishing attack there are no headers to inspect — SPF, DKIM,
DMARC, and Reply-To analysis all become unavailable. However, the
behavioral checklist is channel-agnostic and still works:

- **Steps 1, 4, 5, 6, and 7 still apply** — call the requester back
  on a known number (not the one that just called you), require a
  second approver, verify the payee independently, treat secrecy
  instructions as a red flag, and use delay as a defense.
- **Step 2 and 3 do not apply** — there are no headers on a phone call.

The technical controls protect against spoofed email; the procedural
controls protect against everything else. This is why the checklist
must cover both layers.

---

## 30-minute response — ordered actions

**The wire deadline is 4:47 PM. You have until 5:00 PM.**

1. **Immediately contact Sandra and place a hold on the transfer** —
   before anything else, ensure no one processes the wire while
   investigation is underway. One sentence to Sandra: "Hold everything,
   do not send — I need five minutes."

2. **Reach Marcus Webb through a trusted, out-of-band channel** —
   call his known personal cell or have someone physically locate him.
   Do not reply to this email (Reply-To routes to the attacker). If he
   confirms the request is legitimate, you have your answer. If he
   can't be reached, the transfer does not go out.

3. **Alert your security team and finance manager** — forward the full
   raw headers as evidence, flag this as an active BEC attempt, and
   ensure the incident is logged. If Marcus cannot be reached and the
   5 PM deadline passes, a real vendor relationship will survive a
   one-business-day delay. $84,000 sent to a fraud account will not
   be recovered.

> Replying to the email at any point is not a verification step —
> the Reply-To goes directly to the attacker.
