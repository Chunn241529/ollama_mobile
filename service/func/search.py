from duckduckgo_search import DDGS


def search_duckduckgo_unlimited(query):
    ddgs = DDGS()

    results = []
    seen_links = set()  # Tập hợp lưu các link đã gặp

    # tạo random từ 1 tới 5
    import random

    for result in ddgs.text(
        query, max_results=40 - random.randint(1, 20)
    ):  # Tăng max_results để tránh thiếu dữ liệu
        link = result.get("href")  # Lấy link từ kết quả

        if link in seen_links:
            print("Trùng link, dừng lại!")
            break  # Dừng lại ngay khi gặp link trùng

        seen_links.add(link)  # Thêm link vào tập hợp đã thấy
        results.append(result)  # Lưu kết quả hợp lệ

    return results


def extract_search_info(search_results):
    info = []
    count = 0  # Biến đếm số lượng kết quả

    # Lấy thông tin từ các kết quả tìm kiếm
    for result in search_results or []:
        if result and result.get("title"):
            info.append(f"Title: {result['title']}")
        if result and result.get("href"):  # Trường URL là 'href'
            info.append(f"URL: {result['href']}")
        if result and result.get("body"):
            info.append(f"Description: {result['body']}")
        if result:
            info.append("---")  # Phân tách giữa các kết quả
        count += 1

    # Thêm số lượng kết quả vào thông tin
    info.append(f"Total results: {count}")

    # Kết hợp tất cả thông tin thành một chuỗi
    return "\n".join(info)
