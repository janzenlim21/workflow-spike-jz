# Workflow Spike JZ

This repository contains the resources to deploy two Cloud Functions (`multiply` and `randomgen`) and a workflow (`workflow.yaml`) that utilizes these functions.

## Repository Structure

- **multiply/**: Directory containing the source code for the `multiply` Cloud Function.
- **multiply_error/**: (if applicable) Directory containing error handling or test cases related to the `multiply` function.
- **randomgen/**: Directory containing the source code for the `randomgen` Cloud Function.
- **workflow.yaml**: YAML file defining the workflow that integrates the `multiply` and `randomgen` Cloud Functions.
- **README.md**: This file, providing an overview of the repository.

## Deployment Instructions

### Prerequisites

- Ensure you have the Google Cloud SDK installed and authenticated.
- Enable the necessary APIs:
  - Cloud Functions API
  - Workflows API

### Steps

1. **Deploy the Cloud Functions:**

   Deploy the `multiply` and `randomgen` functions using the following commands:

   ```bash
   gcloud functions deploy multiply \
   --runtime <RUNTIME> \
   --trigger-http \
   --allow-unauthenticated \
   --entry-point <ENTRY_POINT> \
   --region <REGION>

   gcloud functions deploy randomgen \
   --runtime <RUNTIME> \
   --trigger-http \
   --allow-unauthenticated \
   --entry-point <ENTRY_POINT> \
   --region <REGION>

2. **Deploy the Workflow:**


   ```bash
    gcloud workflows deploy workflow-spike-jz \
    --source=workflow.yaml \
    --location=<REGION>

3. **Execute the workflow:**

    ```bash
    gcloud workflows executions describe <EXECUTION_ID> --location=<REGION>