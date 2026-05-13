from flask import Flask, render_template, request, send_file
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_files():
    # Get uploaded files
    exe_file = request.files.get('exe_file')
    png_file = request.files.get('png_file')
    rar_file = request.files.get('rar_file')
    output_filename = request.form.get('output_filename')

    # Validate that all files are present
    if not exe_file or not png_file or not rar_file:
        return "Vui lòng chọn đủ 3 file (EXE, PNG, RAR/ZIP).", 400

    if not output_filename:
        return "Vui lòng nhập tên file đầu ra.", 400

    # Validate file extensions
    if not exe_file.filename.lower().endswith('.exe'):
        return "File 1 phải là file có phần mở rộng .exe", 400

    if not png_file.filename.lower().endswith('.png'):
        return "File 2 phải là file có phần mở rộng .png", 400

    if not (rar_file.filename.lower().endswith('.rar') or rar_file.filename.lower().endswith('.zip')):
        return "File 3 phải là file có phần mở rộng .rar hoặc .zip", 400

    try:
        # Read file contents into memory
        exe_bytes = exe_file.read()
        png_bytes = png_file.read()
        rar_bytes = rar_file.read()

        # Concatenate in order: EXE -> PNG -> RAR
        merged_bytes = exe_bytes + png_bytes + rar_bytes

        # Create a BytesIO object for sending
        merged_io = io.BytesIO(merged_bytes)
        merged_io.seek(0)

        # Send the merged file as download
        return send_file(
            merged_io,
            as_attachment=True,
            download_name=output_filename
        )
    except Exception as e:
        return f"Lỗi khi xử lý file: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)