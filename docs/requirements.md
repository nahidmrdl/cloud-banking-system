# Cloud Based Banking System: Requirements Specification

## 1. Overview
The **Cloud Based Banking System** is a modular and scalable banking application that simulates real-world banking operations. It uses modern software engineering practices.
It allows users to manage their bank accounts, perform transactions, and view their transaction history. All are securely stored in a **Supabase** cloud database.
The system is mainly built with **Python (OOP principles)** and prioritizes clean architecture, cloud integration, and extensibility for GUI or web interfaces.

---

## 2. Objectives
- Realistic simulation of banking operations (accounts, deposits, withdrawals, transfers)
- Demonstrate **Object-Oriented Programming (OOP)** concepts:
  - Encapsulation, Inheritance, Polymorphism, and Abstraction.
- Implement **secure authentication** using **Supabase Auth**.
- Must maintain modular, testable, and extensible design for future GUI or web integration.
- Store and manage all data securely in the cloud.

---

## 3. Stakeholders
| Role | Description |
|------|--------------|
|**Customer** | End user who manages bank accounts and their transactions. |
| **Admin** | System administrator with permissions to view and manage all users and accounts. |
| **Developer** | Maintains, extends, and deploys the system. |

---

## 4. Functional Requirements (FR)

### 4.1 User Management
- **FR1:** Users can register using email and password.
- **FR2:** Users can securely log in and log out.
- **FR3:** Admins can view, update, or delete user information.
- **FR4:** System must use **Supabase Auth** for all authentication processes.

### 4.2 Account Management
- **FR5:** A user can create multiple account types (e.g., Savings, Checking).
- **FR6:** Each account must have a unique ID, type, and current balance.
- **FR7:** Admins can view all user accounts in the system.
- **FR8:** Accounts must support interest rates or overdraft features (depending on type).

### 4.3 Transaction Management
- **FR9:** Users can perform deposits, withdrawals, and transfers between accounts.
- **FR10:** Each transaction must be logged with a timestamp, type, and description.
- **FR11:** Users can view transaction history for any of their accounts.
- **FR12:** The system must ensure balance validation before processing transactions.

### 4.4 Data Persistence
- **FR13:** All data must be persisted in Supabase (PostgreSQL backend).
- **FR14:** CRUD operations must be performed via Supabase SDK, not raw SQL.
- **FR15:** The system should handle network failures gracefully (retry or rollback).

### 4.5 Reporting (Future Plans)
- **FR16:** The system can generate account summaries or transaction reports.
- **FR17:** Reports can be exported as PDF or displayed as charts.

---

## 5. Non-Functional Requirements
| Type | Description |
|------|--------------|
| **Security** | Use Supabase Auth for secure login and data access; credentials must never be stored in plaintext. |
| **Scalability** | Must support multiple users and accounts without performance degradation. |
| **Maintainability** | Code should follow SOLID OOP principles and use modular structure. |
| **Reliability** | Transactions must be atomic — either fully completed or fully rolled back. |
| **Portability** | Must run locally via CLI and be extendable for GUI or web deployment. |
| **Usability** | Simple CLI interface for initial testing; intuitive and clear prompts. |
| **Availability** | Requires internet connectivity to communicate with Supabase backend. |

---

## 6. System Constraints
- **Python 3.10+** required.
- **Supabase** project (PostgreSQL + Auth) must be configured and accessible.
- All environment variables (`SUPABASE_URL`, `SUPABASE_ANON_KEY`, `SUPABASE_SERVICE_ROLE_KEY`) must be set in `.env`.
- The system must not expose service keys in the source code or repository.

---

## 7. Use Case Summary

| ID | Use Case | Actor | Description |
|----|-----------|--------|-------------|
| **UC1** | Register | Customer | Create a new account using email and password. |
| **UC2** | Login | Customer / Admin | Authenticate user with Supabase Auth. |
| **UC3** | Create Account | Customer | Open a new bank account (Savings or Checking). |
| **UC4** | Deposit Funds | Customer | Add money to an existing account. |
| **UC5** | Withdraw Funds | Customer | Withdraw funds if sufficient balance exists. |
| **UC6** | Transfer Funds | Customer | Transfer funds between user’s accounts. |
| **UC7** | View Transaction History | Customer | Display past transactions for an account. |
| **UC8** | Manage Users | Admin | View or remove user accounts. |
| **UC9** | View All Transactions | Admin | Access system-wide transaction logs. |

---

**Date:** *06/11/2025*  
**Version:** 1.0  
**Status:** Draft 