# Python Mono-repository example

This is a simple example of a mono-repository for a typical Data Science project.
This project uses uv for package and workspace management.

The project is composed of multiple components:

## Libraries
The **packages** directory contains the stand-alone libraries used in the project.

### fraud-ml
Sample library containing model architectures, training, and evaluation code.

### data-connector
Sample library containing tools to connect to external data sources.

## Workflows
The **workflows** directory contains the workflows used in the project

### batch-proc
Sample project containing runnable notebooks for batch training or batch inference locally or inside a cluster.
It uses the **fraud-ml** library for model training and evaluation, and the **data-connector**
library for fetching historical data.

## Experiments
The **experiments** directory contains the experiments used in the project, e.g. 
testing out different model architectures.

## Application/Service
The **app** directory contains a FastAPI service for serving the model and exposing an API.
It uses the **fraud-ml** library for model inference, and the **data-connector** 
library for model loading.


