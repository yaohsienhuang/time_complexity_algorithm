# 初學演算法
## Time Complexity & Space Complexity

1. 時間複雜度 (Time Complexity)： 執行演算法時須花費的時間。

- 須算出每一段的功能的執行次數
- 將所有執行次數加總起來後
- 求出此演算法的時間複雜度 ── Big-O。

2. 空間複雜度 (Space Complexity)： 執行演算法時須花費的記憶體空間。

> 即使是同一個演算法，執行速度會因每個人的環境、電腦硬體、設備等而不同。而且現在設備越來越便宜，大家的設備普遍都有一定的等級。
> ***這也就說明時間複雜度比空間複雜度來的重要！***
> 要先了解時間複雜度，就得先學會計算演算法的執行次數。

> 參考：https://ithelp.ithome.com.tw/articles/10216436


### Time Complexity

| 房型 | 說明 | 排序 | 其他例子 |
| -------- | -------- | -------- | -------- |
| O(1) | 陣列讀取 | 優良 | |
| O(n) | 簡易搜尋 | 優良 | |
| O(log n) | 二分搜尋 | 優良 | binary search |
| O(nlogn) | 合併排序 | 可接受 | Merge Sort |
| O(n²) | 選擇排序 | 差 | Bubble Sort |
| O(2^n) | 費波那契數列 | 差 | |

- 在演算法中，log n 的慣例指的是以 2 為底的意思，也就是 2 的幾次方。
> bubble sort : https://ithelp.ithome.com.tw/articles/10276184

> 參考:https://pjchender.dev/dsa/algo-intro/

> 參考:https://towardsdatascience.com/understanding-time-complexity-with-python-examples-2bda6e8158a7

> 生動的例子:https://ithelp.ithome.com.tw/articles/10228248

### Space Complexity

再來要講的是「空間複雜度」，它的概念跟時間複雜度是相仿的。
簡單的來說就是，電腦執行演算法所需要耗費的空間 ( 記憶體 ) 成本。
一般來說​「時間複雜度」與「空間複雜度」之間是可以相互 trade off 的！
而相互 trade off 的意思是：
在某些情況底下，我們是可以讓程式多用一些記憶體空間來多記一些資訊，就可以省去一些重複的運算來加速程式的執行時間；或者我們完全沒有多餘的記憶體資源可以使用，也可以透過把一些原本可以靠記憶體存儲的資訊改用重複計算的方式來取得。
>參考:https://jason-chen-1992.weebly.com/home/time-space-complexity