
## 🔍 Proje Özeti  
Bu proje kapsamında, **"Medical Cost Personal Dataset"** veri seti kullanılarak bireylerin kişisel sağlık bilgileri üzerinden sigorta maliyetlerini (`charges`) tahmin eden bir **regresyon modeli** geliştirilmiştir. Çalışma **gözetimli öğrenme (supervised learning)** temellidir. Sonuç olarak, en başarılı model bir **web arayüzü** ile entegre edilerek kullanıcıların kolayca tahmin yapabileceği bir sistem tasarlanmıştır.

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
**Random Forest**, veri setindeki doğrusal olmayan ilişkileri ve değişkenler arası karmaşık etkileşimleri başarılı bir şekilde öğrenebildiği için en iyi sonucu vermiştir. Aşırı öğrenmeye (overfitting) karşı dayanıklıdır ve yorumlanabilirlik açısından güçlüdür.

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

## 🌐 Streamlit Web Arayüzü  
Model, kullanıcıların sağlık bilgilerini girerek tahmin alabileceği bir **Streamlit arayüzü** ile entegre edilmiştir.

📍 Uygulamayı çalıştırmak için terminale şu komutu yazabilirsiniz:

```bash
streamlit run app.py
```

📌 Web arayüzü lokal olarak şurada çalışmaktadır:  
**http://localhost:8501/**  

Uygulamada kullanıcılar şu bilgileri girerek tahmin alabilir:  
- Yaş  
- Cinsiyet  
- Vücut kitle indeksi (BMI)  
- Çocuk sayısı  
- Sigara içme durumu  
- Bölge (region)

---

## 🚀 Gelecekte Neler Yapılabilir?  
- Model daha büyük ve çeşitli veri kümeleri ile yeniden eğitilebilir.  
- `GridSearchCV` ile hiperparametre optimizasyonu yapılabilir.  
- Streamlit arayüzü, kullanıcı dostu bir tasarımla geliştirilebilir.  
- Model `.pkl` olarak kaydedilip farklı frontend çözümleriyle de entegre edilebilir.  
- Aynı veri seti üzerinde **Clustering** gibi **gözetimsiz öğrenme teknikleri** kullanılarak müşteri segmentasyonu yapılabilir.

---

## 📌 Bağlantılar  
- 📂 Kaggle Notebook: [Kaggle Notebook Linki](https://www.kaggle.com/code/rabiacelik/akbankbootcamp/edit)  
- 🧠 Veri Seti: [Insurance Dataset on Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance)
