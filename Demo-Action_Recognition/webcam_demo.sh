python webcam_demo.py \
configs/recognition/tsn/tsn_r50_video_inference_1x1x3_100e_kinetics400_rgb.py \
checkpoints/tsn_r50_1x1x3_100e_kinetics400_rgb_20200614-e508be42.pth \
demo/label_map_k400.txt \
--average-size 5 \
--threshold 0.2 \
--device cuda:0 \
