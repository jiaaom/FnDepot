# Fygo Cinema

[English](README.md) | 简体中文

在电视上看飞牛影视。NAS 自带的飞牛影视网页版全屏显示在接到 NAS 的电视上，用遥控器操作，视频硬件解码。

![电视上的首页，白框是遥控器移动的焦点](https://raw.githubusercontent.com/jiaaom/fygo-cinema/main/assets/home.jpg)

- **遥控器导航**：每个页面都能用遥控器操作，包括播放器的控制栏（倍速、清晰度、字幕、音轨）。
- **自动登录**：使用在管理页填写的账户，保持登录。
- **跟随电视**：插上电视即启动，声音从电视扬声器播放，遥控器音量键调节电视音量。

源码：<https://github.com/jiaaom/fygo-cinema>

## 安装顺序

1. **飞牛影视**（`trim.media`），在应用中心安装
2. **Appliance Compositor**（`appliance-compositor`）
3. **Fygo Cinema**（`fygo-cinema`）

然后在 fnOS 桌面打开 Fygo Cinema，填写电视要登录的飞牛影视账户，插上电视即可。需要 Intel 显卡。

## 问题反馈

<https://github.com/jiaaom/fygo-cinema/issues>
