const Colors = {
  conservare: ['#25E2E2', '#85D634', '#F6D52B', '#FF7E06', '#FB5D5D'],
  // conservare: ['#25E2E2', '#85D634', '#F6D52B', '#FF7E06', '#FB5D5D'],
}

const BasicFilters = {
  conservare: {
    label: 'Stare de conservare',
    default: {
      background:
        'conic-gradient(from 180deg at 50% 50%, #79D2A4 0deg, #5D86EF 84.38deg, #945DEF 174.38deg, #EF8B5D 270deg, #F24A4A 360deg)',
      value: 'Toate',
    },
    options: [
      {
        id: 1,
        value: 'Foarte bună',
      },
      {
        id: 2,
        value: 'Bună',
      },
      {
        id: 3,
        value: 'Medie',
      },
      {
        id: 4,
        value: 'Proastă',
      },
      {
        id: 5,
        value: 'Foarte proastă',
      },
    ],
  },
  prioritizare: {
    label: 'Prioritizare',
    default: {
      background: '#484646',
      value: 'Toate',
    },
    options: [
      {
        id: 1,
        interval: [1, 5],
        value: 'Ridicată (1-5)',
        size: 24,
      },
      {
        id: 2,
        interval: [6, 10],
        value: 'Medie (6-10)',
        size: 12,
      },
      {
        id: 3,
        interval: [11, 15],
        value: 'Scăzută (11-15)',
        size: 8,
      },
    ],
  },
  valoare: {
    label: 'Valoare patrimoniu',
    default: {
      background: '#2A2828',
      id: '+',
      value: 'Toate',
    },
    options: [
      { id: 'A', value: 'Națională/Internațională' },
      { id: 'B', value: 'Regională' },
      { id: 'C', value: 'Locală' },
    ],
  },
}

const BooleanOptions = {
  true: 'Da',
  false: 'Nu',
}

export { Colors, BooleanOptions, BasicFilters }
