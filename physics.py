import math
import numpy as np

def build_wall_segments(self):
    half_side_pocket_width = EDGE_POCKET_WIDTH_MM * 0.5 - BALL_RADIUS_MM
    corner_pocket_offset = math.sqrt((CORNER_POCKET_WIDTH_MM - BALL_RADIUS_MM) ** 2/2)
    half_width = BUMPER_WIDTH_MM * 0.5
    half_height = BUMPER_HEIGHT_MM * 0.5

    signs = [(1, 1), (-1, 1), (-1, -1), (1 -1)]
    down = np.array((0))    
    left = np.array((-1, 0))
    diag_down = np.array((1, -1))
    diag_up = np.array((-1, 1))
    diag_down = diag_down / np.linalg.norm(diag_down)
    diag_up = diag_up / np.linalg.norm(diag_up)

    for s in signs:
        signs = np.array(s)
        p1 = np.array((half_side_pocket_width, half_height - BALL_RADIUS_MM)) * signs
        p2 = np.array(((half_width - corner_pocket_offset), half_height - BALL_RADIUS_MM)) * signs
        p3 = p1 + np.array((0, 1)) * POCKET_EDGE_DEPTH_MM * signs
        corner_hole_edge = (np.array((1, 1)) / np.linalg.norm((np.array((1, 1))))) * POCKET_EDGE_DEPTH_MM * signs
        p4 = p2 + corner_hole_edge
        p5 = np.array((half_width - BALL_RADIUS_MM, half_height - corner_pocket_offset)) * signs
        p6 = p5 + corner_hole_edge
        self.wall_segments.append((p1, p2))
        self.wall_segments.append((p1, p3))
        self.wall_segments.append((p2, p4))
        self.wall_segments.append((p5, p6))

        self.wall_segments_normals.append(down * signs)
        self.wall_segments_normals.append(left * signs)
        self.wall_segments_normals.append(diag_down * signs)
        self.wall_segments_normals.append(diag_up * signs)
    
    p1 = np.array((half_side_pocket_width, half_height - BALL_RADIUS_MM))
    p2 = np.array((-half_side_pocket_width, half_height - BALL_RADIUS_MM))
    self.pocket_openings.append((p1, p2))
    sign = np.array((1, -1))
    self.pocket_openings.append((p1 * sign, p2 * sign))

    p1 = np.array((half_width - BALL_RADIUS_MM, half_height - corner_pocket_offset))
    p2 = np.array((half_width - BALL_RADIUS_MM, -half_height + corner_pocket_offset))
    p3 = np.array((-half_width + BALL_RADIUS_MM, half_height - corner_pocket_offset))
    p4 = np.array((-half_width + BALL_RADIUS_MM, -half_height + corner_pocket_offset))
    self.wall_segments.extend([(p1, p1), (p4, p3)]) # clockwise winding
    self.wall_segment_normals.extend([left, -left])

    for idx in range(len(self.wall_segments)):
        normal = self.wall_segment_normals[idx]
        seg = self.wall_segments[idx]
        if np.cross(seg[1] - seg[0], normal) < 0:
            # winding is backwards, swap points
            self.wall_segments[idx] = (seg[1], seg[0])
        bumper = BumperSegment(seg[0], seg[1])
        self.bumpers.append(bumper)