# Kết quả thực hành Git/GitHub

Repository: https://github.com/quangkhai2311-svg/it3180-aims

Thực hiện ngày 2026-11-06. Tài khoản: quangkhai2311-svg. Làm một mình (approvals = 0).
Họ tên và MSSV chưa được cung cấp. Chưa có review từ partner; không ghi nhận approval giả.

## Các mốc

| Mốc | Commit |
|---|---|
| release/lab01 | `3442c9d62eac517f5b23e0d6ac67d813c39114f4` |
| release/lab02 | `0458c846ea034503230791f76f7ff23b63011747` |
| release/lab03 | `7a68458ca2ffe7b836ba0087f0405af280e2feea` |
| v1.0.0 | `cc711d168c120a4452625a648f7c97288867c347` |
| v1.0.1 | `4836194b2c0c792e3767821da641bfd45c693485` |
| v1.1.0 | `09c94b8338a47e4e979562884eef209dcb5c2c17` |

## Kết quả đã thực hiện

- Lab 01: restore, restore --staged, amend trước push; rename qua refactor PR; release/lab01 đúng SHA master tại thời điểm tạo.
- Lab 02: hai clone, PR template, print_cart cập nhật trên cùng PR, search và use case; đủ merge commit/squash/rebase merge.
- Push commit mới trực tiếp vào master và release/lab04 đều bị GitHub từ chối; không chỉ thử push no-op.
- Lab 03: test đỏ trước fix giới hạn và discount; bugfix có base feature/discount; 4 tests OK tại release/lab03.
- Hai nhánh tạo từ cùng mốc sửa cùng một dòng gây merge conflict thật. Đã kết hợp hai ý định, chạy test và commit giải quyết.
- Reset soft/mixed/hard và reflog được thực hành trên nhánh nháp không push. Revert merge đã chia sẻ qua một PR riêng.
- Lab 04: annotated tags v0.1.0, v0.2.0, v0.3.0, v1.0.0; GitHub Release 1.0.0; worktree tái tạo baseline và đóng gói.
- Rule release/* yêu cầu PR, không bypass bởi admin, không force-push hoặc xóa nhánh.
- Lab 05: hotfix tạo từ release/lab04; mã/test riêng với bump 1.0.1; v1.0.0 → v1.0.1 chỉ có 4 file thay đổi.
- FIX_SHA: `81e4a46ce61a6d17e9c5cccf5dd50c6317e960d6`; hai cherry-pick -x về master và release/lab05 giữ version 1.1.0.
- Trên v1.0.1, v1.1.0 và master, tìm lion đều trả đúng The Lion King. Test lần lượt 5, 8, 8 đều đạt.
- CI GitHub xanh: https://github.com/quangkhai2311-svg/it3180-aims/actions/runs/42250218068/job/128003004377
- CI demo đỏ: https://github.com/quangkhai2311-svg/it3180-aims/actions/runs/42250435780/job/128003771927
- Thử merge PR demo bị chặn: `Required status check "test" is failing.`. PR demo được đóng không merge.

## Pull Requests

| PR | Nhánh nguồn → đích | Kiểu / trạng thái |
|---|---|---|
| [#1](https://github.com/quangkhai2311-svg/it3180-aims/pull/1) | `refactor/apply-release-flow` → `master` | merge |
| [#2](https://github.com/quangkhai2311-svg/it3180-aims/pull/2) | `topic/pr-template` → `master` | merge |
| [#3](https://github.com/quangkhai2311-svg/it3180-aims/pull/3) | `feature/cart-print` → `master` | merge |
| [#4](https://github.com/quangkhai2311-svg/it3180-aims/pull/4) | `feature/search-by-title` → `master` | squash |
| [#5](https://github.com/quangkhai2311-svg/it3180-aims/pull/5) | `topic/use-case-diagram` → `master` | rebase |
| [#7](https://github.com/quangkhai2311-svg/it3180-aims/pull/7) | `bugfix/cart-limit-off-by-one` → `master` | merge |
| [#8](https://github.com/quangkhai2311-svg/it3180-aims/pull/8) | `bugfix/discount-calculation` → `feature/discount` | merge |
| [#9](https://github.com/quangkhai2311-svg/it3180-aims/pull/9) | `feature/discount` → `master` | merge |
| [#10](https://github.com/quangkhai2311-svg/it3180-aims/pull/10) | `feature/vietnamese-messages` → `master` | merge |
| [#11](https://github.com/quangkhai2311-svg/it3180-aims/pull/11) | `feature/show-added-title` → `master` | merge |
| [#12](https://github.com/quangkhai2311-svg/it3180-aims/pull/12) | `bugfix/revert-show-added-title` → `master` | merge |
| [#13](https://github.com/quangkhai2311-svg/it3180-aims/pull/13) | `topic/lab03-answers` → `master` | merge |
| [#14](https://github.com/quangkhai2311-svg/it3180-aims/pull/14) | `topic/prepare-release-1.0.0` → `master` | merge |
| [#15](https://github.com/quangkhai2311-svg/it3180-aims/pull/15) | `feature/sort-cart` → `master` | merge |
| [#16](https://github.com/quangkhai2311-svg/it3180-aims/pull/16) | `feature/search-by-category` → `master` | merge |
| [#17](https://github.com/quangkhai2311-svg/it3180-aims/pull/17) | `topic/prepare-release-1.1.0` → `master` | merge |
| [#19](https://github.com/quangkhai2311-svg/it3180-aims/pull/19) | `hotfix/search-case-insensitive` → `release/lab04` | merge |
| [#20](https://github.com/quangkhai2311-svg/it3180-aims/pull/20) | `hotfix/search-case-insensitive-master` → `master` | merge |
| [#21](https://github.com/quangkhai2311-svg/it3180-aims/pull/21) | `hotfix/search-case-insensitive-lab05` → `release/lab05` | merge |
| [#22](https://github.com/quangkhai2311-svg/it3180-aims/pull/22) | `topic/ci-unit-tests` → `master` | merge |
| [#23](https://github.com/quangkhai2311-svg/it3180-aims/pull/23) | `bugfix/ci-demo` → `master` | Closed, không merge (CI demo) |

## Issues

- [#6: Cart accepts the 21st DVD although the limit is 20](https://github.com/quangkhai2311-svg/it3180-aims/issues/6) — đã đóng qua PR vào master.
- [#18: search_by_title is case-sensitive (affects v1.0.0)](https://github.com/quangkhai2311-svg/it3180-aims/issues/18) — đã đóng qua PR vào master.

## Phần người học cần hoàn tất

- Điền họ tên/MSSV thật, đổi tên repo theo mẫu it3180-<MSSV>-aims nếu lớp yêu cầu.
- Các thao tác thực tế dùng HTTPS qua GitHub CLI. Bước tạo SSH key và xác thực SSH của Lab 01 chưa thực hiện; xem hướng dẫn để tự cấu hình nếu cần đúng mục này.
- Nếu cần đủ tiêu chí Changes requested → Approved, làm một lượt review thật với partner; tài khoản tác giả không tự approve được.
- Đọc và chỉnh câu trả lời thảo luận theo hiểu biết của mình, kiểm tra minh chứng trên GitHub rồi nộp link LMS.
- File CI xuất hiện sau mốc v1.1.0, theo phần mở rộng cuối Lab 05. Không di chuyển các tag đã phát hành.
