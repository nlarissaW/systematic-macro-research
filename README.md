# systematic-macro-research

Systematic macro research pipeline for Canada and the US using Bayesian stress testing, state-space modeling, and macro strategy backtesting.

## Project motivation
This repository develops a systematic macro research architecture designed to connect three layers of quantitative work:

1. macro-fiscal risk monitoring,
2. latent factor extraction using state-space methods,
3. macro-driven investment strategy design and backtesting.

The project is built around a shared master dataset for Canada and the US and aims to produce a coherent research-to-investment pipeline.

## Repository structure

```text
systematic-macro-research/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_build_master_dataset.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_kalman_factors.ipynb
│   ├── 04_bayesian_stress_test.ipynb
│   └── 05_systematic_backtest.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── features.py
│   ├── backtest.py
│   └── build_master.py
│
├── outputs/
├── requirements.txt
└── README.md


### Research progress
```markdown
## Current status
- [x] Initial project structure created
- [x] Master dataset pipeline MVP built
- [x] First strategy vs SP500 chart generated
- [ ] Data quality checks
- [ ] Feature engineering expansion
- [ ] Kalman factor extraction
- [ ] Bayesian stress testing module
- [ ] Strategy evaluation and robustness checks

## First result
The first MVP pipeline successfully builds a processed macro dataset and generates an initial comparison between a rule-based macro strategy and the S&P 500 benchmark.


## Next steps
- audit the master dataset,
- improve signal construction,
- add Canada-specific macro variables,
- estimate latent macro factors,
- implement Bayesian macro stress scenarios,
- compare strategy performance across regimes.


