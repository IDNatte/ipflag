import argparse
import network
import sys
import ui


def windowApp():
    network_meta = network.get_meta_pubnet()

    if network_meta.get("status") == "fetched":
        meta_city = network_meta.get("data").get("city")
        meta_region = network_meta.get("data").get("region")
        meta_country = network_meta.get("data").get("country")
        meta_ip_addr = network_meta.get("data").get("ip")

        network.get_net_flag(meta_country)
        ui.UIInit(meta_ip_addr, meta_city, meta_region, meta_country)

    else:
        print("ﮙ something wen't wrong !")


def textApp():
    network_meta = network.get_meta_pubnet()

    if network_meta.get("status") == "fetched":
        meta_country = network_meta.get("data").get("country")
        meta_ip_addr = network_meta.get("data").get("ip")

        print(f"{meta_ip_addr} @ {meta_country}")

    else:
        print("ﮙ something wen't wrong !")


if __name__ == "__main__":
    app_opt = argparse.ArgumentParser()
    app_opt.add_argument(
        "--app-type",
        help="display application type, whether it displayed on polybar icon or showing UI",
        required=True,
        choices=["text", "window"],
        type=str,
    )

    option = app_opt.parse_args()

    if option.app_type == "window":
        windowApp()

    elif option.app_type == "text":
        textApp()

    else:
        print("what are you wan't to do ?")
        sys.exit()
