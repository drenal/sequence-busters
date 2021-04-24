# Sequence Busters

A ~~3~~ 5 people team to conquer the world! Or at least win the Copenhagen Bioinformatics Hackathon 2021 Protein Edition... one step at a time.

[Benchmark results comparison table](RESULTS.md)

## Members

- Joaquín Antonio Ramírez Hernández
- Lenard Szantho
- Mario Perez Jimenez
- Christoph Hillisch
- Jun-Hoe Lee

## Setup

Clone our repository: `git clone git@github.com:drenal/sequence-busters.git`

Change dir: `cd sequence-busters`

Create your own branch `git checkout -b YOUR_BRANCH_NAME`

Push it to github so it knows about it: `git push --set-upstream origin YOUR_BRANCH_NAME`

Once you think you have something cool, push it into your branch first:
```
git add .
git commit -m "changes on your branch"
git push 
# maybe git will ask for this the first time:
#git push --set-upstream origin YOUR_BRANC_NAME
```

To merge it with the main and trigger the benchmarking action you can:
- create a pull request on github GUI: https://github.com/drenal/sequence-busters/pulls
- or merge it yourself: 
```
git checkout main
git merge YOUR_BRANCH_NAME
git push
```

### CI integration

When you have a new set of proposed models, you have to change the path to it in 2 files:
In `Dockerfile` and `.dockerignore` replace the line:
```
saved/baseline/0423-201034/checkpoints/model_best.pth 
```
with the path to your model.

And then don't forget to `git add` it with force:
```
git add -f PATH_TO_YOUR_MODEL.pth
```

### To get on track with main branch

```
git checkout YOUR_BRANCH
git merge main
git push
```

Be sure that this step didn't overwrite something of your own work and results!

## Original README

The README provided by Biohacathon is [HERE](README.rst)
