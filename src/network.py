import requests
import constant
import os


def get_meta_pubnet():
    get_network_meta = "https://ipinfo.io/json"

    try:
        network_meta = requests.get(
            get_network_meta,
        )

        return {
            "status": "fetched",
            "status_message": "fetched",
            "data": network_meta.json(),
        }

    except (requests.ConnectionError, requests.HTTPError) as Error:
        return {"status": "error", "error": Error, "data": ""}


def get_net_flag(country_code):
    get_flag = f"https://countryflagsapi.com/png/{country_code}"

    if not os.path.exists(constant.TEMP_FILE_PATH):
        os.makedirs(constant.TEMP_FILE_PATH)

    try:
        flag = requests.get(get_flag)

        with open(os.path.join(constant.TEMP_FILE_PATH, "flag.png"), "wb") as flag_dl:
            flag_dl.write(flag.content)

        return str("logo download !")

    except (requests.ConnectionError, requests.HTTPError) as Error:
        return {"status": "error", "error": Error, "data": ""}
