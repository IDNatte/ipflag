import tkinter.ttk
import constant
import tkinter
import os


def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = tkinter.PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x * oldWidth / newWidth)
            yOld = int(y * oldHeight / newHeight)
            rgb = "#%02x%02x%02x" % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage


def UIInit(ipAddr, city, region, country):
    root = tkinter.Tk()

    root.title("IP Info")
    root.geometry("400x200")
    root.minsize(width=400, height=200)
    root.maxsize(width=400, height=200)
    root.columnconfigure(2, weight=1)
    root.rowconfigure(2, weight=1)

    # Label for ip and location info
    label_location = tkinter.ttk.Label(root, text=f"{city}, {region} {country}")
    label_ip = tkinter.ttk.Label(
        root, text=f"Your IP Address is {ipAddr}", justify="center"
    )

    # add image to UI
    logo = tkinter.PhotoImage(file=os.path.join(constant.TEMP_FILE_PATH, "flag.png"))
    logo = resizeImage(logo, 160, 84)
    logo_canvas = tkinter.Canvas(root, width=160, height=84)

    # IP Address Info
    label_ip.grid(column=2, row=1)
    label_location.grid(column=2, row=2)

    logo_canvas.grid(column=1, row=0, columnspan=2, sticky=tkinter.NS, pady=20)
    logo_canvas.create_image(0, 0, anchor=tkinter.NW, image=logo)

    # disabling resize windows
    root.resizable(width=False, height=False)
    root.mainloop()
