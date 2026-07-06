-- Model the cross-reference relationships between documentation pages.
-- Run in the SQL Editor. After importing, configure Graph Search
-- on doc_links(source_page_id -> target_page_id) to query "which
-- pages link to this one?" via Polygres Graph retrieval.

-- Direct links (page A references page B by name)
CREATE TABLE IF NOT EXISTS doc_links (
  id            SERIAL PRIMARY KEY,
  source_page_id TEXT NOT NULL REFERENCES docs_pages(id),
  target_page_id TEXT NOT NULL REFERENCES docs_pages(id),
  link_text     TEXT NOT NULL,
  UNIQUE(source_page_id, target_page_id, link_text)
);

INSERT INTO doc_links (source_page_id, target_page_id, link_text) VALUES

-- index (home page)
  ('index', 'what-is-polygres', 'What is Polygres?'),
  ('index', 'quickstart', 'Quickstart'),
  ('index', 'key-concepts', 'Key concepts'),
  ('index', 'core-workflow', 'Core workflow'),
  ('index', 'common-use-cases', 'Common use cases'),
  ('index', 'projects-and-orgs', 'Projects and Organizations'),
  ('index', 'load-and-manage-data', 'Load and manage data'),
  ('index', 'security-basics', 'Security basics'),
  ('index', 'dashboard-api-database-access', 'Dashboard, API, and database access'),
  ('index', 'connect-your-app', 'Connect and credentials'),
  ('index', 'connection-examples', 'Connection examples'),
  ('index', 'configure-retrieval', 'Configure and query retrieval'),
  ('index', 'retrieval-integration-patterns', 'Retrieval integration patterns'),
  ('index', 'routes', 'Routes'),
  ('index', 'error-codes', 'Error codes'),

-- what-is-polygres
  ('what-is-polygres', 'quickstart', 'Quickstart'),
  ('what-is-polygres', 'core-workflow', 'Core workflow'),
  ('what-is-polygres', 'connect-your-app', 'Connect and credentials'),
  ('what-is-polygres', 'connection-examples', 'Connection examples'),
  ('what-is-polygres', 'load-and-manage-data', 'Load and manage data'),
  ('what-is-polygres', 'configure-retrieval', 'Configure and query retrieval'),
  ('what-is-polygres', 'retrieval-integration-patterns', 'Retrieval integration patterns'),
  ('what-is-polygres', 'routes', 'Routes'),
  ('what-is-polygres', 'error-codes', 'Error codes'),

-- quickstart
  ('quickstart', 'python-sdk', 'Python SDK'),
  ('quickstart', 'connect-your-app', 'Connect and credentials'),
  ('quickstart', 'load-and-manage-data', 'Load and manage data'),
  ('quickstart', 'configure-retrieval', 'Configure and query retrieval'),
  ('quickstart', 'retrieval-integration-patterns', 'Retrieval integration patterns'),
  ('quickstart', 'routes', 'Routes'),
  ('quickstart', 'error-codes', 'Error codes'),

-- key-concepts
  ('key-concepts', 'connect-your-app', 'Connect Your App'),
  ('key-concepts', 'connection-examples', 'Connection Examples'),
  ('key-concepts', 'dashboard-api-database-access', 'Database Access & Connections'),
  ('key-concepts', 'security-basics', 'Security Basics'),
  ('key-concepts', 'configure-retrieval', 'Configure Retrieval'),
  ('key-concepts', 'query-from-dashboard', 'Querying from Dashboard'),
  ('key-concepts', 'retrieval-integration-patterns', 'Integration Patterns'),
  ('key-concepts', 'limits', 'Limits'),
  ('key-concepts', 'security-basics', 'Security'),
  ('key-concepts', 'troubleshooting', 'Troubleshooting'),
  ('key-concepts', 'routes', 'Routes'),
  ('key-concepts', 'error-codes', 'Error codes'),

-- core-workflow
  ('core-workflow', 'connect-your-app', 'Connect and credentials'),
  ('core-workflow', 'connection-examples', 'Connection examples'),
  ('core-workflow', 'load-and-manage-data', 'Load and manage data'),
  ('core-workflow', 'configure-retrieval', 'Configure and query retrieval'),
  ('core-workflow', 'retrieval-integration-patterns', 'Retrieval integration patterns'),
  ('core-workflow', 'routes', 'Routes'),
  ('core-workflow', 'error-codes', 'Error codes'),

-- common-use-cases
  ('common-use-cases', 'load-and-manage-data', 'Load and manage data'),
  ('common-use-cases', 'configure-retrieval', 'Configure and query retrieval'),
  ('common-use-cases', 'retrieval-integration-patterns', 'Retrieval integration patterns'),
  ('common-use-cases', 'routes', 'Routes'),
  ('common-use-cases', 'error-codes', 'Error codes'),

-- projects-and-orgs
  ('projects-and-orgs', 'security-basics', 'Security basics'),
  ('projects-and-orgs', 'connect-your-app', 'Connect your app'),
  ('projects-and-orgs', 'load-and-manage-data', 'Load and manage data'),
  ('projects-and-orgs', 'configure-retrieval', 'Configure retrieval'),

-- load-and-manage-data
  ('load-and-manage-data', 'configure-retrieval', 'Configure retrieval'),

-- query-from-dashboard
  ('query-from-dashboard', 'security-basics', 'Security basics'),

-- dashboard-api-database-access
  ('dashboard-api-database-access', 'connect-your-app', 'Connect and credentials'),
  ('dashboard-api-database-access', 'connection-examples', 'Connection examples'),
  ('dashboard-api-database-access', 'load-and-manage-data', 'Load and manage data'),
  ('dashboard-api-database-access', 'configure-retrieval', 'Configure and query retrieval'),
  ('dashboard-api-database-access', 'retrieval-integration-patterns', 'Retrieval integration patterns'),
  ('dashboard-api-database-access', 'routes', 'Routes'),
  ('dashboard-api-database-access', 'error-codes', 'Error codes'),

-- sdk/python-sdk
  ('python-sdk', 'retrieval-integration-patterns', 'Retrieval Integration Patterns'),
  ('python-sdk', 'connection-examples', 'Connection Examples'),

-- sdk/connect-your-app
  ('connect-your-app', 'security-basics', 'Security basics'),
  ('connect-your-app', 'query-from-dashboard', 'Query from the dashboard'),

-- sdk/connection-examples
  ('connection-examples', 'query-from-dashboard', 'Query from the dashboard'),
  ('connection-examples', 'retrieval-integration-patterns', 'Retrieval integration patterns'),

-- sdk/configure-retrieval
  ('configure-retrieval', 'query-from-dashboard', 'Query from the dashboard'),

-- sdk/retrieval-integration-patterns
  ('retrieval-integration-patterns', 'query-from-dashboard', 'Query from the dashboard'),

-- reference overview
  ('reference', 'routes', 'Routes'),
  ('reference', 'error-codes', 'Error codes'),
  ('reference', 'roles-and-permissions', 'Roles and permissions'),
  ('reference', 'limits', 'Limits'),
  ('reference', 'troubleshooting', 'Troubleshooting'),

-- troubleshooting
  ('troubleshooting', 'limits', 'Limits');
