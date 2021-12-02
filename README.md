# TheBrain2TiddlyNObsidian
Convert TheBrain database and notes to Tiddly json and Obsidian md, keeping almost all the links.


### Dependencies:
  Python3</br>
  sqlite3 for windows</br>
    https://sqlite.org</br>
  TheBrain (PersonalBrain) 9/10/11</br>
    www.thebrain.com</br>
  Tiddly</br>
    https://github.com/Jermolene/TiddlyDesktop</br>

### Basic Processing Flow:
  TheBrain (Brain.db, notes.html(s)) --> CSV (Thoughts.csv, Links.csv) --> TiddlyDesktop (Thoughts.json) --> Obsidian (md(s))

### Usage
*adjust python scripts first, such as filenames and paths*
echo sql.sql | sqlite3.exe
python3 thoughts2json.py
python3 json2Obsidian.py
