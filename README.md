# 🛡️ Ứng dụng mô hình Transformer trong phát hiện hành vi Phishing Email

## 📚 Giới thiệu đề tài
Phishing email (thư lừa đảo) là một trong những hình thức tấn công mạng phổ biến nhằm đánh cắp thông tin cá nhân, tài khoản hoặc tài chính. Việc phát hiện và phân loại các email độc hại một cách tự động là bài toán quan trọng trong lĩnh vực bảo mật thông tin.

Trong đồ án này, nhóm 13 đã xây dựng một mô hình học sâu dựa trên kiến trúc **Transformer** để nhận diện email lừa đảo từ nội dung URL.

---

## 👥 Nhóm thực hiện

- Nguyễn Thành Nhân
- Đặng Mạng Hoàng
- Nguyễn Việt Hưng
- Phạm Thành Thắng

---

## 🧠 Mô hình sử dụng

- Kiến trúc: **Transformer Encoder**
- Gồm các thành phần:
  - `Embedding` kết hợp `Positional Encoding`
  - `Multi-Head Self-Attention`
  - `Feed-Forward Network`
  - `Layer Normalization` + `Residual Connections`
- Đầu ra: lớp `Dense` với hàm `sigmoid` cho bài toán phân loại nhị phân (Phishing / Legitimate)

---

## 🛠️ Công nghệ & thư viện

| Công cụ           | Phiên bản / Ghi chú     |
|------------------|-------------------------|
| Python           | 3.10 (Anaconda)         |
| TensorFlow       | 2.x                     |
| Flask            | Demo API local          |
| Scikit-learn     | train/test split, metrics |
| Imbalanced-learn | ADASYN                  |
| Matplotlib       | Trực quan hóa dữ liệu   |

---
