from ultralytics import YOLO


model = YOLO("runs/segment/train/weights/best.pt")


# To Test on CPU:
results = model.predict(source='./dataset/test/images',  conf = 0.5, save=True, show = False, save_txt = False, device='cpu')

print("done")