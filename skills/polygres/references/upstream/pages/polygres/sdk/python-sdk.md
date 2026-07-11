source: https://docs.evokoa.com/polygres/sdk/python-sdk
title: Python SDK | Polygres
source_hash: 9c9ea940f2c55a249e8d92929a8cc59f774bf91df573537c543ff2ed63785d91
discovered_from: https://docs.evokoa.com/polygres

# Python SDK | Polygres

Python SDK

The Polygres Python SDK is the official retrieval client for querying your project’s Runtime API. It connects securely using your Project API Key and Runtime API URL without exposing your native database passwords.

Installation

Install the package via pip:

pip install polygres-sdk

Quick Start

Create a Project API Key from your project Settings page, and find the Runtime API URL on your project Connect page.

Store these in your environment variables, then initialize the client:

import os

from polygres import Polygres

client = Polygres(

api_key = os.environ[ "POLYGRES_API_KEY" ],

runtime_url = os.environ[ "POLYGRES_RUNTIME_URL" ],

)

# Bind the client to your active project

project = client.project()

# Check your project's configuration readiness

readiness = project.readiness()

print (readiness.graph, readiness.vector, readiness.hybrid)

Running Queries

The SDK supports all retrieval modes. Instead of duplicating the examples here, we have compiled comprehensive, production-ready Python snippets for every query type in our integration patterns guide:

Vector Retrieval ( project.vector.search )

Text Retrieval ( project.text.tsvector , project.text.fuzzy )

Graph Retrieval ( project.graph.expand , project.graph.related )

Hybrid Retrieval ( project.hybrid.graph_first , project.hybrid.joint )

Head over to Retrieval Integration Patterns to copy the Python code for your specific workflow.

Choosing your access method

Task Use

Runtime retrieval queries in application code (vector, text, graph, hybrid) Python SDK

Project setup, credential output, CSV imports, migrations, retrieval configuration Polygres CLI

Visual project management, SQL editor, query workbench Dashboard

Direct database connections for ORMs, migration tools, bulk inserts Native Postgres driver ( psycopg , SQLAlchemy, etc.)

Direct database connections

The Polygres Python SDK is strictly for Retrieval API queries . It does not bundle Postgres drivers like asyncpg or psycopg , and it is not meant for database migrations, bulk background inserts, or raw SQL execution.

If your backend application needs to establish a direct pooled connection (for example, via SQLAlchemy or psycopg), bypass the SDK and use the direct database credentials. See the Connection Examples guide for Python setup instructions.
