Ovaj softver je prvenstveno namijenjen da pokaze moje vjestine programiranja u Python-u. U pitanju je softver koji je kao product management i napisan je samo u Python-u.

Opis klasa i njihovih funkcionalnosti:

Product
- Svrha: predstavljanje pojedinačnog proizvoda u inventaru.
- Atributi:
- name (str) — naziv proizvoda
- price (float) — jedinična cijena proizvoda (ne-negativna)
- quantity (int) — dostupna količina na zalihama (ne-negativna)
- Glavne metode:
- info() -> str — vraća formatirani string sa imenom, cenom i količinom
- update_quantity(new_quantity: int) — ažurira količinu (validira ne-negativnost)
- total_value() -> float — vraća price * quantity za taj proizvod
- Napomene: konstruktora i metode validiraju negativne vrednosti kako bi se izbegle netačne zalihe.
ProductManager
- Svrha: upravljanje kolekcijom proizvoda (inventar).
- Atributi:
- products (List[Product]) — lista svih dostupnih proizvoda
- Glavne metode:
- add_product(product: Product) — dodaje proizvod u inventar; ako proizvod sa istim imenom već postoji (case‑insensitive), ažurira cenu i sabira količine umjesto dodavanja duplikata
- show_products() -> str — vraća formatiran prikaz svih proizvoda ili poruku ako nema proizvoda
- total_inventory_value() -> float — računa ukupnu vrednost inventara (sum of price * quantity za sve proizvode)
- remove_product_by_name(name: str) -> bool — uklanja prvi proizvod koji odgovara imenu (case‑insensitive); vraća True ako je uklonjen, False ako nije pronađen
- Napomene: logika spajanja po imenu olakšava upravljanje inventarom bez duplikata.
Cart
- Svrha: modeliranje korpe kupca i izračunavanje iznosa za naplatu.
- Atributi:
- cart_items (List[Product]) — lista proizvoda koji su dodati u korpu; svaka stavka može imati svoju quantity vrednost
- Glavne metode:
- add_product(product: Product) — dodaje proizvod u korpu; implementacija obično dodaje kopiju proizvoda ili stavku sa željenom količinom kako promene na originalu ne bi uticale na korpu
- total_due() -> float — računa ukupno za naplatu: sum(item.price * item.quantity) za sve stavke u korpi
- show_cart() -> str — vraća formatiran prikaz sadržaja korpe i iznosa po liniji; ako je prazna, vraća poruku
