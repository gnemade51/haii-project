# haii-project

Open-source code imported:
DeOldify by Jantic is an open-source deep learning model designed for colorizing and restoring old images. In my project, I utilized this model to transform black and white images into colorized versions.
Source: https://github.com/jantic/DeOldify

What changes I made: 
- I adjusted the render_factor to experiment and find the optimal setting for the best results in my project.
- I converted the model into the .pth extension, which is part of the Python Torch library.

What new code I implemented.
- Initially, I developed a two page website using HTML and CSS. One is the homepage that would take user input in form of black and white images. While another is a results page that would display the colorized image to the user.
- Additionally, I developed a Python Flask app to host this model on a local server. This app is connected to my website, allowing users to input an image. By utilizing both get and post requests, the user-uploaded image is processed through my model to generate a colored image. The results are then showcased on the dedicated results page of the website.