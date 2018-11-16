This is used to create point cloud data and their persistence diagrams.<br>
I did this on macOS Mojave 10.14.1, python 3.7.1, homcloud 2.0.0.

# Brief Summary
0. Download homcloud http://www.wpi-aimr.tohoku.ac.jp/hiraoka_labo/homcloud/index.en.html
1. Download pcd folder to your Desktop
2. enter `cd /your_user_name/Desktop/pcd` on the terminal
   (or open the terminal in the downloaded pcd folder.)
3. Try `sh compute_pd.sh --data --torus`

Then, a new data_tda folder is created.<br>
torus.zip is one example.

This folder contains 
- point cloud data as m * d matrix where m is the number of points of \mathbb{R}^d
  (~/pcd/torus/pcd3_num_40/pcd_pd/pcd_3.txt)
- persistence diagram as n * 2 matrix where m is the number of birth-death pairs
  (~/pcd/torus/pcd3_num_40/pcd_pd/dim1_3.txt, dim1 means the dimension of homology)
- picture of point cloud data
  (~/pcd/torus/plot_pcd3_num_40/pcd_pd/pcd_3.txt)
- picture of persistence diagram
  (~/pcd/torus/plot_pd1_pcd3_num_40/pcd_pd/pcd_3.txt)

# Detailed explanations
... will be added later (Nov 16, 2018)
You can create 4 types of point cloud data from {--lattice, --matern, --circle_svm, --torus} as<br>
`sh compute_pd.sh --data --lattice`

lattice and mater are simulaton datasets used in Section 6.2 and 6.3 of https://arxiv.org/abs/1803.08269<br>
circle_svm is a simulation dataset used in Section 4.2 of http://jmlr.org/papers/v18/17-317.html<br>
for torus, please see about_torus.pdf
