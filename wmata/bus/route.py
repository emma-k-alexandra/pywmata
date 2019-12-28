"""MetroBus Routes
"""
from enum import Enum

class Route(Enum):
    _10A = "10A"
    _10A_v1 = "10Av1"
    _10B = "10B"
    _10Bc = "10Bc"
    _10E = "10E"
    _10N = "10N"
    _11Y = "11Y"
    _11Yv1 = "11Yv1"
    _11Yv2 = "11Yv2"
    _11Yv3 = "11Yv3"
    _11Yv4 = "11Yv4"
    _15K = "15K"
    _15Kv1 = "15Kv1"
    _16A = "16A"
    _16C = "16C"
    _16Cv1 = "16Cv1"
    _16E = "16E"
    _16G = "16G"
    _16Gv1 = "16Gv1"
    _16H = "16H"
    _16L = "16L"
    _16Y = "16Y"
    _16Yv1 = "16Yv1"
    _17B = "17B"
    _17G = "17G"
    _17H = "17H"
    _17K = "17K"
    _17L = "17L"
    _17M = "17M"
    _18G = "18G"
    _18H = "18H"
    _18J = "18J"
    _18P = "18P"
    _18Pv1 = "18Pv1"
    _18Pv2 = "18Pv2"
    _1A = "1A"
    _1B = "1B"
    _1C = "1C"
    _1Cv1 = "1Cv1"
    _1Cv2 = "1Cv2"
    _1Cv3 = "1Cv3"
    _1Cv4 = "1Cv4"
    _21A = "21A"
    _21D = "21D"
    _22A = "22A"
    _22Av1 = "22Av1"
    _22C = "22C"
    _22F = "22F"
    _23A = "23A"
    _23B = "23B"
    _23Bv1 = "23Bv1"
    _23T = "23T"
    _25B = "25B"
    _25Bv1 = "25Bv1"
    _25Bv2 = "25Bv2"
    _25Bv3 = "25Bv3"
    _26A = "26A"
    _28A = "28A"
    _28Av1 = "28Av1"
    _28F = "28F"
    _28G = "28G"
    _29C = "29C"
    _29G = "29G"
    _29K = "29K"
    _29Kv1 = "29Kv1"
    _29N = "29N"
    _29Nv1 = "29Nv1"
    _29W = "29W"
    _2A = "2A"
    _2B = "2B"
    _2Bv1 = "2Bv1"
    _2Bv2 = "2Bv2"
    _2Bv3 = "2Bv3"
    _30N = "30N"
    _30S = "30S"
    _31 = "31"
    _32 = "32"
    _32v1 = "32v1"
    _33 = "33"
    _34 = "34"
    _36 = "36"
    _37 = "37"
    _38B = "38B"
    _38Bv1 = "38Bv1"
    _38Bv2 = "38Bv2"
    _39 = "39"
    _3A = "3A"
    _3Av1 = "3Av1"
    _3T = "3T"
    _3Tv1 = "3Tv1"
    _3Y = "3Y"
    _42 = "42"
    _43 = "43"
    _4A = "4A"
    _4B = "4B"
    _52 = "52"
    _52v1 = "52v1"
    _52v2 = "52v2"
    _52v3 = "52v3"
    _54 = "54"
    _54v1 = "54v1"
    _59 = "59"
    _5A = "5A"
    _54v2 = "54v2"
    _54v3 = "54v3"
    _60 = "60"
    _62 = "62"
    _62v1 = "62v1"
    _63 = "63"
    _64 = "64"
    _64v1 = "64v1"
    _70 = "70"
    _70v1 = "70v1"
    _74 = "74"
    _79 = "79"
    _7A = "7A"
    _7Av1 = "7Av1"
    _7Av2 = "7Av2"
    _7Av3 = "7Av3"
    _7C = "7C"
    _7F = "7F"
    _7Fv1 = "7Fv1"
    _7M = "7M"
    _7Mv1 = "7Mv1"
    _7P = "7P"
    _7W = "7W"
    _7Y = "7Y"
    _7Yv1 = "7Yv1"
    _80 = "80"
    _80v1 = "80v1"
    _80v2 = "80v2"
    _80v3 = "80v3"
    _83 = "83"
    _83v1 = "83v1"
    _83v2 = "83v2"
    _83v3 = "83v3"
    _83v4 = "83v4"
    _86 = "86"
    _86v1 = "86v1"
    _86v2 = "86v2"
    _87 = "87"
    _87v1 = "87v1"
    _87v2 = "87v2"
    _87v3 = "87v3"
    _87v4 = "87v4"
    _87v5 = "87v5"
    _87c = "87c"
    _89 = "89"
    _89v1 = "89v1"
    _89M = "89M"
    _8S = "8S"
    _8W = "8W"
    _8Z = "8Z"
    _90 = "90"
    _90v1 = "90v1"
    _90v2 = "90v2"
    _92 = "92"
    _92v1 = "92v1"
    _92v2 = "92v2"
    _96 = "96"
    _96v1 = "96v1"
    _96v2 = "96v2"
    _96v3 = "96v3"
    _96v4 = "96v4"
    _96v5 = "96v5"
    _97 = "97"
    _97v1 = "97v1"
    A12 = "A12"
    A12v1 = "A12v1"
    A12v2 = "A12v2"
    A12v3 = "A12v3"
    A2 = "A2"
    A2v1 = "A2v1"
    A2v2 = "A2v2"
    A2v3 = "A2v3"
    A31 = "A31"
    A32 = "A32"
    A33 = "A33"
    A4 = "A4"
    A4v1 = "A4v1"
    A4v2 = "A4v2"
    A4v3 = "A4v3"
    A4v4 = "A4v4"
    A4v5 = "A4v5"
    A6 = "A6"
    A6v1 = "A6v1"
    A7 = "A7"
    A8 = "A8"
    A8v1 = "A8v1"
    A9 = "A9"
    B2 = "B2"
    B2v1 = "B2v1"
    B2v2 = "B2v2"
    B2v3 = "B2v3"
    B2v4 = "B2v4"
    B21 = "B21"
    B22 = "B22"
    B22v1 = "B22v1"
    B24 = "B24"
    B24v1 = "B24v1"
    B27 = "B27"
    B29 = "B29"
    B29v1 = "B29v1"
    B29v2 = "B29v2"
    B30 = "B30"
    B8 = "B8"
    B8v1 = "B8v1"
    B8v2 = "B8v2"
    B9 = "B9"
    B98 = "B98"
    B99 = "B99"
    C11 = "C11"
    C12 = "C12"
    C13 = "C13"
    C14 = "C14"
    C2 = "C2"
    C2v1 = "C2v1"
    C2v2 = "C2v2"
    C2v3 = "C2v3"
    C21 = "C21"
    C21v1 = "C21v1"
    C21v2 = "C21v2"
    C22 = "C22"
    C22v1 = "C22v1"
    C26 = "C26"
    C26v1 = "C26v1"
    C28 = "C28"
    C28v1 = "C28v1"
    C29 = "C29"
    C29_1 = "C29*1"
    C29_2 = "C29*2"
    C29_4 = "C29*4"
    C29_ = "C29/"
    C290 = "C290"
    C4 = "C4"
    C4v1 = "C4v1"
    C4v2 = "C4v2"
    C4v3 = "C4v3"
    C8 = "C8"
    C8v1 = "C8v1"
    C8v2 = "C8v2"
    C8v3 = "C8v3"
    D1 = "D1"
    D12 = "D12"
    D12v1 = "D12v1"
    D12v2 = "D12v2"
    D13 = "D13"
    D13v1 = "D13v1"
    D14 = "D14"
    D14v1 = "D14v1"
    D14v2 = "D14v2"
    D2 = "D2"
    D2v1 = "D2v1"
    D31 = "D31"
    D32 = "D32"
    D33 = "D33"
    D34 = "D34"
    D4 = "D4"
    D4v1 = "D4v1"
    D4v2 = "D4v2"
    D5 = "D5"
    D51 = "D51"
    D6 = "D6"
    D6v1 = "D6v1"
    D6v2 = "D6v2"
    D6v3 = "D6v3"
    D8 = "D8"
    D8v1 = "D8v1"
    E2 = "E2"
    E4 = "E4"
    E4v1 = "E4v1"
    E4v2 = "E4v2"
    E6 = "E6"
    F1 = "F1"
    F12 = "F12"
    F12v1 = "F12v1"
    F13 = "F13"
    F13v1 = "F13v1"
    F13v2 = "F13v2"
    F13v3 = "F13v3"
    F14 = "F14"
    F14v1 = "F14v1"
    F2 = "F2"
    F2v1 = "F2v1"
    F2v2 = "F2v2"
    F4 = "F4"
    F4v1 = "F4v1"
    F4v2 = "F4v2"
    F6 = "F6"
    F6v1 = "F6v1"
    F6v2 = "F6v2"
    F8 = "F8"
    F99 = "F99"
    G12 = "G12"
    G12v1 = "G12v1"
    G12v2 = "G12v2"
    G13 = "G13"
    G14 = "G14"
    G14v1 = "G14v1"
    G14v2 = "G14v2"
    G16 = "G16"
    G16v1 = "G16v1"
    G2 = "G2"
    G2v1 = "G2v1"
    G8 = "G8"
    G8v1 = "G8v1"
    G8v2 = "G8v2"
    G8v3 = "G8v3"
    G9 = "G9"
    G9v1 = "G9v1"
    H1 = "H1"
    H11 = "H11"
    H12 = "H12"
    H12v1 = "H12v1"
    H13 = "H13"
    H2 = "H2"
    H3 = "H3"
    H4 = "H4"
    H4v1 = "H4v1"
    H6 = "H6"
    H6v1 = "H6v1"
    H8 = "H8"
    H9 = "H9"
    J1 = "J1"
    J1v1 = "J1v1"
    J12 = "J12"
    J12v1 = "J12v1"
    J2 = "J2"
    J2v1 = "J2v1"
    J2v2 = "J2v2"
    J4 = "J4"
    K12 = "K12"
    K12v1 = "K12v1"
    K12v2 = "K12v2"
    K2 = "K2"
    K6 = "K6"
    K6v1 = "K6v1"
    K9 = "K9"
    K9v1 = "K9v1"
    L1 = "L1"
    L2 = "L2"
    L2v1 = "L2v1"
    L2v2 = "L2v2"
    L99 = "L99"
    L8 = "L8"
    M4 = "M4"
    M4v1 = "M4v1"
    M4v2 = "M4v2"
    M6 = "M6"
    M6v1 = "M6v1"
    MW1 = "MW1"
    M99 = "M99"
    N2 = "N2"
    N4 = "N4"
    N4v1 = "N4v1"
    N6 = "N6"
    NH1 = "NH1"
    NH2 = "NH2"
    P12 = "P12"
    P12v1 = "P12v1"
    P12v2 = "P12v2"
    P18 = "P18"
    P19 = "P19"
    P6 = "P6"
    P6v1 = "P6v1"
    P6v2 = "P6v2"
    P6v3 = "P6v3"
    P6v4 = "P6v4"
    P99 = "P99"
    Q1 = "Q1"
    Q2 = "Q2"
    Q2v1 = "Q2v1"
    Q2v2 = "Q2v2"
    Q4 = "Q4"
    Q4v1 = "Q4v1"
    Q5 = "Q5"
    Q6 = "Q6"
    Q6v1 = "Q6v1"
    R1 = "R1"
    R12 = "R12"
    R12v1 = "R12v1"
    R2 = "R2"
    R2v1 = "R2v1"
    R2v2 = "R2v2"
    R3 = "R3"
    R4 = "R4"
    R11 = "R11"
    REX = "REX"
    REXv1 = "REXv1"
    REXv2 = "REXv2"
    REXv3 = "REXv3"
    REXv4 = "REXv4"
    S1 = "S1"
    S2 = "S2"
    S2v1 = "S2v1"
    S35 = "S35"
    S4 = "S4"
    S41 = "S41"
    S80 = "S80"
    S80v1 = "S80v1"
    S80v2 = "S80v2"
    S9 = "S9"
    S9v1 = "S9v1"
    S91 = "S91"
    S91v1 = "S91v1"
    SH99 = "SH99"
    T14 = "T14"
    T14v1 = "T14v1"
    T18 = "T18"
    T18v1 = "T18v1"
    T2 = "T2"
    U4 = "U4"
    U4v1 = "U4v1"
    U4v2 = "U4v2"
    U5 = "U5"
    U6 = "U6"
    U6v1 = "U6v1"
    U6v2 = "U6v2"
    U7 = "U7"
    U7v1 = "U7v1"
    U7v2 = "U7v2"
    U7v3 = "U7v3"
    U7v4 = "U7v4"
    V1 = "V1"
    V12 = "V12"
    V14 = "V14"
    V14v1 = "V14v1"
    V2 = "V2"
    V2v1 = "V2v1"
    V4 = "V4"
    V4v1 = "V4v1"
    V7 = "V7"
    V7v1 = "V7v1"
    V7v2 = "V7v2"
    V7c = "V7c"
    V7cv1 = "V7cv1"
    V8 = "V8"
    V9 = "V9"
    W1 = "W1"
    W14 = "W14"
    W14v1 = "W14v1"
    W14v2 = "W14v2"
    W2 = "W2"
    W2v1 = "W2v1"
    W2v2 = "W2v2"
    W2v3 = "W2v3"
    W2v4 = "W2v4"
    W2v5 = "W2v5"
    W2v6 = "W2v6"
    W2v7 = "W2v7"
    W3 = "W3"
    W3v1 = "W3v1"
    W4 = "W4"
    W4v1 = "W4v1"
    W4v2 = "W4v2"
    W45 = "W45"
    W47 = "W47"
    W5 = "W5"
    W6 = "W6"
    W6v1 = "W6v1"
    W8 = "W8"
    W8v1 = "W8v1"
    W8v2 = "W8v2"
    X1 = "X1"
    X2 = "X2"
    X2v1 = "X2v1"
    X2v2 = "X2v2"
    X2v3 = "X2v3"
    X3 = "X3"
    X3v1 = "X3v1"
    X8 = "X8"
    X9 = "X9"
    X9v1 = "X9v1"
    X9v2 = "X9v2"
    Y2 = "Y2"
    Y7 = "Y7"
    Y8 = "Y8"
    Z11 = "Z11"
    Z11v1 = "Z11v1"
    Z2 = "Z2"
    Z2v1 = "Z2v1"
    Z2v2 = "Z2v2"
    Z2v3 = "Z2v3"
    Z6 = "Z6"
    Z6v1 = "Z6v1"
    Z6v2 = "Z6v2"
    Z7 = "Z7"
    Z7v1 = "Z7v1"
    Z8 = "Z8"
    Z8v1 = "Z8v1"
    Z8v2 = "Z8v2"
    Z8v3 = "Z8v3"
    Z8v4 = "Z8v4"
    Z8v5 = "Z8v5"
    Z8v6 = "Z8v6"
