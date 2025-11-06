-- ==========================================
-- CLOUD-BASED BANKING SYSTEM DATABASE SCHEMA
-- ==========================================

-- Date: 2025-11-06
-- Version: 1.0

-- Description:
--   This schema defines the relational model for the
--   Cloud-Based Banking System.
-- ==========================================

-- =====================
-- TABLE: users
-- =====================
CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role VARCHAR(20) DEFAULT 'customer' CHECK (role IN ('customer', 'admin')),
    created_at TIMESTAMP DEFAULT NOW()
);

-- =====================
-- TABLE: accounts
-- =====================
CREATE TABLE IF NOT EXISTS accounts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    type VARCHAR(20) NOT NULL CHECK (type IN ('savings', 'checking')),
    balance NUMERIC(12, 2) DEFAULT 0.00 CHECK (balance >= 0),
    interest_rate NUMERIC(5, 2), 
    overdraft_limit NUMERIC(12, 2),
    created_at TIMESTAMP DEFAULT NOW() 
);

-- =====================
-- TABLE: transactions
-- =====================
CREATE TABLE IF NOT EXISTS transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    account_id UUID NOT NULL REFERENCES accounts(id) ON DELETE CASCADE,
    type VARCHAR(20) NOT NULL CHECK (type IN ('deposit', 'withdrawal', 'transfer')),
    amount NUMERIC(12, 2) NOT NULL CHECK (amount > 0),
    timestamp TIMESTAMP DEFAULT NOW(),
    description TEXT
);

-- =====================
-- INDEXES
-- =====================
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_accounts_user_id ON accounts(user_id);
CREATE INDEX IF NOT EXISTS idx_transactions_account_id ON transactions(account_id);