# sweoblig3
Repository for oblig 3 running github actions 


Kort forklaring:

I denne obligen satte jeg opp Github Actions for testene fra oblig 2. .yml filen fungerer som en egen maskin så alle avhengigheter
og funksjoner må settes opp manuelt, den setter først opp python i riktig versjon og deretter laster ned avhengigheter fra requirements.txt filen via pip om den finnes (-f). Deretter kjøres pytest ved commit/push til repository. Pytest vil finne testene så lenge de ligger i en test mappe med filnavn test_insertname.py. 

Oppgaven er gjort selvstendig

Log for successful push:

![githubacctionlog1](https://user-images.githubusercontent.com/35852691/140220163-58f65d4c-2dd1-4202-a7ba-98b78d90ab72.png)


Log for unsucessful push:

![githubactionlog2](https://user-images.githubusercontent.com/35852691/140218757-ca9388c4-bffa-46f9-b94f-5c04dc800e54.png)
