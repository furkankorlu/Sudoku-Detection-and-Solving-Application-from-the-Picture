# <font color="azure"><div align="center"><p>**Sudoku Detection and Solving Application from the Picture**</p> </div></font>


<font color="red">**Warning!**</font>

- With the OCR Model, sudoku.py must be in the same folder.Sudoku pictures should be in the sudoku folder.When the application is started, the name of the Sudoku image is requested. Sudoku answer will be created on the console.The answer folder was created to be an example.

## <font color="HoneyDew">**THE PURPOSE OF THE APPLICATION**</font>

**-Through a photo provide by the user;**
- Detecting the Sudoku board.
- Dividing the large board into 81 boxes with calculations. 
- Detecting numbers in boxes with OCR methods. 
- Numbers that are detected as irregularly are listed. Creat a matrix with the numbers in the list. 
- Solve the resulting matrix with Sudoku solving algorithm. 
- Creating a solution matrix.
- The screen shows the Sudoku matrix and the solution matrix.

## <font color="HoneyDew">**REQUIRED LIBRARIES**</font>
- To procure the photo and apply the fıltrations; **OpenCV**
- To represent images as matrices, to perform matrix partiton operations; **NumPy**
- To import/use the OCR model;**Tensorlow**
- For OpenCV auxiliary functions in contuor operations; **Imutils**

|<font color="White">**Package**</font>|<font color="White">**Version**</font>|
| :--------- | :-----:|
| Opencv  | 4.7.0.72 |
| Numpy|    1.19.5 |
| Tensorflow | <font color="red">2.5.0</font> |
| Imutils |    0.5.4 |


## <font color="HoneyDew">**PHASES**</font>

### <font color="HoneyDew">**1-) DETECTION**</font>
Image processing techniques and contour finding algorithms are used to detect the Sudoku board over the photo. Fort his, I used the **alanı_bul** and **perspetif_al** functions in my code.The sudoku board is found with continuous lines detected throgh the photo and is cut with its perspective.

###  <font color="HoneyDew">**a-) IMAGE PROCESSING**</font>

In order fort he contour finding algorithm to work in a healthy way, the photo must undergo appropriate filter processing. 

- First off all, I called the **alanı_bul** function. In this function, I prepared the bilateral fitering process that I will apply by making the photo gray-tone. I sharpened the lines in the photo due to the *Bilateral Filtering* and *Contrast Development* processes. Since I didi not  apply blurs to the photo, I could not get a clear view of softness and numbers, but I prevented the  corners from disappearing. Finally, I obtained a photo suitable for OpenCV s *findContours* function using the *Canny Edge Detection filter*.

- **Bilateral Filtering:** The image is converted into a binary image using a specific threshold value after being grayed.

- **Contrast Development:** Histogram equalization and contrast enhancement techniques are applied to increase the contrast of the Picture. 


![1](https://github.com/furkankorlu/Sudoku-Detection-and-Solving-Application-from-the-Picture/assets/122547302/361c329d-da15-40f3-a106-904333ae4da2)

### <font color="HoneyDew">**b-) FIND CONTOUR**</font>

- I found the contours of the Sudoku board using the contouring algorithms on the image. Because I want it to be an example, I drew the contours I found using OpenCV’s *drawContours* function. By analyzing the contours I found, I detected contours in the form of a square. By analyzing the areas of the square I detected, I found the pixel position of the large Sudoku board in the photo. Since the pictures of different resolutions had to be processed, I obtained the position of the Sudoku board with the **perspektif_al** function, cut it and resized it.


![2](https://github.com/furkankorlu/Sudoku-Detection-and-Solving-Application-from-the-Picture/assets/122547302/fbaf6e22-9599-44a8-9743-663f67ee2651)


- By processing the resulting large Sudoku board with the **kutulara_bol** fonction, I parsed each box. I reflected the 81 boxes I obtained, starting from the upper left row and column, to the screen. I sent it to the model to make OCR in the order I gave it to the screen. 

![3](https://github.com/furkankorlu/Sudoku-Detection-and-Solving-Application-from-the-Picture/assets/122547302/2b7d6aa2-f584-48c9-9996-c4c98539c4ba)

### <font color="HoneyDew">**c-) OCR**</font>
- Optical Character Recognition (OCR) modules are basically Technologies used to convert written text into digital format. I used the *TensorFlow* based *OCR* modüle in my project. This module is a trained model to automatically recognize numbers in written or printed texts. With the order I mentioned earlier, I analyzed the incoming boxes using a model that was only trained to detect numbers. I recognized the numbers and added the results I got to the list called **prediced_numbers**. Throughput;

![4](https://github.com/furkankorlu/Sudoku-Detection-and-Solving-Application-from-the-Picture/assets/122547302/99b58170-8800-4b71-818d-e0371062e943)

- In the list called **predicted_numbers**, I turned the numbers that stand with the order I mentioned above into a 2- dimensional 9*9 size list with Numpy. 

![5](https://github.com/furkankorlu/Sudoku-Detection-and-Solving-Application-from-the-Picture/assets/122547302/30d30bcc-6e64-4cf3-a966-826b4a6c95ce)

## <font color="HoneyDew">**2-) SOLVING**</font>
- The Sudoku solution algorithm solves the Sudoku puzzel by placing the appropriate numbers in place of the spaces on the board.

> I added the number 0 instead of the spaces on the Sudoku board in the list.

- **Backtracking Algorithm:** It is the backtracking algorithm that seeks the right solution by filling in empty celles. 
- **Forward Checking Technical:** Forward checking technique is used, which makes the solution progress faster by making a forward prediction. 

- The loop in the **sudoku_coz** function checks for conformity with the **sayı_uygun** function to place numbers 1 to 9 in the empty cell. The **sayı_uygun** function first places a number in the empty box and checks if the same numbers exists in the row and column it is located in. It then checks if the cell has the same number in the 3*3 box it is in. If the places number follows the rules, **True** is returned, accepting that the number is appropriate, and that number is placed in that cell, and the Sudoku solution is continued by calling the sudoku_coz function again. If a wrong placement has been made, the cell will be assigned a 0 (blank) value to undo the last addition and the next number is called. 

- If Sudoku cannot be resolved as a result of all number attempts, **False** is returned and it is stated that Sudoku is not resolved to the screen. 

- If all empty cells are filled, Sudoku is considered complete and True is returned. As a result of the arrival of True, the algorithm is terminated and the solution of the Sudoku board is offered. 

![6](https://github.com/furkankorlu/Sudoku-Detection-and-Solving-Application-from-the-Picture/assets/122547302/78e1bac4-2c87-476a-962d-c63f84247b23)

# <font color="azure"><div align="center"><p>**Resimden Sudoku Algılama ve Çözme Uygulaması**</p> </div></font>


<font color="red">**Uyarı!**</font>

- OCR Modeli ile sudoku.py aynı klasörde olmalıdır. Sudoku resimleri sudokular klasörü içerisinde olmalıdır. Uygulama başlatıldığında Sudoku görselinin ismi istenmektedir. Sudoku cevabı konsolda oluşturulacaktır. Cevap klasörü örnek olması için oluşturulmuştur.

## <font color="HoneyDew">**AMAÇ**</font>

**-Kullanıcı tarafından sağlanan bir fotoğraf üzerinden;**
- Sudoku tahtasını tespit etmek.
- Hesaplamalar ile büyük tahtayı 81 adet kutucuğa bölmek.
- Kutucuktaki sayıları ORC metotlarıyla okumak.
- Okunup dağınık şekilde listeye eklenen sayılarla bir matris oluşturmak
- Oluşturulan matrisi Sudoku çözme algoritması vasıtasıyla çözmek.
- Çözüm matrisi oluşturmak.
- Sudoku matrisini ve çözüm matrisini ekrana çıkartmak.

## <font color="HoneyDew">**GEREKLİ KÜTÜPHANELER**</font>

- Fotoğrafı almak ve filtrasyonları uygulamak için: **OpenCV**
- Görüntüleri matris olarak temsil etmek, matris bölme işlemleri yapmak için: **NumPy**
- Önceden Eğitilmiş bir karakter tanıma modeli yüklemek/kullanmak için: **TensorFlow**
- Kontur işlemlerinde OpenCV ye yardımcı fonksiyonlar için: **Imutils**

|<font color="White">**Package**</font>|<font color="White">**Version**</font>|
| :--------- | :-----:|
| Opencv  | 4.7.0.72 |
| Numpy|    1.19.5 |
| Tensorflow | <font color="red">2.5.0</font> |
| Imutils |    0.5.4 |

## <font color="HoneyDew">**AŞAMALAR**</font>

### <font color="HoneyDew">**1-)ALGILAMA**</font>

Sudoku tahtasının fotoğraf üzerinden algılanması için görüntü işleme teknikleri ve kontur bulma algoritmaları kullanılır. Bunun için kodumda **alanı_bul** ve **perspektif_al** fonksiyonlarını kullandım. Fotoğraf üzerinden tespit edilen sürekli çizgilerle sudoku tahtası bulunur ve perspektifi alınarak kesilir.

#### <font color="HoneyDew">**a-) RESİM İŞLEME**</font>
Kontur bulma algoritmasının sağlıklı bir şekilde çalışabilmesi için fotoğrafın uygun filtre işlemlerinden geçmesi gerekir.

- Öncelikle **alanı_bul** fonksiyonunu çağırdım. Bu fonksiyonda fotoğrafı gri tonlamalı hale getirerek uygulacağım binarizasyon işlemine hazırlamış oldum. *Binarizasyon* ve *Kontrast Geliştirme* işlemleri sayesinde fotoğraftaki çizgilerin yapılarını keskinleştirdim. Fotoğrafa blur uygulamayarak yumuşaklığı ve sayıların net görüntüsünü elde edemedim ancak köşelerin kaybolmasını engelledim. Son olarak *Canny Edge Detection* filtresini kullanarak OpenCV nin *findContours* fonksiyonuna uygun bir fotoğraf elde ettim.

- **Binarizasyon:** Resim, gri tonlamalı hale getirildikten sonra belirli bir eşik değeri kullanılarak ikili bir görüntüye dönüştürülür.

- **Kontrast Geliştirme:** Resmin kontrastını artırmak için histogram eşitleme ve kontrast geliştirme teknikleri uygulanır.

![1](https://github.com/furkankorlu/Sudoku-Detection-and-Solving-Application-from-the-Picture/assets/122547302/d125a936-5650-450c-8ba2-70e44f20f771)

#### <font color="HoneyDew">**b-) KONTUR BULMA**</font>

- Görüntü üzerinde kontur bulma algoritmaları kullanarak Sudoku tahtasının konturları buldum. Örnek niteliği taşıması istediğimden bulduğum konturları OpenCV nin *drawContours* fonksiyonu aracılığıyla çizdim. Bulduğum konturları analiz ederek Dörtgen biçiminde olan konturları tespit ettim. Tespit ettiğim Dörtgenlerin alanlarını analiz ederek büyük Sudoku tahtasının fotoğraftaki piksel konumunu buldum. Farklı çözünürlükteki resimler işlenmesi gerektiğinden **perspektif_al** fonksiyonu ile Sudoku tahtasının konumunu elde ettim, kestim ve yeniden boyutlandırarak işledim.

![2](https://github.com/furkankorlu/Sudoku-Detection-and-Solving-Application-from-the-Picture/assets/122547302/fbaf6e22-9599-44a8-9743-663f67ee2651)

- Elde edilen büyük Sudoku tahtasını **kutulara_bol** fonksiyonu ile işleyerek,  her bir kutuyu ayrıştırdım. Elde ettiğim 81 adet kutuyu sol en üst satır ve sütundan başlayarak ekrana çıktı olarak verdim. Ekrana verdiğim sıra ile de OCR yapılması için modele gönderdim.

![3](https://github.com/furkankorlu/Sudoku-Detection-and-Solving-Application-from-the-Picture/assets/122547302/2b7d6aa2-f584-48c9-9996-c4c98539c4ba)

#### <font color="HoneyDew">**c-) OCR**</font>

- Optical Character Recognition (Optik karakter tanıma) (OCR) modülleri, temel olarak yazılı metni dijital formata dönüştürmek için kullanılan teknolojilerdir. Ben projemde TensorFlow tabanlı OCR modülü kullandım. Bu modül, yazılı veya basılı metinlerdeki sayıları otomatik olarak tanımak için eğitilmiş bir modeldir.

- Daha önceden belirttiğim sıra ile sadece sayıları algılamak için eğitilmiş bir modeli kullanarak gelen kutuları analiz ettim.

- Sayıları tanıdı ve aldığım sonuçları **predicted_numbers** adlı listeye ekledim. Çıktısı;

![4](https://github.com/furkankorlu/Sudoku-Detection-and-Solving-Application-from-the-Picture/assets/122547302/99b58170-8800-4b71-818d-e0371062e943)

- **predicted_numbers** adlı listede yukarda bahsettiğim sıra ile duran sayıları Numpy ile 2 boyutlu 9x9 boyutunda bir listeye dönüştürdüm.

![5](https://github.com/furkankorlu/Sudoku-Detection-and-Solving-Application-from-the-Picture/assets/122547302/30d30bcc-6e64-4cf3-a966-826b4a6c95ce)

### <font color="HoneyDew">**2-) ÇÖZME**</font>

- Sudoku çözüm algoritması, tahtadaki boşlukların yerine uygun sayıları yerleştirerek Sudoku bulmacasını çözer

> Listede Sudoku tahtası boşluklar yerine 0 sayısını ekledim.

- **Geri İzleme (Backtracking) Algoritması:** Boş hücreleri doldurarak doğru çözümü arayan geri izleme algoritmasıdır.
- **İleri Arama (Forward Checking) Tekniği:** İleriye doğru bir tahmin yaparak çözümün daha hızlı ilerlemesini sağlayan ileri arama tekniği kullanılır.

- **sudoku_coz** fonksiyonu içindeki döngü, 1 den 9 a kadar olan sayıları boş hücreye  yerleştirmek için **sayi_uygun** fonksiyonu ile uygunluk kontrolü yapar. **sayi_uygun** fonksiyonu ilk olarak, boş kutuya bir sayı yerleştirir ve bulunduğu satır ve sütunda aynı sayının olup olmadığını kontrol eder. Ardından, hücrenin içinde bulunduğu 3x3 lük kutuda aynı sayının olup olmadığını kontrol eder. Eğer yerleştirilen sayı kurallara uyuyor ise, sayının uygun olduğu kabul edilerek **True** döndürülür ve o sayı o hücreye yerleştirilir ve sudoku_coz fonksiyonu tekrar çağrılarak Sudoku çözümü devam ettirilir. Eğer yanlış bir yerleştirme yapılmışsa son yapılan yerleştirmeyi geri almak için hücreye 0 (boş) değeri atanır ve bir sonraki sayı denemesine geçilir.

- Eğer tüm sayı denemeleri sonucunda Sudoku çözülememişse, **False** döndürülür ve ekrana Sudokunun çözülemeyeceğine dair bir ifade çıkartılır.

- Eğer tüm boş hücreler doldurulmuşsa Sudoku tamamlanmış olarak kabul edilerek **True** döndürülür. **True** gelmesi sonucu algoritma sonlandırılır ve Sudoku tahtası çözümü sunulur.

![6](https://github.com/furkankorlu/Sudoku-Detection-and-Solving-Application-from-the-Picture/assets/122547302/78e1bac4-2c87-476a-962d-c63f84247b23)

