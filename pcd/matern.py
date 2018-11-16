import numpy as np
import functions


def poisson_pp(num_intensity, dim_pcd):
    num_poisson = np.random.poisson(num_intensity)
    x = np.random.uniform(0, 1, num_poisson)
    y = np.random.uniform(0, 1, num_poisson)
    mat = np.c_[x, y]
    if dim_pcd == 3:
        z = np.random.uniform(0, 1, num_poisson)
        mat = np.c_[mat, z]
    return mat


def matern_one_pp(mat_pcd, val_radius):
    num_points = mat_pcd.shape[0]
    list_thin = []
    for i in range(num_points):
        for j in range(num_points):
            r = np.linalg.norm(mat_pcd[i] - mat_pcd[j])
            if 0 < r < val_radius:
                list_thin.append(i)
                break
    return np.delete(mat_pcd, list_thin, 0)


def matern_two_pp(mat_pcd, val_radius):
    num_points = mat_pcd.shape[0]
    vec_weight = np.random.uniform(0, 1, num_points)

    list_thin = []
    for i in range(num_points):
        for j in range(num_points):
            r = np.linalg.norm(mat_pcd[i] - mat_pcd[j])
            t = vec_weight[i] - vec_weight[j]
            if (0 < r < val_radius) and (t < 0):
                list_thin.append(i)
                break

    return np.delete(mat_pcd, list_thin, 0)


def make_pcd(dim_pcd, num_intensity, val_radius, num_pd, name_dir_data):
    name_dir_pcd = "%s/pcd%s_intensity%s_radius%03d_num%s" % (
        name_dir_data, dim_pcd, num_intensity, val_radius * 100, num_pd)
    functions.mkdir_os(name_dir_pcd)
    # "../matern/pcd2_intensity200_radius003_num100"

    for i in range(3):
        functions.mkdir_pcd("%s/type%s" % (name_dir_pcd, i))
        # "../matern/pcd2_intensity200_radius003_num100/type0/pcd_pd"

    for idx_num in range(num_pd):
        if idx_num % 10 == 0:
            print("pcd_%s" % idx_num)
        else:
            pass
        mat_pcd_poisson = poisson_pp(num_intensity, dim_pcd)
        mat_pcd_matern_one = matern_one_pp(mat_pcd_poisson, val_radius)
        mat_pcd_matern_two = matern_two_pp(mat_pcd_poisson, val_radius)

        np.savetxt("%s/type0/pcd_pd/pcd_%s.txt" % (name_dir_pcd, idx_num),
                   mat_pcd_poisson, delimiter='\t')
        np.savetxt("%s/type1/pcd_pd/pcd_%s.txt" % (name_dir_pcd, idx_num),
                   mat_pcd_matern_one, delimiter='\t')
        np.savetxt("%s/type2/pcd_pd/pcd_%s.txt" % (name_dir_pcd, idx_num),
                   mat_pcd_matern_two, delimiter='\t')
        # "../matern/pcd2_intensity200_radius003_num100/type0/
        # pcd_pd/pcd_3.txt"


def plot_pcd(dim_pcd, num_intensity, val_radius, num_pd, name_dir_data):
    print("saving pcd as png")
    name_dir_plot = "%s/plot_pcd%s_intensity%s_radius%03d_num%s" % (
        name_dir_data, dim_pcd, num_intensity, val_radius * 100, num_pd)

    functions.mkdir_os(name_dir_plot)
    # "../matern/plot_pcd2_intensity200_radius003_num10"

    for idx_num in range(num_pd):
        mat_pcd_poisson = poisson_pp(num_intensity, dim_pcd)
        mat_pcd_matern_one = matern_one_pp(mat_pcd_poisson, val_radius)
        mat_pcd_matern_two = matern_two_pp(mat_pcd_poisson, val_radius)

        vec_lim = np.array([-0.1, 1.1])
        functions.plot_pcd(
            mat_pcd_poisson, "%s/type0_%s.png" % (name_dir_plot, idx_num),
            x_lim=vec_lim, y_lim=vec_lim, z_lim=vec_lim)
        functions.plot_pcd(
            mat_pcd_matern_one, "%s/type1_%s.png" % (name_dir_plot, idx_num),
            x_lim=vec_lim, y_lim=vec_lim, z_lim=vec_lim)
        functions.plot_pcd(
            mat_pcd_matern_two, "%s/type2_%s.png" % (name_dir_plot, idx_num),
            x_lim=vec_lim, y_lim=vec_lim, z_lim=vec_lim)
        # "../matern/plot_pcd2_intensity200_radius003_num10/
        # type1_3.png"
