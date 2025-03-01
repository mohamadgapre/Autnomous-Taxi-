graph = {
    'A': {
        'coordinates': {'x': 175, 'y': 459},
        #'F': {'weight': 261, 'direction': 'L', 'pedestrians': False, 'construction': False},
        'G': {'weight': 195, 'pedestrians': True, 'construction': False},
        'B': {'weight': 1355, 'pedestrians': False, 'construction': False},
    },
    'B': {
        'coordinates': {'x': 278, 'y': 393},
        'A': {'weight': 135, 'pedestrians': False, 'construction': False},
        'H': {'weight': 105, 'pedestrians': False, 'construction': False},
    },
    'C': {# References D
        'coordinates': {'x': 330, 'y': 387},
        'B': {'weight': 54, 'pedestrians': False, 'construction': False},
        'D': {'weight': 144, 'pedestrians': False, 'construction': False}
    },
    'D': {#**************************************************************
        'coordinates': {'x': 175, 'y': 459},
        'C': {'weight': 144, 'pedestrians': False, 'construction': False},
        'K': {'weight': 63, 'pedestrians': False, 'construction': False}
    },

    'E': {#**************************************************************
        'coordinates': {'x': 175, 'y': 459},
        'D': {'weight': 240, 'pedestrians': False, 'construction': False},
        'M': {'weight': 61, 'pedestrians': False, 'construction': False}
    },
    'F': {
        'coordinates': {'x': 23, 'y': 329},
        'A': {'weight': 261, 'pedestrians': False, 'construction': False},
        'G': {'weight': 143, 'pedestrians': True, 'construction': False},
        'R': {'weight': 194, 'pedestrians': False, 'construction': False}
    },
    'G': {
        'coordinates': {'x': 151, 'y': 266},
        'F': {'weight': 143, 'pedestrians': False, 'construction': False},
        'N': {'weight': 63, 'pedestrians': False, 'construction': False},
        'S': {'weight': 134, 'pedestrians': False, 'construction': False}
    },
    'H': {
        'coordinates': {'x': 273, 'y': 307},
        'I': {'weight': 34, 'pedestrians': False, 'construction': False}
    },
    'I': {
        'coordinates': {'x': 305, 'y': 296},
        'O': {'weight': 63, 'pedestrians': False, 'construction': False},
        'J': {'weight': 52, 'pedestrians': False, 'construction': False}
    },
    'J': {
        'coordinates': {'x': 344, 'y': 324},
        'C': {'weight': 72, 'pedestrians': False, 'construction': False},
    },
    'K': {#References D & E
        'coordinates': {'x': 446, 'y': 402},
        'D': {'weight': 63, 'pedestrians': False, 'construction': False},
        'E': {'weight': 149, 'pedestrians': False, 'construction': False},
        'L': {'weight': 109, 'pedestrians': False, 'construction': False}
    },
    'L': {
        'coordinates': {'x': 446, 'y': 293},
        'J': {'weight': 108, 'pedestrians': False, 'construction': False},
        'K': {'weight': 109, 'pedestrians': False, 'construction': False},
        'P': {'weight': 60, 'pedestrians': False, 'construction': False}
    },
    'M': {#References E
        'coordinates': {'x': 579, 'y': 293},
        'L': {'weight': 133, 'pedestrians': False, 'construction': False},
        'E': {'weight': 61, 'pedestrians': False, 'construction': False},
        'Q': {'weight': 60, 'pedestrians': False, 'construction': False}
    },
    'N': {
        'coordinates': {'x': 208, 'y': 241},
        'G': {'weight': 62, 'pedestrians': False, 'construction': False},
        'H': {'weight': 102, 'pedestrians': False, 'construction': False},
        'O': {'weight': 91, 'pedestrians': False, 'construction': False}
    },
    'O': {
        'coordinates': {'x': 299, 'y': 233},
        'N': {'weight': 91, 'pedestrians': False, 'construction': False},
        'I': {'weight': 63, 'pedestrians': False, 'construction': False},
        'P': {'weight': 147, 'pedestrians': True, 'construction': False},
        'U': {'weight': 98, 'pedestrians': False, 'construction': False}
    },
    'P': {
        'coordinates': {'x': 446, 'y': 233},
        'O': {'weight': 147, 'pedestrians': True, 'construction': False},
        'L': {'weight': 60, 'pedestrians': False, 'construction': False},
        'Q': {'weight': 133, 'pedestrians': False, 'construction': False},
        'V': {'weight': 98, 'pedestrians': False, 'construction': False}
    },
    'Q': {
        'coordinates': {'x': 579, 'y': 233},
        'P': {'weight': 133, 'pedestrians': False, 'construction': False},
        'M': {'weight': 60, 'pedestrians': False, 'construction': False},
        'W': {'weight': 98, 'pedestrians': False, 'construction': False}
    },
    'R': {
        'coordinates': {'x': 23, 'y': 135},
        'F': {'weight': 194, 'pedestrians': False, 'construction': False},
        'S': {'weight': 100, 'pedestrians': False, 'construction': True},
        'X': {'weight': 186, 'pedestrians': False, 'construction': False}
    },
    'S': {
        'coordinates': {'x': 123, 'y': 135},
        'R': {'weight': 100, 'pedestrians': False, 'construction': True},
        'T': {'weight': 84, 'pedestrians': False, 'construction': True},
        'X': {'weight': 106, 'pedestrians': False, 'construction': False}
    },
    'T': {
        'coordinates': {'x': 207, 'y': 135},
        'S': {'weight': 84, 'pedestrians': False, 'construction': True},
        'N': {'weight': 106, 'pedestrians': False, 'construction': False},
        'U': {'weight': 92, 'pedestrians': False, 'construction': True}
    },
    'U': {
        'coordinates': {'x': 299, 'y': 135},
        'T': {'weight': 92, 'pedestrians': False, 'construction': True},
        'O': {'weight': 98, 'pedestrians': False, 'construction': False},
        'V': {'weight': 147, 'pedestrians': False, 'construction': False},
        'Z': {'weight': 106, 'pedestrians': False, 'construction': False}
    },
    'V': {
        'coordinates': {'x': 446, 'y': 135},
        'U': {'weight': 147, 'pedestrians': False, 'construction': False},
        'P': {'weight': 98, 'pedestrians': False, 'construction': False},
        'W': {'weight': 133, 'pedestrians': False, 'construction': False},
        'Z1': {'weight': 106, 'pedestrians': False, 'construction': False}
    },
    'W': {
        'coordinates': {'x': 579, 'y': 135},
        'V': {'weight': 133, 'pedestrians': False, 'construction': False},
        'Q': {'weight': 98, 'pedestrians': False, 'construction': False},
        'Z1': {'weight': 228, 'pedestrians': False, 'construction': False}
    },
    'X': {
        'coordinates': {'x': 123, 'y': 29},
        'R': {'weight': 186, 'pedestrians': False, 'construction': False},
        'Y': {'weight': 84, 'pedestrians': False, 'construction': False}
    },
    'Y': {
        'coordinates': {'x': 207, 'y': 29},
        'X': {'weight': 84, 'pedestrians': False, 'construction': False},
        'T': {'weight': 106, 'pedestrians': False, 'construction': False},
        'Z': {'weight': 92, 'pedestrians': False, 'construction': False}
    },
    'Z': {
        'coordinates': {'x': 299, 'y': 29},
        'Y': {'weight': 92, 'pedestrians': False, 'construction': False},
        'U': {'weight': 106, 'pedestrians': False, 'construction': False},
        'Z1': {'weight': 147, 'pedestrians': False, 'construction': False}
    },
    'Z1': {
        'coordinates': {'x': 446, 'y': 29},
        'Z': {'weight': 147, 'pedestrians': False, 'construction': False},
        'V': {'weight': 106, 'pedestrians': False, 'construction': False},
        'W': {'weight': 228, 'pedestrians': False, 'construction': False}
    }
}
