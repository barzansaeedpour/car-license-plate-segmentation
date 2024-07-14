from ultralytics import YOLO


model = YOLO("yolov8n-seg.pt")


# To train on CPU:
results = model.train(data='./dataset/data.yaml',task="segment", epochs=50, imgsz=300, batch=2, device='cpu')

print("done")