import argparse
import numpy as np
import os

# original functions
import functions
import lattice
import matern
import circle
import torus


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path",
                        default="%s/Desktop/data_tda" % os.path.expanduser('~'))
    parser.add_argument("--data", default="lattice",
                        choices=["lattice", "matern", "circle", "torus"])
    parser.add_argument("--num_pd", default=100, type=int)
    parser.add_argument("--dim_pcd", default=2, type=int)
    parser.add_argument("--side", default=20, type=int, help="for lattice")
    parser.add_argument("--intensity", default=100, type=int, help="for matern")
    parser.add_argument("--radius", default=0.03, type=float, help="for matern")
    parser.add_argument("--sample", default=500, type=int, help="for torus")

    args = parser.parse_args()
    name_dir = args.path
    name_data = args.data
    num_pd = args.num_pd
    dim_pcd = args.dim_pcd
    num_side = args.side
    num_intensity = args.intensity
    val_radius = args.radius
    num_sample = args.sample

    functions.mkdir_os(name_dir)
    name_dir_data = "%s/%s" % (name_dir, name_data)
    functions.mkdir_os(name_dir_data)

    if name_data == "lattice":
        list_param = [["gauss", 0.10]]
        list_param.extend([["square", np.sqrt(i + 2) * 0.10] for i in range(3)])
        lattice.make_pcd(list_param, dim_pcd, num_side, num_pd, name_dir_data)
        lattice.plot_pcd(list_param, dim_pcd, 5, 10, name_dir_data)

    elif name_data == "matern":
        matern.make_pcd(dim_pcd, num_intensity, val_radius, num_pd,
                        name_dir_data)
        matern.plot_pcd(dim_pcd, num_intensity, val_radius, 10, name_dir_data)

    elif name_data == "circle":
        circle.make_pcd(num_pd, name_dir_data)
        circle.plot_pcd(10, name_dir_data)

    elif name_data == "torus":
        torus.make_pcd(num_sample, num_pd, name_dir_data)
        torus.plot_pcd(num_sample, num_pd, name_dir_data)

    else:
        pass


if __name__ == "__main__":
    main()
