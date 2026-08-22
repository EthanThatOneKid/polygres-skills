source: https://docs.evokoa.com/polygres/cli/notices
title: CLI notices | Polygres
source_hash: e21c02ec056ab499daf9fdd68e3ae90ff427507970b10e3d4ba46d435b59faee
discovered_from: https://docs.evokoa.com/polygres

# CLI notices | Polygres

CLI notices

Polygres can publish service, security, and release notices without requiring a

new CLI release. After a CLI command completes successfully, the CLI checks for

notices that apply to its version and platform.

Notices always go to standard error. They never change standard output, JSON

documents, or a successful command’s exit status. This remains true with

--json :

polygres --json projects list > projects.json

The notice response is cached locally for up to 10 hours. once notices appear

one time, daily notices appear no more than once per 24 hours, and always

notices appear after every successful command while active. Display history and

the cached response are stored in ~/.config/polygres/notices.json with

owner-only permissions on POSIX systems.

Refresh and display every currently applicable notice explicitly:

polygres notices

Running polygres --version also forces a conditional refresh. These requests

use a short timeout. Offline operation, timeouts, invalid responses, and an

unavailable API are silent and never cause the command to fail.

Notice links and targeting

Notices appear as safe plain text on standard error. A notice can include a

validated HTTPS link and an INFO , WARNING , or CRITICAL label. Polygres can

target notices by active time window, CLI version, release channel, operating

system, and architecture so users receive relevant service and release

guidance.
