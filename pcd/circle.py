import numpy as np

# original functions
import functions


def make_circle(vec_center, val_radius, num_points):
    mat = np.empty((num_points, 3))
    for i in range(num_points):
        vec_grid = np.array(
            [np.cos(2 * np.pi * i / (num_points - 1)) * val_radius,
             np.sin(2 * np.pi * i / (num_points - 1)) * val_radius,
             np.random.uniform(0, 0.01)])
        mat[i, :] = np.array([vec_center[0], vec_center[1], 0]) + vec_grid
    return mat


def make_pcd(num_pd, name_dir_data):
    name_dir_pcd = "%s/pcd3_num%s" % (name_dir_data, num_pd)
    functions.mkdir_pcd(name_dir_pcd)
    # "../circle/pcd3_num200/pcd_pd"

    vec_label = np.ones(num_pd)
    for idx_num in range(num_pd):
        if idx_num % 10 == 0:
            print("pcd_%s" % idx_num)
        else:
            pass
        val_radius = 1 + 8 * np.power(np.random.uniform(0, 1), 2)
        vec_center = [1.5 * val_radius + np.power(np.random.uniform(0, 2), 2),
                      1.5 * val_radius + np.power(np.random.uniform(0, 2), 2)]
        num_points = int(np.ceil(
            np.random.randint(np.ceil(np.pi * val_radius / 2),
                              4 * np.pi * val_radius)) +
                         (2 * np.random.uniform(0, 1)))
        if num_points < 5:
            num_points = 5
        else:
            pass

        mat_pcd = make_circle(vec_center, val_radius, num_points)
        if np.random.rand(1) > 0.5:
            mat_pcd = np.r_[mat_pcd, make_circle([0, 0], 0.2, 10)]
        else:
            vec_label[idx_num] = -1

        np.savetxt("%s/pcd_pd/pcd_%s.txt" % (name_dir_pcd, idx_num),
                   mat_pcd, delimiter='\t')
        # "../circle/pcd3_data200/pcd_pd/pcd_3.txt"
    np.savetxt("%s/label_z2.txt" % name_dir_pcd, vec_label, delimiter='\t')


def plot_pcd(num_pd, name_dir_data):
    print("saving pcd as png")
    name_dir_plot = "%s/plot_pcd2_num%s" % (name_dir_data, num_pd)
    functions.mkdir_os(name_dir_plot)
    # "../circle/plot_pcd2_num200"

    for idx_num in range(num_pd):
        val_radius = 1 + 8 * np.power(np.random.uniform(0, 1), 2)
        vec_center = np.array(
            [np.power(np.random.uniform(0, 2), 2),
             np.power(np.random.uniform(0, 2), 2)]) + 1.5 * val_radius
        num_points = int(np.ceil(
            np.random.randint(np.ceil(np.pi * val_radius / 2),
                              4 * np.pi * val_radius)) +
                         (2 * np.random.uniform(0, 1)))
        if num_points < 4:
            num_points = 4
        else:
            pass

        mat_pcd = make_circle(vec_center, val_radius, num_points)
        idx_label = "f"
        if np.random.rand(1) > 0.5:
            idx_label = "t"
            mat_pcd = np.r_[mat_pcd, make_circle([0, 0], 0.2, 10)]
        else:
            pass

        vec_lim = np.array([-2, 15])
        functions.plot_pcd(mat_pcd[:, 0:2],
                           "%s/circle_%s_%s.png" % (
                               name_dir_plot, idx_label, idx_num),
                           markersize=2, x_lim=vec_lim, y_lim=vec_lim)
        # "../circle/plot_pcd2_num200/circle_1_label-1.png"
