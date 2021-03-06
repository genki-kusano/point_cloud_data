This is used to create point cloud data and their persistence diagrams.<br>
I run these codes on macOS Mojave 10.14.1, python 3.7.1, and HomCloud 2.0.0.<br>
My python codes use matplotlib, mpl_toolkits, argparse, os, and numpy.

# Brief Summary
0. Download HomCloud http://www.wpi-aimr.tohoku.ac.jp/hiraoka_labo/homcloud/index.en.html
1. Download `pcd` folder to your Desktop
2. Go to the pcd folder
   (`cd /Users/your_user_name/Desktop/pcd` on the terminalor or open the terminal in the downloaded pcd folder.)
3. Run `sh compute_pd.sh --data --torus`

Then, `data_tda` folder is created on your desktop.<br>
`torus.zip` is one example of the output.

This folder contains 
- point cloud data as m * d matrix where m is the number of points of \mathbb{R}^d<br>
  (`~/pcd/torus/pcd3_num_40/pcd_pd/pcd_3.txt`)
- persistence diagram as n * 2 matrix where m is the number of birth-death pairs<br>
  (`~/pcd/torus/pcd3_num_40/pcd_pd/dim1_3.txt`, dim1 means the dimension of homology)
- picture of point cloud data<br>
  (`~/pcd/torus/plot_pcd3_num_40/pcd_pd/pcd_3.txt`)
- picture of persistence diagram<br>
  (`~/pcd/torus/plot_pd1_pcd3_num_40/pcd_pd/pcd_3.txt`)

# Detailed explanations
I will explain these codes later (as of Nov 30, 2018)<br>
In addition to the torus dataset, you can create other 3 types of point cloud data.

## lattice and mater
`sh compute_pd.sh --data --lattice` or `sh compute_pd.sh --data --matern`<br>
These are simulaton datasets used in Section 6.2 and 6.3 of https://arxiv.org/abs/1803.08269

I prepare these datasets in order to apply an analysis for probability distributions which generate persistence diagrams (I  tried the two sample test and confidence interval estimation for these datasets).
All point sets in the same folder are samples from the same probability distribution.
For example of `~/pcd/lattice/pcd2_side20_gauss010_num100`, all point sets are samples from the pertubed square lattice with the same Gaussian noise sigma=0.1, i.e., all point sets are given by {(i,j) | i,j=1,...,20} + e where e ~ Normal(0, (0.1)^2). 
You can check the behavior in `~/pcd/lattice/plot_pcd2_side5_num10/gauss010_0.png` to `gauss010_9.png`.

## circle
`sh compute_pd.sh --data --circle`
This is a simulation dataset used in Section 4.2 of http://jmlr.org/papers/v18/17-317.html

I prepare this datase in order to apply the support vector machine for persistence diagrams.
`~/pcd/circle/pcd3_num200/pcd_pd` contains 200 point sets and 200 persistence diagrams.
`~/pcd/circle/pcd3_num200/label_z2.txt` is a label set for the 200 persistence diagrams.
The label is decided whether there exists a small circle. 
You can check this in `~/pcd/circle/plot_pcd2_num10`.
`circle_t_*.png` contains a small circle (true) and `circle_f_*.png` does not contain a small circle (false).
Remark: I will make another label set label_z1 from the persistence diagrams later and use the label set XOR(label_z1, label_z2) for a binary classification problem (for more details, please see the reference http://jmlr.org/papers/v18/17-317.html).
This classification problem is difficut to solve correctly because important features locate close to the diagonal in a persistence diagram (this feature is usually treated as noisy generator).

## torus
`sh compute_pd.sh --data --lattice`
This is a simulation dataset used in https://github.com/genki-kusano/point_cloud_data/blob/master/about_torus.pdf and the resulting dataset will be seen as `torus.zip`

I prepare this dataset in order to apply the principal component analysis and a time series analysis for persistence diagrams.
`~/pcd/torus/pcd3_num_40/pcd_pd/pcd_0.txt` is a sphere and `~/pcd/torus/pcd3_num_40/pcd_pd/pcd_39.txt` is a torus (see also `~/pcd/torus/plot_pcd3_sample500_num40`).
Topologically, (underground suefaces of) pcd_0 to pcd_19 is homotopic to a sphere (the homology group in dimension 1 is zero; H_1=0) and pcd_21 to pcd_39 is homotopic to a torus (H_1=Z^2).
Thus, the change point of this dataset is considered to be pcd_20 (H_1=Z).

