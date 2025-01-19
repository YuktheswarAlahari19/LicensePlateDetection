import cv2

def process_image(img, model, reader):
    results = model(img)
    
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        
        for box in boxes:
            x1, y1, x2, y2 = map(int, box[:4])
            
            plate_img = img[y1:y2, x1:x2]
            ocr_result = reader.readtext(plate_img)
            
            if ocr_result:
                # Extract the text from the OCR result and convert it to a string
                text = str(ocr_result[0][1]) if ocr_result[0][1] else "Unknown"
                print(f"Detected license plate: {text}")
                
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
    
    return img
