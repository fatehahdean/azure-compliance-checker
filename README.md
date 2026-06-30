# Azure Compliance Checker

A Python tool that connects to a live Microsoft Azure subscription and performs basic governance and compliance checks.

## What it does
- Connects to Azure using CLI credentials
- Checks all resource groups for tagging compliance
- Lists all Virtual Machines and their locations
- Flags missing tags as governance warnings

## Why it matters
Missing tags mean we can't track costs by team or project which is a common governance gap in enterprise cloud environments. This tool supports FinOps and cloud operating model best practices.

## Technologies used
- Python 3.13
- Azure SDK (azure-identity, azure-mgmt-resource, azure-mgmt-compute)
- Azure CLI

## How to run
1. Install dependencies: `pip3 install azure-identity azure-mgmt-resource azure-mgmt-compute`
2. Login to Azure: `az login`
3. Run: `python3 azure_checker.py`
