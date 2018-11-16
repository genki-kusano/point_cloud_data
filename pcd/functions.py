from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os


def mkdir_os(name_dir_save):
    if not os.path.exists(name_dir_save):
        os.mkdir(name_dir_save)


def mkdir_pcd(name_dir_pcd):
    mkdir_os(name_dir_pcd)
    name_dir_homcloud = "%s/pcd_pd" % name_dir_pcd
    mkdir_os(name_dir_homcloud)


def plot_pcd(mat_pcd, name_save, markersize=2, x_lim=None, y_lim=None,
                    z_lim=None):
    num_pcd, dim_pcd = mat_pcd.shape
    if dim_pcd == 2:
        plt.figure()
        plt.plot(mat_pcd[:, 0], mat_pcd[:, 1], "bo", markersize=markersize)
        if x_lim is not None:
            plt.xlim(x_lim[0], x_lim[1])
        if y_lim is not None:
            plt.ylim(y_lim[0], y_lim[1])
        plt.savefig(name_save)
        plt.close()
    else:  # dim_pcd == 3
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot(mat_pcd[:, 0], mat_pcd[:, 1], mat_pcd[:, 2], "bo",
                markersize=markersize)
        if x_lim is not None:
            ax.set_xlim(x_lim[0], x_lim[1])
        if y_lim is not None:
            ax.set_ylim(y_lim[0], y_lim[1])
        if z_lim is not None:
            ax.set_zlim(z_lim[0], z_lim[1])
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        plt.savefig(name_save)
        plt.close()
