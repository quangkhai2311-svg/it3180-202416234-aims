# Trả lời thảo luận Lab 01

## Cấu hình global và local khác nhau thế nào?
`--global` áp dụng cho tài khoản người dùng trên máy (thường ở ~/.gitconfig;
cũng có thể dùng đường dẫn XDG). `--local` chỉ áp dụng repo hiện tại,
lưu ở .git/config và ưu tiên hơn global cho cùng khóa. Dùng
`git config --list --show-origin` để xem đường dẫn thực tế.

## Vì sao dùng git mv?
Lệnh này vừa đổi vị trí tệp trong working tree vừa stage thay đổi. Git không
lưu một thuộc tính “rename” riêng; khi diff, Git suy luận đổi tên từ độ giống
nhau của nội dung. Vì vậy `mv` rồi `git add -A` cũng có thể được nhận là rename.
`git log --follow -- aims/cart.py` giúp xem lịch sử qua lần đổi tên.

## release/lab01 có phải baseline?
Có. Nhánh ghi nhận mốc bài nộp đã được tích hợp và kiểm tra. Đầu nhánh có thể
thay đổi khi sửa bài theo hotfix; annotated tag bổ sung định danh bất biến
cho chính xác phiên bản ở thời điểm phát hành.

## Vì sao vẫn dùng PR khi làm một mình?
PR ghi lại mục đích, diff, kiểm tra và quyết định tích hợp; giúp tự review và
để sau này áp dụng cùng quy trình khi có người khác cùng làm.
