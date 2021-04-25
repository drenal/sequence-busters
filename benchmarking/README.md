# Run benchmarking

Provided by: Erik Kiehl and Mads Damgaard

- CASP12_ESM1b.npz is the CASP12 challenge augmented with ESM1b embeddings.
- `predictions.csv` should be the one produced by the model in question.

```
python3 benchmark.py --predictions predictions.csv --labels correct.csv
```
