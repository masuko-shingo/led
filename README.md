# led
ロボットシステム学2020課題2　ROSパッケージ
## 概要

「ROS」を入力するとモールス信号での”R”,”O”,”S”がledで光り、「1」を入力するとledが点灯、「0」を入力するとledが消灯するROSパッケージです。
  
Toda sayaka さんのROSパッケージを参考にしました。  
Githubリンク
https://github.com/todasayaka/led_national_flag
  
改造した部分は、PublisherからSubscriberに送受信するメッセージの型をInt32からStringに変更、Subscriberにtimeライブラリを追加して自分の行いたい内容に改造しました。

---

## 動作環境
|||
|:--:|:--:|
| Raspberry Pi | Raspberry Pi Model 3B+ |
| OS | Ubuntu 20.04 |
| ROS | ROS Noetic |

## インストール,ビルド
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/masuko-shingo/led.git     //このリポジトリをローカルにクローンする
$ cd ..
$ catkin_make     //ビルドする
$ source ~/.bashrc    //bashrcを更新
```

## 実行方法
```
$ cd src/led/myled
$ make    //コンパイル
$ sudo insmod myled.ko      //カーネルモジュールのインストール
$ sudo chmod 666 /dev/myled0      //パーミッションの変更
$ roslaunch led led.launch     //ローンチファイルの実行
$ sudo rmmod myled.ko       //カーネルモジュールのアンインストール
```

## 回路図
![回路図ロボシス課題１](https://user-images.githubusercontent.com/72721963/101239901-aa4b0a80-372e-11eb-9ddb-fcbab11e1ce7.png)

## 動画
https://youtu.be/y1i6_Mqn16c

## Copyright
Copyright © 2020  Sayaka Toda + Shingo Masuko. 

This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
