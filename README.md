## Quick Start (Docker)

You can directly pull and run the prebuilt image without cloning the repo.

```bash
docker pull beekrm/ml-image
docker run -d -p 8000:8000 --name ml-api beekrm/ml-image
