import matplotlib.pyplot as plt
import matplotlib.colors

import argparse
import os
import numpy as np

# original functions
import functions


def make_list_pd(name_dir_pcd, num_pd, dim_pd, scale=True):
    list_pd = []
    for k in range(num_pd):
        mat_pd = np.loadtxt("%s/pcd_pd/dim%s_%s.txt" % (
            name_dir_pcd, dim_pd, k)).reshape(-1, 2)
        # "../lattice/pcd2_side20_square010_num100/pcd_pd/dim1_2.txt"
        if scale:  # scaling to (b^2,d^2) to (b,d)
            list_pd.append(np.sqrt(mat_pd))
        else:  # CGAL uses (b^2,d^2)-coordinate as default
            list_pd.append(mat_pd)
    return list_pd


def plot_pd(name_dir_plot, name_pcd, list_pd, vec_range=None):
    functions.mkdir_os(name_dir_plot)
    # "../lattice/plot_pd1_pcd2_side20_square010_num100"

    num_pd = len(list_pd)
    if vec_range is None:
        vec_min = np.empty(num_pd)
        vec_max = np.empty(num_pd)
        for _k in range(num_pd):
            mat_pd = list_pd[_k]
            vec_min[_k] = np.min(mat_pd[:, 0])
            vec_max[_k] = np.max(mat_pd[:, 1])
        val_min = np.min(vec_min)
        val_max = np.max(vec_max)
    else:
        val_min, val_max = vec_range

    val_pers = val_max - val_min
    val_ratio = 0.2
    val_min -= val_ratio * val_pers
    val_max += val_ratio * val_pers

    for k in range(num_pd):
        mat_pd = list_pd[k]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        hist = ax.hist2d(mat_pd[:, 0], mat_pd[:, 1],
                         bins=[np.linspace(val_min, val_max, 80),
                               np.linspace(val_min, val_max, 80)],
                         norm=matplotlib.colors.LogNorm())

        num_multiplicity = int(hist[1].max() + 1)
        if num_multiplicity > 3:
            hist[3].set_clim(1, num_multiplicity)
        else:
            hist[3].set_clim(1, int(10 ** num_multiplicity))
        fig.colorbar(hist[3], ax=ax)

        x = np.linspace(val_min, val_max, 2)
        plt.plot(x, x, "k-", linewidth=0.3)
        plt.savefig("%s/%s_%s.png" % (
            name_dir_plot, name_pcd, k))
        # "../lattice/plot_pd1_pcd2_side20_square010_num100/square010_3.png"
        plt.close()


def main():
    print("saving pd as png")
    parser = argparse.ArgumentParser()
    parser.add_argument("--path",
                        default="%s/Desktop/data_tda" % os.path.expanduser('~'))
    parser.add_argument("--data", default="lattice",
                        choices=["lattice", "matern", "circle", "torus"])
    parser.add_argument("--num_pd", default=100, type=int)
    parser.add_argument("--dim_pcd", default=2, type=int)
    parser.add_argument("--scale", default=True,
                        help="do you scale squared birth-death coordinates?")
    parser.add_argument("--side", default=20, type=int, help="for lattice")
    parser.add_argument("--intensity", default=100, type=int, help="for matern")
    parser.add_argument("--radius", default=0.03, type=float, help="for matern")
    parser.add_argument("--sample", default=500, type=int, help="for torus")
    parser.add_argument("--dim_pd", default=1, type=int, help="for plot")
    parser.add_argument("--num_plot", default=10, type=int, help="for plot")

    args = parser.parse_args()
    name_dir = args.path
    name_data = args.data
    num_pd = args.num_pd
    num_plot = args.num_plot
    dim_pcd = args.dim_pcd
    dim_pd = args.dim_pd
    scale = args.scale

    num_side = args.side
    num_intensity = args.intensity
    val_radius = args.radius
    num_sample = args.sample

    name_dir_data = "%s/%s" % (name_dir, name_data)

    if name_data == "lattice":
        list_param = [["gauss", 0.10]]
        list_param.extend([["square", np.sqrt(i + 2) * 0.10] for i in range(3)])
        name_dir_plot = "%s/plot_pd%s_pcd%s_side%s_num%s" % (
            name_dir_data, dim_pd, dim_pcd, num_side, num_pd)
        functions.mkdir_os(name_dir_plot)
        # "../lattice/plot_pd1_pcd2_side20_num100"
        for i in range(4):
            name_pcd = "%s%03d" % (list_param[i][0], list_param[i][1] * 100)
            name_dir_pcd = "%s/pcd%s_side%s_%s_num%s" % (
                name_dir_data, dim_pcd, num_side, name_pcd, num_pd)
            # "../lattice/pcd2_side20_square010_num100"
            list_pd = make_list_pd(name_dir_pcd, num_plot, dim_pd, scale=scale)
            plot_pd(name_dir_plot, name_pcd, list_pd,
                    vec_range=np.array([0.4, 0.8]))
            # "../lattice/plot_pd1_pcd2_side20_num10/square010_3.png"

    elif name_data == "matern":
        name_dir_plot = "%s/plot_pd%s_pcd%s_intensity%s_radius%03d_num%s" % (
            name_dir_data, dim_pd, dim_pcd, num_intensity, val_radius * 100,
            num_pd)
        functions.mkdir_os(name_dir_plot)
        # "../matern/plot_pd1_pcd2_intensity200_radius003_num100
        for i in range(3):
            name_dir_pcd = "%s/pcd%s_intensity%s_radius%03d_num%s/type%s" % (
                name_dir_data, dim_pcd, num_intensity, val_radius * 100, num_pd,
                i)
            # "../matern/pcd2_intensity200_radius003_num100"
            list_pd = make_list_pd(name_dir_pcd, num_plot, dim_pd, scale=scale)
            plot_pd(name_dir_plot, "type%s" % i, list_pd,
                    vec_range=np.array([0, 0.15]))
            # "../matern/pcd2_intensity200_radius003_num100/type1_3.png"

    elif name_data == "circle":
        name_dir_plot = "%s/plot_pd%s_pcd3_num%s" % (
            name_dir_data, dim_pd, num_pd)
        functions.mkdir_os(name_dir_plot)
        # "../circle/plot_pd1_pcd3_num200"
        name_dir_pcd = "%s/pcd3_num%s" % (name_dir_data, num_pd)
        # "../circle/pcd3_num200"
        list_pd = make_list_pd(name_dir_pcd, num_plot, dim_pd, scale=scale)
        plot_pd(name_dir_plot, "cricle", list_pd,
                vec_range=np.array([0, 15]))

    elif name_data == "torus":
        name_dir_plot = "%s/plot_pd%s_pcd3_sample%s_num%s" % (
            name_dir_data, dim_pd, num_sample, num_pd)
        functions.mkdir_os(name_dir_plot)
        # "../torus/plot_pd1_pcd3_sample500_num40/pcd_pd"
        name_dir_pcd = "%s/pcd3_sample%s_num%s" % (
            name_dir_data, num_sample, num_pd)
        # "../torus/pcd3_sample500_num40/pcd_pd"
        list_pd = make_list_pd(name_dir_pcd, num_plot, dim_pd, scale=scale)
        plot_pd(name_dir_plot, "torus", list_pd,
                vec_range=np.array([0, 2]))

    else:
        pass


if __name__ == "__main__":
    main()
