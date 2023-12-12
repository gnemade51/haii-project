from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify
import io
import os
import PIL.Image
from werkzeug.utils import secure_filename

from deoldify import device
from deoldify.device_id import DeviceId


from deoldify.visualize import *
import warnings

app = Flask(__name__)

#choices:  CPU, GPU0...GPU7
device.set(device=DeviceId.GPU0)

plt.style.use('dark_background')
torch.backends.cudnn.benchmark=True

warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

colorizer = get_image_colorizer(artistic=True)
render_factor=35 #NOTE:  Max is 45 with 11GB video cards. 35 is a good default

# Set up upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def get_uploaded_file(filename):
    print(app.root_path)
    filename = 'uploads/' + filename
    print(filename)
    return send_from_directory(app.root_path, filename)

@app.route('/result_images/<filename>')
def get_result_file(filename):
    print(app.root_path)
    filename = 'result_images/' + filename
    print(filename)
    return send_from_directory(app.root_path, filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        uploaded_file = request.files['file']

        if uploaded_file.filename == '':
            return redirect(request.url)
        
        if uploaded_file and allowed_file(uploaded_file.filename):
            # Save the uploaded file
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            # print(filename)
            # print(filepath)
            uploaded_file.save(filepath)

            # Colorize the image
            result_path = colorizer.plot_transformed_image(path=filepath, render_factor=render_factor, compare=True)
            # print(result_path)

            # Display the result
            return render_template('result.html', original_image=filename, result_image=os.path.basename(result_path))


    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
