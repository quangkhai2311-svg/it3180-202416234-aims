# AIMS-mini — IT3180

Ứng dụng Python mẫu cho 5 lab Git/GitHub: refactor, feature/topic, bugfix, release và hotfix.

- GitHub: [quangkhai2311-svg](https://github.com/quangkhai2311-svg)
- Họ tên/MSSV: chưa cung cấp; cần bổ sung trước khi nộp bài.
- Thực hiện một mình: approvals = 0; chưa có review từ partner.
- Kết nối hiện tại dùng HTTPS qua GitHub CLI; bước SSH key trong Lab 01 chưa thực hiện.

## Chạy và kiểm thử

Yêu cầu Python >= 3.10; chỉ dùng thư viện chuẩn.

```bash
python3 main.py
python3 -m unittest discover -s tests -v
```

Trên master: banner `AIMS-mini v1.1.0`, tổng tiền `63.89 $`, 8 tests OK.
GitHub Actions chạy test với Python 3.12; required check `test` bảo vệ master.

## Các phiên bản

| Mốc | Nội dung |
|---|---|
| release/lab01, v0.1.0 | Package aims; refactor qua PR |
| release/lab02, v0.2.0 | In giỏ, tìm title, use case; ba kiểu merge |
| release/lab03, v0.3.0 | Fix giới hạn, discount, conflict và revert; 4 test |
| v1.0.0 | Baseline Lab 04; 5 test; search title còn phân biệt hoa thường |
| release/lab04, v1.0.1 | Bản vá tìm title không phân biệt hoa thường; 5 test |
| release/lab05, v1.1.0 | Sort, tìm category và nhận hotfix; 8 test |

Tag giữ phiên bản chính xác; nhánh release có thể tiến lên khi hotfix.
Không merge release ngược vào master; cherry-pick -x riêng commit sửa lỗi.

## Xem lại một phiên bản

```bash
git worktree add ../aims-v1.0.1 v1.0.1
cd ../aims-v1.0.1
python3 main.py
python3 -m unittest discover -s tests -v
```

## Tài liệu và minh chứng

- [Kết quả thực hành và link PR/CI](docs/ket-qua-thuc-hanh.md)
- [Use case](docs/use-case.md)
- Trả lời thảo luận: [Lab 01](docs/answers-lab01.md), [Lab 02](docs/answers-lab02.md), [Lab 03](docs/answers-lab03.md), [Lab 04](docs/answers-lab04.md), [Lab 05](docs/answers-lab05.md).
- [Releases](https://github.com/quangkhai2311-svg/it3180-aims/releases)

PR CI demo cố ý làm sai đã đóng, không merge. Đọc kỹ các câu trả lời, bổ sung
thông tin sinh viên và nộp link repo trên LMS theo yêu cầu lớp.
