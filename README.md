## 🔍 Proje Özeti

Bu proje kapsamında, "Medical Cost Personal Dataset" veri seti kullanılarak bireylerin kişisel sağlık bilgilerinden yola çıkarak sigorta maliyetlerini (charges) tahmin eden bir regresyon modeli geliştirildi. Çalışma gözetimli öğrenme (supervised learning) temellidir.

---

## ⚙️ Kullanılan Modeller ve Karşılaştırma

Üç farklı model eğitilerek performansları karşılaştırılmıştır:

| Model              | MAE   | RMSE  | R² Score |
|-------------------|--------|--------|----------|
| Linear Regression | 4181   | 5796   | 0.784    |
| Random Forest     | **2545** | **4569** | **0.866** ✅ |
| XGBoost           | 2550   | 4599   | 0.864    |

**Random Forest Regressor**, hem hata metriklerinde daha düşük değerler hem de daha yüksek R² skoru ile en başarılı model olmuştur.

---

## 📈 Model Seçimi Gerekçesi

Random Forest, veri setindeki doğrusal olmayan ilişkileri ve değişkenler arası karmaşık etkileşimleri başarılı bir şekilde öğrenebildiği için en iyi sonucu vermiştir. Ayrıca aşırı öğrenmeye (overfitting) karşı dayanıklıdır ve yorumlanabilirlik açısından güçlüdür.

---

## 🧠 Özellik Önem Analizi

Modelin eğitimi sonrasında, sigorta maliyetini en çok etkileyen değişkenler aşağıdaki şekilde sıralanmıştır:

1. **smoker** (sigara içme durumu)
2. **age** (yaş)
3. **bmi** (vücut kitle indeksi)
4. **children** (çocuk sayısı)
5. **sex**, **region** gibi diğer faktörler

Özellikle **sigara kullanımı**, sigorta maliyeti üzerinde çok güçlü bir etkiye sahiptir.

---

## 🚀 Gelecekte Neler Yapılabilir?

- Model daha büyük veri kümeleri ile yeniden eğitilebilir.
- `GridSearchCV` ile hiperparametre optimizasyonu yapılabilir.
- Model `.pkl` dosyası olarak kaydedilip Flask/FastAPI ile web arayüzüne entegre edilebilir.
- Aynı veri seti üzerinde `Clustering` (kümeleme) gibi gözetimsiz öğrenme teknikleri de uygulanarak müşteri segmentasyonu yapılabilir.

---

## 📌 Bağlantılar

- 📂 Kaggle Notebook Linki: (https://www.kaggle.com/code/rabiacelik/akbankbootcamp/edit)
- 🧠 https://www.kaggle.com/datasets/mirichoi0218/insurance
