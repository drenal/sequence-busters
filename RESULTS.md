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
| | Conv1d 100 epoch no ReLU              |  0.7646673917770386   |   0.6345544372286115 | **0.768743** |  **0.628721** |
| | Mario 2x conv1d                       |  0.7716520939554486   |   0.6347624063491821 | | |
| | LM6 conv1d 128 LSTM 512               |  0.7733642969812665   |   0.6407613243375506 | 0.69859426 | 0.5592613 |
| | LM6 conv1d x2 lstm x1                 |  0.7728647845132011   |   0.6361431649753025 | | |
| | LM6 conv1d 64, conv1d 128, LSTM 512   |  0.774354806968144    |   0.6342970643724714 | | |
| | LM6 conv1d 32, conv1d 64, LSTM 64     |  0.7690139923776899   |   0.6209373644420079 | | |
| | LM6 conv1d 32, conv1d 64, LSTM 128    |  0.7685239570481437   |   0.6277188232966832 | | |
| | LM6 conv1d 32, conv1d 64, LSTM 512    |  0.7726321220397949   |   0.6368165016174316 | | |
| | LM5 Conv1d 100 epoch LazyReLU         |  0.7666626232010978   |   0.6362125277519226 | 0.767364939 | 0.6190738 |
| | LM5 Conv1d 100 epoch GELU             |  0.7680633408682687   |   0.6391678282192775 | | | 
