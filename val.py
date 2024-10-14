from ultralytics import YOLO

if __name__ == '__main__':

    model = YOLO('FDADNet.pt')

    metrics = model.val(split='test', iou=0.5, batch=1, data='WBP-DET/data.yaml')
