
### 2018-04-13T16:40:17+02:00

Conviction sur support data science Mini Hackathon pour Qcentral:

hackathons:
- hackathon preparation:
        - data mapping & context identification:
                - 2 days / hackathon: OPEX consultant or proxy PO
        - data cleaning & joining:
                - 5 days / hackathon: Data engineer
        - support to organization:
                - 3 days / hackathon * (N_pax / 20): OPEX consultant or Proxy PO
- hackathon:
        - 2 days / hackathon * (N_pax / 20): OPEX consultant or Proxy PO
        - 2 days / hackathon * (N_pax / 10): Data scientist

PoC teams support:
- algorithmic & coding coaching:
        - 1 day / week / PoC team (recom. 3 PAX) * N_weeks

Example:

4 hackathons of 40 people:
        - 32 days: OPEX consultant
        - 24 days: data scientist
        - 20 days: data engineer
10 teams doing 2 PoC of 8 weeks: 20 "8-weeks PoCs"
        - 640 days: data scientist

### 2018-04-19T10:09:24+02:00

Qcentral: brainsto & mini hackathon

Data from TechRequest:
- Not ingestable in Foundry (today, only data from repair for SRW) because of too sensitive information
- Build a database on COP or on PubliCloud.

- how to ingest data in Hubble (Explorer)
- eTLB Pareto Analysis: developped by the analytics accelerator / DTO. ==> text mining on project which could interest BK-RC.

--------------------
Dictionaries

Purpose
- UC1:
    - As an Airbus DS & Foundry user, I want to understand codes embedded in SAP data, thanks to a table of codes & their translation.
    - Value: SIQA tool (used in SA FAL in France) based on access will be out because of transition to G-suite. Useful for all tables.
- UC2:
    - As an Airbus DS, I want to do text mining easily, thanks a to a translation table of acronyms & their translation.
    - Value:

No direct value, those  use-cases are enablers.

Deliverables
- UC1:
    - Aggregate reference tables
    - Statistics on data quality
    - UI to be able to enter new codes
- UC2:
    - Comparison of dictionaries
    - Stop keywords
    - "Official" harmonized dictionary based on likelihood

Data sources
- UC1:
    - initial table (J. Wahl)
    - NC liability (N. Castet)
    - SCQWT: mapping supplier id - supplier names (Q. Chenevier - Capgemini Consulting)
    - Conquer (F. Neirot)
- UC2:
    - Data clustering (G. Martin)
    - eTLB/QLB text mining (F. Neirot)
    - RCA (J. Brousseau)

Team


--------------------
Inspections
