fake_db = {
    '/company/history': {
        'page_title': 'Company history',
        'page_details': 'Details about company history...',
    },
    '/company/employees': {
        'page_title': 'Our team',
        'page_details': 'Details about company employees ...',
    },
}

def get_page(url: str) -> dict:
    if not url:
        return {}

    url = url.strip().lower()
    url = '/' + url.lstrip('/')
    return fake_db.get(url, {})