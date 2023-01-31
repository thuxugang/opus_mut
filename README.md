# OPUS-Mut

Predicting the effect of protein mutation is crucial in many applications such as protein design, protein evolution, and genetic disease analysis. Structurally, the mutation is basically the replacement of the side chain of a particular residue. Therefore, accurate side-chain modeling is useful in studying the effect of mutation. Here, we propose a computational method, namely OPUS-Mut, which significantly outperforms other backbone-dependent side-chain modeling methods including our previous method OPUS-Rota4. We evaluate OPUS-Mut by four case studies on Myoglobin, p53, HIV-1 protease, and T4 lysozyme. The results show that the predicted structures of side chains of different mutants are consistent well with their experimentally determined results. In addition, when the residues with significant structural shifts upon the mutation are considered, it is found that the extent of the predicted structural shift of these affected residues can be correlated reasonably well with the functional changes of the mutant measured by experiments. OPUS-Mut can also help one to identify the harmful and benign mutations, and thus may guide the construction of a protein with relatively low sequence homology but with similar structure.

## Usage

### Dependency

```
Python 3.7
TensorFlow 2.4
```

1. use `mk_mut_backbone.py` to generate original WT backbone and mutants backbones (.bb).

2. list the backbone paths in `bb_list`.

3. run `run_opus_mut.py` to generate the results of OPUS-Mut (.mut).

4. use `get_difference_summation.py` to caculate the difference between WT and mutants.


The standalone version of OPUS-Mut is hosted on [Baidu Drive](https://pan.baidu.com/s/13blkjz8pwDW_i1Mxv28sJg) with password `o6xo`. It can also be downloaded from [Here](https://drive.google.com/file/d/1ZpFjghkqP5vsIpOk1bYwFyhci7FeNPPD/view?usp=sharing).

Three datasets (CASP14, CAMEO60, and CAMEO65) with single peptide chain can be downloaded directly from [Here](https://github.com/thuxugang/opus_mut/blob/main/opus_mut_datasets.zip).

Three oligomer datasets (CASP14 (11), CAMEO-Homo (65), and CAMEO-Hetero (21)) and the protein-protein docking pose dataset Oligomer-Dock (75) are hosted on [Baidu Drive](https://pan.baidu.com/s/1Esb9_io-XlZMR1UlOXqCMA) with password `wnq4`.


