from ThreeDTool import *

tr = trajectory_generate(h=1, line_width=0.2)

ps = np.array([[0.2, -0.1, 0],
               [1, 0, 0],
               [1, 1, 0]])
pol = Polygon(ps)

points = tr.T

tr2 = line_segments_array_create_from_points(tr.T)

tr3 = trajectories_intersection_create(pol, tr2)

dp2 = Dspl(np.hstack([tr3, tr2, pol]))
dp2.show()
