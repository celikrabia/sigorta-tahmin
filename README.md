# Sigorta Maliyeti Tahmin Uygulaması

Bu proje, müşterilerin sigorta maliyetlerini tahmin eden bir makine öğrenmesi uygulamasıdır. Uygulama, müşterinin yaş, cinsiyet, BMI, çocuk sayısı, sigara kullanımı ve bölge bilgilerine göre sigorta maliyetini tahmin eder.

## Özellikler

- Kullanıcı dostu web arayüzü
- Gerçek zamanlı tahmin
- Tahmin sonuçlarının değerlendirmesi
- Özellik önemliliklerinin görselleştirilmesi

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/KULLANICI_ADINIZ/sigorta-tahmin.git
cd sigorta-tahmin
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Modeli eğitin:
```bash
python train.py
```

4. Uygulamayı başlatın:
```bash
streamlit run app.py
```

## Kullanım

1. Web tarayıcınızda `http://localhost:8501` adresine gidin
2. Formu doldurun:
   - Yaş
   - Cinsiyet
   - BMI (Vücut Kitle İndeksi)
   - Çocuk Sayısı
   - Sigara Kullanımı
   - Bölge
3. "Predict Insurance Cost" butonuna tıklayın
4. Tahmin sonucunu ve değerlendirmeyi görüntüleyin

## Proje Yapısı

- `app.py`: Streamlit web uygulaması
- `train.py`: Model eğitimi
- `utils.py`: Yardımcı fonksiyonlar
- `predict.py`: Tahmin fonksiyonları
- `insurance.csv`: Örnek veri seti
- `requirements.txt`: Gerekli Python paketleri

## Katkıda Bulunma

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: Açıklama'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Bir Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın. 