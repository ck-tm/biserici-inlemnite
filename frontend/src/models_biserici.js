{
    "name": "Biserici",
    "description": "",
    "renders": [
        "application/json",
        "text/html"
    ],
    "parses": [
        "application/json",
        "application/x-www-form-urlencoded",
        "multipart/form-data"
    ],
    "actions": {
        "POST": {
            "pk": {
                "type": "integer",
                "required": false,
                "read_only": true,
                "label": "ID",
                "is_repetition_field": false
            },
            "nume": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Nume",
                "max_length": 50,
                "is_repetition_field": false
            },
            "identificare": {
                "type": "nested object",
                "required": true,
                "read_only": false,
                "label": "Identificare",
                "children": {
                    "codul_lmi": {
                        "type": "string",
                        "required": false,
                        "read_only": false,
                        "label": "Codul LMI",
                        "max_length": 50,
                        "is_repetition_field": false
                    },
                    "categoria": {
                        "type": "field",
                        "required": false,
                        "read_only": false,
                        "label": "Categoria",
                        "fragment": "categorieobiectiv",
                        "is_repetition_field": false
                    },
                    "statut": {
                        "type": "field",
                        "required": false,
                        "read_only": false,
                        "label": "Statut",
                        "fragment": "statut",
                        "is_repetition_field": false
                    },
                    "denumire_oficiala": {
                        "type": "string",
                        "required": false,
                        "read_only": false,
                        "label": "Denumire oficial\u0103 actual\u0103 LMI",
                        "max_length": 250,
                        "is_repetition_field": false
                    },
                    "hram": {
                        "type": "field",
                        "required": false,
                        "read_only": false,
                        "label": "Hram",
                        "fragment": "hram",
                        "is_repetition_field": false
                    },
                    "cult": {
                        "type": "field",
                        "required": false,
                        "read_only": false,
                        "label": "Cult",
                        "fragment": "cult",
                        "is_repetition_field": false
                    },
                    "frecventa_utilizarii": {
                        "type": "nested object",
                        "required": true,
                        "read_only": false,
                        "label": "Frecventa utilizarii",
                        "children": {
                            "id": {
                                "type": "integer",
                                "required": false,
                                "read_only": true,
                                "label": "ID",
                                "is_repetition_field": false
                            },
                            "observatii": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Observa\u021bii",
                                "is_repetition_field": false
                            },
                            "frecventa_utilizarii": {
                                "type": "field",
                                "required": false,
                                "read_only": false,
                                "label": "Frecven\u021ba utiliz\u0103rii",
                                "fragment": "frecventautilizarii",
                                "is_repetition_field": false
                            }
                        },
                        "is_repetition_field": false
                    },
                    "singularitate": {
                        "type": "nested object",
                        "required": true,
                        "read_only": false,
                        "label": "Singularitate",
                        "children": {
                            "observatii": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Observa\u021bii",
                                "is_repetition_field": false
                            },
                            "singularitate": {
                                "type": "field",
                                "required": false,
                                "read_only": false,
                                "label": "Singularitate",
                                "fragment": "singularitate",
                                "is_repetition_field": false
                            }
                        },
                        "is_repetition_field": false
                    }
                },
                "is_repetition_field": false
            },
            "localizare": {
                "type": "nested object",
                "required": true,
                "read_only": false,
                "label": "Localizare",
                "children": {
                    "id": {
                        "type": "integer",
                        "required": false,
                        "read_only": true,
                        "label": "ID",
                        "is_repetition_field": false
                    },
                    "unitati_teritoriale": {
                        "type": "nested object",
                        "required": true,
                        "read_only": false,
                        "label": "Unitati teritoriale",
                        "children": {
                            "stat": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Stat",
                                "max_length": 50,
                                "is_repetition_field": false
                            },
                            "regiune": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Regiune",
                                "max_length": 50,
                                "is_repetition_field": false
                            },
                            "uat_1": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "UAT 1 (superior)",
                                "max_length": 50,
                                "is_repetition_field": false
                            },
                            "uat": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "UAT (intermediar)",
                                "max_length": 50,
                                "is_repetition_field": false
                            },
                            "uat_2": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "UAT 2 (inferior)",
                                "max_length": 50,
                                "is_repetition_field": false
                            },
                            "ut": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "UT",
                                "max_length": 50,
                                "is_repetition_field": false
                            }
                        },
                        "is_repetition_field": false
                    },
                    "adresa": {
                        "type": "nested object",
                        "required": true,
                        "read_only": false,
                        "label": "Adresa",
                        "children": {
                            "denumire_artera": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Denumire Arter\u0103",
                                "max_length": 50,
                                "is_repetition_field": false
                            },
                            "nr_postal": {
                                "type": "integer",
                                "required": false,
                                "read_only": false,
                                "label": "Num\u0103r Po\u0219tal",
                                "min_value": -2147483648,
                                "max_value": 2147483647,
                                "is_repetition_field": false
                            },
                            "cod_postal": {
                                "type": "integer",
                                "required": false,
                                "read_only": false,
                                "label": "Cod Po\u0219tal",
                                "min_value": -2147483648,
                                "max_value": 2147483647,
                                "is_repetition_field": false
                            },
                            "observatii": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Observa\u021bii",
                                "is_repetition_field": false
                            },
                            "coordonate_gps": {
                                "type": "field",
                                "required": false,
                                "read_only": false,
                                "label": "Coordonate GPS",
                                "is_repetition_field": false
                            },
                            "tip_artera": {
                                "type": "field",
                                "required": false,
                                "read_only": false,
                                "label": "Tip artera",
                                "fragment": "tipartera",
                                "is_repetition_field": false
                            }
                        },
                        "is_repetition_field": false
                    },
                    "referinte_cadastrale": {
                        "type": "nested object",
                        "required": true,
                        "read_only": false,
                        "label": "Referinte cadastrale",
                        "children": {
                            "nr_carte_funciara": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Num\u0103r carte funciar\u0103",
                                "max_length": 50,
                                "is_repetition_field": false
                            },
                            "nr_cadastru": {
                                "type": "integer",
                                "required": false,
                                "read_only": false,
                                "label": "Num\u0103r cadastru",
                                "min_value": -2147483648,
                                "max_value": 2147483647,
                                "is_repetition_field": false
                            },
                            "nr_cop_cadastru": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Num\u0103r cop conform cadastru",
                                "max_length": 150,
                                "is_repetition_field": false
                            },
                            "nr_parcela": {
                                "type": "integer",
                                "required": false,
                                "read_only": false,
                                "label": "Num\u0103r parcel\u0103 / topografic",
                                "min_value": -2147483648,
                                "max_value": 2147483647,
                                "is_repetition_field": false
                            },
                            "suprafata_parcela": {
                                "type": "integer",
                                "required": false,
                                "read_only": false,
                                "label": "Suprafa\u021b\u0103 parcel\u0103",
                                "min_value": -2147483648,
                                "max_value": 2147483647,
                                "is_repetition_field": false
                            },
                            "observatii": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Observa\u021bii",
                                "is_repetition_field": false
                            }
                        },
                        "is_repetition_field": false
                    },
                    "regim_proprietate": {
                        "type": "nested object",
                        "required": true,
                        "read_only": false,
                        "label": "Regim proprietate",
                        "children": {
                            "observatii": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Observa\u021bii",
                                "is_repetition_field": false
                            },
                            "tip_regim": {
                                "type": "field",
                                "required": false,
                                "read_only": false,
                                "label": "Tipul Regimului de Proprietate",
                                "fragment": "tipregimproprietate",
                                "is_repetition_field": false
                            }
                        },
                        "is_repetition_field": false
                    }
                },
                "is_repetition_field": false
            },
            "repere_geografice": {
                "type": "nested object",
                "required": true,
                "read_only": false,
                "label": "Repere geografice",
                "children": {
                    "id": {
                        "type": "integer",
                        "required": false,
                        "read_only": true,
                        "label": "ID",
                        "is_repetition_field": false
                    },
                    "forma_relief": {
                        "type": "nested object",
                        "required": true,
                        "read_only": false,
                        "label": "Forma relief",
                        "children": {
                            "denumire": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Denumire Form\u0103 de Relief",
                                "max_length": 150,
                                "is_repetition_field": false
                            },
                            "observatii": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Observa\u021bii",
                                "is_repetition_field": false
                            },
                            "tip_forma": {
                                "type": "field",
                                "required": false,
                                "read_only": false,
                                "label": "Tipul Formei de Relief",
                                "fragment": "tipformarelief",
                                "is_repetition_field": false
                            }
                        },
                        "is_repetition_field": false
                    },
                    "reper_hidrografic": {
                        "type": "nested object",
                        "required": true,
                        "read_only": false,
                        "label": "Reper hidrografic",
                        "children": {
                            "denumire": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Denumire Reper Hidrografic",
                                "max_length": 150,
                                "is_repetition_field": false
                            },
                            "observatii": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Observa\u021bii",
                                "is_repetition_field": false
                            },
                            "tip_reper": {
                                "type": "field",
                                "required": false,
                                "read_only": false,
                                "label": "Tipul Reperului Hidrografic",
                                "fragment": "tipreperhidrografic",
                                "is_repetition_field": false
                            }
                        },
                        "is_repetition_field": false
                    },
                    "zone_naturale": {
                        "type": "nested object",
                        "required": true,
                        "read_only": false,
                        "label": "Zone naturale",
                        "children": {
                            "observatii": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Observa\u021bii",
                                "is_repetition_field": false
                            },
                            "tip_zone": {
                                "type": "field",
                                "required": false,
                                "read_only": false,
                                "label": "Tip Zone Naturale",
                                "fragment": "tipzonenaturale",
                                "is_repetition_field": false
                            }
                        },
                        "is_repetition_field": false
                    }
                },
                "is_repetition_field": false
            },
            "istoric": {
                "type": "nested object",
                "required": true,
                "read_only": false,
                "label": "Istoric",
                "children": {
                    "id": {
                        "type": "integer",
                        "required": false,
                        "read_only": true,
                        "label": "ID",
                        "is_repetition_field": false
                    },
                    "scurt_istoric": {
                        "type": "nested object",
                        "required": true,
                        "read_only": false,
                        "label": "Scurt istoric",
                        "children": {
                            "sinteza": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Sintez\u0103 istoric\u0103",
                                "is_repetition_field": false
                            },
                            "datare": {
                                "type": "field",
                                "required": false,
                                "read_only": false,
                                "label": "Pisanie",
                                "is_repetition_field": false
                            },
                            "bibliografie": {
                                "type": "field",
                                "required": false,
                                "read_only": false,
                                "label": "Bibliografie",
                                "fragment": "bibliografie",
                                "is_repetition_field": false
                            },
                            "justificare_datare": {
                                "type": "field",
                                "required": false,
                                "read_only": false,
                                "label": "Pisanie",
                                "is_repetition_field": false
                            }
                        },
                        "is_repetition_field": false
                    },
                    "pisanie": {
                        "type": "nested object",
                        "required": true,
                        "read_only": false,
                        "label": "Pisanie",
                        "children": {
                            "text": {
                                "type": "string",
                                "required": false,
                                "read_only": false,
                                "label": "Text",
                                "is_repetition_field": false
                            },
                            "tip": {
                                "type": "field",
                                "required": false,
                                "read_only": false,
                                "label": "Tip Pisanie",
                                "fragment": "tippisanie",
                                "is_repetition_field": false
                            }
                        },
                        "is_repetition_field": false
                    },
                    "ctitori": {
                        "type": "field",
                        "required": true,
                        "read_only": false,
                        "label": "Ctitori",
                        "child": {
                            "type": "nested object",
                            "required": true,
                            "read_only": false,
                            "children": {
                                "foto": {
                                    "type": "field",
                                    "required": true,
                                    "read_only": false,
                                    "label": "Foto",
                                    "child": {
                                        "type": "nested object",
                                        "required": true,
                                        "read_only": false,
                                        "children": {
                                            "titlu": {
                                                "type": "string",
                                                "required": false,
                                                "read_only": false,
                                                "label": "Titlu",
                                                "max_length": 150,
                                                "is_repetition_field": false
                                            },
                                            "fisier": {
                                                "type": "image upload",
                                                "required": true,
                                                "read_only": false,
                                                "label": "Fisier",
                                                "max_length": 200,
                                                "is_repetition_field": false
                                            },
                                            "copyright": {
                                                "type": "string",
                                                "required": false,
                                                "read_only": false,
                                                "label": "Copyright",
                                                "max_length": 150,
                                                "is_repetition_field": false
                                            }
                                        },
                                        "is_repetition_field": false
                                    },
                                    "is_repetition_field": true
                                },
                                "nume": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Nume",
                                    "max_length": 150,
                                    "is_repetition_field": false
                                },
                                "observatii": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Observa\u021bii",
                                    "is_repetition_field": false
                                },
                                "sursa": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Sursa",
                                    "is_repetition_field": false
                                }
                            },
                            "is_repetition_field": false
                        },
                        "is_repetition_field": true
                    },
                    "mesteri": {
                        "type": "field",
                        "required": true,
                        "read_only": false,
                        "label": "Mesteri",
                        "child": {
                            "type": "nested object",
                            "required": true,
                            "read_only": false,
                            "children": {
                                "foto": {
                                    "type": "field",
                                    "required": true,
                                    "read_only": false,
                                    "label": "Foto",
                                    "child": {
                                        "type": "nested object",
                                        "required": true,
                                        "read_only": false,
                                        "children": {
                                            "titlu": {
                                                "type": "string",
                                                "required": false,
                                                "read_only": false,
                                                "label": "Titlu",
                                                "max_length": 150,
                                                "is_repetition_field": false
                                            },
                                            "fisier": {
                                                "type": "image upload",
                                                "required": true,
                                                "read_only": false,
                                                "label": "Fisier",
                                                "max_length": 200,
                                                "is_repetition_field": false
                                            },
                                            "copyright": {
                                                "type": "string",
                                                "required": false,
                                                "read_only": false,
                                                "label": "Copyright",
                                                "max_length": 150,
                                                "is_repetition_field": false
                                            }
                                        },
                                        "is_repetition_field": false
                                    },
                                    "is_repetition_field": true
                                },
                                "nume": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Nume",
                                    "max_length": 150,
                                    "is_repetition_field": false
                                },
                                "observatii": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Observa\u021bii",
                                    "is_repetition_field": false
                                },
                                "sursa": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Sursa",
                                    "is_repetition_field": false
                                }
                            },
                            "is_repetition_field": false
                        },
                        "is_repetition_field": true
                    },
                    "zugravi": {
                        "type": "field",
                        "required": true,
                        "read_only": false,
                        "label": "Zugravi",
                        "child": {
                            "type": "nested object",
                            "required": true,
                            "read_only": false,
                            "children": {
                                "foto": {
                                    "type": "field",
                                    "required": true,
                                    "read_only": false,
                                    "label": "Foto",
                                    "child": {
                                        "type": "nested object",
                                        "required": true,
                                        "read_only": false,
                                        "children": {
                                            "titlu": {
                                                "type": "string",
                                                "required": false,
                                                "read_only": false,
                                                "label": "Titlu",
                                                "max_length": 150,
                                                "is_repetition_field": false
                                            },
                                            "fisier": {
                                                "type": "image upload",
                                                "required": true,
                                                "read_only": false,
                                                "label": "Fisier",
                                                "max_length": 200,
                                                "is_repetition_field": false
                                            },
                                            "copyright": {
                                                "type": "string",
                                                "required": false,
                                                "read_only": false,
                                                "label": "Copyright",
                                                "max_length": 150,
                                                "is_repetition_field": false
                                            }
                                        },
                                        "is_repetition_field": false
                                    },
                                    "is_repetition_field": true
                                },
                                "nume": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Nume",
                                    "max_length": 150,
                                    "is_repetition_field": false
                                },
                                "observatii": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Observa\u021bii",
                                    "is_repetition_field": false
                                },
                                "sursa": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Sursa",
                                    "is_repetition_field": false
                                }
                            },
                            "is_repetition_field": false
                        },
                        "is_repetition_field": true
                    },
                    "personalitati": {
                        "type": "field",
                        "required": true,
                        "read_only": false,
                        "label": "Personalitati",
                        "child": {
                            "type": "nested object",
                            "required": true,
                            "read_only": false,
                            "children": {
                                "foto": {
                                    "type": "field",
                                    "required": true,
                                    "read_only": false,
                                    "label": "Foto",
                                    "child": {
                                        "type": "nested object",
                                        "required": true,
                                        "read_only": false,
                                        "children": {
                                            "titlu": {
                                                "type": "string",
                                                "required": false,
                                                "read_only": false,
                                                "label": "Titlu",
                                                "max_length": 150,
                                                "is_repetition_field": false
                                            },
                                            "fisier": {
                                                "type": "image upload",
                                                "required": true,
                                                "read_only": false,
                                                "label": "Fisier",
                                                "max_length": 200,
                                                "is_repetition_field": false
                                            },
                                            "copyright": {
                                                "type": "string",
                                                "required": false,
                                                "read_only": false,
                                                "label": "Copyright",
                                                "max_length": 150,
                                                "is_repetition_field": false
                                            }
                                        },
                                        "is_repetition_field": false
                                    },
                                    "is_repetition_field": true
                                },
                                "nume": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Nume",
                                    "max_length": 150,
                                    "is_repetition_field": false
                                },
                                "observatii": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Observa\u021bii",
                                    "is_repetition_field": false
                                },
                                "sursa": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Sursa",
                                    "is_repetition_field": false
                                }
                            },
                            "is_repetition_field": false
                        },
                        "is_repetition_field": true
                    },
                    "evenimente": {
                        "type": "field",
                        "required": true,
                        "read_only": false,
                        "label": "Evenimente",
                        "child": {
                            "type": "nested object",
                            "required": true,
                            "read_only": false,
                            "children": {
                                "observatii": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Observa\u021bii",
                                    "is_repetition_field": false
                                }
                            },
                            "is_repetition_field": false
                        },
                        "is_repetition_field": true
                    },
                    "mutari": {
                        "type": "field",
                        "required": true,
                        "read_only": false,
                        "label": "Mutari",
                        "child": {
                            "type": "nested object",
                            "required": true,
                            "read_only": false,
                            "children": {
                                "adresa": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Adresa",
                                    "is_repetition_field": false
                                },
                                "latitudine": {
                                    "type": "float",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Latitudine",
                                    "is_repetition_field": false
                                },
                                "longitudine": {
                                    "type": "float",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Longitudine",
                                    "is_repetition_field": false
                                },
                                "observatii": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Observa\u021bii",
                                    "is_repetition_field": false
                                },
                                "sursa": {
                                    "type": "string",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Sursa",
                                    "is_repetition_field": false
                                },
                                "localitate": {
                                    "type": "field",
                                    "required": false,
                                    "read_only": false,
                                    "label": "Tipul Formei de Relief",
                                    "fragment": "localitate",
                                    "is_repetition_field": false
                                }
                            },
                            "is_repetition_field": false
                        },
                        "is_repetition_field": true
                    },
                    "cadru": {
                        "type": "string",
                        "required": false,
                        "read_only": false,
                        "label": "Nume",
                        "max_length": 150,
                        "is_repetition_field": false
                    }
                },
                "is_repetition_field": false
            }
        }
    }
}