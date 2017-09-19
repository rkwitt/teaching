# Uebungsblatt-1

## Aufgabe 1

Schreiben Sie eine Funktion die ein RGB Bild laedt, es ins HSV Farbschema konvertiert 
(nutzen Sie entweder die Konvertierungsfunktionen von `skimage`, oder implementieren Sie die 
Konvertierung selbst) und anschliessend den Mittelwert des H Kanals zurückliefert, z.B.,

```python
def avg_H_global(img_file_name):
  ...
  return avg_H_val
```

Testen Sie Ihre Funktion mit 

```
print avg_H_global('beach.jpg')
```

wobei `beach.jpg` in diesem Verzeichnis zu finden ist.

## Aufgabe 2

Schreiben Sie eine Funktion `avg_H_per_block`, die als Input den Dateinamen eines RGB Bildes, sowie ein 2-Tupel (N, M) erhaelt,
also

```python
def avg_H(image_file, block_size):
  ...
  return avg_H_val
```
Wie oben, soll die Funktion das RGB Bild zuerst ins HSV Farbschema konvertieren. Anschliessend unterteilen Sie das Bild in N * M (nicht-ueberlappende) Bloecke und berechnen für jeden Block den Mittelwert des H Kanals (wir betrachten nur den Fall wo die Bild Dimensionen durch die Blockgroesse teilbar sind). Die Funktion soll ein `numpy` Array der Grösse X * Y zurückgeben wobei an der (i , j )-ten Position des Arrays der mittlere H Wert des (i,j)-ten Blocks steht.

Testen Sie Ihre Funktion mit

```python
H_avg = avg_H('beach.jpg', (16,16))
plt.imshow(H_avg, cmap='gray')
```

**Hinweis**: Beide Uebungen koennen in einem Jupyter/IPython Notebook realisiert und abgegeben werden.



