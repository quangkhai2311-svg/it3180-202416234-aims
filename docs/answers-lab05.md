# Trả lời thảo luận Lab 05

## Upstream first so với release first
Upstream first sửa trên dòng mới trước rồi backport: giảm khả năng quên
sửa master nhưng có thể cần điều chỉnh cho mã cũ. Release first sửa ở đúng
bản phát hành bị lỗi trước: nhanh tái hiện/kiểm tra baseline cũ, nhưng phải
chủ động đưa bản sửa lên mọi dòng còn bị ảnh hưởng. Bài áp dụng release first.

## Quên lan truyền sang release/lab05, phát hiện bằng gì?
Chạy cùng kiểm tra tìm “lion” trên v1.0.1, v1.1.0 và master: dòng chưa được
sửa trả 0 thay vì 1. Trước khi gắn v1.1.0 có thể kiểm tra release/lab05.
Dùng `git cherry -v release/lab05 release/lab04` để kiểm tra patch tương đương.
`git tag --contains FIX_SHA` chỉ kiểm tra quan hệ tổ tiên: bản cherry-pick có
SHA khác nên không đủ để kết luận thiếu bản sửa ở dòng khác.

## Vì sao tách sửa lỗi và bump version?
Chỉ cherry-pick commit chứa search.py và test_search.py sang dòng 1.1.0.
Bump 1.0.1 và changelog của dòng 1.0.x ở commit khác để không hạ version mới.

## Vì sao chưa gắn v1.1.0 ở đầu Lab 05?
Chờ đưa hotfix vào baseline trước khi chốt. Nếu tag đã chia sẻ thì giữ nguyên
và phát hành 1.1.1 cho bản đã sửa, không xóa hoặc dời tag cũ.

## CI hỗ trợ gì?
CI chạy unittest cho PR để phát hiện lỗi trước khi tích hợp. Chỉ khi đã bật
required status check và không bypass thì CI đỏ mới thực sự chặn merge.
Có file workflow chưa đồng nghĩa đã bật cơ chế chặn trên GitHub.
