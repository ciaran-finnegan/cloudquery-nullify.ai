# Nullify.ai Source Plugin
This repo contains a Cloudquery source plugin for Nullify.ai.

## Status
Incomplete prototype. 

Only the Nullify Software Composition Analysis findings are implemented.

These are returned in the following table

```
sca_counts
```

## Getting started

To get started you will need a Nullify.ai API bearer token.

### Getting your API bearer token.

Refer to the Nullify.ai documentation at the URL below;

https://docs.nullify.ai/api-reference/nullify-api/authentication

### Export your token as an environment variable

   ```
   export NULLIFY_API_BEARER_TOKEN=<your_bearer_token>'
   ```

## Configuring Cloudquery
Adust `TestConfig.yaml` to match your plugin

e.g. 

```
kind: source
spec:
  name: "counts"
  registry: "grpc"
  path: "localhost:7777"
  tables: ['*']
  destinations: ["sqlite"]
  spec:
    base_url: https://api.YOUR_NULLIFY_TENANT.nullify.ai
    github_owner_id: GITHUB_OWNER_ID
    access_token: "${NULLIFY_API_BEARER_TOKEN}"
---
kind: destination
spec:
  name: sqlite
  path: cloudquery/sqlite
  version: "v2.4.11"
  spec:
    connection_string: ./db.sqlite
```

## Running Cloudquery

```
cloudquery sync
```

This should result in the creation of a sqlite database `db.sqlite` where you can validate your tables are as expected.




- [Architecture](https://www.cloudquery.io/docs/developers/architecture)
- [Concepts](https://www.cloudquery.io/docs/developers/creating-new-plugin/python-source)
- [Video tutorial](https://youtu.be/TSbGHz5Z09M)
