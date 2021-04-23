FROM python:3.8-slim AS predict

WORKDIR /home/biolib/

# install dependencies
COPY challenge/requirements.txt challenge/requirements.txt
RUN pip install -r challenge/requirements.txt

# move final model
# models should be in saved/{MODEL_NAME}/{TIMESTAMP}/checkpoints/
# Example: COPY saved/baseline/0422-213641/checkpoints/model_best.pth model.pth
COPY saved/{INSERT_MODEL_PATH_HERE} model.pth

# move final configuration
COPY experiments/config.yml config.yml

# copy challenge project
COPY challenge challenge
COPY README.rst README.rst

# install challenge as package
RUN pip install -e challenge

# Make output dir
RUN mkdir out/

# Run evaluation and save metrics in output dir
ENTRYPOINT challenge eval -c config.yml -m model.pth > out/metrics.txt