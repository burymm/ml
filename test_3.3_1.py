import re
import requests


def extract_domains(urls):
    pattern = r'^(?!\.\.?/)(?:https?://|ftp://)?([a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*)(?::\d+)?(?:/|$)'
    domains = []
    for url in urls:
        match = re.match(pattern, url)
        if match:
            domains.append(match.group(1))
    return domains

link_pattern = r'<a\s[^>]*href=["\']([^"\']+)["\'][^>]*>'

link = input()
#
response = requests.get(link)
html = response.text
# html = '<a href="http://stepik.org/courses">\n<a href=\'https://stepik.org\'>\n<a href=\'http://neerc.ifmo.ru:1345\'>\n<a href="ftp://mail.ru/distib" >\n<a href="ya.ru">\n<a href="www.ya.ru">\m<a href="../skip_relative_links">'

links = re.findall(link_pattern, html)
sorted_list = list(set(extract_domains(links)))
sorted_list.sort()
print("\n".join(sorted_list))
# print(links)
