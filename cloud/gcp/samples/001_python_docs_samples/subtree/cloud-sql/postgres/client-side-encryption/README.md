# Encrypting fields in Cloud SQL - Postgres with Tink

## Before you begin

1. If you haven't already, set up a Python Development Environment by following the [python setup guide](https://cloud.google.com/python/setup) and 
[create a project](https://cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).

1. Create a 2nd Gen Cloud SQL Instance by following these 
[instructions](https://cloud.google.com/sql/docs/postgres/create-instance). Note the connection string,
database user, and database password that you create.

1. Create a database for your application by following these 
[instructions](https://cloud.google.com/sql/docs/postgres/create-manage-databases). Note the database
name.

1. Create a KMS key for your application by following these
[instructions](https://cloud.google.com/kms/docs/creating-keys). Copy the resource name of your
created key.

1. Create a service account with the 'Cloud SQL Client' permissions by following these 
[instructions](https://cloud.google.com/sql/docs/postgres/connect-admin-proxy#create-service-account).
Download a JSON key to use to authenticate your connection.

1. **macOS / Windows only**: Configure gRPC Root Certificates: On some platforms you may need to
accept the Google server certificates, see instructions for setting up
[root certs](https://github.com/googleapis/google-cloud-cpp/blob/main/google/cloud/bigtable/examples/README.md#configure-grpc-root-certificates).
 

## Running locally

To run this application locally, download and install the `cloud_sql_proxy` by
following the instructions [here](https://cloud.google.com/sql/docs/postgres/connect-admin-proxy#install).

Instructions are provided below for using the proxy with a TCP connection or a Unix Domain Socket.
On Linux or Mac OS you can use either option, but on Windows the proxy currently requires a TCP
connection.

### Launch proxy with TCP

To run the sample locally with a TCP connection, set environment variables and launch the proxy as
shown below.

#### Linux / Mac OS
Use these terminal commands to initialize environment variables:
```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service/account/key.json
export DB_HOST='127.0.0.1:5432'
export DB_USER='<DB_USER_NAME>'
export DB_PASS='<DB_PASSWORD>'
export DB_NAME='<DB_NAME>'
export GCP_KMS_URI='<GCP_KMS_URI>'
```
Note: Saving credentials in environment variables is convenient, but not secure - consider a more
secure solution such as [Secret Manager](https://cloud.google.com/secret-manager/docs/quickstart) to
help keep secrets safe.

Then use this command to launch the proxy in the background:
```bash
./cloud_sql_proxy -instances=<project-id>:<region>:<instance-name>=tcp:5432 -credential_file=$GOOGLE_APPLICATION_CREDENTIALS &
```

Note: if you are running a local Postgres server, you will need to turn it off before running the command above or use a different port.

#### Windows/PowerShell
Use these PowerShell commands to initialize environment variables:
```powershell
$env:GOOGLE_APPLICATION_CREDENTIALS="<CREDENTIALS_JSON_FILE>"
$env:DB_HOST="127.0.0.1:5432"
$env:DB_USER="<DB_USER_NAME>"
$env:DB_PASS="<DB_PASSWORD>"
$env:DB_NAME="<DB_NAME>"
$env:GCP_KMS_URI='<GCP_KMS_URI>'
```
Note: Saving credentials in environment variables is convenient, but not secure - consider a more
secure solution such as [Secret Manager](https://cloud.google.com/secret-manager/docs/quickstart) to
help keep secrets safe.

Then use this command to launch the proxy in a separate PowerShell session:
```powershell
Start-Process -filepath "C:\<path to proxy exe>" -ArgumentList "-instances=<project-id>:<region>:<instance-name>=tcp:5432 -credential_file=<CREDENTIALS_JSON_FILE>"
```

Note: if you are running a local Postgres server, you will need to turn it off before running the command above or use a different port.

### Launch proxy with Unix Domain Socket
NOTE: this option is currently only supported on Linux and Mac OS. Windows users should use the
[Launch proxy with TCP](#launch-proxy-with-tcp) option.

To use a Unix socket, you'll need to create a directory for the sockets and
initialize an environment variable containing the directory you just created.
For example:

```bash
export DB_SOCKET_DIR=$(mktemp -d cloudsql)
```

Use these terminal commands to initialize other environment variables as well:
```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service/account/key.json
export INSTANCE_CONNECTION_NAME='<MY-PROJECT>:<INSTANCE-REGION>:<INSTANCE-NAME>'
export DB_USER='<DB_USER_NAME>'
export DB_PASS='<DB_PASSWORD>'
export DB_NAME='<DB_NAME>'
export GCP_KMS_URI='<GCP_KMS_URI>'
```
Note: Saving credentials in environment variables is convenient, but not secure - consider a more
secure solution such as [Secret Manager](https://cloud.google.com/secret-manager/docs/quickstart) to
help keep secrets safe.

Then use this command to launch the proxy in the background:
```bash
./cloud_sql_proxy -dir=$DB_SOCKET_DIR --instances=$INSTANCE_CONNECTION_NAME --credential_file=$GOOGLE_APPLICATION_CREDENTIALS &
```

### Install requirements

Next, setup install the requirements into a virtual environment:
```bash
virtualenv --python python3 env
source env/bin/activate
pip install -r requirements.txt
```

### Run the demo

Add new votes:
```bash
python snippets/encrypt_and_insert_data.py 
```

View the collected votes:
```bash
python snippets/query_and_decrypt_data.py 
```
