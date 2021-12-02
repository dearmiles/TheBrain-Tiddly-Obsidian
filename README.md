# TheBrain2TiddlyNObsidian
Convert TheBrain database and notes to Tiddly json and Obsidian md, while keeping almost all the links.

Tired of the changing of fee and licensing policy for TheBrain when main release come out, I tried several alternatives for TheBrain. The two most useful tools among those alternatives are Tiddly, especially TiddlyDesktop, and Obsidian. And Obsidian stands out for the better and seemingly sustainable community support. I've recorded core scripts along the process which I followed when migrating from TheBrain to these 2 tools. 

I uploaded all of these here, with a brief description.

### Dependencies:
  - Python3</br>
  - sqlite3 for windows</br>
    https://sqlite.org</br>
  - TheBrain (PersonalBrain) 9/10/11</br>
    http://www.thebrain.com</br>
  - Tiddly</br>
    https://github.com/Jermolene/TiddlyDesktop</br>
  - Obsidian
    https://obsidian.md/

### Basic Processing Flow:
  TheBrain (Brain.db, notes.html(s)) --> CSV (Thoughts.csv, Links.csv) --> TiddlyDesktop (Thoughts.json) --> Obsidian (md(s))

### Usage
*adjust python scripts first, such as filenames and paths, should you store your Brains or sqlite-tools in a different directory*

echo sql.sql | sqlite3.exe

python3 thoughts2json.py

python3 json2Obsidian.py

