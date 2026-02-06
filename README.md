# CSV-JSON-mini

## Topshiriq mazmuni
CSV fayldan ma'lumotlarni o'qib:
- qatorma-qator tekshirish (name bo'sh bo'lmasin, age manfiy bo'lmasin),
- city bo'yicha filter,
- JSON faylga yozish,
- va barcha xatolarni markazlashtirilgan context manager orqali boshqarish.

### Majburiy talablar (topshiriqdan qisqa konspekt)
- Custom exception: `Invalid(Exception)` (age < 0 bo'lsa).
- Custom context manager: `FileManager` (fayl ochish/yopish + xatolarni markazlashtirish).
- `read_csv(path) -> list[dict]`:
  - `csv.DictReader` bilan o'qish.
  - bo'sh CSV uchun `ValueError("CSV file is empty")`.
  - faqat `FileManager` orqali ochish.
- `validate_rows(rows) -> list[dict]`:
  - `id`, `age` -> `int`.
  - `name` bo'sh bo'lsa `ValueError` (xabarida `row=...` bo'lsin).
  - `age < 0` bo'lsa `Invalid`.
- `filter_by_city(rows, city)`.
- `to_json(rows, out_path)`:
  - yozish ham `FileManager` orqali.
- Logging (bonus):
  - console: INFO+
  - file: ERROR+
  - bosqich loglari: "CSV read started...", "Rows validated", "Filtered by city", "Saved JSON".

## Loyihamdagi fayllar (menda mavjud bo'lgan nomlar bilan)
- `main.py` — asosiy funksiya va oqim.
- `managers.py` — `FileManager` class.
- `exceptions.py` — custom exceptionlar.
- `logging_config.py` — logger sozlamalari (rangli console log).
- `data/users.csv` — test CSV.
- `output/users.json` — chiqarilgan JSON.

## Men bajargan ishlar (amaldagi kod bo'yicha)
- `csv.DictReader` bilan CSV o'qilgan.
- `FileManager` orqali file ochish ishlatilgan.
- `CSV file is empty` uchun `ValueError` bor.
- Qatorlarni tekshirish (name/id/age) mavjud.
- City bo'yicha filter bor.
- JSON yozish bor (format talabi e'tibordan chetda).

## Baholash (shartga ko'ra, nomlarga e'tibor bermasdan)
**Baho: 75/100**

### Nima uchun shu baho?
- **Talablar qisman bajarilgan**, lekin markaziy error handling va exception flow to'liq emas.
- **JSON chiqishi bor**, shuning uchun format sharti hisobga olinmadi.

#### Kuchli tomonlar
- CSV o‘qish `DictReader` bilan to‘g‘ri ishlatilgan.
- `FileManager` yordamida file ochish ishlatilgan.
- Bo‘sh CSV holati (`CSV file is empty`) ko‘tariladi.
- `row=` ko‘rsatish bor.

#### Kamchiliklar (bahoni pasaytirgan)
- `Invalid` exception ko‘tarilishi shart edi, lekin amalda log bilan “yutilib” ketadi.
- `__exit__` ichida `Invalid` alohida ishlanishi talab qilingan, hozir esa markaziy boshqaruv yo‘q.
- Xato bo‘lganda dastur to‘xtashi kerak (row=3/4), amalda esa davom etadi.
- Logging talablari to‘liq bajarilmagan (console INFO+, file ERROR+, bosqich loglari).

## Test CSV (berilgan shart)
`data/users.csv`
```
id,name,age,city
1,Ali,20,Tashkent
2,Vali,22,Samarkand
3,,19,Tashkent
4,Sardor,-1,Bukhara
```

## Qanday ishga tushirish
```
python main.py
```

## Izoh
Baholash nomlarga emas, ishlash prinsiplariga qarab qilindi. JSON format talabi (indent/ensure_ascii) bahoga ta'sir qilmadi.

## Yakuniy baho 
**75/100**
**Boshlangich middle lavel**

## Baholash manbai (AI)
Ushbu baho sun'iy intellekt tomonidan Cursor muhitida, GPT oilasidagi model yordamida berildi.
