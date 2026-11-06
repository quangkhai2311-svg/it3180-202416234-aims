# Trả lời thảo luận Lab 04

## Vì sao chuẩn bị phiên bản trên master?
Version và changelog là thay đổi sản phẩm cần qua PR/review. Khi đã được
tích hợp, tạo release từ master để baseline có đầy đủ mã và tài liệu nhất quán.

## Vì sao không merge release/* vào master?
Theo quy trình học phần, nhánh release duy trì baseline cũ và có thể chứa
bump version riêng. Merge ngược kéo thay đổi không phù hợp vào dòng mới.
Chọn commit sửa lỗi cần lan truyền bằng cherry-pick -x để giữ dấu nguồn gốc.

## So sánh với GitFlow
GitFlow thường có main, develop và release, với các bước hợp nhất lại
những dòng thích hợp sau phát hành. Release Flow của bài dùng master làm
dòng tích hợp, release/labXX giữ bài nộp và lan truyền bản sửa có chọn lọc.
Đây là quy ước của học phần, không phải giới hạn kỹ thuật của Git.

## Vì sao 1.0.0 thay vì 0.4.0?
1.0.0 công bố API/hành vi được xem là ổn định. Đây là quyết định mức độ ổn
định, không phải vì đã hoàn thành bốn lab. Nếu chưa cam kết ổn định thì vẫn
có thể tiếp tục 0.y.z; trong bài, dùng 1.0.0 theo kế hoạch phát hành.

## Tag và nhánh release khác nhau thế nào?
Tag chỉ một phiên bản chính xác và không được di chuyển sau khi chia sẻ.
Nhánh có thể tiến lên khi hotfix. Vì vậy v1.0.0 vẫn giữ nguyên dù đầu nhánh
release/lab04 sau này ở v1.0.1.
