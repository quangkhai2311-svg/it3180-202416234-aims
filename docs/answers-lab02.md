# Trả lời thảo luận Lab 02

## Vì sao đồng bộ master trước khi PR?
Nhánh được tạo từ master cũ có thể chưa chứa tính năng mới hoặc có xung đột.
Merge master vào nhánh rồi chạy chương trình/test kiểm tra trạng thái tích hợp.
Trên nhánh đã chia sẻ, merge tránh viết lại các commit mà người khác đang dùng.

## Khi nào không được rebase?
Không rebase master, release/* hoặc commit đã chia sẻ mà người khác dựa vào.
Trong bài này chỉ viết lại commit chưa chia sẻ. Rebase làm đổi SHA và có thể
khiến lịch sử của người cùng làm bị phân kỳ.

## feature/* khác topic/* thế nào?
feature/* tập trung vào tính năng người dùng, ví dụ in giỏ hàng. topic/* dành
cho chủ đề công việc như template PR, tài liệu hoặc cấu hình CI. Về kỹ thuật
Git không phân biệt hai loại tên này.

## Ba cách merge khác nhau thế nào?
Merge commit giữ commit của nhánh và tạo commit có hai parent. Squash đưa
toàn bộ thay đổi vào một commit mới. Rebase and merge phát lại commit trên
base, tạo lịch sử tuyến tính và SHA mới. Sau squash, `branch -d` có thể chưa
nhận nhánh đã merge; phải kiểm tra PR và thay đổi đã tích hợp trước khi xóa.

## Vì sao dismiss stale approvals?
Khi có commit mới, nội dung PR thay đổi; cần review lại để đúng nội dung
được duyệt là nội dung được tích hợp.
