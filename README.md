# Lightweight and Rapid Bidirectional Search (Larbsa)

This project has 3 seperate tools which can be used to compare different algorithms.

## Animate Mode
The goal of this mode is to visualise different algorithms.
The server will host a html web page on port 5005 by default.
You can then use the interface to compare the behaviour of the algorithms which you have selected.

You can run it like so:

```
python3 -m animate
```

## Quick Compare
The goal of this mode is to quickly compare the performance of different algorithms.
A table will be produced, presenting various metrics

You can run it like so:

```
python3 main.py -m quick-compare \
--grid-type robustness \
--grid-size 20 \
--grid-density 10 \
--grid-seed 100 \
--grid-algorithms '*'
```

--grid-density is only needed when the --grid-type is robustness.

## Record Tests
The goal of this mode, is to record the performance of algorithms over a variety of different graphs.
By defining an 'initialSeed', which is the seed to start from, we can produce a variety of different graphs.
The tests can be reproduced using the seed and other dependencies like gridSize.

To allow for flexibility, the tests are defined in a yaml file. 
You can find an example in ./testConfig.yaml.

The following fields are only valid for 'type' of robustness:
    - densityStart: what density to start from
    - densityIncrimentAfter: after N interations, the density should be increased
    - densityIncriment: after N interations, the density should be increased by the value defined here

You can run it like so:

```
python3 -m animate --test-config testConfig.yaml
```

When running the program, --test-config argument specifies the file path.