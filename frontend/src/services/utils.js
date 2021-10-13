const Colors = {
  categories: {
    edu: '#287DFF',
    cul: '#EB28FF',
    soc: '#8228FF',
    med: '#4AD1A8',
    san: '#FF2828',
    bus: '#28C8FF',
    dig: '#FF8428',
    adm: '#5A28FF',
  },
}

const DummyFilters = {
  basic: {
    judete: [
      {
        id: 3,
        value: 'Arad',
      },
    ],
    localitati: [
      {
        id: 8,
        value: 'Corbesti',
        judet: 3,
      },
    ],
    conservare: [],
    valoare: [],
    prioritizare: [],
  },
  advanced: [
    {
      title: 'Identificare',
      key: 'identificare',
      filters: [],
    },
    {
      title: 'Istoric',
      key: 'istoric',
      filters: [],
    },
    {
      title: 'Descriere Arhitectură / Peisaj',
      key: 'descriere',
      filters: [
        {
          title: 'Amplasament',
          key: 'amplasament',
          values: [
            {
              id: 1,
              nume: 'În cadrul așezării',
            },
          ],
        },
        {
          title: 'Topografie',
          key: 'topografie',
          values: [
            {
              id: 2,
              nume: 'La înălțime',
            },
          ],
        },
        {
          title: 'Relatia Cu Cimitirul',
          key: 'relatia_cu_cimitirul',
          values: [
            {
              id: 1,
              nume: 'În cadrul cimitirului',
            },
          ],
        },
      ],
    },
    {
      title: 'Descriere Componenta Artistică',
      key: 'componenta_artistica',
      filters: [],
    },
    {
      title: 'Conservare',
      key: 'conservare',
      filters: [],
    },
    {
      title: 'Valoare',
      key: 'valoare',
      filters: [],
    },
  ],
}

export { Colors, DummyFilters }
