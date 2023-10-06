"""a"""
from getkey import getkey

hiragana_kana = {
    "あ": ["a"],
    "え": ["e"],
    "い": ["i"],
    "お": ["o"],
    "う": ["u"],
    "か": ["ka"],
    "け": ["ke"],
    "こ": ["ki"],
    "く": ["ku"],
    "さ": ["sa"],
    "せ": ["se"],
    "し": ["shi"],
    "そ": ["so"],
    "す": ["su"],
    "た": ["ta"],
    "て": ["te"],
    "ち": ["chi"],
    "と": ["to"],
    "つ": ["tsu"],
    "な": ["na"],
    "ね": ["ne"],
    "に": ["ni"],
    "の": ["no"],
    "ぬ": ["nu"],
    "は": ["ha"],
    "へ": ["he"],
    "ひ": ["hi"],
    "ほ": ["ho"],
    "ふ": ["hu", "fu"],
    "ま": [""],
    "め": [""],
    "み": [""],
    "も": [""],
    "む": [""],
    "": [""],
    "": [""],
    "": [""]
}

print("KANA TEST\n")
while True:
    hiragana_or_katakana = input("Hiragana (1) or Katana (2): ")
    if hiragana_or_katakana in ["1","2"]:
        break

if hiragana_or_katakana == "1":
    # hiragana test

elif hiragana_or_katakana == "2":
    # katakana test