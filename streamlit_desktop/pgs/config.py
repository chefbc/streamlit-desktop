from . import home, upload

# https://icons.getbootstrap.com

PAGES = {
    "Home": {
        "icon": "house",
        "method": home.show,
    },
    "Upload": {
        "icon": "cloud-upload",
        "method": upload.show,
    },
}