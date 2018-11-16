import numpy as np
import functions


def make_torus(val_r_big, val_r_small, num_sample):
    list_pcd = []
    val_ratio = np.arccos(np.min([1, val_r_big / val_r_small]))

    for _ in range(num_sample):
        val_theta = np.pi * ((2 * np.random.rand()) - 1)
        val_eta = (np.pi - val_ratio) * ((2 * np.random.rand()) - 1)
        val_x = (val_r_big * np.cos(val_theta) +
                 val_r_small * np.cos(val_eta) * np.cos(val_theta))
        val_y = (val_r_big * np.sin(val_theta) +
                 val_r_small * np.cos(val_eta) * np.sin(val_theta))
        val_z = val_r_small * np.sin(val_eta)
        list_pcd.append([val_x, val_y, val_z])
    return np.asarray(list_pcd)


def make_pcd(num_sample, num_pd, name_dir_data):
    val_r_small = 2
    name_dir_pcd = "%s/pcd3_sample%s_num%s" % (
        name_dir_data, num_sample, num_pd)
    functions.mkdir_pcd(name_dir_pcd)
    # "../torus/pcd3_sample500_num40/pcd_pd"

    for idx_num in range(num_pd):
        if idx_num % 10 == 0:
            print("pcd_%s" % idx_num)
        else:
            pass
        mat_pcd = make_torus(val_r_big=val_r_small * (0.5 + (idx_num / num_pd)),
                             val_r_small=val_r_small, num_sample=num_sample)

        np.savetxt("%s/pcd_pd/pcd_%s.txt" % (name_dir_pcd, idx_num),
                   mat_pcd, delimiter='\t')
        # "../torus/pcd3_sample500_num40/pcd_pd/pcd_3.txt"


def plot_pcd(num_sample, num_pd, name_dir_data):
    print("saving pcd as png")
    val_r_small = 2
    name_dir_plot = "%s/plot_pcd3__sample%s_num%s" % (
        name_dir_data, num_sample, num_pd)
    functions.mkdir_os(name_dir_plot)
    # "../torus/plot_pcd3_sample500_num40"

    for idx_num in range(num_pd):
        mat_pcd = make_torus(val_r_big=val_r_small * (0.5 + (idx_num / num_pd)),
                             val_r_small=val_r_small, num_sample=num_sample)

        functions.plot_pcd(
            mat_pcd, "%s/torus_%s.png" % (name_dir_plot, idx_num), markersize=2,
            z_lim=np.array([-1.5 * val_r_small, 1.5 * val_r_small]))
        # "../torus/plot_pcd3_sample500_num40/torus_3.png"
