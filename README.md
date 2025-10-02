# 🔗 LinkSaver

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-orange.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![Requests](https://img.shields.io/badge/Requests-latest-red.svg)](https://requests.readthedocs.io/)

> A lightweight, efficient web scraping utility that extracts and exports all hyperlinks from any website into a structured text file.

---

## 📋 Overview

**LinkSaver** is a Python-based web scraping tool designed to streamline the process of extracting hyperlinks from websites. Whether you're conducting SEO audits, performing competitive analysis, building sitemaps, or validating external links, LinkSaver provides a quick and reliable solution for link extraction.

This tool demonstrates practical application of web scraping techniques using industry-standard libraries, showcasing skills in HTTP request handling, HTML parsing, and data extraction—essential competencies for modern software development and data engineering roles.

### 🎯 Use Cases

- **SEO Analysis**: Extract all internal and external links for comprehensive site audits
- **Link Validation**: Identify broken links and outdated references across web properties
- **Competitive Research**: Analyze competitor website structures and link strategies
- **Sitemap Generation**: Create preliminary data for sitemap construction
- **Content Migration**: Document existing link structures before website redesigns
- **Academic Research**: Collect reference links from research databases or documentation sites

---

## ✨ Key Features

- **🚀 Simple & Fast**: Extract all links from a webpage with a single command
- **🎯 Comprehensive Extraction**: Captures all `<a>` tag href attributes from target URLs
- **📝 Clean Output**: Exports links to organized, line-separated text files for easy processing
- **🔧 Minimal Setup**: Only two lightweight dependencies required
- **💻 Cross-Platform**: Works seamlessly on Windows, macOS, and Linux
- **🔍 HTML Parser**: Leverages BeautifulSoup4's robust parsing capabilities for reliable extraction
- **🌐 HTTP Handling**: Built on the Requests library for stable and efficient web requests
- **📦 Lightweight**: Minimal resource footprint, perfect for automation and batch processing

---

## 🛠️ Tech Stack

### Core Technologies
- **Python 3.7+**: Modern Python leveraging clean syntax and robust standard libraries
- **Requests**: Industry-standard HTTP library for making web requests with elegant API
- **BeautifulSoup4**: Powerful HTML/XML parsing library for web scraping and data extraction

### Design Approach
This project follows a functional programming paradigm with a focus on simplicity and maintainability. The architecture prioritizes:
- **Separation of Concerns**: Distinct function for link extraction logic
- **Reusability**: Modular design allows easy integration into larger projects
- **Readability**: Clean, self-documenting code following Python best practices (PEP 8)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher installed on your system
- pip (Python package manager)
- Internet connection for web requests

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/ensuca/linkSaver.git
cd linkSaver
```

2. **Install Dependencies**
```bash
pip install requests
pip install beautifulsoup4
```

Or install both at once:
```bash
pip install requests beautifulsoup4
```

### Configuration

Before running the script, configure your target URL:

1. Open `linkSaver.py` in your preferred text editor
2. Locate line 18:
```python
url = 'https://www.example.com'  # Write the address of the website which you want the link addresses
```
3. Replace `'https://www.example.com'` with your target website URL
4. (Optional) Modify the output filename on line 19 if desired:
```python
output_file = 'links.txt'
```

---

## 💡 Usage

### Basic Usage

After configuring your target URL, simply run:

```bash
python linkSaver.py
```

The script will:
1. Send an HTTP GET request to the specified URL
2. Parse the HTML response
3. Extract all `href` attributes from `<a>` tags
4. Save the results to `links.txt` in the current directory

### Example

```python
# Configure your target in linkSaver.py
url = 'https://www.python.org'
output_file = 'python_links.txt'

# Run the script
save_links_to_file(url, output_file)
```

**Output** (`python_links.txt`):
```
https://www.python.org/about/
https://www.python.org/downloads/
https://www.python.org/doc/
https://www.python.org/community/
/success-stories/
...
```

### Integration Example

LinkSaver can be easily integrated into larger projects:

```python
from linkSaver import save_links_to_file

# Extract links from multiple sites
websites = [
    'https://example1.com',
    'https://example2.com',
    'https://example3.com'
]

for i, site in enumerate(websites):
    save_links_to_file(site, f'links_site_{i}.txt')
    print(f"✅ Extracted links from {site}")
```

---

## 📁 Project Structure

```
linkSaver/
├── linkSaver.py        # Main script containing link extraction logic
├── README.md           # Project documentation (this file)
├── README.txt          # Legacy documentation
├── .gitattributes      # Git configuration
└── links.txt           # Output file (generated after running)
```

### Core Components

**`save_links_to_file(url, output_file)`**
- **Parameters**:
  - `url` (str): Target website URL to scrape
  - `output_file` (str): Path for output text file
- **Returns**: None
- **Functionality**: Orchestrates HTTP request, HTML parsing, link extraction, and file writing

**Location**: linkSaver.py:5

---

## 🔍 How It Works

### Technical Implementation

1. **HTTP Request**: Uses `requests.get()` to fetch the HTML content from the target URL
2. **HTML Parsing**: BeautifulSoup parses the raw HTML into a navigable tree structure
3. **Link Extraction**: The `.find_all('a')` method locates all anchor tags in the document
4. **Attribute Extraction**: Extracts `href` attributes using `.get('href')` with null checking
5. **File Output**: Writes each link to a new line in the specified output file

### Code Flow

```
User Input (URL)
    ↓
HTTP GET Request (requests)
    ↓
HTML Response
    ↓
Parse HTML (BeautifulSoup)
    ↓
Extract <a> tags
    ↓
Get href attributes
    ↓
Write to File (links.txt)
    ↓
Complete ✅
```

---

## ⚡ Performance Considerations

- **Lightweight**: Minimal memory footprint, suitable for scraping large pages
- **Efficient Parsing**: BeautifulSoup4's lxml parser (if available) provides optimal performance
- **Single Request**: One HTTP request per execution minimizes network overhead
- **Stream Writing**: File is written incrementally, preventing memory issues with large link sets

### Typical Execution Time
- Small website (<100 links): < 1 second
- Medium website (100-1000 links): 1-3 seconds
- Large website (1000+ links): 3-10 seconds

*Performance varies based on network speed and target server response time*

---

## 🧪 Testing

### Manual Testing Procedure

1. **Test with a known website**:
```bash
# Set url = 'https://www.python.org' in linkSaver.py
python linkSaver.py
```

2. **Verify output**:
```bash
cat links.txt  # Linux/Mac
type links.txt  # Windows
```

3. **Validate link count**:
```python
with open('links.txt', 'r') as f:
    link_count = len(f.readlines())
    print(f"Extracted {link_count} links")
```

### Test Cases

✅ **Valid Website URL**: Successfully extracts links
✅ **HTTPS URLs**: Handles secure connections
✅ **Relative Links**: Captures partial URLs (e.g., `/about`, `#contact`)
✅ **Empty href**: Filters out null/empty href attributes
✅ **Large Pages**: Processes pages with 1000+ links

---

## 🚀 Deployment & Automation

### Scheduled Execution (Linux/Mac)

Add to crontab for daily link extraction:
```bash
0 2 * * * cd /path/to/linkSaver && /usr/bin/python3 linkSaver.py
```

### Windows Task Scheduler

Create a batch file (`run_linksaver.bat`):
```batch
@echo off
cd C:\Projects\linkSaver
python linkSaver.py
```

Schedule via Task Scheduler for automated execution.

### Docker Deployment

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY linkSaver.py .
RUN pip install requests beautifulsoup4
CMD ["python", "linkSaver.py"]
```

---

## 🗺️ Roadmap & Future Enhancements

### Planned Features

- [ ] **Command-Line Interface**: Add argparse for URL and output file arguments
- [ ] **Error Handling**: Implement try-except blocks for network errors and invalid URLs
- [ ] **Link Validation**: Add HTTP status code checking for each extracted link
- [ ] **Format Options**: Support JSON, CSV, and XML output formats
- [ ] **Recursive Crawling**: Option to follow links and extract from multiple pages
- [ ] **Filter Options**: Filter by domain, protocol (http/https), or URL patterns
- [ ] **Progress Indicator**: Add progress bar for large sites using tqdm
- [ ] **Async Requests**: Implement async HTTP requests for faster bulk scraping
- [ ] **GUI Interface**: Tkinter-based desktop application for non-technical users
- [ ] **Link Categorization**: Classify links as internal, external, images, or documents
- [ ] **robots.txt Compliance**: Respect website crawling rules automatically
- [ ] **Rate Limiting**: Implement delays to avoid overwhelming target servers

### Known Limitations

- No error handling for network failures or invalid URLs
- Cannot process JavaScript-rendered content (SPA applications)
- No support for authentication-required pages
- Extracts all links without filtering duplicates
- Relative URLs are not converted to absolute URLs

*These limitations represent opportunities for enhancement and demonstrate awareness of production-grade requirements*

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test changes before submitting PRs
- Update README for new features

---

## 📄 License

This project is licensed under the MIT License - feel free to use, modify, and distribute as needed.

---

## 👨‍💻 Author

**Enes Uca**

- 🌐 Portfolio: [ensuca.github.io](https://ensuca.github.io/ensuca.githubio)
- 💼 LinkedIn: [linkedin.com/in/enes-uca-41039327b](https://www.linkedin.com/in/enes-uca-41039327b)
- 🐙 GitHub: [@ensuca](https://github.com/ensuca)

---

## 🙏 Acknowledgments

- **BeautifulSoup4**: Leonard Richardson for creating this excellent parsing library
- **Requests**: Kenneth Reitz for the elegant HTTP library
- **Python Community**: For comprehensive documentation and support

---

## 📞 Support

If you encounter issues or have questions:

1. Check existing [GitHub Issues](https://github.com/ensuca/linkSaver/issues)
2. Create a new issue with detailed description
3. Contact via LinkedIn for professional inquiries

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

*Built with Python and passion for clean code*

</div>

---
---

# 🇹🇷 Türkçe

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/lisans-MIT-green.svg)](LICENSE)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4-orange.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![Requests](https://img.shields.io/badge/Requests-latest-red.svg)](https://requests.readthedocs.io/)

> Herhangi bir web sitesinden tüm bağlantıları çıkarıp yapılandırılmış bir metin dosyasına aktaran hafif ve verimli bir web kazıma aracı.

---

## 📋 Genel Bakış

**LinkSaver**, web sitelerinden bağlantı çıkarma sürecini kolaylaştırmak için tasarlanmış Python tabanlı bir web kazıma aracıdır. İster SEO denetimi yapıyor olun, ister rekabet analizi, site haritası oluşturma veya harici bağlantı doğrulama yapıyor olun, LinkSaver bağlantı çıkarma için hızlı ve güvenilir bir çözüm sunar.

Bu araç, endüstri standardı kütüphaneler kullanarak web kazıma tekniklerinin pratik uygulamasını gösterir ve HTTP istek yönetimi, HTML ayrıştırma ve veri çıkarma becerilerini sergiler—bu beceriler modern yazılım geliştirme ve veri mühendisliği rolleri için temel yetkinliklerdir.

### 🎯 Kullanım Alanları

- **SEO Analizi**: Kapsamlı site denetimleri için tüm dahili ve harici bağlantıları çıkarma
- **Bağlantı Doğrulama**: Web varlıklarında kırık bağlantıları ve güncel olmayan referansları belirleme
- **Rekabet Araştırması**: Rakip web sitesi yapılarını ve bağlantı stratejilerini analiz etme
- **Site Haritası Oluşturma**: Site haritası oluşturmak için ön veri hazırlama
- **İçerik Taşıma**: Web sitesi yeniden tasarımları öncesi mevcut bağlantı yapılarını belgeleme
- **Akademik Araştırma**: Araştırma veritabanlarından veya dokümantasyon sitelerinden referans bağlantıları toplama

---

## ✨ Temel Özellikler

- **🚀 Basit ve Hızlı**: Tek bir komutla web sayfasındaki tüm bağlantıları çıkarma
- **🎯 Kapsamlı Çıkarma**: Hedef URL'lerden tüm `<a>` etiketi href özelliklerini yakalama
- **📝 Temiz Çıktı**: Bağlantıları kolay işleme için düzenli, satır bazlı metin dosyalarına aktarma
- **🔧 Minimal Kurulum**: Sadece iki hafif bağımlılık gerekiyor
- **💻 Çapraz Platform**: Windows, macOS ve Linux'ta sorunsuz çalışma
- **🔍 HTML Ayrıştırıcı**: Güvenilir çıkarma için BeautifulSoup4'ün sağlam ayrıştırma yeteneklerinden yararlanma
- **🌐 HTTP Yönetimi**: Kararlı ve verimli web istekleri için Requests kütüphanesi üzerine inşa edilmiş
- **📦 Hafif**: Minimal kaynak kullanımı, otomasyon ve toplu işleme için mükemmel

---

## 🛠️ Teknoloji Yığını

### Ana Teknolojiler
- **Python 3.7+**: Temiz sözdizimi ve sağlam standart kütüphanelerden yararlanan modern Python
- **Requests**: Zarif API ile web istekleri yapmak için endüstri standardı HTTP kütüphanesi
- **BeautifulSoup4**: Web kazıma ve veri çıkarma için güçlü HTML/XML ayrıştırma kütüphanesi

### Tasarım Yaklaşımı
Bu proje, basitlik ve sürdürülebilirliğe odaklanan fonksiyonel programlama paradigmasını takip eder. Mimari şu öncelikleri benimser:
- **Endişelerin Ayrılması**: Bağlantı çıkarma mantığı için ayrı fonksiyon
- **Yeniden Kullanılabilirlik**: Modüler tasarım, daha büyük projelere kolay entegrasyona olanak tanır
- **Okunabilirlik**: Python en iyi uygulamalarını (PEP 8) takip eden temiz, kendi kendini belgeleyen kod

---

## 🚀 Başlarken

### Ön Gereksinimler

- Sisteminizde Python 3.7 veya üzeri kurulu olmalı
- pip (Python paket yöneticisi)
- Web istekleri için internet bağlantısı

### Kurulum

1. **Depoyu Klonlayın**
```bash
git clone https://github.com/ensuca/linkSaver.git
cd linkSaver
```

2. **Bağımlılıkları Yükleyin**
```bash
pip install requests
pip install beautifulsoup4
```

Ya da ikisini birden yükleyin:
```bash
pip install requests beautifulsoup4
```

### Yapılandırma

Betiği çalıştırmadan önce hedef URL'nizi yapılandırın:

1. `linkSaver.py` dosyasını tercih ettiğiniz metin düzenleyicide açın
2. 18. satırı bulun:
```python
url = 'https://www.example.com'  # Bağlantı adreslerini istediğiniz web sitesinin adresini yazın
```
3. `'https://www.example.com'` ifadesini hedef web sitesi URL'nizle değiştirin
4. (İsteğe bağlı) İsterseniz 19. satırda çıktı dosya adını değiştirin:
```python
output_file = 'links.txt'
```

---

## 💡 Kullanım

### Temel Kullanım

Hedef URL'nizi yapılandırdıktan sonra, basitçe çalıştırın:

```bash
python linkSaver.py
```

Betik şunları yapacak:
1. Belirtilen URL'ye HTTP GET isteği gönderecek
2. HTML yanıtını ayrıştıracak
3. `<a>` etiketlerinden tüm `href` özelliklerini çıkaracak
4. Sonuçları mevcut dizinde `links.txt` dosyasına kaydedecek

### Örnek

```python
# linkSaver.py dosyasında hedefinizi yapılandırın
url = 'https://www.python.org'
output_file = 'python_links.txt'

# Betiği çalıştırın
save_links_to_file(url, output_file)
```

**Çıktı** (`python_links.txt`):
```
https://www.python.org/about/
https://www.python.org/downloads/
https://www.python.org/doc/
https://www.python.org/community/
/success-stories/
...
```

### Entegrasyon Örneği

LinkSaver, daha büyük projelere kolayca entegre edilebilir:

```python
from linkSaver import save_links_to_file

# Birden fazla siteden bağlantı çıkarma
websites = [
    'https://example1.com',
    'https://example2.com',
    'https://example3.com'
]

for i, site in enumerate(websites):
    save_links_to_file(site, f'links_site_{i}.txt')
    print(f"✅ {site} adresinden bağlantılar çıkarıldı")
```

---

## 📁 Proje Yapısı

```
linkSaver/
├── linkSaver.py        # Bağlantı çıkarma mantığını içeren ana betik
├── README.md           # Proje dokümantasyonu (bu dosya)
├── README.txt          # Eski dokümantasyon
├── .gitattributes      # Git yapılandırması
└── links.txt           # Çıktı dosyası (çalıştırdıktan sonra oluşturulur)
```

### Ana Bileşenler

**`save_links_to_file(url, output_file)`**
- **Parametreler**:
  - `url` (str): Kazınacak hedef web sitesi URL'si
  - `output_file` (str): Çıktı metin dosyası yolu
- **Dönüş**: None
- **İşlevsellik**: HTTP isteği, HTML ayrıştırma, bağlantı çıkarma ve dosya yazmayı düzenler

**Konum**: linkSaver.py:5

---

## 🔍 Nasıl Çalışır

### Teknik Uygulama

1. **HTTP İsteği**: Hedef URL'den HTML içeriğini almak için `requests.get()` kullanır
2. **HTML Ayrıştırma**: BeautifulSoup, ham HTML'yi gezinilebilir bir ağaç yapısına ayrıştırır
3. **Bağlantı Çıkarma**: `.find_all('a')` metodu belgede tüm anchor etiketlerini bulur
4. **Özellik Çıkarma**: Null kontrolü ile `.get('href')` kullanarak `href` özelliklerini çıkarır
5. **Dosya Çıktısı**: Her bağlantıyı belirtilen çıktı dosyasında yeni bir satıra yazar

### Kod Akışı

```
Kullanıcı Girdisi (URL)
    ↓
HTTP GET İsteği (requests)
    ↓
HTML Yanıtı
    ↓
HTML Ayrıştırma (BeautifulSoup)
    ↓
<a> Etiketlerini Çıkar
    ↓
href Özelliklerini Al
    ↓
Dosyaya Yaz (links.txt)
    ↓
Tamamlandı ✅
```

---

## ⚡ Performans Değerlendirmeleri

- **Hafif**: Minimal bellek kullanımı, büyük sayfaları kazımak için uygun
- **Verimli Ayrıştırma**: BeautifulSoup4'ün lxml ayrıştırıcısı (mevcutsa) optimal performans sağlar
- **Tek İstek**: Yürütme başına bir HTTP isteği, ağ yükünü minimize eder
- **Akış Yazma**: Dosya artımlı olarak yazılır, büyük bağlantı setleriyle bellek sorunlarını önler

### Tipik Çalıştırma Süresi
- Küçük web sitesi (<100 bağlantı): < 1 saniye
- Orta web sitesi (100-1000 bağlantı): 1-3 saniye
- Büyük web sitesi (1000+ bağlantı): 3-10 saniye

*Performans, ağ hızına ve hedef sunucu yanıt süresine göre değişir*

---

## 🧪 Test

### Manuel Test Prosedürü

1. **Bilinen bir web sitesi ile test edin**:
```bash
# linkSaver.py içinde url = 'https://www.python.org' ayarlayın
python linkSaver.py
```

2. **Çıktıyı doğrulayın**:
```bash
cat links.txt  # Linux/Mac
type links.txt  # Windows
```

3. **Bağlantı sayısını doğrulayın**:
```python
with open('links.txt', 'r') as f:
    link_count = len(f.readlines())
    print(f"{link_count} bağlantı çıkarıldı")
```

### Test Senaryoları

✅ **Geçerli Web Sitesi URL'si**: Bağlantıları başarıyla çıkarır
✅ **HTTPS URL'leri**: Güvenli bağlantıları işler
✅ **Göreceli Bağlantılar**: Kısmi URL'leri yakalar (örn., `/about`, `#contact`)
✅ **Boş href**: Null/boş href özelliklerini filtreler
✅ **Büyük Sayfalar**: 1000+ bağlantılı sayfaları işler

---

## 🚀 Dağıtım ve Otomasyon

### Zamanlanmış Çalıştırma (Linux/Mac)

Günlük bağlantı çıkarma için crontab'a ekleyin:
```bash
0 2 * * * cd /path/to/linkSaver && /usr/bin/python3 linkSaver.py
```

### Windows Görev Zamanlayıcı

Bir batch dosyası oluşturun (`run_linksaver.bat`):
```batch
@echo off
cd C:\Projects\linkSaver
python linkSaver.py
```

Otomatik çalıştırma için Görev Zamanlayıcı ile planlayın.

### Docker Dağıtımı

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY linkSaver.py .
RUN pip install requests beautifulsoup4
CMD ["python", "linkSaver.py"]
```

---

## 🗺️ Yol Haritası ve Gelecek Geliştirmeler

### Planlanan Özellikler

- [ ] **Komut Satırı Arayüzü**: URL ve çıktı dosyası argümanları için argparse ekleme
- [ ] **Hata Yönetimi**: Ağ hataları ve geçersiz URL'ler için try-except blokları uygulama
- [ ] **Bağlantı Doğrulama**: Her çıkarılan bağlantı için HTTP durum kodu kontrolü ekleme
- [ ] **Format Seçenekleri**: JSON, CSV ve XML çıktı formatlarını destekleme
- [ ] **Özyinelemeli Tarama**: Bağlantıları takip etme ve birden fazla sayfadan çıkarma seçeneği
- [ ] **Filtreleme Seçenekleri**: Domain, protokol (http/https) veya URL desenlerine göre filtreleme
- [ ] **İlerleme Göstergesi**: Büyük siteler için tqdm kullanarak ilerleme çubuğu ekleme
- [ ] **Asenkron İstekler**: Daha hızlı toplu kazıma için asenkron HTTP istekleri uygulama
- [ ] **GUI Arayüzü**: Teknik olmayan kullanıcılar için Tkinter tabanlı masaüstü uygulaması
- [ ] **Bağlantı Kategorilendirme**: Bağlantıları dahili, harici, resim veya belge olarak sınıflandırma
- [ ] **robots.txt Uyumu**: Web sitesi tarama kurallarına otomatik uyum
- [ ] **Hız Sınırlama**: Hedef sunucuları bunaltmamak için gecikmeler uygulama

### Bilinen Sınırlamalar

- Ağ hataları veya geçersiz URL'ler için hata yönetimi yok
- JavaScript ile oluşturulan içeriği işleyemez (SPA uygulamaları)
- Kimlik doğrulama gerektiren sayfalar için destek yok
- Tüm bağlantıları filtreleme yapmadan çıkarır, tekrarları kaldırmaz
- Göreceli URL'ler mutlak URL'lere dönüştürülmez

*Bu sınırlamalar, geliştirme fırsatlarını temsil eder ve üretim kalitesindeki gereksinimlerin farkındalığını gösterir*

---

## 🤝 Katkıda Bulunma

Katkılar, sorunlar ve özellik istekleri kabul edilir!

### Nasıl Katkıda Bulunulur

1. Depoyu fork edin
2. Bir özellik dalı oluşturun (`git checkout -b feature/MuhteşemÖzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Muhteşem bir özellik ekle'`)
4. Dalı push edin (`git push origin feature/MuhteşemÖzellik`)
5. Bir Pull Request açın

### Geliştirme İlkeleri

- PEP 8 stil kılavuzlarını takip edin
- Karmaşık mantık için yorumlar ekleyin
- PR göndermeden önce değişiklikleri test edin
- Yeni özellikler için README'yi güncelleyin

---

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - gerektiğinde kullanmakta, değiştirmekte ve dağıtmakta özgürsünüz.

---

## 👨‍💻 Yazar

**Enes Uca**

- 🌐 Portfolio: [ensuca.github.io](https://ensuca.github.io/ensuca.githubio)
- 💼 LinkedIn: [linkedin.com/in/enes-uca-41039327b](https://www.linkedin.com/in/enes-uca-41039327b)
- 🐙 GitHub: [@ensuca](https://github.com/ensuca)

---

## 🙏 Teşekkürler

- **BeautifulSoup4**: Bu mükemmel ayrıştırma kütüphanesini oluşturduğu için Leonard Richardson'a
- **Requests**: Zarif HTTP kütüphanesi için Kenneth Reitz'e
- **Python Topluluğu**: Kapsamlı dokümantasyon ve destek için

---

## 📞 Destek

Sorunlarla karşılaşırsanız veya sorularınız varsa:

1. Mevcut [GitHub Issues](https://github.com/ensuca/linkSaver/issues) sayfasını kontrol edin
2. Detaylı açıklama ile yeni bir issue oluşturun
3. Profesyonel sorular için LinkedIn üzerinden iletişime geçin

---

<div align="center">

**⭐ Faydalı bulduysanız bu depoyu yıldızlayın!**

*Python ve temiz kod tutkusuyla inşa edilmiştir*

</div>
