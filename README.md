# Sequence Busters

A ~~3~~ 5 people team to conquer the world! Or at least win the Copenhagen Bioinformatics Hackathon 2021 Protein Edition... one step at a time.

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
