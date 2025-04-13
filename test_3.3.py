import requests
import sys
import re

source = input()
target = input().replace('stepik.org', 'stepic.org')
# source = 'https://stepik.org/media/attachments/lesson/24472/sample0.html'
# target = 'https://stepik.org/media/attachments/lesson/24472/sample2.html'.replace('stepik.org', 'stepic.org')

def find_links(source_link):
    source_res = requests.get(source_link)
    # print(source_res.status_code)
    # print(source_res.text)

    pattern = r'<a\s[^>]*href=["\']([^"\']+)["\'][^>]*>'

    # print(re.search(pattern, source_res.text).group())
    url = re.findall(pattern, source_res.text)
    # print(url)
    # url = url.replace('<a href="', '').replace('">', '')

    return url


first_links = find_links(source)
second_links = sum(list(map(find_links, first_links)), [])
# print(second_links)
print('Yes' if target in second_links else 'No' )
# print('Yes' if target == second_link else 'No' )


