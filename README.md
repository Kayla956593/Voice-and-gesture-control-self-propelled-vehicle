# 語音及手勢控制自走車  
## Voice and Gesture Controlled Autonomous Car

## 功能 | Features
藉由語音指令或手勢辨識來控制自走車的行進方向。  
The autonomous car is controlled using either voice commands or gesture recognition.

- **手勢控制 | Gesture Control**:  
  說出用手控制的指令，可以切換到手勢辨識模式，用手勢控制車子的方向。  
  Use hand signals to control the car after switching to gesture recognition mode.  
  - 各手勢對應功能如下：  
    - 翹起大拇指：後退  
      Thumbs up: Move backward
    - 比數字 5：停止  
      Number 5: Stop
    - 比數字 7：前進  
      Number 7: Move forward
    - 比數字 8：左轉  
      Number 8: Turn left
    - 比數字 9：右轉  
      Number 9: Turn right

![Gesture Control](https://user-images.githubusercontent.com/79260866/196335494-7d7133b8-852b-4d28-a430-31001e6a03db.png)

- **語音控制 | Voice Control**:  
  語音控制包括前進、後退、左轉、右轉、加速、減速、開關燈等功能，並可切換到手勢辨識模式。  
  Voice commands control the car with commands like "move forward," "move backward," "turn left," "turn right," "speed up," "slow down," and "toggle lights." You can also switch between voice and gesture recognition modes.
  
![Voice Control](https://user-images.githubusercontent.com/79260866/196335511-d9943781-45a4-4e3a-97ea-b2dce2b4cc24.png)

- **軟體程式流程圖 | Software Flowchart**:  
  下圖展示了程式的條件判斷、循環等流程。  
  The following flowchart shows the software's condition handling, loops, and general flow.

![Software Flowchart](https://user-images.githubusercontent.com/79260866/196336317-f71e5999-9616-4876-8fb3-87199dc8582a.jpg)

## 參考資源 | References
- 課程 1、2、7、8、9、10 章節的代碼和內容  
  Code and content from Chapters 1, 2, 7, 8, 9, and 10 of the course
- 網路手勢辨識資源： [Hand Gesture Recognition on Raspberry Pi](https://core-electronics.com.au/tutorials/hand-identification-raspberry-pi.html)  
  Online gesture recognition tutorial

## 開發過程與挑戰 | Development Process and Challenges
我們在開發過程中遇到最大的挑戰是在設定樹莓派的網路連接時，意外覆寫了 SD 卡的內容，導致必須重新下載樹莓派的原始系統。這導致我們花費額外時間來複習課程的 7、8、9、10 章節，重新設定系統後，開始進行手勢辨識功能的開發。

首先，我們實現了根據手勢控制車子的基本功能，例如前進、後退、左轉、右轉等。每個手勢代表不同的指令，比如翹起大拇指代表後退。由於手勢辨識的準確度不夠，我們對手勢檢測進行了多次調整，特別是針對大拇指的檢測，因其比其他手指短，容易導致識別錯誤。

接下來，我們開發了語音控制的功能。這部分相對簡單，但我們希望結合語音和手勢控制功能，這使得開發過程變得更加複雜。為了合併兩個功能模組，我們花費了大量時間理解兩者的邏輯，並解決許多程式錯誤（bugs）。最終，我們還額外加入了車子的加速與減速功能。

---

The most time-consuming part of our project was connecting the Raspberry Pi to our network. In the process, we accidentally overwrote the SD card contents and had to re-download the Raspberry Pi system, which took additional time. We also revisited chapters 7, 8, 9, and 10 of the course materials to refresh our understanding.

We first implemented the gesture recognition to control the car's movement, like moving forward, backward, turning left, and turning right, based on the number of raised fingers. For instance, a thumbs-up gesture signals the car to move backward. Due to recognition inaccuracies, we fine-tuned the system and added a separate detection for thumbs, which are shorter than the other fingers and caused recognition errors.

Next, we worked on voice control. While this part was straightforward, combining gesture and voice control proved more challenging. We spent considerable time merging the two features, understanding the logic of both, and debugging the integrated system. In the end, we added additional functionality like speed control (accelerate and decelerate).
