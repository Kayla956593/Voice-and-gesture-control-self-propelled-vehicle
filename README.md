# Voice-and-gesture-control-self-propelled-vehicle
語音及手勢控制自走車 

功能: 
藉由喇叭語音或切換 Camera 去辨識手勢來控制自走車的的行進方向，語音內容包含口述的前進、往後、左轉、右轉、加速和開關燈，並配合著語音提示，例如後退就會說"車子後退"並配合 LED 提示模擬車子後退，左轉就會說"車子左轉"讓車子往我們要的方向走，然後也可切換成手勢辨識，一樣可以進行前進、後退、左轉、右轉以及停的功能，翹起大拇指是代表車子的後退，比數字 5 代表停止，比數字 7 代表車子的前進，比數字 8 代表車子左轉，比數字 9 代表車子的右轉。 
專題操作及執行流程:  
先跑語音辨識車子的部分，對麥克風說往前、往後、左轉、右轉、加速、減速等指令，自走車做相應的動作。   

![image](https://user-images.githubusercontent.com/79260866/196335494-7d7133b8-852b-4d28-a430-31001e6a03db.png)
![擷取](https://user-images.githubusercontent.com/79260866/196337924-a3b16a7b-cdbc-4a5e-891c-19f0dcdf01d2.PNG)

說出用手控制的指令，可以切換出用手勢辨識去控制車。 

![image](https://user-images.githubusercontent.com/79260866/196335511-d9943781-45a4-4e3a-97ea-b2dce2b4cc24.png)

藉由語音去控制車子並用語音切換 Camera 去辨識手勢來控制自走車，語音內容包含口述的前進、往後、左轉、右轉、加速和開關燈，並配合著語音提示，然後也可切換成手勢辨識，不同手勢對應不同功能，一樣可以進行前進、後退、左轉、右轉以及停的功能。 
軟體程式執行流程圖 (表示程式功能條件判斷分支、循環…等) 
![期末報告](https://user-images.githubusercontent.com/79260866/196336317-f71e5999-9616-4876-8fb3-87199dc8582a.jpg)


參考的課程實驗或是網路資源: 
課程 1、2、7、8、9、10 章節 code 和內容 
網路手勢辨識： https://core-electronics.com.au/tutorials/hand-identification-raspberry-pi.html 

開發最耗時的部份與原因 (最少 200 字) 
我們為了可以用自己的網路連接樹莓派，在設定網路時連接不到，不小心把 sd 卡的內容複寫掉了。所以又載回了原本的樹莓派版本，並把上課內容的 7、8、9、10 等章節全部複習了一遍哈哈。我們先做手勢辨識去控制車子的前進，後退，左轉，右轉等功能。根據五隻手指豎起的數量，去讓車子做相應的動作。例如翹起大拇指是代表車子的後退。在這個部分，因辨識上不夠準確，所以我們又調整了許多內容，也加入大拇指的判別，並進行修改，因它比其他手指更短，辨識上會有些錯誤性。 
隨後我們做用語音控制自走車的前後左右動作，這個部分並不難。但因我們想結合手勢辨識和語音控制功能，在這部分我們費時較多。因為要了解兩邊 code 的程式邏輯再進行結合，也 de 了很多 bug。並且多加了車子加速減速功能。 

物聯網期末專題 demo 影片 
https://www.youtube.com/watch?v=RuODc_Zbce8&ab_channel=Y
