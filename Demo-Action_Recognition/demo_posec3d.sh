python demo_posec3d.py test.mp4 demo/posec3d_demo.mp4 \
    --config configs/skeleton/posec3d/slowonly_r50_u48_240e_ntu120_xsub_keypoint.py \
    --checkpoint checkpoints/slowonly_r50_u48_240e_ntu120_xsub_keypoint-6736b03f.pth \
    --det-config demo/faster_rcnn_r50_fpn_2x_coco.py \
    --det-checkpoint checkpoints/faster_rcnn_r50_fpn_2x_coco_bbox_mAP-0.384_20200504_210434-a5d8aa15.pth \
    --det-score-thr 0.9 \
    --pose-config demo/hrnet_w32_coco_256x192.py \
    --pose-checkpoint checkpoints/hrnet_w32_coco_256x192-c78dce93_20200708.pth \
    --label-map demo/label_map_ntu120.txt