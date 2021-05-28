# VLN2-H12
**Verklegt námskeið 2, vor 2021**
**Hópur 12**
### Github
  - https://github.com/karljohann/VLN2-H12
## Efnisyfirlit

- [Til að byrja með](#til-ad-byrja-med)
  - [Ræsa hugbúnað](#raesa-hugbunad)
- [Example of features](#Example-of-features)
- [Vinnufyrirkomulag](#vinnufyrirkomulag)
- [Efni](#efni)


## Til að byrja með
### Forkröfur
`Python >= 3`
Sjá [requirements.txt](https://github.com/karljohann/VLN2-H12/blob/master/requirements.txt)

### Ræsa hugbúnað
* Keyra `python manage.py runserver`
* Keyra `python -m http.server 8001` úr sömu möppu
* Til að versla þarf að búa til notanda

### Tengjast grunn (dev)
cereal12-db@35.246.61.58
cereal12-db-user

## Example of extra features
   * Front page shows staff picks
   * Users have their own profile page to view
   * Users can view their order history
   * BLACK METAL THEMED
   * Pure covid team photo
   * Users can save their email address
   * Users can save their shipping/billing address
   * Users can save their payment information for later
   * Users can order products by brand
   * Superuser has access to an admin panel

## Vinnufyrirkomulag
### Fundir
Héldum morgunfundi klukkan 9

### Git issues
Notuðum git issues fyrir issue tracking

### Að vinna með branch í git
* `git checkout master` ef þið eruð ekki þar nú þegar
* `git pull` til að ná í nýjustu breytingar
* `git checkout -b new-branch-with-descriptive-name`
  - Nafnið á branchinu getur verið hvað sem er ([a-zA-Z0-9/-]) en það er ágætt að hafa eitthvað samræmi allavega. Eins og t.d. `project-name/branch-name-issuenumber` (`nan-ui/employee-list-84`) eða bara `emp-list`
* Gera svo það sem þið ætlið að gera
* `git add .` ef allt á að fara inn (passa hvað fer inn samt), `git add . -p` ef þið viljið fara yfir breytingarnar og samþykkja (góð venja) eða `git add -p path-to-file`
* `git commit -m "Allt sem þið gerðuð í stuttu máli, t.d. Adds functionality to print employees"` (næstum öll fyrirtæki á Íslandi eru með kóða, komment og git commit á ensku svo það er ágætt að venja sig á það)
* `git push`

Þá ætti kóðinn að vera kominn upp á Github. Þá þarf að fara í [Pull requests](https://github.com/karljohann/VLN2-H12/pulls) og búa til nýja pullu. Þar þarf að velja (hægra megin) það branch sem þið voruð að vinna á og master (vinstra megin). Í komment þar er fínt að skrifa nákvæmlega hvað þið voruð að gera og *hvernig á að testa það*. Stundum er nóg að fara yfir kóðann en ef það er einhver virkni þá þarf að skoða það sérstaklega og vera viss um að hún virki.

Frábært líka að muna að **eyða branch-inu** þegar maður er búinn að samþykkja PR-ið.

