"""
 Generate the 3D  sparse face shape corresponding to  IBug 68 landmark model .The 3D shape are extracted from Surrey Face Model .
 (https://github.com/patrikhuber/eos)
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import eos

if __name__ == '__main__':

    sfm_model = eos.morphablemodel.load_model("./sfm_shape_3448.bin").get_shape_model()

    # Note the 61-th , 65-th indices are not defined .
    sfm_ibug_indice = [
        # 1 to 8 are the right contour landmarks
        380,
        356,
        359,
        365,
        364,
        391,
        393,
        21,

        # 9  =   33  # chin bottom
        33,

        # 10 to 17 are the left contour landmarks
        795,
        773,
        776,
        782,
        781,
        805,
        807,
        464,

        225,
        229,
        233,
        2086,  # right eyebrow between middle and inner corner
        157,  # right eyebrow inner-corner (19)
        590,  # left eyebrow inner-corner (23)
        2091,  # left eyebrow between inner corner and middle
        666,  # left eyebrow middle (24)
        662,  # left eyebrow between middle and outer corner
        658,  # left eyebrow outer-corner (22)
        2842,  # bridge of the nose (parallel to upper eye lids)
        379,  # middle of the nose, a bit below the lower eye lids
        272,  # above nose-tip (1cm or so)
        114,  # nose-tip (3)
        100,  # right nostril, below nose, nose-lip junction
        2794,  # nose-lip junction
        270,  # nose-lip junction (28)
        2797,  # nose-lip junction
        537,  # left nostril, below nose, nose-lip junction
        177,  # right eye outer-corner (1)
        172,  # right eye pupil top right (from subject's perspective)
        191,  # right eye pupil top left
        181,  # right eye inner-corner (5)
        173,  # right eye pupil bottom left
        174,  # right eye pupil bottom right
        614,  # left eye inner-corner (8)
        624,  # left eye pupil top right
        605,  # left eye pupil top left
        610,  # left eye outer-corner (2)
        607,  # left eye pupil bottom left
        606,  # left eye pupil bottom right
        398,  # right mouth corner (12)
        315,  # upper lip right top outer
        413,  # upper lip middle top right
        329,  # upper lip middle top (14)
        825,  # upper lip middle top left
        736,  # upper lip left top outer
        812,  # left mouth corner (13)
        841,  # lower lip left bottom outer
        693,  # lower lip middle bottom left
        411,  # lower lip middle bottom (17)
        264,  # lower lip middle bottom right
        431,  # lower lip right bottom outer

        # 61 not defined - would be right inner corner of the mouth

        416,  # upper lip right bottom outer
        423,  # upper lip middle bottom
        828,  # upper lip left bottom outer

        # 65 not defined - would be left inner corner of the mouth

        817,  # lower lip left top outer
        442,  # lower lip middle top
        404,  # lower lip right top outer
    ]

    all_pts = []
    for i in range(0, len(sfm_ibug_indice)):
        pts_= sfm_model.get_mean_at_point(sfm_ibug_indice[i])
        all_pts.append(pts_)
    all_pts = np.array(all_pts)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range( all_pts.shape[0] ):
        ax.scatter(all_pts[i,0], all_pts[i,1], all_pts[i,2])  # plot the point (2,3,4) on the figure
    plt.show()