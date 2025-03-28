"""
author: hova88
date: 2021/03/16
"""
import numpy as np
from visual_tools import draw_clouds_with_boxes
import open3d as o3d
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--cloud_path', type=str, default='../data/test/000000.bin')
parser.add_argument('--boxes_path', type=str, default='../data/test/000000.txt')
parser.add_argument('--score_thr', type=float, default=0.1)
parser.add_argument('--verbose', action='store_true')
parser.add_argument('--draw_arrow', action='store_true')

if __name__ == "__main__":
    args = parser.parse_args()
    cloud_path = args.cloud_path
    boxes_path = args.boxes_path
    score_thr = args.score_thr

    print("Score threshold:", score_thr)

    cloud = np.fromfile(cloud_path, dtype=np.float32).reshape(-1,4)
    boxes = np.loadtxt(boxes_path).reshape(-1,9)
    boxes = boxes[boxes[:, -1] > score_thr][:, :7]
    
    classes = boxes[:, -2].astype(int)  # Second last column

    draw_clouds_with_boxes(cloud, boxes, classes, draw_arrow=args.draw_arrow, verbose=args.verbose)
