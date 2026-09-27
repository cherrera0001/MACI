#!/bin/bash
# Setup Cloudflare DNS for maci.c4a.cl
# Usage: bash 03_SCRIPTS/setup_cloudflare_dns.sh

set -e

# Load environment
if [ ! -f .env.cloudflare ]; then
    echo "ERROR: .env.cloudflare not found"
    echo "Copy .env.cloudflare.example to .env.cloudflare and fill in your credentials"
    exit 1
fi

source .env.cloudflare

# Validate required variables
for var in CLOUDFLARE_API_TOKEN CLOUDFLARE_ACCOUNT_ID CLOUDFLARE_ZONE_ID; do
    if [ -z "${!var}" ]; then
        echo "ERROR: $var not set in .env.cloudflare"
        exit 1
    fi
done

echo "=== Cloudflare DNS Configuration ==="
echo "Zone ID: $CLOUDFLARE_ZONE_ID"
echo "Creating CNAME record: maci.c4a.cl → cname.vercel.app"
echo ""

# Create CNAME record
RESPONSE=$(curl -s -X POST "https://api.cloudflare.com/client/v4/zones/$CLOUDFLARE_ZONE_ID/dns_records" \
  -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "CNAME",
    "name": "maci",
    "content": "cname.vercel.app",
    "ttl": 0,
    "proxied": false
  }')

# Check response
if echo "$RESPONSE" | grep -q '"success":true'; then
    echo "✅ DNS record created successfully"
    echo ""
    echo "Details:"
    echo "$RESPONSE" | jq '.result | {id, type, name, content, ttl, proxied}'
    echo ""
    echo "Status: Propagation may take 5-15 minutes"
    echo "Verify: nslookup maci.c4a.cl"
else
    echo "❌ Failed to create DNS record"
    echo "$RESPONSE" | jq '.'
    exit 1
fi
