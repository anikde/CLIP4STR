## Root path
```
/DATA1/ocrteam/anik/git/CLIP4STR
```

## Training Command
```
python train.py +experiment=vl4str
```

## Inference Command
```
python read.py --checkpoint=/DATA1/ocrteam/anik/git/CLIP4STR/output/vl4str_2024-11-14_17-36-29/checkpoints/last.ckpt --images_path=/DATA1/ocrteam/anik/splitonBSTD/recognition/test/meitei
```