def links(request):
    return {
        "home": "/home/",
        "site_menu": {
            "Talks": {
                "dropdown": "true",
                "submenu": {
                    "Call for Participation": "/talks/cfp/",
                    "Selection Process": "/talks/selection_process/",
                    "Schedule": "/talks/schedule/",
                    # "Speakers": "/talks/speakers/",
                },
            },
            "Information": {
                "dropdown": "true",
                "submenu": {
                    "Dublin": "/information/dublin/",
                    "Venue": "/information/venue/",
                    "Visa": "/information/visa_guide/",
                    "Grants": "/information/grants/",
                    "Sprints": "/information/sprints/",
                    "Mentorship Program": "/information/mentorship/",
                    # "Django Girls": "/information/django_girls/",
                    "Hospitality": "/information/hospitality/",
                    "Party": "/information/social_events/",
                    "T-Shirts": "/information/tshirts/",
                    "Announcements": "/information/announcements/",
                },
            },
            "Sponsors/Jobs": {
                "dropdown": "true",
                "submenu": {
                    "Sponsors": "/sponsors/sponsors",
                    "Jobs": "/sponsors/jobs/",
                    "Sponsorship": "/sponsors/sponsorship/",
                },
            },
            "Conduct": {
                "dropdown": "true",
                "submenu": {
                    "Code of Conduct": "/conduct/code_of_conduct/",
                    "Response Guide": "/conduct/response_guide/",
                    "Privacy Guide": "/conduct/privacy_guide/",
                },
            },
            # "Tickets": {
            #     "dropdown": "false",
            #     "href": "https://pretix.evolutio.pt/evolutio/djceu2025/",
            # },
            "About": {
                "dropdown": "true",
                "submenu": {
                    "Contact": "/about/contact/",
                    "Credits": "/about/credits/",
                    # "Call for Proposals report": "/about/cfp_report/",
                },
            },
        },
        "social_media": {
            "twitter": "https://twitter.com/DjangoConEurope/",
            "fosstodon": "https://fosstodon.org/@djangoconeurope/",
            "slack": "https://join.slack.com/t/djangoconeurope/shared_invite/zt-340erqj3r-s5ekP4aYz95jv14GZMPCAg",
            "youtube": "https://youtube.com/user/djangoconeurope/",
            "linkedin": "https://linkedin.com/company/djangocon-europe/",
            "github": "https://github.com/djangocon/2025.djangocon.eu/",
        },
    }
