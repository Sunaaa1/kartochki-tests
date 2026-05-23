CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT,
    name TEXT NOT NULL,
    google_sub TEXT UNIQUE,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE,
    email_verified_at TIMESTAMP,
    email_verification_token_hash TEXT,
    email_verification_expires_at TIMESTAMP,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS organizations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    slug TEXT NOT NULL UNIQUE,
    plan TEXT NOT NULL DEFAULT 'free',
    credits_remaining INTEGER NOT NULL DEFAULT 10,
    credits_purchased INTEGER NOT NULL DEFAULT 0,
    credits_used INTEGER NOT NULL DEFAULT 0,
    balance_usd_cents INTEGER NOT NULL DEFAULT 0,
    balance_rub_kopecks INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS org_members (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    user_id UUID,
    role TEXT NOT NULL DEFAULT 'member',
    invited_email TEXT,
    invite_token TEXT,
    invite_expires_at TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'active',
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID REFERENCES organizations(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    image_storage_path TEXT,
    processed_image_url TEXT,
    processed_image_storage_path TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    marketplace TEXT NOT NULL,
    brand_id UUID,
    seo_title TEXT,
    description TEXT,
    attributes JSONB,
    category_id TEXT,
    keywords TEXT[] DEFAULT '{}',
    bullet_points JSONB,
    marketplace_data JSONB,
    custom_prompt TEXT,
    error_message TEXT,
    additional_images TEXT[] DEFAULT '{}',
    bg_removed_images TEXT[] DEFAULT '{}',
    exported_at TIMESTAMP,
    exported_to TEXT,
    is_exported BOOLEAN DEFAULT FALSE,
    wb_sync_status TEXT DEFAULT 'none',
    wb_nomenclature_id TEXT,
    wb_published_at TIMESTAMP,
    wb_sync_error TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    product_id UUID NOT NULL,
    status TEXT NOT NULL DEFAULT 'queued',
    progress INTEGER NOT NULL DEFAULT 0,
    error_message TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS credit_transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    amount INTEGER NOT NULL,
    type TEXT NOT NULL,
    description TEXT NOT NULL,
    product_id UUID,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS balance_transactions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    org_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
    currency TEXT NOT NULL,
    amount_cents INTEGER NOT NULL,
    type TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'completed',
    description TEXT NOT NULL,
    payment_provider TEXT,
    payment_id TEXT,
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);