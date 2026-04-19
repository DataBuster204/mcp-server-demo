# MCP Server Demo — Secure Multi-Tenant Financial Data Layer

Built by [Olumide Daramola](https://olumidedaramola.dev)

## What this is

A working Model Context Protocol (MCP) server that exposes financial GL data 
as structured, scoped tools for AI agents — with token-based authentication 
and strict per-customer data isolation.

Built to demonstrate the exact architecture required for agentic AI middleware 
over sensitive financial data.

---

## What it demonstrates

- **MCP server** built with FastMCP (Anthropic's Python SDK)
- **Multi-tenant data isolation** — each customer only accesses their own data
- **Token-based auth** — customer identity resolved server-side from API tokens
- **Tool discovery** — AI clients discover and call tools dynamically
- **Security boundary** — invalid tokens rejected before any data is touched

---

## Project Structure

| File | Purpose |
|---|---|
| `server.py` | MCP server — exposes GL lookup and financial summary tools |
| `database.py` | Simulated multi-tenant database with per-customer GL data |
| `auth.py` | Token resolution layer — maps API tokens to customer IDs |
| `test_client.py` | Python MCP client — tests all tools including auth rejection |

---

## How it works