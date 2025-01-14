from os import walk

# import markdown
from django.shortcuts import render
from config.settings.base import APPS_DIR


def default_view(request, menu="home", submenu=None):
    sponsors = {
        "Platinum": [],
        "Gold": [
            {
                "name": "Foxley Talent",
                "url": "https://foxleytalent.com/",
                "logo": "images/sponsors/foxley.png",
                "filter": True,
            },
        ],
        "Silver": [
            {
                "name": "Ambient Digital",
                "url": "https://ambientdigital.com.vn/",
                "logo": "images/sponsors/ambient.svg",
                "filter": True,
            },
            {
                "name": "Caktus Group",
                "url": "https://www.caktusgroup.com/",
                "logo": "images/sponsors/caktus-logo.png",
                "filter": True,
            },
            {
                "name": "Monit ",
                "url": "https://monitdata.com/?lang=en",
                "logo": "images/sponsors/monit.png",
                "filter": True,
            },
        ],
        "Bronze": [
            {
                "name": "HackSoft",
                "url": "https://www.hacksoft.io/",
                "logo": "images/sponsors/hacksoft-logo.png",
                "filter": True,
            
            }
                
            ],
        "Sponsor": [],
        "Grants": [
            {
                "name": "Django Software Foundation",
                "url": "https://www.djangoproject.com/foundation/",
                "logo": "images/sponsors/dsf.png",
                "filter": False,
            }
        ],
        "Organizer": [
            {
                "name": "Ad Evolutio",
                "url": "https://www.evolutio.pt/",
                "logo": "images/sponsors/evolutio.png",
                "filter": True,
            }
        ],
    }

    path = APPS_DIR.__str__() + "/content/" + menu + ("/" + submenu if submenu else "")
    page = ""
    ctx = dict(menu=(menu if not submenu else submenu).capitalize().replace("_", " "))
    files = []

    for dirpath, dirname, filenames in walk(path):
        files.extend(filenames)
        break

    ctx["files"] = []
    for f in sorted(files):
        content = f"{path}/{f}"
        ctx["files"].append(content)

    if menu == "home":
        page += "pages/" + menu
        ctx["files"].append(
            f"{APPS_DIR.__str__()}/content/sponsors/sponsors/sponsors.md"
        )

        ctx["sponsors"] = {
            category: sponsors_list
            for category, sponsors_list in sponsors.items()
            if sponsors_list
        }
    elif menu == "sponsors" and submenu == "sponsors":
        # Sponsors page logic: Load sponsors.md with sponsor_page layout
        page += "modules/sponsor_page"
        sponsors_file_path = (
            f"{APPS_DIR.__str__()}/content/sponsors/sponsors/sponsors.md"
        )
        ctx["sponsors"] = {
            category: sponsors_list
            for category, sponsors_list in sponsors.items()
            if sponsors_list
        }
    elif len(files) == 0:
        page += "404"
    else:
        page += "pages/" + "default"

    return render(request, page + ".html", ctx)
