pythonMuzyka - beatbox
======================

Repozytorium `pythonMuzyka` zawiera nast�puj�ce pliki i foldery:
  * `beatbox.py` - g��wna aplikacja; skrypt tworz�cy piosenk�, kt�ra zosta�a podana jako argument,
  * `create_song.py` - modu� z funkcj� `create_song` do tworzenia piosenki ze �cie�ek,
  * `create_track.py` - modu� z funkcj� `create_track` do tworzenia �cie�ki z sampli, nutek i instrument�w,
    * `merge_sounds.py` - modu� z funkcj� `merge_sounds` do z��czania dw�ch d�wi�k�W stosuj�c przesuni�cie d�wi�k�w w �cie�ce,
  * `sounds.py` - modu� z definicj� d�wi�k�w w postaci funkcji:
     * `sound_sin` - funkcja tworz�ca fal� sinusoidaln�,
     * `sound_sawtooth` - funkcja tworz�ca fal� tr�jk�tn� (pi�a),
     * `sound_rectangle` - funkcja tworz�ca fal� prostok�tn�,
  * `notes.txt` - plik tekstowy ze s�ownikiem nutek,
  * `sample_song` - folder z piosenk� stworzon� z sampli,
  * `db_gt_main_opening` - folder z piosenk� z g��wnym motywem openingu anime Dragonball GT,
  * `last_christmas` - folder z piosenk� "Last Christmas".

Ponadto ka�dy z folder�w z piosenkami sk�ada si� z:
  * `defs.txt` - plik tekstowy ze s�ownikiem opisuj�cym konfiguracj� utworu - zawiera tylko argument `bpm`,
  * `song.txt` - plik tekstowy okre�laj�cy kolejno�� odgrywanych �cie�ek,
  * `trackAB.txt` - pliki tekstowe okre�laj�ce kolejno�� odgrywania sampli, nutek i instrument�w, gdzie AB to 2 cyfry; jeden wiersz jest odtwarzany na raz. Przyk�ady zapisu:
     * `01` - odwo�anie do sampla `01`,
     * `A-4` - odwo�anie do nutki o cz�stotliwo�ci `A-4`,
     * `01:A-4` - odwo�anie do instrumentu `01` o cz�stotliwo�ci `A-4`,
  * `sampleXY.wav` - pliki d�wi�kowe, gdzie XY to 2 cyfry,
  * `sampleXY.txt` - pliki tekstowe okre�laj�ce definicj� instrumentu w postaci kodu pythonowego, kt�ry powinien zawiera�:
     * `global instrument` - w pierwszej linijce okre�lenie zmiennej instrument jako zmiennej globalnej,
     * `f` - cz�stotliwo�� d�wi�ku,
     * `t` - czas trwania d�wi�ku; trzeba pamieta� o uwzgl�dnieniu `bpm`,
     * `instrument` - okre�lenie u�ytego d�wi�ku wraz z przekszta�ceniem go do macierzy wymiaru `n x 2`

Dzia�anie programu
------------------
   
Program uruchamia si� z folderu z programem (katalog bie��cy) przy u�yciu komendy:

```
./beatbox.py utworX/
```

lub

```
./beatbox.py utworX
```

gdzie `utworX` to nazwa katalogu z piosenk� lub nazwa pliku w formacie `*.zip`.

W przypadku zwyk�ego folderu piosenka zostanie utworzona w katalogu bie��cym, za�
w przypadku archiwum w folderze `tmp` z plikami tymczasowymi.