# OPUS-Mut

Predicting the effect of protein mutation is crucial in many applications such as protein design, protein evolution, and genetic disease analysis. Structurally, the mutation is basically the replacement of the side chain of a particular residue. Therefore, accurate side-chain modeling is useful in studying the effect of mutation. Here, we propose a computational method, namely OPUS-Mut, which significantly outperforms other backbone-dependent side-chain modeling methods including our previous method OPUS-Rota4. We evaluate OPUS-Mut by four case studies on Myoglobin, p53, HIV-1 protease, and T4 lysozyme. The results show that the predicted structures of side chains of different mutants are consistent well with their experimentally determined results. In addition, when the residues with significant structural shifts upon the mutation are considered, it is found that the extent of the predicted structural shift of these affected residues can be correlated reasonably well with the functional changes of the mutant measured by experiments. OPUS-Mut can also help one to identify the harmful and benign mutations, and thus may guide the construction of a protein with relatively low sequence homology but with similar structure.

## Usage

### Dependency

```
Python 3.7
TensorFlow 2.4
```

The standalone version of OPUS-Mut is hosted on [Baidu Drive](https://pan.baidu.com/s/13blkjz8pwDW_i1Mxv28sJg) with password `o6xo`. Three oligomer datasets (CASP14 (11), CAMEO-Homo (65), and CAMEO-Hetero (21)) and the protein-protein docking pose dataset Oligomer-Dock (75) are hosted on [Baidu Drive](https://pan.baidu.com/s/1Esb9_io-XlZMR1UlOXqCMA) with password `wnq4`.


