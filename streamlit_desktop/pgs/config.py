from . import home, upload, keyring, password

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
    "My Passwords": {
        "icon": "key",
        "method": keyring.show,
    },
    "Passwords": {
        "icon": "shield-lock",
        "method": password.show,
    },
}