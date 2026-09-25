source: https://docs.evokoa.com/polygres/mcp
title: Connect an MCP client | Polygres
source_hash: 565849118936f0e3c3e5d6cd344ee07d6038515d408a1854d98a623a608ad168
discovered_from: https://docs.evokoa.com/polygres

# Connect an MCP client | Polygres

Connect an MCP client

Polygres MCP gives an AI client access to the projects and features you choose.

You sign in with your Polygres account, review the connection, and approve it in

your browser.

Connect one project

Open the project in Polygres, choose Connect , and open the MCP tab. The

page selects the current project for you. Choose your MCP client, select View

only or View and make changes , and choose the feature groups you want to

share. The page then gives you setup instructions for that client.

A one-project connection uses this form:

https://mcp.polygres.com/mcp?project_id=<project-id>

This is the recommended choice for most work. Project tools use the selected

project automatically, so their input forms leave out project_id .

Connect your organization

Open Organization → MCP connections when the client needs to work across

projects. Choose a specific project or All accessible projects . The

organization-wide option covers every project you can access now and any

project you gain access to later.

An organization-wide connection uses the base URL:

https://mcp.polygres.com/mcp

Project tools ask for an exact project_id with each call. This keeps every

action tied to a visible target.

Choose the access level

View only adds read_only=true . The connection receives read scopes and

shows read tools.

View and make changes makes approved change tools available according to

your Polygres role and the selected features. Each important change includes a

separate action review before it runs.

You can also select feature groups:

projects : project details, setup, capacity, and operations

database : table discovery, row reads, validation, and one-row upsert

imports : signed CSV uploads, reviewed import start, progress, and cancellation

sync : synchronized-project setup and lifecycle controls

context : AI Search collections, retrieval, filters, points, and operations

graph : graph setup, builds, retrieval, and maintenance

debugging : project and retrieval health information

docs : the public Polygres documentation included with the MCP release

For example, this connection shares Context and Graph reads for one project:

https://mcp.polygres.com/mcp?project_id=<project-id>&read_only=true&features=context,graph

features uses the lowercase names above, separated by commas. Select each

feature once. The connection builder prepares the complete address for you.

Approve the connection

Your MCP client opens Polygres in a browser. Sign in and review the client,

organization, project boundary, access level, feature groups, and scopes. Choose

Allow connection to return access to the client.

The completion page confirms that Polygres returned access to the client. You

can close the browser window and continue there.

Change or remove access

Connection settings stay fixed for the life of an installation. Create a new

connection when you want another project, additional features, or change

access. Open Organization → MCP connections to review active installations

and revoke access at any time. Revocation ends the installation and its refresh

session.

MCP address

The production MCP address is:

https://mcp.polygres.com/mcp

The connection builder adds your selected project, access level, and feature

groups. Copy the generated address into the client setup shown on the page.

Connect with Cursor or another client

In Connect > MCP , choose Cursor for workspace setup instructions. Copy

the generated configuration into .cursor/mcp.json , keeping your other MCP

servers. Authenticate through Cursor’s MCP controls and enable Polygres for

Agent. Ask it to read the selected project’s details to check the connection.

Choose General for another client that supports Streamable HTTP MCP and

browser authorization. Copy the full generated URL into that client’s MCP

settings, including its project and access parameters. Complete browser sign-in,

then request a simple project read to confirm access.

If the client already has a Polygres connection, compare its URL with the one

shown in the dashboard before replacing it.
