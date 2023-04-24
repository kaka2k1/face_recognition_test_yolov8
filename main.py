from ultralytics import YOLO
model = YOLO("./yolov8-mask.pt")
results = model.predict(source= 0, show = True)
