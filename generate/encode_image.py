import base64


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        base64_image = base64.b64encode(image_file.read()).decode("utf-8")
        image_url = f"data:image/jpeg;base64,{base64_image}"
        return image_url
    

    
