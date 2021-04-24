# Benchmark results

Let's summarize the benchmark results of our models in this file

| config.yml as in commit | model name | q3_train | q8_train | q3_secret | q8_secret |
|-------------------------|------------|----------|----------|-----------|-----------|
| [c5a43164f2daefd370ea30870a35c0cbe8970a78](https://github.com/drenal/sequence-busters/commit/c5a43164f2daefd370ea30870a35c0cbe8970a78) | Baseline   | 0.744823 | 0.613314 | | |
| [2c4b8e8c70cecd909b98e2b01312126a3279ff4c](https://github.com/drenal/sequence-busters/commit/2c4b8e8c70cecd909b98e2b01312126a3279ff4c) | Linear     | 0.767157 | 0.627129 | 0.761852  | 0.615077 |
| [d39bcb3fecaf6b925d3b63ea3e243d293335961b](https://github.com/drenal/sequence-busters/commit/d39bcb3fecaf6b925d3b63ea3e243d293335961b) | LenardModel2 (Bilinear) |0.686900 | 0.571329 | | |
| | LenardModel4 with ReLU |     0.7660833256585258 |     0.6195413555417743 | | |
| | LenardModel4 without ReLU |  0.7678060105868748 |     0.6201206530843463 | | |
| | LenardModel4 first ReLU  |   0.7670386603900364 |    0.6197986858231681 | | | 
| | Conv1d 100 epoch ReLU   |    0.7649000542504447 |   0.6341337050710406 | | |
