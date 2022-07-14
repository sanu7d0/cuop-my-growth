import pandas as pd
from bs4 import BeautifulSoup
import requests


def get_proxy_list(only_https=False):
    url = "https://free-proxy-list.net/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, "html.parser")
    # dom = etree.HTML(str(soup))

    html_table = soup.find(
        "table", attrs={"class": "table table-striped table-bordered"}
    )
    df_table = pd.read_html(str(html_table))[0]

    proxy_server_list = []
    for i in range(len(df_table)):
        ip = df_table.loc[i, "IP Address"]
        port = df_table.loc[i, "Port"]
        https = df_table.loc[i, "Https"]

        if (only_https and https == "yes") or not only_https:
            server = f"{ip}:{port}"
            proxy_server_list.append(server)

    return proxy_server_list
