# Polyglot File Merger

Một ứng dụng web nội bộ bằng Flask để ghép 3 file (exe, png, rar/zip) thành một file duyệt theo thứ tự nhị phân: EXE -> PNG -> RAR.

## Yêu cầu

- Python 3.x
- pip

## Cài đặt

1. Clone hoặc tải xuống mã nguồn này.
2. Điều hướng đến thư mục dự án.
3. Cài đặt các phụ thuộc:

```bash
pip install -r requirements.txt
```

## Chạy ứng dụng

```bash
python app.py
```

Ứng dụng sẽ chạy tại `http://127.0.0.1:5000`.

## Sử dụng

1. Mở trình duyệt và truy cập `http://127.0.0.1:5000`.
2. Chọn file .exe, file .png và file .rar hoặc .zip.
3. Nhập tên file đầu ra (ví dụ: `final_output.png`).
4. Nhấn nút "Merge Files".
5. Tệp đã ghép sẽ được tự động tải xuống.

## Lưu ý

- Tệp đầu ra có thể bị trình duyệt hoặc phần mềm antivirus chặn vì chứa mã thực thi ẩn.
- Ứng dụng này chỉ dành cho mục đích giáo dục và thử nghiệm nội bộ.

## Cấu trúc thư mục

```
.
├── app.py
├── requirements.txt
├── README.md
└── templates
    └── index.html
```

## Giấy phép

Este proyecto está bajo la Licencia MIT.