import numpy as np
import scipy.spatial.transform.rotation as R
import itertools

vec = [404,-588,-901]

rotated_vectors = []

rotation_axis = np.array(list(itertools.product((1,0), repeat=3)))
for axis in rotation_axis:
    for rotation_degrees in [90, 180, 270]:
        rotation_radians = np.radians(rotation_degrees)
        rotation_vector = rotation_radians * axis
        rotation = R.Rotation.from_rotvec(rotation_vector)
        rotated_vec = rotation.apply(vec)
        rotated_vectors.append(rotated_vec)