import io

from flask import Flask, render_template, send_file, request

from main import strategies_infographic_fn

app = Flask(__name__)

ETHPASER_URL = "https://ethparser-api.herokuapp.com"

@app.route('/')
def base():
    return render_template('base.html')

def serve_pil_image(pil_img):
    img_io = io.StringIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

@app.route('/strategies_infographic')
def strategies_infographic_gen():
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')

    image = strategies_infographic_fn(from_date, to_date, ETHPASER_URL)
    buf = io.BytesIO()
    image.save(buf, format='JPEG')
    byte_im = buf.getvalue()

    return send_file(
        io.BytesIO(byte_im),
        mimetype='image/jpeg',
        as_attachment=True,
        attachment_filename='strategies_infographic.jpg')


if __name__ == '__main__':
    app.run(threaded=True, port=5000)