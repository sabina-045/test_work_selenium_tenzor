from selenium.webdriver.chrome.options import Options


def get_chrome_download_permission(upload_file_path):
    """Получаем разрешение от Хром на скачивание файлов."""
    chrome_options = Options()
    chrome_options.add_argument("--allow-running-insecure-content")
    chrome_options.add_argument(
        f"--unsafely-treat-insecure-origin-as-secure=https://sbis.ru/download?tab=plugin&innerTab=default")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": upload_file_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    return chrome_options
