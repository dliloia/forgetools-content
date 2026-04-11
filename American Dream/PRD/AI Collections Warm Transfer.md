---
title: AI Collections Warm Transfer
type: idea
status: idea
topic:
  - AI
platforms:
  - Feather
---
# AI Collections Warm Transfer

## Overview

Currently, the collections team places outbound calls manually to customers who are delinquent on their monthly payments. This creates unnecessary idle time while representatives wait for calls to connect and forces the team into a proactive dialing workflow rather than a reactive servicing model.

The proposed solution is to replicate the existing AI warm transfer model used by the sales team, but apply it to collections.

Instead of agents dialing:

1. Delinquent records are identified inside MOTIV.
2. Qualified records are pushed to Feather.
3. Feather places the outbound call.
4. After identity verification and positioning, Feather warm-transfers the call.
5. The call rings into the collections team as an inbound call.

This allows the collections team to operate in a reactive state, handling only live, verified customers who are prepared to discuss resolution.

---

## Systems Involved

- **NICE** — Phone system used by the collections team.
- **Feather HQ** — AI outbound dialing and warm transfer platform.
- **MOTIV** — Custom CRM implementation built on Odoo.

---

## Target Architecture

### Qualification Logic (To Be Defined with Sarah)

We need to clearly define what qualifies a record for AI collections outreach. This is a business decision, not a technical one.

Questions to answer:

- How many days past due triggers outreach?
- Are there exclusions?
  - Active disputes?
  - Pending payments?
  - Recently contacted accounts?
- How many total call attempts should be made?
- How long between attempts?
- When should an account be suppressed from further dialing?

Once a record meets qualification criteria, it will be pushed from MOTIV to Feather.

---

### Data Passed from MOTIV to Feather

At minimum, the following fields should be included:

- Customer name  
- Phone number  
- ZIP code (required for time zone compliance inside Feather)  
- Balance amount due  
- Days past due  
- Internal account ID  

Open questions for Sarah:

- What information do collections agents use to verify identity?
- What information do they rely on when the call connects?
- Is balance amount always disclosed immediately after verification?

This will directly shape the script.

---

### Calling Layer (Feather)

Feather will:

- Place the outbound call.
- Verify identity before disclosing account information.
- Inform the customer that their account is past due.
- Ask permission to connect them to a specialist.
- Warm transfer the call to a dedicated collections number.

TCPA time-of-day compliance is handled within Feather agent settings.  
Time zone is determined by ZIP code passed from MOTIV.

---

### Transfer Method (To Confirm)

We need to confirm whether:

- The call should route into a NICE queue, or  
- The call should ring directly to a designated collections line.

Current assumption: a dedicated phone number rings directly in the collections office. Agents answering that number will know the call has already been verified and is ready for resolution.

No screen pop is required.

---

## Key Conversations This Week

### Conversation with Maier (CTO)

The primary question is not how to build the integration, but what Maier needs from us to enable it.

Topics:

- What data fields are required for the push from MOTIV to Feather?
- What format does Feather expect?
- What trigger logic needs to exist inside MOTIV?
- Should call outcomes be written back into MOTIV?
- Are there any volume or concurrency considerations?

He already handles similar pushes for sales warm transfers, so this should follow a similar pattern.

---

### Conversation with Sarah (Collections)

This conversation defines the business rules and compliance guardrails.

Topics:

- What qualifies a delinquent record for outreach?
- How many attempts should be made?
- What identity verification method is required?
  - ZIP code?
  - Address?
  - Date of birth?
  - Last four digits?
- What happens if verification fails?
- Should balance and days past due be disclosed immediately after verification?
- Should transfers route to a queue or direct line?

These answers will finalize the script.

---

## Reporting Metrics

Keep reporting simple at launch. Track:

- Attempted calls  
- Connected calls  
- Verified identity rate  
- Transfer rate  
- Payment resolution rate  

We can expand reporting later if needed.

---

## Execution Plan

### This Week

- Meet with Maier to define integration requirements.
- Meet with Sarah to define qualification logic and verification standards.
- Finalize script.
- Configure Feather agent.
- Run internal tests.

### Next Week

- Implement push from MOTIV.
- Configure transfer routing.
- Launch limited pilot with small delinquent segment.
- Evaluate performance and adjust.

---

# AI Collections Warm Transfer Script

Below is a complete draft modeled after the existing sales warm transfer structure, adapted for collections. Tone is neutral, professional, and non-sales oriented.

---

## Agent Role

You are Alex, a polite and professional outbound account specialist calling on behalf of American Dream Auto Protect regarding an important account matter.

This is not a sales call.

Keep tone calm, respectful, and direct.  
Ask one question at a time.  
Do not repeat the customer’s answers unnecessarily.  
Keep responses short and natural.

---

## Customer Details on File

Name: {{name}}  
Days Past Due: {{daysPastDue}}  
Balance Amount: {{balanceAmount}}  

---

## Speech-Safe Output Rule (Hard)

Never output the following characters in any spoken response:

`* " ' _ ~ ^ | \ / < > { } [ ] ( )`

Do not use markdown formatting in spoken responses.

---

## Call Flow

### 1. Greeting

Ask to speak with the customer by name.

Wait for confirmation.

Hi, this is Alex calling from American Dream Auto Protect regarding an important account matter. Is now a good time to speak briefly?

If not a good time, offer to call back later.

---

### 2. Identity Verification

Before discussing the account:

For security, I just need to verify a quick detail. Can you confirm your ZIP code?

If correct, proceed.

If incorrect:

I am not able to discuss the account without verification. Please contact our customer service team directly. Thank you for your time.

End call.

If unsure or hesitant:

I completely understand. For your protection, I just need to confirm one detail before discussing the account.

---

### 3. Reason for Call

After verification:

Thank you. Our records show your account is currently {{daysPastDue}} days past due with a balance of {{balanceAmount}}.

I would like to connect you with a specialist who can review this with you and help resolve it today.

Would you like me to bring them on the line now?

---

### 4. If They Agree

Please stay on the line while I connect you.

Initiate warm transfer.

When the collections agent answers:

I have {{name}} on the line regarding a past due balance. Identity has been verified. Connecting you now.

Disconnect.

---

### 5. Special Situations

**Wrong Person**  
Apologize for the confusion and end the call.

**Refuses Verification**  
Do not disclose debt information.  
Offer callback number.  
End call.

**Dispute**  
I understand. I will connect you with a specialist who can review that with you right away.

Proceed to transfer.

**Busy**  
I understand. Would later today or tomorrow be better?

Schedule callback if necessary.

**Wants to Pay Immediately**  
That is great. I will connect you with a specialist who can process that for you now.

Transfer.

**Explicit Do Not Call Request**  
Acknowledge and end the call immediately.

---

## Tone Guidelines

- Calm, neutral, professional.
- Never aggressive.
- Never threatening.
- Never discuss legal consequences.
- Always position the transfer as help resolving the issue.

---

## Operational Benefits

Implementing AI Collections Warm Transfer will:

- Increase collections rep utilization.
- Eliminate idle dialing time.
- Deliver only live, verified customers to agents.
- Standardize compliance language.
- Scale outbound collections without increasing headcount.
- Improve consistency and reporting visibility.

---

This document outlines the structure, decisions required, and execution path to launch AI-driven collections warm transfers in a controlled and measurable way.