from flask import Flask, render_template, request, jsonify
from skimage import io
from pyxelate import Pyx
import base64
import io as sysio

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/generate", methods=['POST'])
def generate_response():
    print(request.files)

    img_file = request.files['image']

    if img_file:
        print("### Reading image...")

        # Original image
        original_img = io.imread(img_file)
        
        img_bytes = sysio.BytesIO()
        io.imsave(img_bytes, original_img, format='PNG')
        img_bytes.seek(0)
        base64_image_ori = base64.b64encode(img_bytes.getvalue()).decode('utf-8')

        print("### Making image...")
        # Pixelated image
        downsample=10
        palette=10
        pixel_img_bytes = sysio.BytesIO()
        pyx = Pyx(factor=downsample, palette=palette, dither='none').fit_transform(original_img)
        io.imsave(pixel_img_bytes, pyx, format='PNG')
        pixel_img_bytes.seek(0)
        base64_image_pix = base64.b64encode(pixel_img_bytes.getvalue()).decode('utf-8')

        # Prepare response
        response = {
            'base64_image_original': base64_image_ori,
            'base64_image_pixelated': base64_image_pix
        }

        return jsonify(response)


if __name__ == "__main__":
    app.run()