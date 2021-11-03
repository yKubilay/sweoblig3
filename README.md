# sweoblig3
Repository for oblig 3 running github actions 

![Uploading 4b8f4bbc39ed3ade8639c9a91110b54b.png…]()

Kort forklaring:

I denne obligen satte jeg opp Github Actions for testene fra oblig 2. .yml filen fungerer som en egen maskin så alle avhengigheter
og funksjoner må settes opp manuelt, den setter først opp python i riktig versjon og deretter laster ned avhengigheter fra requirements.txt filen via pip om den finnes (-f). Deretter kjøres pytest ved commit/push til repository. Pytest vil finne testene så lenge de ligger i en test mappe med filnavn test_insertname.py. 

Oppgaven er gjort selvstendig
