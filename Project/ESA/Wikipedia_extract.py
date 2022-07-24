import wikipedia
import argparse
import os
import datetime
from bs4 import BeautifulSoup
from mediawikiapi import MediaWikiAPI



def main(topic, level, folder_name):
    """
    Function to get content and store in txt file.
    :param folder_name: Name of the folder in which the contents will be stored
    :param topic: Keywords to find pages related to it
    :param level: no of levels to get contents of links
    level 1 (Page A) - Scrape everything - Doesn't visit any link
    level 2 (Page A) - Scrapes everything, gets the links on the page and scrapes the contents of those links

    :return: None
    """
    
    list_pages = wikipedia.search(topic,results=2)
    # print(list_pages)
    for i in range(0, level):
        if level > 1 and level != i-1:
            list_pages = create_content(list_pages, folder_name, links_req=True)
        else:
            create_content(list_pages, folder_name, links_req=False)
    

def create_content(list_pages, folder_name, links_req):
    all_links = []
    seen_pages = []
    try:
        seen_pages = os.listdir(folder_name + '/')
    except FileNotFoundError as e:
        pass
    for each_page in list_pages:
        try:
            page_wiki_obj = wikipedia.page(each_page)
            if each_page + ".txt" not in seen_pages:
                content = page_wiki_obj.content
                write_to_txt(each_page, content, folder_name)
            if links_req:
                all_links.append(page_wiki_obj.links)
        except Exception as e:
            pass
    if links_req and all_links:
        return [each_link for list_of_links in all_links for each_link in list_of_links]
    else:
        return None

# def create_content(list_pages, folder_name, links_req):
#     all_links = []
#     seen_pages = []
#     try:
#         seen_pages = os.listdir(folder_name + '/')
#     except FileNotFoundError as e:
#         logger.info("Novel Scrape")
#     for each_page in list_pages:
#         try:
#             page_wiki_obj = wikipedia.page(each_page)
#             if each_page + ".txt" not in seen_pages:
#                 content = page_wiki_obj.content
#                 table_contents = get_table_contents(each_page)
#                 write_to_txt(each_page, content, table_contents, folder_name)
#             else:
#                 logger.info("Seen: " + each_page + ".txt")
#             if links_req:
#                 all_links.append(page_wiki_obj.links)
#         except Exception as e:
#             logger.error(each_page)
#             logger.error(e)
#     if links_req and all_links:
#         return [each_link for list_of_links in all_links for each_link in list_of_links]
#     else:
#         return None

# def get_table_contents(wiki_page):
#     # load page
#     mediawikiapi = MediaWikiAPI()
#     mwa_page = mediawikiapi.page(wiki_page)

#     # scrape the HTML with BeautifulSoup to find tables
#     soup = BeautifulSoup(mwa_page.html(), 'html.parser')
#     tables = soup.findAll("table", {"class": "wikitable"})
#     # select target table and apply custom function to export it to pandas
#     table_contents = None
#     if tables:
#         for i in range(0, len(tables)):
#             if table_contents:
#                 table_contents = table_contents + "== Table: " + str(i) + " ==" + "\n"
#             else:
#                 table_contents = "== Table: " + str(i) + " ==" + "\n"
#             headers = [th.text.encode("utf-8").decode('utf-8') for th in tables[i].select("tr th")]
#             header = ",".join(headers)
#             table_contents = table_contents + str(header)
#             table_contents = table_contents + '\n'
#             for row in tables[0].select("tr + tr"):
#                 for td in row.find_all("td"):
#                     if td.a:
#                         try:
#                             table_contents = table_contents + td.a['title'] + ","
#                         except KeyError as e:
#                             pass
#                         table_contents = table_contents + str(td.text.encode("utf-8").decode('utf-8')) + ","
#                         continue
#                     else:
#                         table_contents = table_contents + str(td.text.encode("utf-8").decode('utf-8')) + ","
#                 table_contents = table_contents + '\n'
#             table_contents = table_contents + "==============="
#     return table_contents



def write_to_txt(page_name, content_to_write,folder_name):
    os.makedirs(folder_name, exist_ok=True)
    with open(folder_name + "/" + page_name + '.txt', "w", encoding="utf-8") as text_file:
        text_file.write(content_to_write)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-topic", type=str)
    parser.add_argument("-level", type=int)
    parser.add_argument("-folder", type=str)
    args = parser.parse_args()

    main(args.topic, args.level, args.folder)

