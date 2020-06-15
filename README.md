ICCM Individualized TransSet
============================

Companion repository for the 2020 article "Extending TransSet: An Individualized Model for Human Syllogistic Reasoning" published in the proceedings of the 18th International Conference on Cognitive Modeling (ICCM)

### Overview

- `analysis/`: Contains the files needed to run the analyses in the article.
    - `/ccobra_coverage_results`: Contains the results from coverage analyses performed by CCOBRA.
        - `/mreasoner_phm_ragni2016_cogsci2020indiv.csv`: Results of PHM and mReasoner for the CCOBRA coverage analysis performed by Riesterer (2020).
        - `/transset_ragni2016.csv.csv`: Results of the coverage analysis for TransSet, MFA and the uniform model. 
    - `/data`: Contains the Ragni2016 dataset.
    - `/models`: Contains the model implementations.
        - `/mfa`: Implementation of the M(ost) F(requent) A(nswer) model.
        - `/transset`: Implementation of the TransSet model.
        - `/uniform`: Implementation of the Uniform model.
    - `/parameterization`: Contains the best parameter configurations for each subject.
    - `eval-ragni-coverage.json`: CCOBRA benchmark to perform the coverage analysis.
    - `mannwhitneyu.py`: Calculates the MannWhitneyU statistic for TransSets performance.
    - `plot_param_distribution.py`: Generates the parameter distribution plot (Figure 3 in the article).
    - `plot_performance.py`: Generates the performance swarmplot (Figure 2 in the article).

### Dependencies

- Python 3
    - CCOBRA
    - pandas
    - numpy
    - seaborn
    - scipy

### Usage

After downloading the repository, navigate to the analysis subfolder, e.g., by using the following command:

```
cd /path/to/repository/analysis
```

If CCOBRA is installed, the following command will start the evaluation:

```
$> ccobra eval-ragni-coverage.json
```

A website will open and present the results of the analysis. A CSV file containing the results can be downloaded from the website. The website itself is saved in the folder of the benchmark as an HTML file.

The python scripts (`mannwhitneyu.py`, `plot_param_distribution.py` and `plot_performance.py`) take no arguments and can therefore be executed directly:

```
$> python [script.py]
```
    
### References

Brand, D., Riesterer, N.,  & Ragni, M. (in press). Extending TransSet: An Individualized Model for Human Syllogistic Reasoning. In proceedings of the 18th International Conference on Cognitive Modeling.

Riesterer, N., Brand, D., & Ragni, M. (2020). Do Models Capture Individuals? Evaluating Parameterized Models for Syllogistic Reasoning. In Proceedings of the 42nd Annual Conference of the Cognitive Science Society.