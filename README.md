# Dias API Automation

Bu proje, [Restful Booker](https://restful-booker.herokuapp.com/apidoc/index.html) servisleri üzerinde Python + Pytest kullanarak API otomasyon testleri yapmayı amaçlar. Her test çalışmasından sonra otomatik olarak HTML rapor oluşturulur.

## 🔧 Kurulum

```bash
# Reponun klonlanması
git clone https://github.com/goktugyavuz1/DiasAPIAutomation.git
cd DiasAPIAutomation


🚀 Kullanım
# Tüm testleri çalıştırmak için
pytest



🧪 Test Yapısı
├── tests/              # Test senaryoları
├── api_requests/       # API request tanımları
├── utils/              # Yardımcı fonksiyonlar
├── reports/            # Otomatik oluşturulan test raporları
├── conftest.py         # Ortak Pytest fixture'ları ve ayarları
├── config.py           # Ortam konfigürasyonu
└── requirements.txt    # Gerekli kütüphaneler


✅ Özellikler
Otomatik HTML test raporu

API seviyesinde CRUD testleri

Test verilerinin dinamik olarak alınması

Token bazlı kimlik doğrulama desteği

Pytest ile test sıralaması


