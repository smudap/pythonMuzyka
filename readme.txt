pythonMuzyka - beatbox
======================

Repozytorium `pythonMuzyka` zawiera nastêpuj¹ce pliki i foldery:
  * `beatbox.py` - g³ówna aplikacja; skrypt tworz¹cy piosenkê, która zosta³a podana jako argument,
  * `create_song.py` - modu³ z funkcj¹ `create_song` do tworzenia piosenki ze œcie¿ek,
  * `create_track.py` - modu³ z funkcj¹ `create_track` do tworzenia œcie¿ki z sampli, nutek i instrumentów,
    * `merge_sounds.py` - modu³ z funkcj¹ `merge_sounds` do z³¹czania dwóch dŸwiêkóW stosuj¹c przesuniêcie dŸwiêków w œcie¿ce,
  * `sounds.py` - modu³ z definicj¹ dŸwiêków w postaci funkcji:
     * `sound_sin` - funkcja tworz¹ca falê sinusoidaln¹,
     * `sound_sawtooth` - funkcja tworz¹ca falê trójk¹tn¹ (pi³a),
     * `sound_rectangle` - funkcja tworz¹ca falê prostok¹tn¹,
  * `notes.txt` - plik tekstowy ze s³ownikiem nutek,
  * `sample_song` - folder z piosenk¹ stworzon¹ z sampli,
  * `db_gt_main_opening` - folder z piosenk¹ z g³ównym motywem openingu anime Dragonball GT,
  * `last_christmas` - folder z piosenk¹ "Last Christmas".

Ponadto ka¿dy z folderów z piosenkami sk³ada siê z:
  * `defs.txt` - plik tekstowy ze s³ownikiem opisuj¹cym konfiguracjê utworu - zawiera tylko argument `bpm`,
  * `song.txt` - plik tekstowy okreœlaj¹cy kolejnoœæ odgrywanych œcie¿ek,
  * `trackAB.txt` - pliki tekstowe okreœlaj¹ce kolejnoœæ odgrywania sampli, nutek i instrumentów, gdzie AB to 2 cyfry; jeden wiersz jest odtwarzany na raz. Przyk³ady zapisu:
     * `01` - odwo³anie do sampla `01`,
     * `A-4` - odwo³anie do nutki o czêstotliwoœci `A-4`,
     * `01:A-4` - odwo³anie do instrumentu `01` o czêstotliwoœci `A-4`,
  * `sampleXY.wav` - pliki dŸwiêkowe, gdzie XY to 2 cyfry,
  * `sampleXY.txt` - pliki tekstowe okreœlaj¹ce definicjê instrumentu w postaci kodu pythonowego, który powinien zawieraæ:
     * `global instrument` - w pierwszej linijce okreœlenie zmiennej instrument jako zmiennej globalnej,
     * `f` - czêstotliwoœæ dŸwiêku,
     * `t` - czas trwania dŸwiêku; trzeba pamietaæ o uwzglêdnieniu `bpm`,
     * `instrument` - okreœlenie u¿ytego dŸwiêku wraz z przekszta³ceniem go do macierzy wymiaru `n x 2`

Dzia³anie programu
------------------
   
Program uruchamia siê z folderu z programem (katalog bie¿¹cy) przy u¿yciu komendy:

```
./beatbox.py utworX/
```

lub

```
./beatbox.py utworX
```

gdzie `utworX` to nazwa katalogu z piosenk¹ lub nazwa pliku w formacie `*.zip`.

W przypadku zwyk³ego folderu piosenka zostanie utworzona w katalogu bie¿¹cym, zaœ
w przypadku archiwum w folderze `tmp` z plikami tymczasowymi.