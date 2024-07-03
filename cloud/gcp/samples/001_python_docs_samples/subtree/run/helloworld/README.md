# Cloud Run Hello World Sample

https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service

This sample shows how to deploy a Hello World application to Cloud Run.

[![Run in Google Cloud][run_img]][run_link]

[run_img]: https://storage.googleapis.com/cloudrun/button.svg
[run_link]: https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/GoogleCloudPlatform/python-docs-samples&cloudshell_working_dir=run/helloworld

## Build

* Set an environment variable with your GCP Project ID:

```
export GOOGLE_CLOUD_PROJECT=<PROJECT_ID>
```

* Use a [Buildpack](https://github.com/GoogleCloudPlatform/buildpacks) to build the container:

```sh
gcloud builds submit --pack image=gcr.io/${GOOGLE_CLOUD_PROJECT}/helloworld

https://console.cloud.google.com/artifacts/docker/${GOOGLE_CLOUD_PROJECT}/us/gcr.io?project=${GOOGLE_CLOUD_PROJECT}


```

## Run Locally

```sh
docker run --rm gcr.io/${GOOGLE_CLOUD_PROJECT}/helloworld
```

## Test

```
pytest
```

_Note: you may need to install `pytest` using `pip install pytest`._

## Deploy

```sh
# Set an environment variable with your GCP Project ID
export GOOGLE_CLOUD_PROJECT=<PROJECT_ID>

# Deploy to Cloud Run
gcloud run deploy helloworld --source .
gcloud config set run/region europe-central2
# Deploying from source requires an Artifact Registry Docker repository to store built containers. A repository named [cloud-run-source-deploy] in region [europe-central2] will be 
# Enable run.googleapis.com API
# This command is equivalent to running `gcloud builds submit --pack image=[IMAGE] y` and `gcloud run deploy y 
# --image [IMAGE]`
# Warsaw (europe-central2)


# Cloud Build
# https://console.cloud.google.com/cloud-build/builds/a29a2be8-0410-40e7-a284-b346e3402ad9;step=0?project=${GOOGLE_CLOUD_PROJECT}
```


## Final solution
https://console.cloud.google.com/run?project=${GOOGLE_CLOUD_PROJECT}

For more details on how to work with this sample read the [Python Cloud Run Samples README](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/run)
