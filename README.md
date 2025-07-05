# Lightweight and Rapid Bidirectional Search (Larbsa)

## Introduction
This project makes use of python version *3.12.6*.
The project includes a requirements.txt for all the dependencies and their versions.
Before doing anything, be sure to run it with:

```
pip3 install -r requirements.txt
```

This project has 3 seperate tools which can be used to compare different algorithms.
The entry point to the project is *./main.py*.

## Animate Mode
The goal of this mode is to visualise different algorithms.
The server will host a html web page on port *5005* by default. **Right now, this cannot be changed**.
You can then use the interface to compare the behaviour of the algorithms which you have selected.

You can run it like so:

```
python3 -m animate
```

Going to http://localhost:5005 should present a web page, where you can then visualise & compare.

## Quick Compare
The goal of this mode is to quickly compare the performance of different algorithms.
A table will be produced, presenting various metrics.

You can run it like so:

```
python3 main.py -m quick-compare \
--grid-type robustness \
--grid-size 20 \
--grid-density 10 \
--grid-seed 100 \
--grid-algorithms '*'
```

*--grid-density* is only needed when the *--grid-type* is *robustness*.

## Record Tests
The goal of this mode, is to record the performance of algorithms over a variety of different graphs.
By defining an *initialSeed*, we can produce a variety of different graphs.
The seed, alongside fields like *gridSize* can be used to reproduce the tests.

To allow for flexibility, the tests are defined in a yaml file. 
You can find an example in *./testConfig.yaml*.

The following fields are only valid for 'type' of *robustness*:
1. *densityStart*: what density to start from
2. *densityIncrimentAfter*: after N interations, the density should be increased
3. *densityIncriment*: after N interations, the density should be increased by the value defined here

In the case that the test terminates unintentionally, the 'tests can continue where they left' of as they simply
append to the output csv files, rather than overriding them. This assuming that the name of the test does not change.
One caveat, this does not apply to the *robustness* tests, as these add a "_N" suffix, where **N** represents the density group.

You can run it like so:

```
python3 -m record-tests --test-config testConfig.yaml
```

When running the program, *--test-config* argument specifies the file path to the test config.
Test results are stored in *./results/TEST_NAME* where *TEST_NAME* corresponds to the *name* field in the config.