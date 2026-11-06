def search_by_title(items, keyword):
    """Tìm các DVD có tiêu đề chứa từ khóa (phiên bản Lab 02)."""
    return [dvd for dvd in items if keyword in dvd.title]
