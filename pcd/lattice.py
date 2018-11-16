import numpy as np
import functions


def measure_square(val_radius, dim_pcd):
    vec = np.empty(dim_pcd)
    for i in range(dim_pcd):
        vec[i] = np.random.uniform(-1 * val_radius, val_radius)
    return vec


def measure_circle(val_radius, dim_pcd):
    vec = np.random.randn(dim_pcd)
    r = np.linalg.norm(vec)
    if r != 0:
        vec /= r
    return val_radius * vec * np.power(np.random.random(), 1 / dim_pcd)


def measure_gauss(val_sigma, dim_pcd):
    vac_mean = np.zeros(dim_pcd)
    mat_cov = np.diag(np.ones(dim_pcd) * (val_sigma ** 2))
    return np.random.multivariate_normal(vac_mean, mat_cov)


def measure(name_measure, val_radius, dim_pcd):
    if name_measure == "gauss":
        return measure_gauss(val_radius, dim_pcd)
    elif name_measure == "circle":
        return measure_circle(val_radius, dim_pcd)
    else:  # uniform on square
        return measure_square(val_radius, dim_pcd)


def make_lattice(num_side, dim_pcd):
    list_lat = []
    if dim_pcd == 3:
        for i in range(num_side):
            for j in range(num_side):
                for k in range(num_side):
                    list_lat.append([i, j, k])
    else:  # dim_pcd = 2
        for i in range(num_side):
            for j in range(num_side):
                list_lat.append([i, j])
    return list_lat


def make_pcd(list_param, dim_pcd, num_side, num_pd, name_dir_data):
    num_param = len(list_param)
    for idx_param in range(num_param):

        name_dir_pcd = "%s/pcd%s_side%s_%s%03d_num%s" % (
            name_dir_data, dim_pcd, num_side, list_param[idx_param][0],
            list_param[idx_param][1] * 100, num_pd)
        functions.mkdir_pcd(name_dir_pcd)
        # "../lattice/pcd2_side20_square010_num100/pcd_pd"

        for idx_num in range(num_pd):
            if idx_num % 10 == 0:
                print("pcd_%s" % idx_num)
            else:
                pass
            list_pcd = make_lattice(num_side, dim_pcd)
            num_pcd = len(list_pcd)
            for idx_point in range(num_pcd):
                list_pcd[idx_point] += measure(list_param[idx_param][0],
                                               list_param[idx_param][1],
                                               dim_pcd)

            np.savetxt("%s/pcd_pd/pcd_%s.txt" % (name_dir_pcd, idx_num),
                       np.asarray(list_pcd), delimiter='\t')
            # "../lattice/pcd2_side20_square010_num100/pcd_pd/pcd_3.txt"


def plot_pcd(list_param, dim_pcd, num_side, num_pd, name_dir_data):
    print("saving pcd as png")
    num_param = len(list_param)
    for idx_param in range(num_param):
        name_dir_plot = "%s/plot_pcd%s_side%s_num%s" % (
            name_dir_data, dim_pcd, num_side, num_pd)
        functions.mkdir_os(name_dir_plot)
        # "../lattice/plot_pcd2_side20_num20"

        for idx_num in range(num_pd):
            list_pcd = make_lattice(num_side, dim_pcd)
            num_pcd = len(list_pcd)
            for idx_point in range(num_pcd):
                list_pcd[idx_point] += measure(list_param[idx_param][0],
                                               list_param[idx_param][1],
                                               dim_pcd)
            vec_lim = np.array([-1, num_side])
            functions.plot_pcd(np.asarray(list_pcd), "%s/%s%03d_%s.png" % (
                    name_dir_plot, list_param[idx_param][0],
                    list_param[idx_param][1] * 100, idx_num),
                               x_lim=vec_lim, y_lim=vec_lim, z_lim=vec_lim)
            # "../lattice/plot_pcd2_side20_num20/square010_3.png"
