import os
import sys
from bs4 import BeautifulSoup
import argparse

def add_script_to_html(html_path, ip):
    print("Injecting Perfume scripts into the following html file: " + html_path)
    soup = BeautifulSoup(open(html_path, "rb"), "lxml")
    with open("./static/send_perfume_metrics.js") as js_in:
        js_to_inject = js_in.read()
        js_to_inject = js_to_inject % ip
    print(js_to_inject)
    if soup.find("head"):
        perfumeSource = soup.new_tag('script')
        perfumeSource['src'] = "/static/perfume.umd.min.js"
        script = soup.new_tag('script')
        script.string = js_to_inject
        soup.head.insert(0, perfumeSource)
        soup.head.insert(1, script)

    with open(html_path, "w") as file:
        file.write(str(soup))

    print("Finished injecting perfume scripts")

def inject_perfume(webpages_directory ,ip):
    for directory in os.listdir(webpages_directory):
        directory = os.path.join(webpages_directory, directory)

        if not os.path.isdir(directory):
            continue

        for cat in os.listdir(directory):
            if cat == "index.html" or cat == "index.htm":
                path = os.path.join(directory, cat)
                print("Found index.html file: " + path)
                add_script_to_html(path, ip)
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Inject Perfume script into an html file')
    parser.add_argument('-f', '--folder', type=str, required=True,
                        help='Folder webpages are stores', dest='folder')
    parser.add_argument('-i', '--ip', type=str, required=True,
                        help="IP address where to send perfume metrics to in the format: http://IP:8080", dest='ip')

    args = parser.parse_args()
    inject_perfume(args.folder, args.ip)
