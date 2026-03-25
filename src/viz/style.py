import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib as mpl


class viz:
    """Define the default visualize configure."""

    # basic
    Blue = np.array([46, 107, 149]) / 255
    new_blue = np.array([98, 138, 174]) / 255
    new_red = np.array([195, 102, 101]) / 255
    lBlue = np.array([241, 247, 248]) / 255
    lBlue2 = np.array([166, 201, 222]) / 255
    Green = np.array([8, 154, 133]) / 255
    lGreen = np.array([242, 251, 238]) / 255
    dRed = np.array([108, 14, 17]) / 255
    Red = np.array([199, 111, 132]) / 255
    lRed = np.array([253, 237, 237]) / 255
    lRed2 = np.array([249, 179, 173]) / 255
    dYellow = np.array([129, 119, 14]) / 255
    Yellow = np.array([220, 175, 106]) / 255
    lYellow2 = np.array([166, 201, 222]) / 255
    lYellow = np.array([252, 246, 238]) / 255
    Purple = np.array([108, 92, 231]) / 255
    ocGreen = np.array([90, 196, 164]) / 255
    oGrey = np.array([176, 166, 183]) / 255
    orange = np.array([228, 149, 92]) / 255
    Palette = [Blue, Yellow, Red, ocGreen, Purple, orange]

    # seaborn palette
    snsPalette = sns.color_palette("ch:s=-.2,r=.6", as_cmap=True)

    # addiction block,
    add_block = np.array([164, 221, 211]) / 255
    add_inter = np.array([249, 179, 173]) / 255
    add_palette = [add_block, add_inter]

    # pairs
    green1 = np.array([81, 121, 112]) / 255
    green2 = np.array([133, 168, 140]) / 255
    green3 = np.array([201, 210, 197]) / 255
    green4 = np.array([190, 176, 137]) / 255
    greenPairs = [green1, green2, green3, green4]

    # palette for agents
    b1 = np.array([43, 126, 164]) / 255
    r1 = np.array([249, 199, 79]) / 255
    r2 = np.array([228, 149, 92]) / 255
    r3 = np.array([206, 98, 105]) / 255
    m2 = np.array([188, 162, 149]) / 255
    g = np.array([0.7, 0.7, 0.7])
    Pal_agent = [b1, g, Red, r2, m2]

    # palette for block types
    dGreen = np.array([15, 93, 81]) / 255
    fsGreen = np.array([79, 157, 105]) / 255
    Ercu = np.array([190, 176, 137]) / 255
    Pal_type = [dGreen, fsGreen, Ercu]

    # Morandi
    m0 = np.array([101, 101, 101]) / 255
    m1 = np.array([171, 84, 90]) / 255
    m2 = np.array([188, 162, 149]) / 255
    Pal_fea = [m0, m1, m2]

    # lambda gradient
    lmbda0 = np.array([249, 219, 189]) / 255
    lmbda1 = np.array([255, 165, 171]) / 255
    lmbda2 = np.array([218, 98, 125]) / 255
    lmbda3 = np.array([165, 56, 96]) / 255
    lmbda4 = np.array([69, 9, 32]) / 255
    lmbda_gradient = [lmbda0, lmbda1, lmbda2, lmbda3, lmbda4]

    # task color
    color_task_a = np.array([249, 192, 138]) * 0.95 / 255
    color_task_b = np.array([159, 216, 195]) * 0.85 / 255

    # for insights
    BluesMap = matplotlib.colors.LinearSegmentedColormap.from_list("vizBlues", [lBlue, Blue])
    RedsMap = matplotlib.colors.LinearSegmentedColormap.from_list("vizReds", [lRed, dRed])
    YellowsMap = matplotlib.colors.LinearSegmentedColormap.from_list("vizYellows", [lYellow, orange])
    GreensMap = matplotlib.colors.LinearSegmentedColormap.from_list("vizGreens", [lGreen, Green])

    @staticmethod
    def get_style():
        # Larger scale for plots in notebooks
        sns.set_context("notebook")
        sns.set_style("ticks", {"axes.grid": False})
        mpl.rcParams["pdf.fonttype"] = 42
        mpl.rcParams["axes.spines.right"] = False
        mpl.rcParams["axes.spines.top"] = False
        mpl.rcParams["axes.linewidth"] = 1.75
        mpl.rcParams["axes.labelsize"] = 11
        mpl.rcParams["font.weight"] = "regular"
        mpl.rcParams["savefig.format"] = "pdf"
        mpl.rcParams["savefig.dpi"] = 300
        mpl.rcParams["figure.facecolor"] = "None"
        mpl.rcParams["figure.edgecolor"] = "None"
        mpl.rcParams["axes.facecolor"] = "None"
        mpl.rcParams["legend.frameon"] = False
        plt.rcParams["xtick.labelsize"] = 10
        plt.rcParams["ytick.labelsize"] = 10
        plt.rcParams["xtick.major.size"] = 3.5
        plt.rcParams["ytick.major.size"] = 3.5
        plt.rcParams["xtick.direction"] = "in"
        plt.rcParams["ytick.direction"] = "in"

    @staticmethod
    def violin(
        ax,                      # figure axis 
        data,                    # dataframe
        x,                       # x variable
        y,                       # y variable
        order,                   # order of the variables
        palette,                 # palette for the plot
        orient="v",              # orientation of the plot
        hue=None,                # hue variable
        hue_order=None,          # order of the hue variables
        shade_alpha=0.1,         # alpha of the shade
        scatter_size=7,          # size of the scatter points
        scatter_alpha=1,         # alpha of the scatter points
        scatter_lw=0,            # line width of the scatter points
        scatter_edge_color="w",  # edge color of the scatter points
        scatter_type="swarm",    # type of the scatter points
        mean_marker_size=6,      # size of the mean marker
        error_capsize=0.11,      # cap size of the error bars
        add_errs=True,           # whether to add error bars
        errorbar=("ci", 95),     # type of error bars
        error_color=[0.3] * 3,   # color of the error bars
        error_lw=2,              # line width of the error bars
    ):
        g_var = y if orient == "h" else x
        v_var = x if orient == "h" else y
        v = sns.violinplot(
            data=data,
            x=x,
            y=y,
            order=order,
            hue=g_var if hue is None else hue,
            hue_order=order if hue is None else hue_order,
            orient=orient,
            palette=palette,
            legend=False,
            alpha=shade_alpha,
            inner=None,
            density_norm="width",
            ax=ax,
        )
        plt.setp(v.collections, alpha=0.5, edgecolor="none")
        if scatter_type == "strip":
            sns.stripplot(
                data=data,
                x=x,
                y=y,
                order=order,
                hue=g_var if hue is None else hue,
                hue_order=order if hue is None else hue_order,
                orient=orient,
                palette=palette,
                size=scatter_size,
                linewidth=scatter_lw,
                edgecolor=scatter_edge_color,
                jitter=True,
                alpha=scatter_alpha,
                dodge=False if hue is None else True,
                legend=False,
                zorder=2,
                ax=ax,
            )
        elif scatter_type == "swarm":
            sns.swarmplot(
                data=data,
                x=x,
                y=y,
                order=order,
                orient=orient,
                hue=g_var if hue is None else hue,
                hue_order=order if hue is None else hue_order,
                palette=palette,
                size=scatter_size,
                edgecolor=scatter_edge_color,
                alpha=scatter_alpha,
                dodge=False if hue is None else True,
                legend=False,
                zorder=2,
                ax=ax,
            )

        if add_errs:
            groupby = [g_var, hue] if hue is not None else [g_var]
            sns.barplot(
                data=data,
                x=x,
                y=y,
                order=order,
                orient=orient,
                hue=g_var if hue is None else hue,
                hue_order=order if hue is None else hue_order,
                errorbar=errorbar,
                linewidth=1,
                legend=False,
                edgecolor=(0, 0, 0, 0),
                facecolor=(0, 0, 0, 0),
                capsize=error_capsize,
                err_kws={"color": error_color, "linewidth": error_lw, "solid_capstyle": "projecting"},
                ax=ax,
            )
            sns.stripplot(
                data=data.groupby(by=groupby)[v_var].mean().reset_index(),
                x=x,
                y=y,
                order=order,
                hue=hue,
                hue_order=hue_order,
                palette=[error_color] * len(hue_order) if hue is not None else None,
                dodge=False if hue is None else True,
                legend=False,
                marker="_",
                size=mean_marker_size,
                color=error_color,
                ax=ax,
            )

    @staticmethod
    def violin_with_tar(
        ax,                      # figure axis 
        data,                    # dataframe
        x,                       # x variable
        y,                       # y variable
        color,                   # color of the plot
        order,                   # order of the variables
        orient="v",              # orientation of the plot
        hue=None,                # hue variable
        hue_order=None,          # order of the hue variables
        shade_alpha=0.4,         # alpha of the shade
        scatter_size=4,          # size of the scatter points
        scatter_alpha=1,         # alpha of the scatter points
        mean_marker_size=6,      # size of the mean marker
        error_capsize=0.14,      # cap size of the error bars
        errorbar=("ci", 95),     # type of error bars
        error_lw=3,              # line width of the error bars
        error_color=[0.5] * 3,   # color of the error bars
    ):
        g_var = y if orient == "h" else x
        sns.violinplot(
            data=data,
            x=x,
            y=y,
            order=order,
            hue=g_var if hue is None else hue,
            hue_order=order if hue is None else hue_order,
            orient=orient,
            palette=[[0.9] * 3, color],
            legend=False,
            alpha=shade_alpha,
            inner=None,
            density_norm="width",
            edgecolor="none",
            gap=0.15,
            split=True,
            ax=ax,
        )
        sns.stripplot(
            data=data.query(f'{hue}=="{hue_order[0]}"'),
            x=x,
            y=y,
            order=order,
            hue=g_var if hue is None else hue,
            hue_order=order if hue is None else hue_order,
            orient=orient,
            palette=[color, [0.9] * 3],
            size=scatter_size,
            edgecolor="w",
            linewidth=0.5,
            jitter=True,
            alpha=scatter_alpha,
            dodge=True,
            legend=False,
            zorder=2,
            ax=ax,
        )
        point_palette = [error_color, color]
        sns.pointplot(
            data=data,
            x=x,
            y=y,
            order=order,
            orient=orient,
            hue=hue,
            hue_order=hue_order,
            legend=False,
            palette=point_palette,
            ls="none",
            dodge=0.4,
            errorbar=errorbar,
            marker="_",
            markeredgewidth=error_lw,
            markersize=mean_marker_size,
            capsize=error_capsize,
            err_kws={"linewidth": error_lw},
            ax=ax,
        )

