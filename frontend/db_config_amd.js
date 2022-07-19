define({
    "pages": {
        "bibliografie": {
            "url": "bibliografie",
            "name": "bibliografie",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 300,
                    "type": "string"
                }
            ],
            "verbose_name": "bibliografie",
            "verbose_name_plural": "Bibliografie",
            "ordering": [
                "nume"
            ]
        },
        "localitate": {
            "url": "localitate",
            "name": "localitate",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 50,
                    "type": "string"
                },
                {
                    "name": "judet",
                    "label": "Judet",
                    "bind": {
                        "required": true
                    },
                    "type": "select one",
                    "wq:ForeignKey": "judet"
                },
                {
                    "name": "comuna",
                    "label": "Comuna",
                    "type": "select one",
                    "wq:ForeignKey": "comuna"
                }
            ],
            "verbose_name": "localitate",
            "verbose_name_plural": "Localit\u0103\u021bi",
            "ordering": [
                "nume"
            ]
        },
        "statut": {
            "url": "statut",
            "name": "statut",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 150,
                    "type": "string"
                }
            ],
            "verbose_name": "statut",
            "verbose_name_plural": "Statut",
            "ordering": [
                "nume"
            ]
        },
        "singularitate": {
            "url": "singularitate",
            "name": "singularitate",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 150,
                    "type": "string"
                }
            ],
            "verbose_name": "singularitate",
            "verbose_name_plural": "Singularitate",
            "ordering": [
                "nume"
            ]
        },
        "tipformarelief": {
            "url": "tipformarelief",
            "name": "tipformarelief",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 150,
                    "type": "string"
                }
            ],
            "verbose_name": "tip forma relief",
            "verbose_name_plural": "Tipul Formei de Relief",
            "ordering": [
                "nume"
            ]
        },
        "tippisanie": {
            "url": "tippisanie",
            "name": "tippisanie",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 300,
                    "type": "string"
                }
            ],
            "verbose_name": "tip pisanie",
            "verbose_name_plural": "Tip pisanie",
            "ordering": [
                "nume"
            ]
        },
        "tipcadrupeisaj": {
            "url": "tipcadrupeisaj",
            "name": "tipcadrupeisaj",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 300,
                    "type": "string"
                }
            ],
            "verbose_name": "tip cadru peisaj",
            "verbose_name_plural": "Tip Cadru Peisaj",
            "ordering": [
                "nume"
            ]
        },
        "hram": {
            "url": "hram",
            "name": "hram",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 150,
                    "type": "string"
                }
            ],
            "verbose_name": "hram",
            "verbose_name_plural": "Hram",
            "ordering": [
                "nume"
            ]
        },
        "secol": {
            "url": "secol",
            "name": "secol",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 300,
                    "type": "string"
                }
            ],
            "verbose_name": "secol",
            "verbose_name_plural": "Secole",
            "ordering": [
                "nume"
            ]
        },
        "tipreperhidrografic": {
            "url": "tipreperhidrografic",
            "name": "tipreperhidrografic",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 150,
                    "type": "string"
                }
            ],
            "verbose_name": "tip reper hidrografic",
            "verbose_name_plural": "Tipul Reperului Hidrografic",
            "ordering": [
                "nume"
            ]
        },
        "frecventautilizarii": {
            "url": "frecventautilizarii",
            "name": "frecventautilizarii",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 150,
                    "type": "string"
                }
            ],
            "verbose_name": "frecventa utilizarii",
            "verbose_name_plural": "Frecven\u021ba Utiliz\u0103rii",
            "ordering": [
                "nume"
            ]
        },
        "categorieobiectiv": {
            "url": "categorieobiectiv",
            "name": "categorieobiectiv",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 150,
                    "type": "string"
                }
            ],
            "verbose_name": "categorie obiectiv",
            "verbose_name_plural": "Categorie Obiectiv",
            "ordering": [
                "nume"
            ]
        },
        "justificaredatare": {
            "url": "justificaredatare",
            "name": "justificaredatare",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 300,
                    "type": "string"
                }
            ],
            "verbose_name": "justificare datare",
            "verbose_name_plural": "Justificare Datare",
            "ordering": [
                "nume"
            ]
        },
        "tipzonenaturale": {
            "url": "tipzonenaturale",
            "name": "tipzonenaturale",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 150,
                    "type": "string"
                }
            ],
            "verbose_name": "tip zone naturale",
            "verbose_name_plural": "Zone Naturale (Arii Protejate)",
            "ordering": [
                "nume"
            ]
        },
        "tipartera": {
            "url": "tipartera",
            "name": "tipartera",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 150,
                    "type": "string"
                }
            ],
            "verbose_name": "tip artera",
            "verbose_name_plural": "Tip arter\u0103",
            "ordering": [
                "nume"
            ]
        },
        "judet": {
            "url": "judet",
            "name": "judet",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 50,
                    "type": "string"
                },
                {
                    "name": "cod",
                    "label": "Cod",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 2,
                    "type": "string"
                }
            ],
            "verbose_name": "judet",
            "verbose_name_plural": "Jude\u021be",
            "ordering": [
                "nume"
            ]
        },
        "comuna": {
            "url": "comuna",
            "name": "comuna",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 50,
                    "type": "string"
                }
            ],
            "verbose_name": "comuna",
            "verbose_name_plural": "Comune",
            "ordering": [
                "nume"
            ]
        },
        "tipregimproprietate": {
            "url": "tipregimproprietate",
            "name": "tipregimproprietate",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 150,
                    "type": "string"
                }
            ],
            "verbose_name": "tip regim proprietate",
            "verbose_name_plural": "Tipul Regimului de Proprietate",
            "ordering": [
                "nume"
            ]
        },
        "cult": {
            "url": "cult",
            "name": "cult",
            "list": true,
            "form": [
                {
                    "name": "nume",
                    "label": "Nume",
                    "bind": {
                        "required": true
                    },
                    "wq:length": 150,
                    "type": "string"
                }
            ],
            "verbose_name": "cult",
            "verbose_name_plural": "Cult",
            "ordering": [
                "nume"
            ]
        },
        "index": {
            "url": "",
            "name": "index",
            "show_in_index": false,
            "verbose_name": null
        }
    },
    "site_title": null,
    "router": {
        "base_url": ""
    },
    "store": {
        "service": "",
        "defaults": {
            "format": "json"
        }
    },
    "debug": true
});
