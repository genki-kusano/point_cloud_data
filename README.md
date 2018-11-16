Edited by Genki Kusano https://sites.google.com/site/genkikusano/home
This is used to create point cloud data and their persistence diagrams.

# Brief Summary
0. Download homcloud http://www.wpi-aimr.tohoku.ac.jp/hiraoka_labo/homcloud/index.en.html
1. Download pcd folder to your Desktop
2. enter cd /your_user_name/Desktop/pcd on the terminal
   (or open the terminal in the downloaded pcd folder.)
3. Try sh compute_pd.sh --data --torus
Then, a new data_tda folder is created.
This folder contains 
- point cloud data as N * d matrix where N is # of points and d is of \mathbb{R}^d
  (see ~/pcd/torus/pcd3_num_40/pcd_pd/pcd_3.txt)
- persistence diagram as N * 2 matrix, which is a collection of birth and death pairs
  (see ~/pcd/torus/pcd3_num_40/pcd_pd/dim1_3.txt, dim1 means the dimension of homology)
- picture of point cloud data
  (see ~/pcd/torus/plot_pcd3_num_40/pcd_pd/pcd_3.txt)
- picture of persistence diagram
  (see ~/pcd/torus/plot_pd1_pcd3_num_40/pcd_pd/pcd_3.txt)

# Detailed explanations
... will be added later (Nov 16, 2018)

for torus, please see about_torus.pdf
