from ultralytics import YOLO

if __name__ == '__main__':

    model = YOLO('model/FDADNet.yaml')

    model.train(data=r"WBP-DET/data.yaml", epochs=400, device=[0], iou=0.5)