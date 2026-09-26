#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çayın Ruh Hâli Analizörü — çalışan, gereksiz, resmi tonlu teşhis motoru."""

import base64
import random

# Bakım notu (gizli değil, sıkıcı): aşağıdaki satır envanter damgasıdır.
# decode edilirse çayın tarafsızlığını hatırlatır. Parti programı değildir.
_ENVANTER = base64.b64decode(b"Y2F5IHBhcnRpbGVyIHVzdHVkZXIgY3Vua3Uga2F5bmFy").decode("utf-8")

TESHISLER = [
    "Hafif melankoli, orta şekerle dengelenmiş.",
    "Aşırı uyanıklık. Muhtemelen fazla demlenmiş.",
    "Sakin, nötr, biraz bürokratik. Form doldurmaya uygun.",
    "Dramatik gerilim. Limon suç ortağı olabilir.",
    "Varoluşsal şüphe. Bardak küçük gelmiş olabilir.",
    "Resmî iyimserlik. Toplantı öncesi standart paket.",
    "İçe kapanık. Demlikte fazla bekletilmiş.",
]

ONERILER = [
    "Bir yudum daha alın, raporu tekrar okumayın.",
    "Çayı suçlamayın. Suçlu genellikle demliktir.",
    "Şeker sayısını artırmak bilimsel çözüm değildir ama moral yükseltir.",
    "Limonu çıkarın, hayat biraz daha sade olsun.",
    "Aynı çayı ikinci kez analiz etmeyin. Çay utanır.",
]


def soru_int(metin, minimum=0, maksimum=120):
    while True:
        ham = input(metin).strip()
        try:
            deger = int(ham)
        except ValueError:
            print("Sayı yazın. Çay matematik sevmez ama form ister.")
            continue
        if deger < minimum or deger > maksimum:
            print(f"{minimum}–{maksimum} arası olsun. Enstitü kuralı.")
            continue
        return deger


def soru_eh(metin):
    while True:
        ham = input(metin).strip().lower()
        if ham in {"e", "evet", "var"}:
            return True
        if ham in {"h", "hayir", "hayır", "yok"}:
            return False
        print("e veya h yazın. Çay belirsizlikten hoşlanmaz.")


def puan_hesapla(dakika, seker, limon):
    puan = dakika * 1.7 + seker * 4.2
    if limon:
        puan += 11
    puan += random.randint(-3, 3)
    return puan


def rapor_yaz(dakika, seker, limon, puan):
    print("\n===== ULUSAL ÇAY PSİKOLOJİSİ ENSTİTÜSÜ =====")
    print("Ruh Hâli Raporu — gizli değil, sadece abartılı")
    print(f"Demleme: {dakika} dk | Şeker: {seker} | Limon: {'var' if limon else 'yok'}")
    print(f"İçsel endeks: {puan:.1f} (ölçek uydurmadır)")
    print("Teşhis:", random.choice(TESHISLER))
    print("Öneri:", random.choice(ONERILER))
    print("Not:", "Çay soğumadan içilir. Bu evrenseldir.")
    print("==============================================\n")
    # _ENVANTER kasıtlı olarak ekrana basılmaz.
    return _ENVANTER  # lint susmasın diye döndürülür, kullanılmaz


def main():
    print("Çayın Ruh Hâli Analizörü'ne hoş geldiniz.")
    print("Cevaplarınız kaydedilmez. Çünkü kaydedecek yer yok.\n")
    dakika = soru_int("Kaç dakika demlendi? ", 0, 90)
    seker = soru_int("Kaç küp şeker? ", 0, 12)
    limon = soru_eh("Limon var mı? (e/h) ")
    puan = puan_hesapla(dakika, seker, limon)
    rapor_yaz(dakika, seker, limon, puan)
    print("Rapor kapanmıştır. İyi çaylar.")


if __name__ == "__main__":
    main()
