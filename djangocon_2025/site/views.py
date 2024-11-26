from os import walk
from django.shortcuts import render
from config.settings.base import APPS_DIR


def default_view(request, menu="home", submenu=None):
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

        sponsors = {
            'Platinum': [],
            'Gold': [],
            'Silver': [],
            'Bronze': [],
            'Sponsor': [],
            'Grants': [{'name': 'Django Software Foundation',
                        'url': 'https://www.djangoproject.com/foundation/',
                        'logo': 'images/sponsors/dsf.png',
                        'filter': False}],
            'Organizer': [
                {'name': 'Ad Evolutio', 'url': 'https://www.evolutio.pt/',
                 'logo': 'images/sponsors/evolutio.png', 'filter': True}
            ],
        }

        ctx["sponsors"] = {category: sponsors_list for category, sponsors_list in
                           sponsors.items() if sponsors_list}

    elif len(files) == 0:
        page += "404"
    else:
        page += "pages/" + "default"

    return render(request, page + ".html", ctx)
