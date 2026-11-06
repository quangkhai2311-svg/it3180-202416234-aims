# Trả lời thảo luận Lab 03

## Merge base là gì?
Merge base là tổ tiên chung tốt nhất của hai commit. Git dùng trạng thái
chung này cùng hai đầu nhánh để xác định thay đổi của mỗi phía khi merge.
Xem bằng `git merge-base master feature/show-added-title` khi nhánh còn tồn tại.

## Vì sao master/release/* phải dùng revert?
Revert thêm commit đảo ngược và giữ nguyên lịch sử đã chia sẻ. Reset/rebase
có thể làm con trỏ hoặc SHA thay đổi, khiến clone khác mất đồng bộ và phá
truy vết baseline. Khi đảo merge commit, `git revert -m 1 SHA` chọn parent 1
làm dòng chính để tính phần thay đổi cần đảo ngược.

## Reset soft/mixed/hard khác nhau thế nào?
Soft di chuyển HEAD, giữ index và working tree. Mixed còn đặt lại index,
giữ working tree. Hard đặt lại cả index và nội dung tệp được theo dõi;
chỉ thực hành trên nhánh nháp với thay đổi tự tạo. Reflog ghi chuyển động
HEAD để tìm lại commit; không bảo đảm khôi phục nội dung chưa từng commit.

## Vì sao test phải fail trước fix?
Test đỏ trên mã cũ xác nhận nó bắt đúng lỗi. Sau fix, cùng test chuyển xanh
và giữ lại làm regression test. Các commit `test:` và `fix:` tách nhau giúp
review và truy vết.

## Vì sao PR sửa discount có base feature/discount?
Lỗi thuộc tính năng chưa được tích hợp. Sửa ngay trên dòng phát triển của
tính năng, kiểm tra nó trước khi PR tính năng vào master.
